"""Terminal guideline chat: python guideline_chat/chat.py"""
import argparse
import os
import sys
import time

import app


def display(result, show_sources=False, elapsed=None):
    kind = result.get('kind', result.get('mode'))
    print(f"\nCopilot ({kind}{f', {elapsed:.1f}s' if elapsed is not None else ''}):")
    for block in result.get('blocks', [{'text': result['message'], 'citations': []}]):
        citations = ' '.join(f'[{number}]' for number in block['citations'])
        print(block['text'] + (' ' + citations if citations else ''))
        print()
    for notice in result.get('notices', []):
        print('Note:', notice)
    cited = {number for block in result.get('blocks', []) for number in block['citations']}
    if result['mode'] == 'excerpts':
        cited = set(range(1, len(result['sources']) + 1))
    for number in sorted(cited):
        source = result['sources'][number - 1]
        doc = source['document']
        page = f"{source.get('page_kind', 'PDF page')} {source['page']}" if source['page'] else 'Word document'
        print(f"[{number}] {doc['title']} | {doc['version']} | {page}")
        if source.get('heading_path'):
            print('    Section:', source['heading_path'])
        if result['mode'] == 'excerpts':
            print(source['text'])
    if show_sources and result['mode'] != 'excerpts' and result['sources']:
        print('Retrieved chunks:')
        for number, source in enumerate(result['sources'], 1):
            heading = (source.get('heading_path') or '').split(' > ')[-1]
            print(f"  [{number}] {source.get('chunk_id')} | p.{source['page']} | {heading[:70]}")
    print()

def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8', errors='replace')
    parser = argparse.ArgumentParser(description='Chat with your facility guidelines in the terminal.')
    parser.add_argument('--program', default='All programs', choices=['All programs'] + sorted({p for d in app.DOCS for p in d['programs']}))
    parser.add_argument('--question', help='Ask one question and exit.')
    parser.add_argument('--exclude-drafts', action='store_true', help='Leave out the unconfirmed 2026 STI draft (included by default here).')
    parser.add_argument('--top-k', type=int, default=6, help='Retrieval limit (default 6).')
    parser.add_argument('--no-expand', action='store_true', help='Turn off section expansion.')
    parser.add_argument('--sources', action='store_true', help='List every retrieved chunk after each answer.')
    parser.add_argument('--excerpts', action='store_true', help='Test document retrieval without the model.')
    args = parser.parse_args()
    os.environ.setdefault('RETRIEVAL_TOP_K', str(args.top_k))
    os.environ.setdefault('RETRIEVAL_EXPANSION', '0' if args.no_expand else '1')
    if args.excerpts:
        app.os.environ['LLM_MODEL'] = ''
    app.build_index()
    print('Facility Copilot |', args.program)
    print('Embeddings ·', app.embedding_model())
    print(f"RAG chat · {app.os.environ.get('LLM_MODEL', app.DEFAULT_LLM_MODEL)}" if app.ai_enabled() else 'Document excerpts only')
    if app.ai_enabled():
        print('Questions, recent conversation, and retrieved passages are sent to the ML server at', app.os.environ.get('LLM_BASE_URL', app.DEFAULT_LLM_URL))
    print('Type /new to reset or /quit to exit.\n')
    history = []
    while True:
        try:
            question = args.question if args.question is not None else input('You: ').strip()
            if question.lower() in ('/quit', '/exit'):
                return 0
            if question == '/new':
                history = []
                print('Started a new conversation.\n')
                continue
            if not question:
                if args.question is not None:
                    print('Enter a nonempty question.', file=sys.stderr)
                    return 1
                continue
            print('Searching guidelines…', flush=True)
            started = time.time()
            result = app.answer({'question': question, 'program': args.program, 'history': history[-6:],
                                 'include_drafts': not args.exclude_drafts})
            display(result, args.sources, time.time() - started)
            history.extend([{'role': 'user', 'content': question}, {'role': 'assistant', 'content': '\n\n'.join(b['text'] for b in result.get('blocks', [])) or result['message'][:8000]}])
            history = history[-6:]
            if args.question is not None:
                return 0
        except (EOFError, KeyboardInterrupt):
            print('\nChat closed.')
            return 0
        except (ValueError, RuntimeError) as exc:
            print('Could not answer:', str(exc), file=sys.stderr)
            if args.question is not None:
                return 1


if __name__ == '__main__':
    sys.exit(main())
