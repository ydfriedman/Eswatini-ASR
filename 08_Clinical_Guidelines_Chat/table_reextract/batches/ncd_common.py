C = lambda t, cs=1, rs=1: {"t": t, **({"cs": cs} if cs > 1 else {}), **({"rs": rs} if rs > 1 else {})}
Y = C("✓"); NO = C("—")
CH1 = "Chapter 1: Prevention, Health Education and Routine Health Examinations"
CH2 = "Chapter 2: Endocrinology"
def T(tid, page, hp, cap, repl, header, body, rhc=1, **kw):
    d = {"table_id": "ncdimh-" + tid, "page": page, "image_only": False, "heading_path": hp, "caption": cap,
         "replaces_chunks": ["ncdimh-" + r for r in repl], "row_header_cols": rhc, "header": header, "body": body,
         "footnotes": [], "source_flags": []}
    d.update(kw); return d
def D(tid, page, hp, cap, repl, content, flags=(), **kw):
    d = {"kind": "diagram", "table_id": "ncdimh-" + tid, "page": page, "image_only": False, "heading_path": hp, "caption": cap,
         "replaces_chunks": ["ncdimh-" + r for r in repl], "content": content, "footnotes": [],
         "source_flags": list(flags)}
    d.update(kw); return d
def B(tid, page, hp, cap, repl, content, flags=(), **kw):
    d = {"kind": "box", "table_id": "ncdimh-" + tid, "page": page, "image_only": False, "heading_path": hp, "caption": cap,
         "replaces_chunks": ["ncdimh-" + r for r in repl], "content": content, "footnotes": [], "source_flags": list(flags)}
    d.update(kw); return d
