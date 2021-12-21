L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar (p):"))
v = int(input("Digite o outro valor a procurar (v):"))
x = 0
P = -1
V = -1
primeiro = 0
while x < len(L):
    if L[x] == p:
        P = x
    if L[x] == v:
        achouV = x
    x += 1
if P != -1:
    print(f"p: {p} encontrado na posição {P}")
else:
    print(f"p: {p} não encontrado")
if V != -1:
    print(f"v: {v} encontrado na posição {V}")
else:
    print(f"v: {v} não encontrado")

if P != -1 and V != -1:
    if P <= V:
        print("p foi achado antes de v")
    else:
        print("v foi achado antes de p")