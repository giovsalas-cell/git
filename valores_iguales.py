
def verificar_valores_iguales(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)): # Empezamos desde i+1 para no comparar lo mismo
            if array[i] == array[j]:
                print(f"Encontrado un duplicado: {array[i]}")
        
   

arreglo=[1,2,3,4,1]

verificar_valores_iguales(arreglo)



