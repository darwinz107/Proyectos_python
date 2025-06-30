
list_num = []


def funcion_analizar_lista(list_num):
    
    cant = len(list_num) -1
    for num in list_num:
      contadorMax =0
      contadorMin=0    
      for num2 in list_num:
          if int(num) > int(num2) and int(num) != int(num2):
              contadorMax +=1
          elif int(num) < int(num2) and int(num) != int(num2):
              contadorMin +=1
      if contadorMax == cant:
           print(f"Numero {num} es el mayor")
      elif contadorMin == cant:
          print(f"Numero {num} es el menor")   
          
def promedio(list_num):
    suma = 0
    
    for num in list_num:
        suma = suma + int(num)
    prom = suma/len(list_num)        
    print(f"El promedio es: {prom:.2f}")                
       

def par_o_impar(list_num):
    count_par = 0
    count_impar = 0
    for num in list_num:
        if int(num) % 2 != 0:
            count_impar +=1
        else:
            count_par +=1 
    print(f"Numeros pares total: {count_par}")
    print(f"Numeros pares total: {count_impar}")

list_num= list(input("Ingrese varios numeros separados por una coma:").split(","))


funcion_analizar_lista(list_num)
promedio(list_num)
par_o_impar(list_num)