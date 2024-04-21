import pyomo.environ as pyo
from pyomo.opt import TerminationCondition

model = pyo.ConcreteModel()

M = 25
num_machines = 3
num_jobs = 8
job_durations = [0,8,4,3,7,3,2,4,4] # job 0 is a dummy job with duration 0 to simplify indexing

model.s = pyo.Var(range(1, num_jobs+1), within=pyo.NonNegativeIntegers) # decision variable: start time of each job
model.y = pyo.Var(range(1, num_jobs), within=pyo.Binary) # decision variable: order of jobs
model.z = pyo.Var(within=pyo.NonNegativeIntegers) # decision variable: makespan (end time of last job)

model.makespan_constraints = pyo.ConstraintList()
model.makespan_constraints.add(model.z >= model.s[2] + job_durations[2])
model.makespan_constraints.add(model.z >= model.s[5] + job_durations[5])
model.makespan_constraints.add(model.z >= model.s[7] + job_durations[7])

model.paper_sequence_constraints = pyo.ConstraintList()
model.paper_sequence_constraints.add(model.s[1] + job_durations[1] <= model.s[2])
model.paper_sequence_constraints.add(model.s[4] + job_durations[4] <= model.s[3])
model.paper_sequence_constraints.add(model.s[3] + job_durations[3] <= model.s[5])
model.paper_sequence_constraints.add(model.s[8] + job_durations[8] <= model.s[6])
model.paper_sequence_constraints.add(model.s[6] + job_durations[6] <= model.s[7])

model.job_concurrency_constraints = pyo.ConstraintList()
model.job_concurrency_constraints.add(model.s[1] + job_durations[1] <= model.s[3] + M*(1-model.y[1]))
model.job_concurrency_constraints.add(model.s[3] + job_durations[3] <= model.s[1] + M*model.y[1])
model.job_concurrency_constraints.add(model.s[1] + job_durations[1] <= model.s[6] + M*(1-model.y[2]))
model.job_concurrency_constraints.add(model.s[6] + job_durations[6] <= model.s[1] + M*model.y[2])
model.job_concurrency_constraints.add(model.s[3] + job_durations[3] <= model.s[6] + M*(1-model.y[3]))
model.job_concurrency_constraints.add(model.s[6] + job_durations[6] <= model.s[3] + M*model.y[3])
model.job_concurrency_constraints.add(model.s[4] + job_durations[4] <= model.s[7] + M*(1-model.y[4]))
model.job_concurrency_constraints.add(model.s[7] + job_durations[7] <= model.s[4] + M*model.y[4])
model.job_concurrency_constraints.add(model.s[2] + job_durations[2] <= model.s[5] + M*(1-model.y[5]))
model.job_concurrency_constraints.add(model.s[5] + job_durations[5] <= model.s[2] + M*model.y[5])
model.job_concurrency_constraints.add(model.s[2] + job_durations[2] <= model.s[8] + M*(1-model.y[6]))
model.job_concurrency_constraints.add(model.s[8] + job_durations[8] <= model.s[2] + M*model.y[6])
model.job_concurrency_constraints.add(model.s[5] + job_durations[5] <= model.s[8] + M*(1-model.y[7]))
model.job_concurrency_constraints.add(model.s[8] + job_durations[8] <= model.s[5] + M*model.y[7])

model.obj = pyo.Objective(expr=model.z, sense=pyo.minimize)

# model.pprint()

opt = pyo.SolverFactory('cbc')
results = opt.solve(model, tee=True)

condition = results.solver.termination_condition
print(f'Solver condition: {condition}')

if condition == TerminationCondition.optimal or condition == TerminationCondition.maxTimeLimit:
    print('Objective value is (= how many hours it takes)', pyo.value(model.obj))
    print('How to schedule the jobs: ')
    for j in range(1, num_jobs+1):
        start_time = pyo.value(model.s[j])
        print(f'Job {j} starts at {start_time} hours and ends at {start_time + job_durations[j]} hours')
elif condition == TerminationCondition.infeasible :
    print('infeasible - check model again!') 