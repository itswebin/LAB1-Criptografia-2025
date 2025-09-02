def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():  # solo letras
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
        else:
            resultado += char  # deja espacios y símbolos igual
    return resultado


if __name__ == "__main__":
    # Pedir datos al usuario
    texto = input("Ingrese el texto a cifrar: ")
    desplazamiento = int(input("Ingrese el número de desplazamientos: "))

    resultado = cifrado_cesar(texto, desplazamiento)
    print("\nTexto resultante:", resultado)
