# calculo da media escolar

# Defininido as variaveis nesse caso as notas 1, 2, 3, e 4, usando o float para que o usuario possa digitar numeros com virgula
nota1 = float(input("primeira nota: "))
nota2 = float(input("segunda nota: ")) # ops: lembrando que a função input e usada para o usuario digitar algo
nota3 = float(input("terceira nota: "))
nota4 = float(input("quarta nota: "))

# variavel frequencia seria de faltas, usando int para que o usuario digite apenas numeros inteiros
frequencia = int(input("digite a frequencia: "))

# usando if para verificar se o usuario foi aprovado ou reprovado

if (frequencia > 75):  # estrutura de condição
    # calculo da média escolar, as notas 1, 2, 3, e 4 são somadas e divididas por 4 que é a quantidade de notas
    media = (nota1 + nota2 + nota3 + nota4) / 4

    # usando if para verificar se o usuario foi aprovado ou reprovado

    if (media >= 7):  # calculando se a média é maior ou igual a 7
        print("aprovado, média: ", media) # se for maior ou igual é aprovado e a média é mostrada

    elif (media > 4): # se a média é menor que 7 e maior que 4, o aluno tem a possibilidade de fazer recuperação
        print("recuperação ") # aparecera a mensagem de recuperação

    else:
        # se a média for menor que 4, o aluno é reprovado e a média é mostrada
        print("reprovado, média: ", media)

# usando else para verificar se o usuario foi reprovado por falta

else:  # sendo reprovado diréto por falta
    print("reprovado por falta, frequencia:", frequencia)

# OBSERVAÇÃO: nesse caso foi usado if, uma estrutura de condição para dar opções de escolha para o usuario,
# dos numeros que forem colocado pelo usuario, pode se observar que acima foi utilizado um (elif) a principal diferença
# entre o (elif) e o (else) é que o elif possibilita continuar a estrutura de repetição, seria meio que uma variação
# entre o (if) e o (else) que apenas finalizaria a estrutura caso o dado colocado dentro da estrutura fosse falso.
