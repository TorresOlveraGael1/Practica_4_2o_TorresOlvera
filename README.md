# Practica_4_2o_TorresOlvera

Torres Olvera Gael

En esta practica realizamos multiples codigos en python

# Punto 1.

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

![image](https://github.com/user-attachments/assets/fd215aa2-23bd-4a30-89e1-a4368e631d8a)
![image](https://github.com/user-attachments/assets/cedcff0a-30c9-493d-9566-c6e239d3bfa7)

# Punto 2.

#En este programa realizaremos un codigo que traduzca una palabra que ya establecimos en otra

print (" ")

print ("Torres Olvera Gael")

print (" ")


#Diccionario de traducción predefinido, seleccionando unas cuantas palabras

diccionario_traduccion = {

    "hola": "hello",
    
    "adiós": "goodbye",
    
    "mundo": "world",
    
    "gracias": "thank you",
    
    "por favor": "please",
    
    "sí": "yes",
    
    "no": "no",
    
    "buenos días": "good morning",
    
    "buenas tardes": "good afternoon",
    
    "buenas noches": "good night"
    
}

#Función para traducir una frase que ya se encuentre en el diccionario

def traducir_frase(frase, diccionario):

    palabras = frase.split()
    
    traduccion = []
    
    palabras_no_encontradas = []

    for palabra in palabras:
    
        if palabra in diccionario:
        
            traduccion.append(diccionario[palabra])
            
        else:
        
            traduccion.append(palabra)
            
            palabras_no_encontradas.append(palabra)

    return ' '.join(traduccion), palabras_no_encontradas

#Entrada del usuario, lo que establece el punto de origen para el codigo

frase_espanol = input("Introduce una frase en español para traducir: ")

frase_traducida, palabras_no_encontradas = traducir_frase(frase_espanol, diccionario_traduccion)

print("Frase traducida:", frase_traducida)

if palabras_no_encontradas:

    print("Palabras no encontradas en el diccionario:", ', '.join(palabras_no_encontradas))

![image](https://github.com/user-attachments/assets/07c5a475-976d-43bc-8234-0e9d1c5526df)
![image](https://github.com/user-attachments/assets/916c4da2-7203-476d-a775-321ecf70f316)

