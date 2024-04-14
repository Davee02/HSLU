import pyomo.environ as pyo
from pyomo.opt import SolverStatus, TerminationCondition
import os
import sys
import csv

#Input reading

os.chdir(sys.path[0])
problemDataFileName = 'transhipmentInput.txt'

demand = {} #nodes with demand, key = node, value = demand
unitCost = {} #arcs with length, key = (start node, end node), value length

with open(problemDataFileName, "r", encoding="utf8") as tanshipmentFile:
    tsv_reader = csv.reader(tanshipmentFile, delimiter="\t")

    #-demand / supply
    firstLine = next(tanshipmentFile).split()
    for i in range(len(firstLine)) :
        if ('#' in firstLine[i]) :
            break
        else :
            splitted = firstLine[i].split(":")
            node = int(splitted[0])
            demandOfNode = int(splitted[1])
            demand[node] = demandOfNode

    for row in tsv_reader:
        fromNode = int(row[0])
        toNode = int(row[1])
        cost = int(row[2])
        unitCost[(fromNode, toNode)] = cost

#Input reading finished
V = demand.keys() #node set
A = unitCost.keys() #arc set
Aout = {} #arc set out of each node
Ain = {} #arc set into each node
for v in V :
    Aout[v] = []
    Ain[v] = []
for (v,w) in A :
    Aout[v].append((v,w))
    Ain[w].append((v,w))

# Kreiere Modell
model = pyo.ConcreteModel()

# x_v,w variablen: flow
model.x =  pyo.Var(A, within = pyo.NonNegativeReals)

#Falls Sie Probleme mit der Implementation des generischen Modells (mit den Mengen) haben,
#bitte einfach die konkrete Problemstellung (mit konkreten Werten) implementieren.

#constraints
def kapazitaet(model, s):
   return sum(model.x[s,m] for m in M) <= data['capa'][s] * model.y[s]
model.kapa = pyo.Constraint(S, rule=kapazitaet)

#objective
# model.objective = pyo.Objective(expr = )

# Kreiere Solver und löse Problem mit 'cbc'
opt = pyo.SolverFactory('cbc')
# tee = true -> see solver output
results = opt.solve(model, tee=True)

model.pprint()
model.display()

condition = results.solver.termination_condition
print('Solver condition: ', condition)

if condition == TerminationCondition.optimal or condition == TerminationCondition.maxTimeLimit :
    # Do something when the solution is optimal or feasible
    #load results into model
    print('objective value is', pyo.value(model.obj))
    print('the positive arc flows are:')
    for (v,w) in A:
        if  pyo.value(model.x[v,w]) > 0.00001 : #precision 0.00001
            print('from ', v , ' to ' , w, ': ' , pyo.value(model.x[v,w]), ' with total cost ' , pyo.value(model.x[v,w]) * unitCost.get((v,w)))
elif condition == TerminationCondition.infeasible :
    # Do something when model in infeasible
    print('infeasible - check model again!')
