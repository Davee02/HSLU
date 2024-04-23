import pyomo.environ as pyo
from pyomo.opt import SolverStatus, TerminationCondition
from math import floor, ceil
import os
import sys

os.chdir(sys.path[0])

""" Constants """
TIMELIMIT = 600
d_st = 16
p_min = 100
p_ev = 20
p_br = 10
pen_we_ends = 1000;

""" Read all inputs """
data_file = open("dates.txt", 'r') # put your own path and .col file
lines = [line for line in data_file]

q = int(lines[0].split()[0]) # nr of days
R = int(lines[1].split()[0]) # nr of rounds
t = int(lines[2].split()[0]) # nr of teams

teams = {i: 'MT'+str(i) for i in range(1,t+1)}

days = list()
rounds = {i:[] for i in range(1,R+1)}

sa = set() #saturdays
su = set() #sundays
ho = set() #holidays
we_hol = set() #weekend or holiday
match_days = list()

matches = {(i,j) for i in range(1,t+1) for j in range(1,t+1) if i!=j}

for i in range(4,4+q): # read the information for all dates
    day_nr, rou, is_match_day, saturday, sunday, holiday = lines[i].split()
    day_nr, rou, is_match_day, saturday, sunday, holiday = int(day_nr), int(rou), int(is_match_day), int(saturday), int(sunday), int(holiday)
    days.append(day_nr)
    if is_match_day:
        rounds[rou].append(day_nr)
        match_days.append(day_nr)
        if saturday:
            sa.add(day_nr)
        if sunday:
            su.add(day_nr)
        if holiday:
            ho.add(day_nr)
        if saturday or sunday or holiday:
            we_hol.add(day_nr)

data_file.close()

""" Modell and variable declaration """

model = pyo.ConcreteModel()


#start modeling
#variables
model.x =  pyo.Var([(i,j,d) for i in teams.keys() for j in teams.keys() for d in match_days if i!=j], within = pyo.NonNegativeReals) # 1 if a match between team i (at home) and team j happens on day d, 0 otherwise

#auxiliary variables
model.xh = pyo.Var([(i,d) for i in teams.keys() for d in match_days], within = pyo.NonNegativeReals) # 1 if team i is home on day d, 0 otherwise
model.xa = pyo.Var([(i,d) for i in teams.keys() for d in match_days], within = pyo.NonNegativeReals) # 1 if team i is away on day d, 0 otherwise


#variables for penalty costs
model.y = pyo.Var([(i,d)  for i in teams.keys() for d in match_days if d<=q-2], within = pyo.NonNegativeReals) # will be used to penalize match sequences that have only 1 day of rest between two matches
model.z = pyo.Var([(i,d)  for i in teams.keys() for d in match_days if d<=q-6], within = pyo.NonNegativeReals) # will be used to penalize stretches of 7 days where a team doesn't have 1-2 matches

#variables for h/a break costs
break_min = 2
break_max = 8
model.bre = pyo.Var([(i,l,k) for i in teams.keys() for l in range(break_min, break_max+1) for k in range(len(match_days)-l+1)], within = pyo.NonNegativeReals)
# @variable(
#     vtpp,
#     bre[i in 1:t, l in breakMin:breakMax, k in 1:length(matchDays)-l+1] >= 0
# )

#variables penalty soft weekend constraints
model.we_pen = pyo.Var(teams.keys(), within = pyo.NonNegativeReals)

""" Constraints """
model.cons = pyo.ConstraintList()

# aux variables linking constraints
for i in teams:
    for d in match_days:
        model.cons.add(model.xh[i,d] == sum(model.x[i,j,d] for j in teams if i != j))
        model.cons.add(model.xa[i,d] == sum(model.x[j,i,d] for j in teams if i != j))

# each match is played R/2 times
for i,j in matches:
    model.cons.add(sum(model.x[i,j,d] for d in match_days) == R/2)

# 1 additional change home-away for each pair of teams i j from round to round
# for r in range(1,R):
#     for i,j in matches:
#         model.cons.add(sum(x[i,j,d] for d in rounds[r]) + sum(x[i,j,d] for d in rounds[r+1]) == 1)

#Probably two games should also not be one after the other (only problem with)
#here min distance = 8 game days (a bit more than a week)
#gap_same_match = set()
#nr_days_gap = 5 #in both sets -> total gap = 2 * nrDaysGap
# for r in range(1,R):
#     game_list = list()
#     length_l = length(rounds[r])
#     for k in range(length_l-nr_days_gap,length_l+1):
#         game_list.append(round[r][k])
#     for k in range(1,nr_days_gap+1):
#         game_list.append(rounds[r+1][k])
# for i,j in matches:
#     for days in gap_same_match:
#         model.cons.add(sum(x[i,j,d] + x[j,i,d] for d in days) <= 1)

#2) one of the matches (i,j) (j,i) is played in each round
for i,j in matches:
    for r in rounds:
        model.cons.add(sum(model.x[i,j,d] + model.x[j,i,d] for d in rounds[r]) == 1)

#3) (t-1)/2 home and away matches in each round for each team
for i in teams:
    for r in rounds:
        model.cons.add(sum(model.xh[i,d] for d in rounds[r]) == (t-1)/2)
        model.cons.add(sum(model.xa[i,d] for d in rounds[r]) == (t-1)/2)

#4) at most one match per possible match day, else 0
for d in match_days:
    model.cons.add(sum(model.x[i,j,d] for i,j in matches) <= 1)

#6)
model.cons.add(sum(model.x[i,j,1] for i,j in matches) == 1)


#7)
for i in teams:
    model.cons.add(sum(model.xh[i,d] for d in range(1,d_st+1) if d in match_days) >= 1)

#8)
#balance saturday home matches
nr_matches_sa_low = floor(len(sa) / t)
nr_matches_sa_high = ceil(len(sa) / t)
print("sa: %i - high %i"%(nr_matches_sa_low, nr_matches_sa_high))
for i in teams:
    model.cons.add(sum(model.xh[i,d] for d in sa) >= nr_matches_sa_low)
    model.cons.add(sum(model.xh[i,d] for d in sa) <= nr_matches_sa_high)


#balance sunday home matches
nr_matches_su_low = floor(len(su) / t)
nr_matches_su_high = ceil(len(su) / t)
print("su: %i - high %i"%(nr_matches_su_low, nr_matches_su_high))
for i in teams:
    model.cons.add(sum(model.xh[i,d] for d in su) >= nr_matches_su_low)
    model.cons.add(sum(model.xh[i,d] for d in su) <= nr_matches_su_high)


#only one holiday
nr_matches_ho_low = floor(len(ho) / t)
nr_matches_ho_high = ceil(len(ho) / t)
print("holidays: %i - high %i"%(nr_matches_ho_low, nr_matches_ho_high))
for i in teams:
    model.cons.add(sum(model.xh[i,d] for d in ho) >= nr_matches_ho_low)
    model.cons.add(sum(model.xh[i,d] for d in ho) <= nr_matches_ho_high)

#balance overall weekend and holidays
nr_matches_low = floor(len(we_hol) / t)
nr_matches_high = ceil(len(we_hol) / t)
print("we: %i - high %i"%(nr_matches_low, nr_matches_high))
for i in teams:
    model.cons.add(sum(model.xh[i,d] for d in we_hol) >= nr_matches_low)
    model.cons.add(sum(model.xh[i,d] for d in we_hol) <= nr_matches_high)

#construct objective function correctly
             
""" Objective """
model.obj = pyo.Objective(expr = p_min*sum(model.y[i,d] for i in teams for d in range(1,q-1) if d in match_days) +
                                 p_ev*sum(model.z[i,d] for i in teams for d in range(1,q-5) if d in match_days) +
                                 pen_we_ends*sum(model.we_pen[i] for i in teams) +
                                 p_br*sum(model.bre[i,l,k] for i in teams for l in range(break_min, break_max+1) for k in range(len(match_days)-l+1)), sense = pyo.minimize)

# The constraints defined in the following method are added iteratively, per round
def add_constraints_round(r):
    #5) at least one rest day between consecutive matches of each team
    for i in teams:
        for d in rounds[r]:
            if d in match_days and d+1 in match_days:
                model.cons.add(model.xh[i,d] + model.xa[i,d] + model.xh[i,d+1] + model.xa[i,d+1] <= 1)
            
    #9) H/A Patterns
    break_min_three = 5
    break_max_three = 15
    #construct sequence of match days
    for i in teams:
        for l in range(break_min_three, break_max_three+1):
            for d_index_str in range(len(match_days)-l+1):
                if match_days[d_index_str] in rounds[r]:
                    model.cons.add(sum(model.xh[i,match_days[k]] - (l//3-1)*model.xa[i, match_days[k]] for k in range(d_index_str, d_index_str+l)) <= 2)
                    model.cons.add(sum(model.xa[i,match_days[k]] - (l//3-1)*model.xh[i, match_days[k]] for k in range(d_index_str, d_index_str+l)) <= 2)

    #10)
    for i in teams:
        for d in range(1,q-1):
            if d in match_days and d+2 in match_days and d in rounds[r]:
                model.cons.add(model.y[i,d] >= model.xh[i,d] + model.xa[i,d] + model.xh[i,d+2] + model.xa[i,d+2] - 1)
            
    #11)
    #more than two matches in one week
    #we do not check if it is a break period (as we have only an upper bound on the matches)
    for i in teams:
        for d in range(1,q-5):
            if d in match_days and d in rounds[r]:
                model.cons.add(model.z[i,d] >=sum(model.xh[i,d2] + model.xa[i,d2] for d2 in range(d,d+7) if d2 in match_days)- 2)

    #less than one = zero matches
    #check first if from d to d+6, there are six or more non-match days
    for i in teams:
        for d in range(1,q-5):
            if d in match_days and sum(1 for d2 in range(d,d+7) if d2 in match_days) >= 6 and d in rounds[r]:
                model.cons.add(model.z[i,d] >= 1-sum(model.xh[i,d2] + model.xa[i,d2] for d2 in range(d,d+7) if d2 in match_days))

    #12 penalty for h/a break
    for i in teams:
        for l in range(break_min, break_max+1):
            for d_index_str in range(len(match_days)-l+1):
                if d in rounds[r]:
                    model.cons.add(model.xh[i, match_days[d_index_str]] + model.xh[i,match_days[d_index_str+l-1]] <=
                     1 + model.bre[i,l,d_index_str] + sum(model.xa[i, match_days[k]] for k in range(d_index_str+1, d_index_str+l-1))) #HH
                    model.cons.add(model.xa[i, match_days[d_index_str]] + model.xa[i,match_days[d_index_str+l-1]] <=
                     1 + model.bre[i,l,d_index_str] + sum(model.xh[i, match_days[k]] for k in range(d_index_str+1, d_index_str+l-1))) #AA

# Iteratively solve the problem
""" Create the solver and solve problem """
#opt = pyo.SolverFactory('cbc')
#opt.options['seconds'] = TIMELIMIT #for cbc solver

opt = pyo.SolverFactory('gurobi') # Choose gurobi or cplex for better performance - academic licenses are available online
opt.options['TimeLimit'] = TIMELIMIT #for gurobi solver

add_constraints_round(1) # Add the constraints for the first round
for r in rounds:
    if r < R:
        add_constraints_round(r+1) # Add the constraints for the following round (to improve feasibility)
    
    for d in rounds[r]:
        for i,j in matches:
            model.x[i,j,d].domain = pyo.Binary
        for i in teams:
            model.xh[i,d].domain = pyo.Binary
            model.xa[i,d].domain = pyo.Binary
            
    print('optimize round '+str(r))
    results = opt.solve(model, tee=True)
    condition = results.solver.termination_condition
    print('Status of the solver is: ', condition)
    # retrieve values of the solution
    fix_vals_to_1 = []
    for d in rounds[r]:
        for i,j in matches:
            if model.x[i,j,d].value > 0.5:
                fix_vals_to_1.append((i,j,d))
    # now fix values from this round
    if r < R:
        for d in rounds[r]:
            for i,j in matches:
                if (i,j,d) in fix_vals_to_1:
                    model.cons.add(model.x[i,j,d] == 1)
                    model.cons.add(model.xh[i,d] == 1)
                    model.cons.add(model.xa[j,d] == 1)
                    model.cons.add(model.xh[j,d] == 0)
                    model.cons.add(model.xa[i,d] == 0)
                else:
                    model.cons.add(model.x[i,j,d] == 0)

""" Output """
condition = results.solver.termination_condition
print('Status of the solver is: ', condition)
with open("solution.txt", "w") as f:
    if results.solver.status == SolverStatus.ok and condition == TerminationCondition.optimal:
        print('Optimal solution found. Optimal objective value = '+str(pyo.value(model.obj)))
    elif results.solver.status == SolverStatus.ok and condition in [TerminationCondition.maxTimeLimit, TerminationCondition.userInterrupt]:
        print('Solution found - objective value = '+str(pyo.value(model.obj)))
    else:
        print("no feasible solution found")
        exit(0)
    
    # if a solution exists - otherwise the code would have exited before - print out the solution
    #print to console
    counter_games = 0
    for d in match_days:
        for i in teams:
            if model.xh[i,d].value > 0.01:
                print(str(i)+' plays at home in period '+str(d)+' (value '+str(model.xh[i,d].value)+')')
            if model.xa[i,d].value > 0.01:
                print(str(i)+' plays away in period '+str(d)+' (value '+str(model.xa[i,d].value)+')')
            for j in teams:
                if i != j and model.x[i, j, d].value > 0.01:
                    counter_games += 1
                    print(str(i) + " plays " + str(j) + " at " + str(d) + " (with value " + str(model.x[i, j, d].value) + ")")
        
    print("\ngame counter: " + str(counter_games))
    
    #objective function values contributions
    #objective
    print("\nminimum rest")
    for i in teams:
        for d in range(1,q-1):
            if d in match_days and model.y[i, d].value > 0.01:
                print(str(i) + " at " + str(d) + ": y[i,d] = " + str(model.y[i,d].value))
    
    print("\n even distribution of matches")
    for i in teams:
        for d in range(1,q-5):
            if d in match_days and model.z[i,d].value > 0.01:
                print(str(i) + ' at ' +str(d) +': z[i,d] = '+str(model.z[i,d].value))
    
    print("\n weekend match penalties")
    for i in teams:
        if model.we_pen[i].value > 0.01:
            print(str(i)+ " we_pen[i] = " + str(model.we_pen[i].value))

    print("\n h/a break")
    for i in teams:
        for l in range(break_min, break_max+1):
            for k in range(len(match_days)-l+1):
                if model.bre[i,l,k].value > 0.01:
                    print(str(i) + " length " + str(l) + " day " + str(match_days[k]) + " value :breA[i,l,k]+breH[i,l,k]=" + str(model.bre[i, l, k].value))

    #print to file
    for i in teams:
        f.write(teams[i])
        if i < t:
            f.write('\t')
    f.write('\n')
    for d in days:
        if d in match_days:
            for i in teams:
                for j in teams:
                    if i != j:
                        if model.x[i,j,d].value > 0.5:
                            f.write(teams[j])
                        if model.x[j,i,d].value > 0.5:
                            f.write("@"+teams[j])
                if i < t:
                    f.write('\t')
            f.write('\n')
        else:
            if d < q:
                f.write('\n')