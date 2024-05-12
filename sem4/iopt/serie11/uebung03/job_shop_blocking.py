from ortools.sat.python import cp_model
from dataJobShop import create_data_model

# Kreiere Modell
model = cp_model.CpModel()

#Kreiere Daten
data = create_data_model()
anzMa = 0
anzOp = 0
anzJo = len(data)
totDur = 0
for entry in data:
    anzOp = anzOp + len(entry)
    for op in entry:
        print(op[0])
        anzMa = max(anzMa,op[0]+1)
        totDur += op[1]

print('Anzahl Maschinen:', anzMa, '\t Anzahl Aufträge: ', anzJo, '\t Anzahl Operationen', anzOp, '\t tot Bearbeitung: ', totDur)
H = totDur #Time horizon
#Ende Kreiere Daten

# Kreiere Modell
model = cp_model.CpModel()

#Store variables and precedence constraints
jobStartTimes = {}
jobEndTimes = {}
IVVars = {}
machineInvervals = [[] for i in range(anzMa)]
precCons = []
dynamicDurations = {}

# Creates job intervals and add to the corresponding machine lists.
countOps = 0
for job in data:
    firstOfJob = True
    prev_op_index = None  # Track index of the previous operation
    for op in job:
        machine = op[0]
        base_duration = op[1]
        jobStartTimes[countOps] = model.NewIntVar(0, H, 'x_{}'.format(countOps))
        jobEndTimes[countOps] = model.NewIntVar(0, H, 'y_{}'.format(countOps))
        dynamicDurations[countOps] = model.NewIntVar(base_duration, H, 'd_{}'.format(countOps))
        intervalVar = model.NewIntervalVar(jobStartTimes[countOps], base_duration, jobEndTimes[countOps],
                                                'IV_{}'.format(countOps))
        IVVars[countOps] = intervalVar
        machineInvervals[machine].append(intervalVar)
        if prev_op_index is not None:
            # Ensure the previous operation extends until this operation can start
            model.Add(jobEndTimes[prev_op_index] <= jobStartTimes[countOps])
            # Optional: Add constraint to dynamically adjust duration based on next job start
            # model.Add(dynamicDurations[prev_op_index] == jobStartTimes[countOps] - jobStartTimes[prev_op_index])

        prev_op_index = countOps
        countOps += 1

#makespan variable
z = model.NewIntVar(0, H, 'x_{}'.format(countOps))

#Präzedenzbedingungen erfüllen
for precCon in precCons:
    model.Add(jobStartTimes[precCon[1]] >= jobEndTimes[precCon[0]])

#Ende nach allen anderen Operationen
for i in range(countOps):
    model.Add(z >= jobEndTimes[i])

#Maschine nie doppelt belegen (mit noOverlap)
for mach in range(anzMa):
    model.AddNoOverlap(machineInvervals[mach])

# Zielfunktion: min nr of colors
model.Minimize(z)

# Kreiere Solver und löse Problem (solve) mit "Solver-Standardeinstellungen"
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Print solution when exists
if status == cp_model.OPTIMAL:
     print('ok')
     print('Makespan: ', solver.Value(z))
     print('Op. ID', 'Startzeit')
     for i in range(countOps):
            print('{}:'.format(i), solver.Value(jobStartTimes[i]))
elif status == cp_model.INFEASIBLE:
    print('infeasible model')
else:
    print('no solution found')
