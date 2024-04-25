import pyomo.environ as pyo
from pyomo.opt import TerminationCondition

num_edges = 15

# For each vertex i, the list vertices[i] contains the edges incident to i
incident_edges = [
    [1,2,3], # V1
    [1,10], # V2
    [4,9,11], # V3
    [2,4,5,6], # V4
    [5,7,9,14], # V5
    [10,12,15,14], # V6
    [3,11,13,15], # V7
    [6,7,12,15] # V8
]

model = pyo.ConcreteModel()

model.x = pyo.Var(range(1, num_edges + 1), within=pyo.Binary) # decision variable: place edge i

model.constraints = pyo.ConstraintList()
for i in range(0, len(incident_edges)):
    model.constraints.add(sum(model.x[j] for j in incident_edges[i]) <= 1)

model.constraints.add(model.x[8] == 0) # disable edge 9 because it was wrongly added as an edge

model.obj = pyo.Objective(expr=sum(model.x[i] for i in range(1, num_edges + 1)), sense=pyo.maximize) # maximize the number of edges

model.pprint()

opt = pyo.SolverFactory('gurobi')
results = opt.solve(model, tee=True)

condition = results.solver.termination_condition
print(f'Solver condition: {condition}')

if condition == TerminationCondition.optimal or condition == TerminationCondition.maxTimeLimit:
    print('Objective value is (= how many edges)', pyo.value(model.obj))
    print('Edges to place: ')
    for i in range(1, num_edges + 1):
        if pyo.value(model.x[i]) > 0.5:
            print(f'Edge {i}')
elif condition == TerminationCondition.infeasible :
    print('infeasible - check model again!') 