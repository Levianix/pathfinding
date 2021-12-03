grafo={
    "A": ("B","G","F"),
    "F": ("A","B","G","L","K"),
    "K": ("F","G","L","R","Q"),
    "Q": ("K","L","R","V","U"),
    "U": ("Q","R","V")
}

for g in grafo.values():
    print(g)


l=[]
for k in grafo["A"]:
    print(k)

    l.append(k)

print("l: ",l)
