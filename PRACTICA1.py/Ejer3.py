payasos_peso = 112
muñecas_peso = 75

payasos = int(input("Cantidad de payasos para enviar: "))
muñecas = int(input("Cantidad de muñecas para enviar: "))

peso_paquete = payasos_peso * payasos + muñecas_peso * muñecas
print("Peso total por paquete es de " + str(peso_paquete))