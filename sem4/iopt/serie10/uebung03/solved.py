import pyomo.environ as pyo
from pyomo.opt import TerminationCondition

model = pyo.ConcreteModel()

S = range(0, 3)
T = range(0, 4)
g = [1, 4, 5, 8]
M = sum(g)
P = [
    [130, 80, 0],
    [120, 120, 90],
    [140, 110, 85]
]

model.x = pyo.Var(S, T, within=pyo.NonNegativeIntegers)
model.y = pyo.Var(S, T, within=pyo.Binary)
model.Q = pyo.Var(range(0, len(P)), range(0, len(P[0])), within=pyo.Binary)

model.constraints = pyo.ConstraintList()

model.constraints.add(sum(model.x[0,t] for t in T) <= 7)
model.constraints.add(model.Q[0,2] == 0)

for t in T:
    model.constraints.add(sum(model.y[s,t] for s in S) == 1)

for s in S:
    for t in T:
        model.constraints.add(model.x[s,t] <= M * model.y[s,t])

for s in S:
    model.constraints.add(sum(model.Q[s,n] for n in range(0, len(P[s]))) == 1)

for t in T:
    model.constraints.add(sum(model.x[s,t] for s in S) >= g[t])

for s in S:
    model.constraints.add(model.Q[s,0] * sum(model.x[s,t] for t in T) <= model.Q[s,0] * 3)
    model.constraints.add(model.Q[s,1] * sum(model.x[s,t] for t in T) >= model.Q[s,1] * 3)
    model.constraints.add(model.Q[s,1] * sum(model.x[s,t] for t in T) <= model.Q[s,1] * 7)
    model.constraints.add(model.Q[s,2] * sum(model.x[s,t] for t in T) >= model.Q[s,2] * 7)

model.obj = pyo.Objective(expr=(sum(model.x[s,t] * sum(P[s][n] * model.Q[s,n] for n in range(0, len(P[s]))) for s in S for t in T)), sense=pyo.minimize) # minimize the price of the transports

model.pprint()

opt = pyo.SolverFactory('gurobi')
results = opt.solve(model, tee=True)

condition = results.solver.termination_condition
print(f'Solver condition: {condition}')

if condition == TerminationCondition.optimal or condition == TerminationCondition.maxTimeLimit:
    print('Objective value is ', pyo.value(model.obj))
    print('How to transport them: ')
    for s in S:
        for t in T:
            if pyo.value(model.y[s,t]) > 0.5:
                print(f"Transport {t+1}: Spediteur {s+1} transports {pyo.value(model.x[s,t])} tons")

        price_pre_ton_for_speditetor = 0
        for n in range(0, len(P[s])):
            if(pyo.value(model.Q[s,n]) > 0.5):
                price_pre_ton_for_speditetor = P[s][n]
        print(f"Speditetor {s+1} transports a total of {sum(pyo.value(model.x[s,t]) for t in T)} tons for the price per ton of {price_pre_ton_for_speditetor}")
    
    for s in S:
        for n in range(0, len(P[s])):
            print(pyo.value(model.Q[s,n]), end=' ')
        print()

    for s in S:
        print(pyo.value(model.Q[s,1] * sum(model.x[s,t] for t in T)))
elif condition == TerminationCondition.infeasible :
    print('infeasible - check model again!') 