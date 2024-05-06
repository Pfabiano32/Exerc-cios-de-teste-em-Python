# calculadora

# Logo abaixo é definido a logica da calculadora, usando a função def para definir e depois é so puxar no codigo
def adição(x, y):
    return x + y
# Se repete a logica acima nesses 4 casos com adição, subtração, multiplicação e divisão

def subtração(x, y):
    return x - y

def multiplicação(x, y):
    return x * y

def divisão(x, y): # Nesse caso, como não se pode dividir um numero por 0 é necessário um tratamento de erro
    if y == 0 or x == 0: # Se o valor de y for 0 ou x for 0, o programa vai aparecer a mensagem abaixo
        raise ValueError("Não é possível dividir por zero")

    else: # Se não for 0, o programa vai retornar o valor da divisão   
        return x / y

def calculadora(): # Aqui é deifinido a logica da calculadora, como antes, aqui usa a função def 
    while True:  # Cria uma estrutura de loop, no qual se for verdadeira ira vontinuar repetindo o pragrama infinitamente  
        try:
            num1 = float(input("Digite um numero: ")) # Aqui é onde o usuario vai digitar o numero
            operador = input("digite um operador (+, -, *, /): ") # Aqui é onde o usuario vai digitar o operador
            num2 = float(input("digite um numero: ")) # Aqui é onde o usuario vai digitar o segundo numero

            # Aqui é onde é definido o que vai acontecer de acordo com o operador

            if operador == "+":
                resultado = adição(num1, num2)

            elif operador == "-":
                resultado = subtração(num1, num2)
                                                            
            elif operador == "*":
                resultado = multiplicação(num1, num2) # sendo uma estrutura de condição, funcionara de acordo com o operador que o usuario colocar

            elif operador == "/":
                resultado = divisão(num1, num2)

            else:
                print(f"Operador invalido '{operador}', por favor use +, -, *, ou /.")
                continue # a mensagem acima so aparecera se o usuario digitar um operador invalido   
        
            print(f"Resultado é: {resultado}")
        
            continuar = input("Deseja continuar? (s/n): ") # Aqui é onde o usuario vai digitar se ele quer continuar ou não com s ou n
            if continuar.lower() != 's': # caso o usuario digite algo diferente que s, ira fechar o codigo
                print("calculadora desligada")
                break

        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inexperado: {e}")


calculadora()
