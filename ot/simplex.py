def display(equations, z, ratios, pivotrow, pivotcol):
    
    #print headings
    print('\t\t\t', end='')
    for coeff in z: print(coeff, end='\t')
    print('\nB\tCb\tXb\t', end='')
    for i in range(1, variables):
        print(f'x{i}\t', end='')
    for i in range(1, variables):
        print(f'S{i}\t', end='')
    print("Ratio")
    
    # print basic variables and coeffients
    for i in range(constraints):
        print(f'S{i+1}\t', end='')
        print(z[i + constraints], end='\t')
        print(equations[i][-1], end='\t')
        for variable in range(len(equations[i])-1):
            if i == pivotrow and variable == pivotcol:
                print(F"[{equations[i][variable]}]", end='\t')
            else: print(equations[i][variable], end='\t')
        print(ratios[i])

def slack(equations, z):
    for i in range(constraints):
        for coeff in range(constraints):
            if i == coeff: equations[i].insert(-1, 1) # insert before last element
            else: equations[i].insert(-1, 0)
    for _ in range(constraints): z.append(0)
    

def solve(equations, z):
    delta = []
    pivotrow, pivotcol = None, None

    # calculate dj
    for col in range(variables + constraints - 1):
        zj = 0
        for row in range(constraints):
            zj += (z[row + constraints] * equations[row][col])
        delta.append(zj - z[col])

    # find pivot column
    minimumdelta = float('inf')
    for col in range(len(delta)):
        if minimumdelta > delta[col]:
            minimumdelta = delta[col]
            pivotcol = col
    
    # calculate ratio and find pivot row
    ratios = ['-' for _ in range(constraints)]
    minimumratio = float('inf')
    for row in range(constraints):
        if equations[row][pivotcol] > 0:
            ratios[row] = equations[row][-1] / equations[row][pivotcol]
            if minimumratio > ratios[row]:
                minimumratio = ratios[row]
                pivotrow = row
    

    if pivotrow is not None and pivotcol is not None: 
        display(equations, z, ratios, pivotrow, pivotcol)
        return f"Pivot = {equations[pivotrow][pivotcol]}"
    return "No solution"

'''
max Z = 3x1 + 5x2 + 4x3
subject to
2x1 + 3x2 <= 8
2x2 + 5x3 <= 10
3x1 + 2x2 + 4x3 <= 15
'''
equations = [
    [2, 3, 0, 8],
    [0, 2, 5, 10],
    [3, 2, 4, 15]
]

z = [3, 5, 4]
variables = len(equations[0])
constraints = len(equations)
slack(equations, z)
pivot = solve(equations, z)
print(f"\n{pivot}")