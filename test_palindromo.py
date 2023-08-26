from palindromo import verificar_palindromo

def test_palindromo_True():
    assert verificar_palindromo('radar') == True
    assert verificar_palindromo('A man a plan a canal Panama')



def test_palindromo_False():
    assert verificar_palindromo('python') == False
    assert verificar_palindromo('hello word') == False
   
