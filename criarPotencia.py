# Criando um decorador sem notação
def criar_potencia(x): #x^y
  def potencia(y):
    return x ** y
  return potencia

# Potência de 5 elevado a 10
resultado = criar_potencia(55)
print(resultado(3))