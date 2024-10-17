# Diccionario de traducción predefinido
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

# Función para traducir una frase
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

# Entrada del usuario
frase_espanol = input("Introduce una frase en español para traducir: ")
frase_traducida, palabras_no_encontradas = traducir_frase(frase_espanol, diccionario_traduccion)

print("Frase traducida:", frase_traducida)

if palabras_no_encontradas:
    print("Palabras no encontradas en el diccionario:", ', '.join(palabras_no_encontradas))
