''' Jerry.AI question
input: [1,2,3,4]
output: ['1-2+3']
'''

formulas = []
def dfs_generate_formula(cur_index, cur_formula):
    for c in ['+', '-', '']:
        cur_formula_copy = cur_formula
        cur_formula_copy += c + str(input_list[cur_index])
        if cur_index == len(input_list) - 1:
            formulas.append(cur_formula_copy)
        else:
            dfs_generate_formula(cur_index + 1, cur_formula_copy)

input_list = [i for i in range(1,4)]
dfs_generate_formula(0, '')

target = 2
ans = set()
for i, formula in enumerate(formulas):
    if eval(formula) == target:
        if formula[0] == '+':
            ans.add(formulas[i][1:])
        else:
            ans.add(formulas[i])
print(ans)
