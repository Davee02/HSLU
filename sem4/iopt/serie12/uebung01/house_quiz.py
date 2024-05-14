from ortools.sat.python import cp_model

house_colors = ["rot", "grün", "weiss", "gelb", "blau"]
nationalities = ["Grossbritannien", "Schweden", "Dänemark", "Norwegen", "Deutschland"]
foods = ["Banane", "Kartoffeln", "Schokolade", "Brot", "Apfel"]
drinks = ["Kaffee", "Tee", "Milch", "Wasser", "Bier"]
pets = ["Vogel", "Hund", "Pferd", "Katze", "Fisch"]

n_houses = 5

model = cp_model.CpModel()

h = [[model.NewBoolVar('h_{}{}'.format(i,j)) for j in range(1, n_houses + 1)] for i in range(1, n_houses + 1)] # house colors
n = [[model.NewBoolVar('n_{}{}'.format(i,j)) for j in range(1, n_houses + 1)] for i in range(1, n_houses + 1)] # nationalities
e = [[model.NewBoolVar('e_{}{}'.format(i,j)) for j in range(1, n_houses + 1)] for i in range(1, n_houses + 1)] # foods
t = [[model.NewBoolVar('t_{}{}'.format(i,j)) for j in range(1, n_houses + 1)] for i in range(1, n_houses + 1)] # drinks
ht = [[model.NewBoolVar('ht_{}{}'.format(i,j)) for j in range(1, n_houses + 1)] for i in range(1, n_houses + 1)] # pets

for i in range(0, n_houses):
    # each house has exactly one of each attribute
    model.Add(sum(h[i][j] for j in range(0, n_houses)) == 1)
    model.Add(sum(n[i][j] for j in range(0, n_houses)) == 1)
    model.Add(sum(e[i][j] for j in range(0, n_houses)) == 1)
    model.Add(sum(t[i][j] for j in range(0, n_houses)) == 1)
    model.Add(sum(ht[i][j] for j in range(0, n_houses)) == 1)

    # each attribute is assigned to exactly one house
    model.Add(sum(h[j][i] for j in range(0, n_houses)) == 1)
    model.Add(sum(n[j][i] for j in range(0, n_houses)) == 1)
    model.Add(sum(e[j][i] for j in range(0, n_houses)) == 1)
    model.Add(sum(t[j][i] for j in range(0, n_houses)) == 1)
    model.Add(sum(ht[j][i] for j in range(0, n_houses)) == 1)

for j in range(0, n_houses):
    model.Add(h[1-1][j] == n[1-1][j]) # 1
    model.Add(n[2-1][j] == ht[2-1][j]) # 2
    model.Add(n[3-1][j] == t[2-1][j]) # 3
    model.Add(h[2-1][j] == t[1-1][j]) # 5
    model.Add(e[1-1][j] == ht[1-1][j]) # 6
    model.Add(h[4-1][j] == e[3-1][j]) # 8
    model.Add(e[5-1][j] == t[5-1][j]) # 12
    model.Add(n[5-1][j] == e[2-1][j]) # 14

    if (0 < j < n_houses - 1):
        model.Add(e[4-1][j-1] + e[4-1][j+1] == ht[4-1][j]) # 10
        model.Add(ht[3-1][j-1] + ht[3-1][j+1] == e[3-1][j]) # 11
        # model.Add(n[4-1][j-1] + n[4-1][j+1] == h[5-1][j]) # 13
        # model.Add(e[4-1][j-1] + e[4-1][j+1] == t[4-1][j]) # 15
    elif (j == 0):
        model.Add(e[4-1][j+1] == ht[4-1][j]) # 10
        model.Add(ht[3-1][j+1] == e[3-1][j]) # 11
        # model.Add(n[4-1][j+1] == n[5-1][j]) # 13
    elif (j == n_houses - 1):
        model.Add(e[4-1][j-1] == ht[4-1][j]) # 10
        model.Add(ht[3-1][j-1] == e[3-1][j]) # 11
        # model.Add(h[4-1][j-1] == h[5-1][j]) # 13

    if (j > 0):
        model.Add(h[2-1][j-1] == h[3-1][j]) # 4

model.Add(t[3-1][3-1] == 1) # 7
model.Add(n[4-1][1-1] == 1) # 9

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    for j in range(1, n_houses + 1):
        print("Haus", j)

        print("Hausfarbe:", end = " ")
        for i in range(1, n_houses + 1):
            if solver.Value(h[i-1][j-1]) == 1:
                print(house_colors[i-1])

        print("Nationalität:", end = " ")
        for i in range(1, n_houses + 1):
            if solver.Value(n[i-1][j-1]) == 1:
                print(nationalities[i-1])

        print("Essen:", end = " ")
        for i in range(1, n_houses + 1):
            if solver.Value(e[i-1][j-1]) == 1:
                print(foods[i-1])

        print("Trinken:", end = " ")
        for i in range(1, n_houses + 1):
            if solver.Value(t[i-1][j-1]) == 1:
                print(drinks[i-1])

        print("Haustier:", end = " ")
        for i in range(1, n_houses + 1):
            if solver.Value(ht[i-1][j-1]) == 1:
                print(pets[i-1])

        print()
elif status == cp_model.INFEASIBLE:
    print('infeasible model')
else:
    print('no solution found') 