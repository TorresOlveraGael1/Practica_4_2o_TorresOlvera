#En este programa realizaremos un codigo que meta la informacion de un usuario

print (" ")
print ("Torres Olvera Gael")
print (" ")


#Crear un diccionario para almacenar la información del usuario

usuario = {
    'nombre' : ' ',
    'edad' : ' ',
    'sexo' : ' ',
    'telefono' : ' ',
    'gmail': ' '
}

#Solicitar información al usuario
usuario['nombre'] = input("Introduce tu nombre: ")
usuario['edad'] = input("Introduce tu edad: ")
usuario['sexo'] = input("Introduce tu sexo: ")
usuario['telefono'] = input("Introduce tu numero telefonico: ")
usuario['gmail'] = input("Introduce tu gmail: ")
print (" ")

#Mostrar la información en el formato deseado
print(f"El nombre del usuario es: {usuario['nombre']}")
print (" ") 
print (f"El usuario tiene: {usuario['edad']} años,")
print (" ") 
print (f"El usuario es: {usuario['sexo']}")
print (" ") 
print (f"su número de teléfono es: {usuario['telefono']}.")
print (" ") 
print (f"El correo electronico del usuario es: {usuario['gmail']}")
print (" ")