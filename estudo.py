

#lista_preços = [1500, 100, 500, 2000]

#taxa_imposto = 0.1


#for preço in lista_preços:
    #imposto = preço * taxa_imposto
    #print(f"preço do produto {preço}, imposto é de {imposto}")


#total_imposto = 0
#for preço in lista_preços:
 #   if preço > 1000:
#        taxa = 0.15
 #   else:
 #       taxa = 0.1
 #   imposto = taxa * preço
#
#    total_imposto = total_imposto + imposto
#
#    print(f"preço do produto: {preço}, imposto: {imposto}\n") 
#    print(total_imposto)


lista_números = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_nomes = ["Thiago", "Gabriel", "Eduardo", "Nicolas"]
lista_anos = [2009, 2026]
soma_impar = 0

for número in lista_números:
    if número %2:
        soma_impar = soma_impar + número

print(soma_impar)
