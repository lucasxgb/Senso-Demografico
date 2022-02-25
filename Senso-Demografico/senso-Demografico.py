#/*******************************************************************************
#Autor: Lucas Gabriel da Silva Lima Reis
#Componente Curricular: Algoritmos I
#Concluido em: 14/08/2019
#******************************************************************************************/

#função para transformar os arquivos em dicionarios
def dicionario(arquivo, segundo, ultimo):#parâmetros utilizados para fazer a transformação
    arquivo_dic = {}
    if arquivo == "tecnicosIBGE.txt":#condicional para que se o arquivo tiver o nome de tecnicos ele abrir sem precisar inserir a codificação "UTF8"
        arquivo = open(arquivo, "r") #abrindo o arquivo em mode de leitura
        next(arquivo) #pulando a primeira linha do arquivo
        for line in arquivo: #pra cada linha no arquivo
            arquivo = line.strip().split(';') #ele vai fazer a iteração dos itens, para tirar os espaços, o '\n' e o ;
            arq_dic = {arquivo[0]: arquivo[(segundo):(ultimo)]} #definindo as chaves e os valores do dicionario
            arquivo_dic.update(arq_dic) #atualizando o valor do dicionario
    else:
        arquivo = open(arquivo, "r", encoding="utf8") #se o nome do arquifo for diferente de tecnicos ibge ele insere a codificação utf8
        next(arquivo) #pula a primeira linha do arquivo
        for line in arquivo:#aqui ele repete os mesmos passos do dic anterior
            arquivo = line.strip().split(';')
            arq_dic = {arquivo[2]: arquivo[segundo:ultimo]} #o que se altera é a chave, pois para validação precisamos de chaves diferente
            arquivo_dic.update(arq_dic)
    return arquivo_dic #retorna o dicionario


def validar(indice): #função para validar os itens
    validos = 0 #contador para os tecnicos e regioes validos
    invalidos = 0 #contador para os tecnicos e regioes invalidas
    faltam = [] #lista para adicionar os valores que faltam
    dic_tec = dicionario('tecnicosIBGE.txt', 1, 4) #utilizando a função dicionario para abrir e transformar os arquivos em dicionario
    dic_reg = dicionario('regioes.txt', 1, 6) #utilizando a função dicionario para abrir e transformar os arquivos em dicionario
    exe = open('ExemploPesquisa.txt', 'r', encoding='utf8') #abrindo o exemplo pesquisa separadamente para fazer a verificação dos itens de tecnicos e regioes
    next(exe)
    for line in exe: #realizando a iteração dos itendos no arquivo exemplos, para transformalo em uma lista
        exemplo = line.strip()
        pesquisa = exemplo.split(';')
        if indice == 'dic_tec': #verificando os parâmetros pois se o indice for igual a dic_tec, ele tem que verificar os itens em pesquisa[0]
            if pesquisa[0] in dic_tec.keys(): # se a pesquisa [0] estiver nas chaves do dicionario tecnicos o contador recebe +=1 pra cada linha no arquivo exe
                validos += 1
                tecok = 'Todos os tecnicos estão cadastrados ☑' #variavél local para retornar printar ao usuário se o tecnico está ou não cadastrado
            else:
                invalidos += 1 #se os indices em pesquisa[0] não tiverem nas chaves do dicionario
                faltam.append(pesquisa[0]) #a lista vazia criada antes recebe os itens que não são validos
                tecerro = faltam #retornando a variavel para o erro
        if indice == 'dic_reg': #verificando os parâmetros pois se o indice for igual a dic_reg, ele tem que verificar os itens em pesquisa[1]
            if pesquisa[1] in dic_reg.keys():#se a pesquisa [1] estiver nas chaves do dicionario regioes o contador recebe +=1 pra cada linha no arquivo exe
                validos += 1 #contador recebendo +1
                regok = 'Todas as regiões estão cadastradas ☑ ' #variavél local para retornar printar ao usuário se a região está ou não cadastrada
            else:
                invalidos += 1 # se os indices em pesquisa[1] não tiverem nas chaves do dicionario
                faltam.append(pesquisa[1])#adicona as regioes invalidas nas pesquisas
                regerro = faltam #retorna o erro
    exe.close()#fechando o arquivo para baixar o acoplamento na memoria
    if indice == 'dic_tec':#verificando pelos indices os retornos que tiveram no questionario acima para finalizar a validação
        if invalidos > 0:
            return tecerro #se os tecnicos invalidos forem maiores que 0 ele vai retornar o erro nos tecnicos
        else:
            return tecok #se nao ele retorna o ok
    if indice == 'dic_reg':
        if invalidos > 0:
            return regerro # o mesmo acontece para região
        else:
            return regok


import sys #importação da biblioteca sys para fechar o programa bruscamente se tiver algum erro na validação


def erro():#confirmação da validação utilizando a função validar
    confirmando_tec = validar('dic_tec')#definir uma variavél para os dois dicionarios
    confirmando_reg = validar('dic_reg')
    if type(confirmando_tec) == str: #utilizar condicionais para verificar o retorno do erro, ou se está ok
        print('')
        print('\033[4;34m' + confirmando_tec + '\033[0;0m')
        print('')
    elif type(confirmando_tec) == list: #se o valor retornado for uma lista ele printa o erro, pois a lista foi atribuida ao erro na função validar
        print('\033[4;31m' + 'ARQUIVO INVALIDO !!! TECNICOS NÃO CADASTRADOS XXX : {}'.format(confirmando_tec))
        sys.exit()
    if type(confirmando_reg) == str: # o mesmo ocorre para o dicionario de regioes
        print('\033[4;34m' + confirmando_reg + '\033[0;0m')
        print('')
    elif type(confirmando_tec) == list:
        print('\033[4;31m' + 'ARQUIVO INVALIDO !!! REGIOES NÃO CADASTRADAS XXX: {}'.format(confirmando_reg))
        sys.exit()


def funcaoerro(): #chamada da função de erro dentro do programa
    err0 = erro()


def resp1(): #respondendo a primeira questão
    exe = open('exemploPesquisa.txt', 'r', encoding='utf8')#abri o arquivo, pulei uma linha adicionei um contador a essa linha:
    next(exe) #pular a primeira linha do arquivo
    c = 0
    for line in exe:# analisei pra cada linha no arquivo exe ele vai adicionar o contador +1
        c += 1
    print('=' * 60)
    print('O número de domicilios utilizados para coleta foram de:')
    print('')
    print(c) #ao fim ele vai printar a quantidade de linhas no arquivo, que equivale ao total de pesquisas
    print('')
    print('=' * 60)
    exe.close()


import collections #importar a biblioteca collections para realizar as contas dos valores


def resp2():
    exe = open('exemploPesquisa.txt', 'r', encoding='utf8')
    next(exe)
    c = 0 #informando os contadores necessarios para obter o valor de cada resposta
    c1 = 0
    c2 = 0
    for line in exe: #iterando o arquivo
        exemplo = line.strip()
        pesquisa = exemplo.split(';')
        for line in pesquisa[3]: #lendo linha por linha do indice [3] de pesquisa que é o indice necessario para a resposta
            c += line.count('1') #utilizando o metódo count para contar quantos valores daquele item tem, linha por linha do arquivo
            c1 += line.count('5')
            c2 += line.count('6')
    print('=' * 60) #printando respostas
    print('O número de domicilios particulares, já pagos:')
    print('')
    print(c)
    print('')
    print('O número de domicilios particulares, sendo pagos:')
    print('')
    print(c1)
    print('')
    print('O número de domicilios particulares,alugados:')
    print('')
    print(c2)
    print('')
    print('=' * 60)
    exe.close()

def resp3():
    reg = open('regioes.txt', 'r', encoding='utf8') #abrindo os arquivos para a resposta
    next(reg)
    exe = open('exemploPesquisa.txt', 'r', encoding='utf8')
    next(exe)
    for line in exe:
        exemplo = line.strip()
        pesquisa = exemplo.split(';')
        for line in pesquisa[6]: #verificando linha por linha do indice pesquisa[6] que são os indices necessarios para a resposta
            c = 0 #contador para calcular todas as respostas
            c1 = 0 #contador para respostas negativas
            if line > '0': #se o valor da linha for maior que 0 o contador recebe + 1 senão o c1 recebe +1
                c += 1
            else:
                c1+= 1
            for line in reg:
                regioes1 = line.strip()
                regioes2 = regioes1.split(';')
                nome = regioes2[1] #definindo os nomes das regiões, que estão no indice [1]
                print('Na cidade de {}'.format(nome)) #printando todas as respostas
                print('=' * 60)
                print('O número de domicilios que possue banheiro é:')
                print(c)
                print('=' * 60)
                print('O número de domicilios que não possue banheiro é:')
                print(c1)
                print('=' * 60)
    exe.close()
    reg.close()


def resp6():
    exe = open('exemploPesquisa.txt', 'r', encoding='utf8')
    next(exe)
    c = 0 #criando contadores para realizar o calculo de quantas vezes o indice aparece naquela lista
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    d = 0 #atribuindo um contador extra que irar contar o numero de linhas para fazer a porcentagem
    for i in exe:
        line = i
        exemplo = line.strip()
        pesquisa = exemplo.split(';')
        d+=1 #pra cada linha o contador extra recebe +1
        for line in pesquisa[18]: #ele vai percorrer linha por linha no item pesquisas[18] que é onde estão as raças
            c += line.count('1') #cada contador recebe a soma de todos os indices dentro daquela lista
            c1 += line.count('2')
            c2 += line.count('3')
            c3 += line.count('4')
            c4 += line.count('5')
    branca = (c/d)*100 # atribuimos uma variavél, para realizar o percentual dividimos o tando de itens do contador pelo tamanho do d, e ao fim mutiplicamos por 100
    preta = (c1/d)*100 #para obter os resultados e porcentagens
    amarela = (c2/d)*100
    parda = (c3/d)*100
    indigena = (c4/d)*100
    print('Percentual de moradores que participaram da entrevista por cor ou raça.') #printando as respostas
    print('=' * 60)
    print('Brancos : {}%'.format(branca))
    print('Preta : {}%'.format(preta))
    print('Amarela : {}%'.format(amarela))
    print('Parda : {}%'.format(parda))
    print('Indigena : {}%'.format(indigena))
    print('=' * 60)
    exe.close()


def resp7():
    listco = ['GO','DF', 'MT', 'MS'] #atribuindo as siglas de cada estado a uma lista com nomes esquivalentes #lista centro oeste
    listn = ['AC', 'AP','AM','PA','RO', 'RR' ,'TO'] #lista norte
    listanordest = ['AL', 'BA', 'CE', 'MA', 'PB', 'PI', 'PE','RN', 'SE'] #lista nordeste
    listsul = ['PR', 'SC', 'RS'] #lista sul
    listsudeste = ['SP', 'MG',  'RJ', 'ES'] #lista sudeste
    regioes = open('regioes.txt','r', encoding='utf8')
    next(regioes)
    for line in regioes: #iterando o arquivo regioes
        regi = line.strip()
        cadastror = regi.split(';')
        cco = 0 #criando um contador para cada regiaão #regiao centro oeste
        cn = 0 #contador norte
        cnordest = 0 #contador nordeste
        csul = 0 #contador sul
        csudeste = 0 #contador sudeste
        for line in regioes: #pra cada linha no arquivo regioes
            if cadastror[3] in listanordest: #ele vai verificar no indice [3] se aquela regiao faz parte dessa lista
                cnordest += 1
            elif cadastror[3] in listn: #se a regiao fizer parte seu contador vai receber +1 para cada valor
                cn +=1
            elif cadastror[3] in listsul:
                csul +=1
            elif cadastror[3] in listsudeste:
                csudeste +=1
            elif cadastror[3] in listco:
                cco += 1
        if cco > cn and cco > cnordest and cco > csul and cco > csudeste: #ao final ele vai comparar cada contador, para printar a regiao que aparece mais vezes
            print('='*60)
            print('A Região com maior Numero de Munícipios pesquisados é o CENTRO-OESTE.')
            print('=' * 60)
        elif cn > cco and cn > cnordest and cn > csul and cn > csudeste:
            print('=' * 60)
            print('A Região com maior Numero de Munícipios pesquisados é o NORTE.')
            print('=' * 60)
        elif cnordest > cco and cnordest > cn and cnordest > csul and cnordest > csudeste:
            print('=' * 60)
            print('A Região com maior Numero de Munícipios pesquisados é o NORDESTE.')
            print('=' * 60)
        elif csul > cco and csul > cn and csul > cnordest and csul > csudeste:
            print('=' * 60)
            print('A Região com maior Numero de Munícipios pesquisados é o SUL.')
            print('=' * 60)
        elif csudeste > cco and csudeste > cn and csudeste > cnordest and csudeste > csul:
            print('=' * 60)
            print('A Região com maior Numero de Munícipios pesquisados é o SUDESTE.')
            print('=' * 60)
    regioes.close()

def menu(): #criação de um menu para exibição da respostas
    funcaoerro() #iniciando a função erro pois se tiver algum erro o programa não vai rodar
    c = 0 #atribuindo um contador inicialmente em 0
    print('''[1] = Digite para entrar no programa
[0] = Digite para sair ''')
    c = int(input('Informe sua escolha:'))#mostrando as opções de escolha e perguntando ao usuário o que ele deseja
    if c == 1: #se a resposta dele for maior que zero ele entra no programa
            print('=' * 60)
            print('Bem - Vindo ao Censo demografico 2020')#informando ao usuário o processo que acontece dentro do menu
            print('')
            print('Existem 7 estatisticas ao todo')
            print('')
            print('No momento só é possivel á visualização de 5 estatísticas')
            print('')
            print('As estatisticas 4 e 5 estão INDISPONIVEIS!!!')
            print('')
            print('Você pode vizualizar as respostas de dois modos: ') #exibindo e perguntando qual modo de exibição o usuário quer
            print('Modo [1] uma estatistica:')
            print('Modo [2] mais de uma estatística')
            print('=' * 60)
            modo = int(input('DIGITE O MODO DE VISUALIZAÇÃO:'))
            print('')
            print('=' * 60)
            print('Escolha qual estatística que vizualizar') #printando as estatiscticas disponiveis para o usuário
            print('[ 1 ] = Primeira Estatística')
            print('[ 2 ] = Segunda Estatística')
            print('[ 3 ] = Terceira Estatística')
            print('[ 6 ] = Sexta Estatística')
            print('[ 7 ] = Sétima Estatística')
            print('=' * 60)
            while c > 0: #criando um loop de repetição para repruduzir o programa até o usuário decidir sair
                if modo == 1: # o modo que de vizualização que o usuario digitar for igual a um
                    print('Para vizualizar uma unica estatística digite o seu número:')
                    n = int(input('Qual estatistica Você quer ver?')) #perguntar qual estátistica o usuario quer ver
                    if n == 1: #dependendo da resposta ele ira printar a estatistica
                        a = resp1()
                    elif n == 2:
                        a = resp2()
                    elif n == 3:
                        a = resp3()
                    elif n == 6:
                        a = resp6()
                    elif n == 7:
                        a = resp7()
                    else: #se ele digitar uma estatistica errada aparece pra ele tentar novamente
                        print('')
                        print('Você digitou uma estatística invalida')
                        print('')
                    print('''[1] = Quer ver outra estatística?
[0] = Digite para sair ''')
                    c = int(input('Informe sua escolha:'))#depois das respostas perguntar se o usuario quer ver outra estatistica
                    if c == 0: #se ele responder que 0 o programa fecha
                        print('=' * 60)
                        print('')
                        print('Muito obrigado, volte sempre, programa foi finalizado!!!!!')
                        print('')
                        print('=' * 60)
                elif modo ==2: # se o usuario digitar o modo 2 ele printa todas as estatisticas de uma vez só
                    resp1(),resp2(),resp3(),resp6(),resp7()
                    print('''[1] = Quer ver outra estatística?
    [0] = Digite para sair ''')
                    c = int(input('Informe sua escolha:'))
    elif c==0:
        print('Muito obrigado, volte sempre, programa foi finalizado!!!!!') #se o usuário digitar 0 o programa fecha



print(menu())

