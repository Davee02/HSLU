import pyomo.environ as pyo
from pyomo.opt import SolverStatus, TerminationCondition
import os
import sys
import csv

#Input reading
# --- 
round = 1
day = 5
# ---
os.chdir(sys.path[0])
problemDataStr = 'problemData/round' + str(round) + '-day' + str(day) + '_'
demandTruckDataPath = problemDataStr + 'demand_truck_data.csv'
problemDataPath = problemDataStr + 'problem_data.csv'
#demandNodeDataPath = problemDataStr  + 'demand_node_data.csv' #currently not used
#truckNodeDataPath = problemDataStr + 'truck_node_data.csv' #currently not used

I = set() #set of sites (Orte)
J = set() #set of truck places (Plätze)
b = dict() #demand per demand site - truck place tuple
dist = dict() #distance for each demand site - truck place tuple
f = 0 #cost per truck
r = 0 #burrito incredient cost
p = 0 #burrito unit price


with open(problemDataPath, "r", encoding="utf8") as problemFile:
    problemFileReader = csv.reader(problemFile, delimiter=",")
    next(problemFileReader)
    secondLine = next(problemFileReader)
    p = int(secondLine[0])
    r = int(secondLine[1])
    f = int(secondLine[2])

with open(demandTruckDataPath, "r", encoding="utf8") as detailedDataFile:
    detailedDataReader = csv.reader(detailedDataFile, delimiter=",")
    next(detailedDataReader) #skip first line
    for row in detailedDataReader:
        demandSite = row[0]
        truckPlace = row[1]
        distance = float(row[2])
        demand = int(row[3])
        I.add(demandSite)
        J.add(truckPlace)
        b[(demandSite,truckPlace)] = demand
        dist[(demandSite,truckPlace)] = distance

# Kreiere Modell
model = pyo.ConcreteModel()

# x_j : truck auf Platz j
model.x =  pyo.Var(J, within = pyo.Binary)

# y_ij : 1 falls Ort i zu truck am Platz j 
model.y =  pyo.Var(I,J, within = pyo.Binary)

#Constraints
model.constraints = pyo.ConstraintList()

# people from demand site i can only be assigned to exactly one truck j
for i in I:
    model.constraints.add(sum(model.y[i,j] for j in J) == 1)

# people from demand site i can only be assigned to truck j if truck j is placed
for j in J:
    for i in I:
        model.constraints.add(model.y[i,j] <= model.x[j])

# Additional constraints to ensure that a demand site is assigned to the nearest truck place
for i in I:
    for j in J:
        # Constraint to ensure that if there is a closer truck place 'k' that is available,
        # then demand site 'i' cannot be assigned to truck place 'j'.
        for k in J:
            if dist[(i, k)] < dist[(i, j)]:
                # Add constraint only if there is a closer truck place
                model.constraints.add(model.y[i, j] <= model.x[k] + (1 - model.x[j]))


#Objective

# maximize profit by maximizing the difference between revenue and costs
model.obj = pyo.Objective(expr = (p - r) * sum(b[i,j] * model.y[i,j] for i in I for j in J) - f * sum(model.x[j] for j in J), sense = pyo.maximize)

# Kreiere Solver und löse Problem mit 'cbc'
opt = pyo.SolverFactory('gurobi')
# tee = true -> see solver output
results = opt.solve(model, tee=True)

# model.pprint()
# model.display()

condition = results.solver.termination_condition
print('Solver condition: ', condition)

if condition == TerminationCondition.optimal or condition == TerminationCondition.maxTimeLimit :
    # Do something when the solution is optimal or feasible
    print('objective value is', pyo.value(model.obj))
    print('the following trucks are placed:')
    for j in J:
        if  pyo.value(model.x[j]) > 0.5 :
            print(j)
    print('the demand places are assigned to the following truck sites:')
    for i in I:
        for j in J:
            if  pyo.value(model.y[i,j]) > 0.5 :
                print(i , ' to ' , j , ' with demand ' , b.get((i,j)))
        
elif condition == TerminationCondition.infeasible :
    # Do something when model in infeasible
    print('infeasible - check model again!')
