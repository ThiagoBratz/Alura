

lista_preços = [1500, 100, 500, 2000]

taxa_imposto = 0.1


#for preço in lista_preços:
    #imposto = preço * taxa_imposto
    #print(f"preço do produto {preço}, imposto é de {imposto}")


total_imposto = 0
for preço in lista_preços:
    if preço > 1000:
        taxa = 0.15
    else:
        taxa = 0.1
    imposto = taxa * preço

    total_imposto = total_imposto + imposto

    print(f"preço do produto: {preço}, imposto: {imposto}\n") 
    print(total_imposto)