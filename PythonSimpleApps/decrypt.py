
# Define una función para encontrar la verdadera letra con una cantidad especificada
def lasso_letter( letter, shift_amount ):
    # Invoca la funcion para traducir la letra a su codigo ASCII
    # Guarda el código de la letra en la variable
    letter_code = ord(letter.lower())

    # Representación número ASCII de la letra 'a' minuscula
    a_ascii = ord('a')

    # El número de letras en el alfabeto
    tamanio_alfabeto = 26

    # La formula calcula el número ASCII para decodificar la letra
    # Tenga en cuenta la repetición del alfabeto
    true_letter_code = a_ascii + (((letter_code - a_ascii) + shift_amount) % tamanio_alfabeto)

    # Convierte el número ASCII a la letra
    decoded_letter = chr(true_letter_code)
    # Devolvemos la letra decodificada
    return decoded_letter


# Desplaza las letras de una palabra por una cantidad determinada para descubrir la palabra oculta
def lasso_word(word, shit_amount):

    # Esta variable se actualiza cada vez que se descodifica otra letra
    decode_word = ""

    # Este bucle for itera por cada letra del parámetro de la palabra
    for letra in word:
        decode_letter = lasso_letter(letra, shit_amount) # La funcion lasso_letter() se invoca con cada letra y la cantidad de desplazamiento.
        # El resultado (letra descodificada) se almacena en una variable llamada decode_letter.
        print(letra+":"+decode_letter)

    # El valor decode_letter se agrega al final del valor decode_word + decode_letter
    decode_word =  decode_word + decode_letter

    # El valor de decode_word se deuelve a la linea de codigo que invoco esta función
    return decode_word


# Intentar decodificar
print( "Tierra con un desplazamiento de 13: \n" + lasso_word( "Tierra", 13 ) )
print( "Ncevy con un desplazamiento de 13 gives: \n" + lasso_word( "Ncevy", 13 ) )
print( "gpvsui con un desplazamiento de 25 gives: \n" + lasso_word( "gpvsui", 25 ) )
print( "ugflgkg con un desplazamiento de -18 gives: \n" + lasso_word( "ugflgkg", -18 ) )
print( "wjmmf con un desplazamiento de -1 gives: \n" + lasso_word( "wjmmf", -1 ) )

print( "p con un desplazamiento de -1 gives: \n" + lasso_word( "p", -2 ) )