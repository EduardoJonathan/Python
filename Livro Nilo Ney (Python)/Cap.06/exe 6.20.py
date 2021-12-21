versao_1 = {1, 2, 3}
versao_2 = {2, 3, 4}
#Os elementos que não mudaram
print(versao_1 & versao_2)

#Os novos elementos
print(versao_2 - versao_1)

#E os elementos repetidos
print(versao_1 - versao_2)
