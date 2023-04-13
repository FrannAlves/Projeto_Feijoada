#********************COMEÇO DA FUNÇÃO VOLUME_FEIJOADA********************
def volume_feijoada():#funcao para a quantidade de feijoada que o usuario deseja compar
    while True:
        try:
            volume = int(input('Qual a quantidade de feijoada que deseja (ml)?\n>>'))
            if (volume >= 300) and (volume <= 5000):
                return volume * 0.08
            elif volume < 300:#caso o usuario digite um valor abaixo de 300 aparece a mensagem do print abaixo e retorna para o começo do laço
                print('nao aceitamos porções menores que 300ml e maiores que 5l. Tente novamente.')
                continue
            elif (volume > 5000):#se digitar acima de 5000 tambem aparece a mensagem e retorna para o começo do laço
                print('nao aceitamos porções menores que 300ml e maiores que 5l. Tente novamente.')
                continue
        except: ValueError#try except trata erros,no caso se o usuario digitar um valor nao numerico
        print('Voce digitou um valor nao numérico')
#**********************FIM DA FUNÇÃO VOLUME_FEIJOADA*********************


#********************COMEÇO DA FUNÇÃO OPÇÃO_FEIJOADA*********************
def opcao_feijoada():#funcao pede para o usuario digitar a opçao desejada
    while True:
        opcao = input('Entre com a opção desejada:\nMENU OPÇÃO FEIJOADA\nb- Básica (feijão + paiol +costelinha\np- Premium (feijão + paiol +costelinha + partes do porco\ns- Suprema (feijão + paiol +costelinha + partes do porco + calabresa + bacon)\n>>')
        if opcao == 'b':
            return 1.00
        elif opcao == 'p':
            return 1.25
        elif opcao == 's':
            return 1.50
        else:
            print('opcao invalida')#caso o usuario digite uma opçao que nao esta no menu aparece a mensagem do print e retorna para o começo do laço
            continue
#***********************FIM DA FUNÇÃO OPÇÃO_FEIJOADA*********************

#*******************COMEÇO DA FUNÇÃO ACOMPANHAMENTO_FEIJOADA*************

def acompanhamento_feijoada():
    soma = 0#variavel para somar os valores dos acompanhamentos escolhidos
    while True:
        try:
            acompanhamento = int(input('Deseja mais algum acompanhamento?\n'+
                                       '0- Não desejo mais acompanhamentos (Encerrar pedido)\n'+
                                       '1- 200g de arroz\n'+
                                       '2- 150g de farofa especial\n'+
                                       '3- 100g de couve cozida\n'+
                                       '4- 1 laranja descascada\n'+
                                       '>>'))
            if acompanhamento == 0:
                print('Pedido encerrado.')#caso digite 0 o pedido é encerrado
                return soma + 0
            elif acompanhamento == 1:
                soma+= 5
                continue
            elif acompanhamento == 2:
                soma += 6
                continue
            elif acompanhamento == 3:
                soma += 7
                continue
            elif acompanhamento == 4:
                continue
                soma += 3
                continue
            else:
                print('opção Invalida.Digite o número referente a opção que deseja escolher.')
                continue
            print('MENU ACOMPANHAMENTO FEIJOADA')
        except ValueError:
            print('opção Invalida.Digite o número referente a opção que deseja escolher:')


#*******************FIM DA FUNÇÃO ACONPANHAMENTO_FEIJOADA****************

#***********************************COMEÇO DA MAIN*****************************
print('Bem vindo a Casa da Feijoada')
print('O valor total a pagar é R$ {:.2f}'.format(volume_feijoada() * opcao_feijoada() + acompanhamento_feijoada()))#aqui foram chamadas as tres funções e feito o calculo final que mostra o valor que o cliente deve pagar

#**************************************FIM DA MAIN*****************************

