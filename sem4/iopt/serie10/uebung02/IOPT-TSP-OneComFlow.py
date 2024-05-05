import pyomo.environ as pyo
from pyomo.opt import SolverStatus, TerminationCondition
import tsplib95 as tsplib  # Inputs https://tsplib95.readthedocs.io/en/stable/
import os
import sys

#print("Current working directory: {0}".format(os.getcwd()))
os.chdir(sys.path[0])
problemData = tsplib.load('dantzig42.tsp')

I = tuple(problemData.get_nodes())
A = [(i,j) for i in I for j in I if i != j]
APrime = [(i,j) for i in I for j in I if i != j and j != I[0]]
IWithoutFirst = [i for i in I if i != I[0]]

# Kreiere Modell
model = pyo.ConcreteModel()

# x_i,j variablen 
model.x =  pyo.Var(A, within = pyo.Binary)
#z_i,j flow variablen
model.z =  pyo.Var(APrime, within = pyo.NonNegativeReals)

# einmal raus pro Stadt
def raus(model, i):
    return sum(model.x[(i,j)] for j in I if (i,j) in A) == 1
model.raus = pyo.Constraint(I, rule=raus)

# einmal rein pro Stadt
def rein(model, i):
    return sum(model.x[(j,i)] for j in I if (j,i) in A) == 1
model.rein = pyo.Constraint(I, rule=rein)

# z-flow rein - raus = 1 für alle ausser erstem Knoten
def zFlowSum(model, i):
    if i != I[0] :
        return sum(model.z[(j,i)] for j in I if (j,i) in APrime) - sum(model.z[(i,j)] for j in I if (i,j) in APrime) == 1
model.zFlowEquals1 = pyo.Constraint(IWithoutFirst, rule=zFlowSum)

model.zFlowRaus = pyo.Constraint(expr = sum(model.z[(I[0],j)] for j in IWithoutFirst) == len(IWithoutFirst))

#Verlinke z und x
def linkXundZ(model, i, j):
    return (len(I) - 1) * model.x[(i,j)] >= model.z[(i,j)]
model.linkXundZ = pyo.Constraint(APrime, rule=linkXundZ)

#Zielfunktion
model.obj = pyo.Objective(expr = sum(problemData.get_weight(i,j) * model.x[(i,j)] for (i,j) in A), sense = pyo.minimize)

# Kreiere Solver und löse Problem mit 'cbc'
opt = pyo.SolverFactory('cbc')
# tee = true -> see solver output
results = opt.solve(model, tee=True)

# model.pprint()
# model.display()
# results.write()

condition = results.solver.termination_condition
print('Solver condition: ', condition)

if condition == TerminationCondition.optimal or condition == TerminationCondition.maxTimeLimit :
    # Do something when the solution is optimal or feasible
    print('objective value is', pyo.value(model.obj))
    print('z-flow')
    for i in I :
        print(' z flow for node ', i, end = ": ")
        for j in I :
            if (j,i) in APrime and pyo.value(model.z[(j,i)]) > 0 :
                print(i, '->', j , ':', pyo.value(model.z[(j,i)]), end = ' - ')
        print('')
    print('x-flow')
    for i in I :
        for j in I :
            if (i,j) in A and pyo.value(model.x[(i,j)]) > 0.5 :
                print('from ', i , ' to ' , j)
    print('This gives the tour: ', I[0] ,' -> ', end = '')
    currentNode = I[0] 
    count = 1
    while count < len(I):
        for j in I :
            if (currentNode,j) in A and pyo.value(model.x[(currentNode,j)]) > 0.5 :
                print(j, end = ' -> ')
                currentNode = j
                count += 1
                break
    print('0')
elif condition == TerminationCondition.infeasible :
    # Do something when model in infeasible
    print('infeasible - check model again!')
