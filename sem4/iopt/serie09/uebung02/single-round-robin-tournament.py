import pyomo.environ as pyo
import numpy as np
from pyomo.opt import SolverStatus, TerminationCondition
from math import floor, ceil

model = pyo.ConcreteModel()

n = 6 # number of teams
D = range(1, n) # set of days
T = range(1, n + 1) # set of teams

model.x = pyo.Var(T, T, D) # decision variable: team i plays against team j at home on day d
model.x_h = pyo.Var([(i,d) for i in T for d in D], within = pyo.Binary) # helper variable: team i plays at home on day d

model.constraints = pyo.ConstraintList()

# each team plays exactly one game against each other team
for i in T:
    for j in T:
        if j > i:
            model.constraints.add(sum(model.x[i, j, d] + model.x[j, i, d] for d in D) == 1)

# each team plays exactly one game per day
for j in T:
    for i in T:
        model.constraints.add(sum(model.x[i, j, d] for d in D) == 1)

# each team has between floor((n-1)/2) and ceil((n-1)/2) home games
for i in T:
    model.constraints.add(sum(model.x_h[i, d] for d in D) >= floor((n-1)/2))
    model.constraints.add(sum(model.x_h[i, d] for d in D) <= ceil((n-1)/2))

# dummy objective
model.obj = pyo.Objective(expr = 0, sense = pyo.minimize)

opt = pyo.SolverFactory('cbc')
results = opt.solve(model, tee=True)

condition = results.solver.termination_condition
print(f'Solver condition: {condition}')

if condition == TerminationCondition.optimal or condition == TerminationCondition.maxTimeLimit:
    for d in D:
        print(f'--- Day {d} ---')
        for i in T:
            for j in T:
                if i != j and pyo.value(model.x[i, j, d]) > 0.5:
                    print(f"  Team {i} spielt gegen Team {j} zu hause")
elif condition == TerminationCondition.infeasible :
    print('infeasible - check model again!') 