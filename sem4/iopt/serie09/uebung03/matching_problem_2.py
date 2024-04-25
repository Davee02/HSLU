import pyomo.environ as pyo
from pyomo.opt import TerminationCondition

# set of vertices
V = set(range(1, 9))

# set of edges: each edge is a tuple (i,j) where i,j are the vertices it connects
E = [(0,0), # dummy edge to simplify indexing
     (1,2),
     (1,4),
     (1,7),
     (2,6),
     (3,4),
     (3,5),
     (3,7),
     (4,5),
     (4,8),
     (5,6),
     (5,8),
     (6,7),
     (6,8),
     (7,8)
]

# weight of each edge is the difference of the vertices it connects
w = [(j-i) for i,j in E]

model = pyo.ConcreteModel()

model.x = pyo.Var(range(1, len(E) + 1), within=pyo.Binary) # decision variable: place edge i

model.constraints = pyo.ConstraintList()
for i in range(1, len(V) + 1):
    model.constraints.add(sum(model.x[j] for j in range(1, len(E)) if i in E[j]) <= 1)

model.obj = pyo.Objective(expr=sum(model.x[i] * w[i] for i in range(1, len(E) )), sense=pyo.maximize) # maximize the number of edges

model.pprint()

opt = pyo.SolverFactory('gurobi')
results = opt.solve(model, tee=True)

condition = results.solver.termination_condition
print(f'Solver condition: {condition}')

if condition == TerminationCondition.optimal or condition == TerminationCondition.maxTimeLimit:
    print('Objective value is (= cumulative weight)', pyo.value(model.obj))
    print('Edges to place: ')
    for i in range(1, len(E)):
        if pyo.value(model.x[i]) > 0.5:
            print(f'Edge {E[i]}')
elif condition == TerminationCondition.infeasible :
    print('infeasible - check model again!') 