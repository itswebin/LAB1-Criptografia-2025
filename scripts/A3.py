def descifrar_cesar(texto):
    resultados = []
    for d in range(26):  # probar todos los desplazamientos
        resultado = ""
        for char in texto:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                resultado += chr((ord(char) - base - d) % 26 + base)
            else:
                resultado += char
        resultados.append((d, resultado))
    return resultados


def es_mas_probable(texto, diccionario):
    """Cuenta cuántas palabras del diccionario aparecen en el texto"""
    texto_lower = texto.lower()
    return sum(1 for palabra in diccionario if palabra in texto_lower)


if __name__ == "__main__":
    mensaje_cifrado = input("Ingrese el mensaje interceptado: ")
    resultados = descifrar_cesar(mensaje_cifrado)

    # Diccionario básico de palabras comunes en español
    diccionario = ["hola", "mundo", "mensaje", "prueba", "secreto", "texto", "clave"]

    # Calcular puntuación para cada resultado
    puntuaciones = [(d, texto, es_mas_probable(texto, diccionario)) for d, texto in resultados]

    # Ordenar por la puntuación (mayor probabilidad primero)
    puntuaciones.sort(key=lambda x: x[2], reverse=True)

    print("\nPosibles mensajes :\n")
    for d, texto, score in puntuaciones:
        if score > 0:  # si tiene palabras del diccionario → verde
            print(f"\033[92mDesplazamiento {d}: {texto}  <-- más probable\033[0m")
        else:
            print(f"Desplazamiento {d}: {texto}")
