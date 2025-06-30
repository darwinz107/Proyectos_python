import re, json, csv, os

list_products = []

def agregar_products():

  nom_product = input('Ingrese el nombre del producto:')
  cod_unico = input('Ingrese un codigo unico:')
  precio = float(input('Ingrese el precio del producto:'))
  cantidad_stock = int(input('Ingrese el stock:'))
  categoria = input('Ingrese la categoria:')
  list_products.append({
    "Producto":nom_product,
    "Codigo unico":cod_unico,
    "Precio":precio,
    "Stock":cantidad_stock,
    "Categoria":categoria
  })

def busqueda_avanzanda():
  
  while True:
   print("1.-Buscar por palabra")
   print("2.-Buscar por precio")
   print("3.-Salir")
   opcion =int(input("Digite una opcion:"))
   if opcion ==1:
     
     buscar_palabra= input("Escriba la categoria o producto a buscar:")
     filtrador = re.compile(f".*{buscar_palabra}.*",re.IGNORECASE)
     for products in list_products:
       if filtrador.match(products["Producto"]) or filtrador.match(products["Categoria"]):
        print(products)
   elif opcion ==2:
       maxPrecio = float(input("Digite el precio maximo:"))
       minPrecio = float(input("Digite el precio minimo:"))  
       for products in list_products:
        if minPrecio <= products["Precio"] <= maxPrecio:
          print(products)
   elif opcion ==3:
        break   
   else:
     print("Valor incorrecto")


def modificar_productos():
  list_campos =[]
  buscar_palabra= input("Escriba la categoria, codigo o producto que desea editar:")
  filtrador = re.compile(f".*{buscar_palabra}",re.IGNORECASE)
  while True:
   campo = input("Escriba el campo a editar: ")
   valor = input("Escriba el nuevo valor: ")
   list_campos.append({"Campo":campo, "Valor":valor})
   opcion = (input("¿Desea continuar con la edicion de campos?: "))
   if opcion.lower() =="no":
     break
   elif opcion != "si":
     while True:
       print("Opcion incorrecta")
       opcion = (input("¿Desea continuar con la edicion de campos? "))
       if opcion == "si":
         break
  for producto in list_products:
    if filtrador.match(producto["Producto"]) or filtrador.match(producto["Codigo unico"]) or filtrador.match(producto["Categoria"]):
      print(f"Se encontro el productos o los productos {producto}")
      opcion= input("¿Es correcto? Si-No")
      if opcion.lower() =="no":
         break
      elif opcion.lower()=="si":
        for lista in list_campos:
           producto[lista["Campo"]] = lista["Valor"]
      else:
          print("Opcion incorrecta")    

def eliminar_productos():
  
  while True:
    buscar_palabra= input("Escriba la categoria, codigo o producto que desea eliminar:")
    filtrador = re.compile(f".*{buscar_palabra}.*",re.IGNORECASE)
    productos_filter = [producto for producto in list_products if filtrador.match(producto["Producto"]) or filtrador.match(producto["Codigo unico"]) or filtrador.match(producto["Categoria"])]
    print(f"Se encontro el productos o los productos: ")
    for p in productos_filter:
      print(p)
    opcion= input("¿Es correcto? Si-No").lower()
    if opcion =="si":
        for producto in productos_filter:
         list_products.remove(producto)
        break   
    elif opcion =="no":     
         print()
         
    else:
      print("Opcion incorrecta")     


def calcular_cantidad(umbral_stock):
  valor_total =0
  stock_total =0
  categorias = {}
  debajo_umbral = {}
  for producto in list_products:
      stock_total = stock_total + producto["Stock"]
      valor_total = valor_total + (int(producto["Stock"]) * float(producto["Precio"]))

      
      if producto["Stock"]<umbral_stock:
          debajo_umbral[producto["Producto"]]= producto["Stock"]

      categoria = producto["Categoria"]
      if categoria in categorias:
        categorias[categoria] += producto["Stock"]
      else:
        categorias[categoria] = producto["Stock"]      

  print(f"Total productos en inventario: {stock_total}")
  print("Total productos por categoria:")
  for categoria, total in categorias.items():
    print(f"Categoria: {categoria}, Total : {total}")    
  print(f"Valor total del inventario: {valor_total}")
  print("Productos con bajo stock:")
  for prod,stock in debajo_umbral.items():
    print(f"Producto: {prod}, Stock: {stock}")

def ordenar():  
  print("1.- Ordernar por precio")
  print("2.- Ordenar por stock")
  print("3.- Ordenar por categoria")
  print("4.- Ordenar por nombre") 
  ordenarPor = int(input("Elija una opcion:"))
  if ordenarPor == 1:
    list_products.sort(key=lambda x:x["Precio"])
    print(list_products)
  elif ordenarPor ==2:
    list_products.sort(key=lambda x:x["Stock"])
    print(list_products)
  elif ordenarPor ==3:
    list_products.sort(key=lambda x:x["Categoria"])
    print(list_products)
  elif ordenarPor ==4:
    list_products.sort(key=lambda x:x["Producto"])
    print(list_products)  
  else:
     print("Opcion incorrecto")      
  
def imprimir():
  try:
    print("Productos a guardar:", list_products) 
    with open("inventario.txt","w", encoding="utf-8") as file:
      json.dump(list_products, file, indent=4)
      print("Archivos generados en:", os.getcwd())
  except Exception as e:
    print("Error al generar el json:",e)    

  try:
    with open("inventario.csv","w",newline="", encoding="utf-8") as csvFile:
        campos = ["Producto","Codigo unico","Precio","Stock","Categoria"]
        writer = csv.DictWriter(csvFile,fieldnames=campos)
        writer.writeheader()
        for product in list_products:
          writer.writerow(product)
        print("Archivos generados en:", os.getcwd())
  except Exception as e:
    print("Error al generar el excel:",e)        


while True:
  opcion = 0  
  print("1.-Añadir un nuevo producto")
  print("2.-Búsqueda Avanzada con Wildcards")
  print("3.-Actualización de Productos por Cualquier Campo")
  print("4.-Eliminación de Productos por Cualquier Campo")
  print("5.-Análisis del Inventario")
  print("6.-Generar archivos")
  print("7.-Ordenar")
  print("8.-Salir")
  opcion = int(input("Elija una opcion(1-8): "))  
  if opcion == 1:
      agregar_products()
  elif opcion ==2:
       busqueda_avanzanda()
  elif opcion ==3:
      modificar_productos()
  
  elif opcion ==4:
      eliminar_productos()
  
  elif opcion ==5:
      
      definir_umbral= float(input("Escribe el precio minimo de stocks:"))
      calcular_cantidad(definir_umbral)
  elif opcion ==6:
      imprimir()

  elif opcion ==7:
      ordenar()

  elif opcion == 8:
      print("Gracias por su visita")
      break
  
  else:
      print("Opcion no valida")   