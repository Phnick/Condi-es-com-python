#Condicionais

if 9<7:
    print('Condição verdadeira')
else:
    print('Condição falsa')  


# Uso do > ou <
idade_maria = int(input('Digite a idade de Maria: '))
idade_pedro = int(input('Digite a idade de Pedro: '))
if idade_maria > idade_pedro:
    print('Maria é mais velha que Pedro')
else:
    print('Pedro é mais velho que Maria ')  



#Uso do >=
empregados_empresa1 = int(input('Digite o número de empregados da empresa 1: '))
empregados_empresa2 = int(input('Digite o número de mepregados da empresa 2: '))
if empregados_empresa1 >= empregados_empresa2:
    print('Empresa 1 tem um número de empregados maior ou igual a empresa 2 ')


#Uso do ==

livro_1 = input('Digite o título do livro 1')
livro_2 = input('Digite o título do livro 2')
if livro_1 == livro_2:
    print('Os dois livros tem o mesmo título')

media = float(input('Digite a sua média: '))
if media >= 6.0:
    print('Aprovado')
else:
    print('Reprovado')    


# Quando tem 3 condições (if), não se usa o else
media = float(input('Digite a sua média: '))
if media >= 6.0:
    print('Aprovado')
if 6.0 > media >= 4.0:
    print('Recuperação')
if media < 4.0:
    print('Reprovado')    


# Elif é usado como um 'se não'
sorteio = int(input('Digite um númedo de 0 a 100: '))
if sorteio == 10:
    print('Parabéns voc~e foi sorteado')
elif sorteio < 10:
    print('Tente mais uma vez!')
else:
    print("Você perdeu")         
