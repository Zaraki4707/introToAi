import json

with open(r'E:\1 ENSIA 2 by me\S2\intro to Ai\labai\LAB11_CSP_Empty.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

code_cell = [c for c in nb['cells'] if c.get('cell_type') == 'code'][0]
source = ''.join(code_cell['source'])

bt_start = source.find('def backtrack(self, assignment, domains):')
bt_doc_end = source.find('"""', bt_start + 10) + 3
bt_code_start = source.find('# your code here', bt_doc_end)
bt_code_end = source.find('def solve', bt_code_start)

print('=== backtrack method to replace ===')
print('Found at position:', bt_code_start)

s_start = source.find('def solve(self):')
s_doc_end = source.find('"""', s_start + 10) + 3
s_code_start = source.find('# your code here', s_doc_end)
s_code_end = source.find('def evaluate_solution', s_code_start)

print('=== solve method to replace ===')
print('Found at position:', s_code_start)