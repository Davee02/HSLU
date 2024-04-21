import pyomo.environ as pyo
from pyomo.opt import SolverStatus, TerminationCondition
import os
import sys
import csv

#Input reading

os.chdir(sys.path[0])
problemDataFileName = 'inputSudoku.txt'

I = range(1,10) #coordinates from 1 to 9 , for row and column
Iquad = [0, 3, 6]
F = {} #fixed values, key = tuple (Reihe, Kolonne) for coordinates and value for fixed value

with open(problemDataFileName, "r", encoding="utf8") as sudokuFile:
    sudokuReader = csv.reader(sudokuFile, delimiter="\t")
    next(sudokuReader) #jump over first line
    for line in sudokuReader:
        rowNumber = int(line[0])
        colNumber = int(line[1])
        value  = int(line[2])
        F[(rowNumber, colNumber)] = value

# Kreiere Modell
model = pyo.ConcreteModel()

# x_i,j,k is value k in cell(i,j) - 1 if yes, 0 if false
model.x =  pyo.Var(I,I,I, within = pyo.Binary)

#constraints
model.rows = pyo.ConstraintList()
model.cols = pyo.ConstraintList()
model.vals = pyo.ConstraintList()
model.quads = pyo.ConstraintList()
model.known = pyo.ConstraintList()

# each value k is only once in each row
for k in I:
    for j in I:
        model.rows.add(sum(model.x[i,j,k] for i in I) == 1)

# each value k is only once in each column
for i in I:
    for k in I:
        model.cols.add(sum(model.x[i,j,k] for j in I) == 1)

# each cell has only one value
for i in I:
    for j in I:
        model.vals.add(sum(model.x[i,j,k] for k in I) == 1)

# each value k is only once in each row
for k in I:
    for p in Iquad:
        for q in Iquad:
            model.quads.add(sum(model.x[r+p,c+q,k] for r in range(1,4) for c in range(1,4)) == 1)

# fixed values
for knownValue in F:
    knownRow = knownValue[0]
    knownColumn = knownValue[1]
    knownCellValue = F[knownValue]

    for val in I:
        model.known.add(model.x[knownRow, knownColumn, val] == (1 if val == knownCellValue else 0))

#no objective
model.obj = pyo.Objective(expr = 0, sense = pyo.maximize)

# Kreiere Solver und löse Problem mit 'cbc'
opt = pyo.SolverFactory('cbc')
# tee = true -> see solver output
results = opt.solve(model, tee=True)

# model.pprint()
# model.display()

condition = results.solver.termination_condition
print('Solver condition: ', condition)

if condition == TerminationCondition.optimal or condition == TerminationCondition.maxTimeLimit :
    # Do something when the solution is optimal or feasible
    print('solution of the Sudoku: ')
    for i in I :
        for j in I:
            for k in I:
                if  pyo.value(model.x[i,j,k]) > 0.5 :
                    print(k, end = '  ')
        print('')
elif condition == TerminationCondition.infeasible :
    # Do something when model in infeasible
    print('infeasible - check model again!')

