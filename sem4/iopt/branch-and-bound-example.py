import pyomo.environ as pyo
from pyomo.opt import TerminationCondition

model = pyo.ConcreteModel()

model.x = pyo.Var(within=pyo.NonNegativeReals)
model.y = pyo.Var(within=pyo.NonNegativeReals)

model.constraints = pyo.ConstraintList()
model.constraints.add(8 * model.x - 2 * model.y <= 15)
model.constraints.add(4 * model.x + 5 * model.y <= 36)
model.constraints.add(model.y <= 4) # constraint after first branching
model.constraints.add(model.x <= 2) # constraint after second branching

model.obj = pyo.Objective(expr=(6 * model.x - model.y), sense=pyo.maximize)

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
elif condition == TerminationCondition.unbounded:
    print('unbounded - check model again!')
else:
    print('Solver condition not recognized!')
