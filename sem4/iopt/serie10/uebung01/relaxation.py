import pyomo.environ as pyo
from pyomo.opt import TerminationCondition

model = pyo.ConcreteModel()

model.x = pyo.Var(within=pyo.NonNegativeReals)
model.y = pyo.Var(within=pyo.NonNegativeReals)
# model.x = pyo.Var(within=pyo.NonNegativeIntegers)
# model.y = pyo.Var(within=pyo.NonNegativeIntegers)

model.constraints = pyo.ConstraintList()
model.constraints.add(8000 * model.x + 4000 * model.y <= 40000)
model.constraints.add(15 * model.x + 30 * model.y <= 200)

model.constraints.add(model.y >= 5)

model.obj = pyo.Objective(expr=(100 * model.x + 30 * model.y), sense=pyo.maximize) # maximize the number of edges

model.pprint()

opt = pyo.SolverFactory('gurobi')
results = opt.solve(model, tee=True)

condition = results.solver.termination_condition
print(f'Solver condition: {condition}')

if condition == TerminationCondition.optimal or condition == TerminationCondition.maxTimeLimit:
    print('Objective value is ', pyo.value(model.obj))
    print('x = ', pyo.value(model.x))
    print('y = ', pyo.value(model.y))
elif condition == TerminationCondition.infeasible :
    print('infeasible - check model again!') 