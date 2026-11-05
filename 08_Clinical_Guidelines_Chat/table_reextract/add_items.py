"""Append/replace items in a guideline spec: python3 add_items.py SPEC.json BATCH.py  (BATCH defines ITEMS)."""
import json, sys
spec_path, batch = sys.argv[1], sys.argv[2]
ns = {}
exec(open(batch).read(), ns)
spec = json.load(open(spec_path))
new = {t['table_id']: t for t in ns['ITEMS']}
spec['tables'] = [t for t in spec['tables'] if t['table_id'] not in new] + list(new.values())
spec['tables'].sort(key=lambda t: (t['page'], t['table_id']))
json.dump(spec, open(spec_path, 'w'), ensure_ascii=False, indent=1)
print(len(spec['tables']), 'items in', spec_path)
