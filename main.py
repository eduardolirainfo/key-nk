def converter_para_teclado(palavra):
    teclas = {'a': '2', 'b': '22', 'c': '222',
              'd': '3', 'e': '33', 'f': '333',
              'g': '4', 'h': '44', 'i': '444',
              'j': '5', 'k': '55', 'l': '555',
              'm': '6', 'n': '66', 'o': '666',
              'p': '7', 'q': '77', 'r': '777', 's': '7777',
              't': '8', 'u': '88', 'v': '888',
              'w': '9', 'x': '99', 'y': '999', 'z': '9999',
              ' ': '0'}

    resultado = ''
    for letra in palavra:
        if letra.lower() in teclas:
            if resultado and resultado[-1] != '0':
                resultado += ' '
            resultado += teclas[letra.lower()]
        else:
            resultado += letra

    return resultado


palavra = input("Digite uma palavra: ")
resultado = converter_para_teclado(palavra)
print("Saída:", resultado)
