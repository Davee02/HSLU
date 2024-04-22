import pyomo.environ as pyo
from pyomo.opt import SolverStatus, TerminationCondition
import os
import sys
import csv

#Input reading

# Definiere die Breiten der Rollen und die Gesamtbreite einer Standardrolle
roll_widths = [90, 80, 70, 60] # in cm
max_width = 300 # Gesamtbreite einer Standardrolle in cm

os.chdir(sys.path[0])
problemDataFileName = 'inputCuttingPatterns.txt'

breadth = (90, 80, 70, 60) #in cm
demands  = {90 : 17, 80 : 12, 70: 53, 60 : 34}  #in number of rolls of given breadth

patterns = {} #map of patterns, each pattern has an id and a map giving the number of pieces for each length

with open(problemDataFileName, "r", encoding="utf8") as cuttingStockFile:
    csfReader = csv.reader(cuttingStockFile, delimiter="\t")
    counter = 1
    next(csfReader) #jump over first line
    for row in csfReader:
        onePattern = {}
        onePattern[90] = int(row[0])
        onePattern[80]  = int(row[1])
        onePattern[70]  = int(row[2])
        onePattern[60]  = int(row[3])
        patterns[counter] = onePattern
        counter += 1

#for simplification, store keys of patterns in own variable
patternIds = patterns.keys()

# Kreiere Modell
model = pyo.ConcreteModel()

# x_m : how many copies of pattern m to cut
model.x =  pyo.Var(patterns, within = pyo.NonNegativeIntegers)

#constraints
model.constraints = pyo.ConstraintList()
for b in breadth :
    model.constraints.add(sum(model.x[m] * patterns[m][b] for m in patternIds) >= demands[b]) # demand coverage

#objective
model.obj = pyo.Objective(expr = sum(model.x[m] for m in patternIds), sense = pyo.minimize)

# Kreiere Solver und löse Problem mit 'cbc'
opt = pyo.SolverFactory('cbc')
# tee = true -> see solver output
results = opt.solve(model, tee=True)

# model.pprint()
# model.display()

condition = results.solver.termination_condition
print('Solver condition: ', condition)

if condition == TerminationCondition.optimal or condition == TerminationCondition.maxTimeLimit :
    print('objective value is (= number of big rolls to cut)', pyo.value(model.obj))
    print('how to cut them: ')
    for m in patternIds :
        if  pyo.value(model.x[m]) > 0.5 :
            print(pyo.value(model.x[m]), ' times pattern' , m ,' = pattern: ' , patterns.get(m))
elif condition == TerminationCondition.infeasible :
    # Do something when model in infeasible
    print('infeasible - check model again!')
