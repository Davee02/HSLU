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
xVars = {}
yVars = {}
IVVars = {}
machineInvervals = [[] for i in range(anzMa)]
precCons = []

# Creates job intervals and add to the corresponding machine lists.
countOps = 0
for job in data:
    firstOfJob = True
    for op in job:
        machine = op[0]
        duration = op[1]
        xVars[countOps] = model.NewIntVar(0, H, 'x_{}'.format(countOps))
        yVars[countOps] = model.NewIntVar(0, H, 'y_{}'.format(countOps))
        intervalVar = model.NewIntervalVar(xVars[countOps], duration, yVars[countOps],
                                                'IV_{}'.format(countOps))
        IVVars[countOps] = intervalVar
        machineInvervals[machine].append(intervalVar)
        if not(firstOfJob):
            precCons.append((countOps-1, countOps))
        firstOfJob = False
        countOps += 1

#makespan variable
z = model.NewIntVar(0, H, 'x_{}'.format(countOps))

#Präzedenzbedingungen erfüllen
for precCon in precCons:
    model.Add(xVars[precCon[1]] >= yVars[precCon[0]])

#Ende nach allen anderen Operationen
for i in range(countOps):
    model.Add(z >= yVars[i])
#model.AddMaxEquality(z, [yVars[i] for i in range(countOps)])

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
            print('{}:'.format(i), solver.Value(xVars[i]))
elif status == cp_model.INFEASIBLE:
    print('infeasible model')
else:
    print('no solution found')  
