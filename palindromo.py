def verificar_palindromo(string):
    string = string.replace('','').lower()
    return string == string[::-1]
input_text = input('digite o texto: ')


if verificar_palindromo(input_text):
    print('é palíndromo')

else:
    print('não é palindromo')


  
