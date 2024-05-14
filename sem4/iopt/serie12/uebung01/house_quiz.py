from ortools.sat.python import cp_model

house_colors = ["rot", "grün", "weiss", "gelb", "blau"]
nationalities = ["Grossbritannien", "Schweden", "Dänemark", "Norwegen", "Deutschland"]
foods = ["Banane", "Kartoffeln", "Schokolade", "Brot", "Apfel"]
drinks = ["Kaffee", "Tee", "Milch", "Wasser", "Bier"]
pets = ["Vogel", "Hund", "Pferd", "Katze", "Fisch"]

n_houses = 5

model = cp_model.CpModel()

h = [[model.NewBoolVar('h_{}{}'.format(i,j)) for j in range(1, n_houses + 1)] for i in range(1, n_houses + 1)]
n = [[model.NewBoolVar('n_{}{}'.format(i,j)) for j in range(1, n_houses + 1)] for i in range(1, n_houses + 1)]
e = [[model.NewBoolVar('e_{}{}'.format(i,j)) for j in range(1, n_houses + 1)] for i in range(1, n_houses + 1)]
t = [[model.NewBoolVar('t_{}{}'.format(i,j)) for j in range(1, n_houses + 1)] for i in range(1, n_houses + 1)]
ht = [[model.NewBoolVar('ht_{}{}'.format(i,j)) for j in range(1, n_houses + 1)] for i in range(1, n_houses + 1)]

for i in range(0, n_houses):
    model.Add(sum(h[i][j] for j in range(0, n_houses)) == 1)
    model.Add(sum(n[i][j] for j in range(0, n_houses)) == 1)
    model.Add(sum(e[i][j] for j in range(0, n_houses)) == 1)
    model.Add(sum(t[i][j] for j in range(0, n_houses)) == 1)
    model.Add(sum(ht[i][j] for j in range(0, n_houses)) == 1)

for j in range(0, n_houses):
    model.Add(sum(h[i][j] for i in range(0, n_houses)) == 1)
    model.Add(sum(n[i][j] for i in range(0, n_houses)) == 1)
    model.Add(sum(e[i][j] for i in range(0, n_houses)) == 1)
    model.Add(sum(t[i][j] for i in range(0, n_houses)) == 1)
    model.Add(sum(ht[i][j] for i in range(0, n_houses)) == 1)

for j in range(0, n_houses):
    model.Add(h[1-1][j] == n[1-1][j])
    model.Add(n[2-1][j] == ht[2-1][j])

model.Add(t[3-1][3-1] == 1)
model.Add(n[4-1][1-1] == 1)

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