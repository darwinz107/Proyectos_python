list_producto_precio = []

def añadir_producto():
  producto = input("Digita un producto: ")
  precio = float(input("Digita un precio: "))
  categoria = input("Digita una categoria: ")

  list_producto_precio.append({"producto":producto, "precio":precio,"categoria":categoria})   

def buscar_producto(nombre):
    contador = 0
    for producto in list_producto_precio:
        if producto["producto"]==nombre:
          print(producto)
          contador +=1
    if contador ==0:
            print("Producto no encontrado")
def eliminar_producto(nombre):
    contador = 0
    for producto in list_producto_precio:
        if producto["producto"] == nombre:
            list_producto_precio.remove(producto)
            contador +=1
    if contador ==0:
            print("Producto no encontrado")
            
def editar_producto(nombre):
    for producto in list_producto_precio:
        contador =0
        opcion = 0
        if producto["producto"] == nombre:
            print("1.-Editar nombre")
            print("2.-Editar precio")
            print("3.- Editar categoria")
            opcion =int(input("Elije una opcion(1-3):"))
            contador +=1
            if opcion == 1:
                nombre_act = input("Atualice el nombre:")
                producto["producto"]=nombre_act
            elif opcion ==2:
                precio_act = int(input("Actualice el precio:"))
                producto["precio"]= precio_act
            elif opcion ==3:
                categoria_act = input("Actualice la categoria:")
                producto["categoria"]= categoria_act    
    if contador ==0:
                print("Producto no encontrado")        
           
        
def filtar_categoria(categoria):
    print(f"**{categoria}**")
    contador =0
    for producto in list_producto_precio:
        if producto["categoria"]==categoria:
            print(producto)
            contador +=1
    if contador ==0:
            print("Producto no encontrado")        
            
def rango_precio(precMin,precMax):
    print(f"**Precios entre {precMin} y {precMax}**")
    contador =0
    for producto in list_producto_precio:
        if producto["precio"] >= precMin and producto["precio"] <= precMax:
            print(producto)
            contador +=1
    if contador ==0:
            print("No hay productos")    
                               

while True:
  opcion = 0  
  print("1.-Ingresar un producto")
  print("2.-Buscar un producto")
  print("3.-Eliminar un producto")
  print("4.-Editar informacion de un producto")
  print("5.-Filtar por categoria")
  print("6.-Filtar por rango de precio")
  print("7.-Mostrar productos ordenados")
  print("8.-Salir")
  opcion = int(input("Elija una opcion(1-8): "))  
  if opcion == 1:
      añadir_producto()
  elif opcion ==2:
       producto_a_buscar = input("Digita el nombre del producto a buscar: ")
       buscar_producto(producto_a_buscar)
  elif opcion ==3:
      producto_eliminar = input("Digite un producto a eliminar:")
      eliminar_producto(producto_eliminar)
  
  elif opcion ==4:
      product_actualizar = input("Digite el nombre del producto para modificar su informacion: ")
      editar_producto(product_actualizar)
  
  elif opcion ==5:
      categoria_filtro = input("Digite la categoria a filtar:")
      filtar_categoria(categoria_filtro)
  elif opcion ==6:
      precio_min = float(input("Digite un precio minimo:"))
      precio_max = float(input("Digite un precio maximo:"))
      rango_precio(precio_min,precio_max)
  elif opcion ==7:
      list_producto_precio.sort(key=lambda x:x["producto"])
      print(list_producto_precio)
  elif opcion == 8:
      break
  
  else:
      print("Opcion no valida")    
      
  
   