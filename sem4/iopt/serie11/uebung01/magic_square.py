from ortools.sat.python import cp_model

# Kreiere Modell
model = cp_model.CpModel()

#size of board
n = 7
nSq = n * n

#To do: set up the model
x = [[model.NewIntVar(1,nSq,'x_{}{}'.format(i,j)) for i in range(n)] for j in range(n)]
magNumber = model.NewIntVar(1, n**3,'magNumber')

model.AddAllDifferent([x[i][j] for i in range(n) for j in range(n)])

for i in range(n):
    model.Add(sum(x[i][j] for j in range(n)) == magNumber) # row
    model.Add(sum(x[j][i] for j in range(n)) == magNumber) # column

model.Add(sum(x[i][i] for i in range(n)) == magNumber) # diag 1
model.Add(sum(x[i][n-i-1] for i in range(n)) == magNumber) # diag 2
#end
          
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Print solution when exists
if status == cp_model.OPTIMAL:
    print('Solution')
    for i in range(n):
        for j in range(n):
            print(solver.Value(x[i][j]),end=' ')
        print('')
    print(f'\nMagic number: {solver.Value(magNumber)}')
elif status == cp_model.INFEASIBLE:
    print('infeasible model')
else:
    print('no optimal solution found')

    
