from pprint import pprint

grafoAux={
    # primer columna
    "A": ("B","G","F"),
    "F": ("A","B","G","L","K"),
    "K": ("F","G","L","R","Q"),

    # segunda columna
    "B": ("A","F","G","H","C"),
    "G": ("A","B","C","H","M","L","K","F"),
    "L": ("K","F","G","H","M"),

    # tercer columna
    "C": ("B","G","H"),
    "H": ("C","B","G","L","M"),
    "M": ("H","G","L")
}


grafo={
    # primer columna
    "A": ("B","G","F"),
    "F": ("A","B","G","L","K"),
    "K": ("F","G","L","R","Q"),
    "Q": ("K","L","R","V","U"),
    "U": ("Q","R","V"),

    # segunda columna
    "B": ("A","F","G","H","C"),
    "G": ("A","B","C","H","M","L","K","F")
}

"""
for g in grafo.values():
    print(g)
"""

l=[]
for k in grafo["A"]:
    l.append(k)
    
#pprint(grafoAux)

print("l: ",l)
