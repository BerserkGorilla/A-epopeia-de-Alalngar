#-*- coding: utf-8 -*
import time
import os

def strelevante(string):
    f1 = open('main.sav','r')    
    f2 = open('tmp.sav','w')
    for i in f1:
        if i.startswith("It"):
            break
        f2.write(i)
    f2.write(string+"\n")
    f2.write(i)
    for i in f1:
        f2.write(i)
    f1.close()
    f2.close()
    os.replace('tmp.sav','main.sav')
    print(string)
    time.sleep(2)

def printrelevante():
    f1 = open('main.sav','r')
    for i in f1:
        if i.startswith("It"):
            break
        print(i)
def PuzzleOuro(itens,magias):
    itens = itens
    magias = magias
    strelevante("O corredor da caverna é escuro, apertado e umido")
    time.sleep(0.4)
    strelevante("Um som estrondoso acontece em suas costas, uma pedra fechou a entrada")
    strelevante("Sua única opção é seguir em frente, mas o sacerdote avisou-lhe")
    time.sleep(0.5)
    strelevante("Você chega a um lugar estranho, duas coroas douradas se encontram em um pequeno corpo de água a sua direita.")
    strelevante("Uma das coroas está boiando, enquanto a outra se encontra no fundo do corpo.")
    strelevante("Ao lado desse poço existe um buraco quadrado com cerca de um metro de lado.")
    userInput = ""
    Saida = 0
    while True:
        os.system('cls')
        printrelevante()
        userInput = str(input("Selecione sua ação (itens, magias, ambiente, concentrar) ")).lower()
        if userInput == "itens":
            if itens != []:
                print ("Os itens que carrego comigo são:")
                for m in itens:
                    print(m)
                while True:
                    userInput = str(input("Selecione um item ")).lower().title()
                    if userInput not in itens:
                        print("Opção Inválida")
                    else:
                        print("\'Acho que "+userInput+" não vai me ajudar aqui não\'")
                        print("Para ser sincero, acho que nenhum dos itens irá.")
                        break
            else:
                print("Não estou carregando nenhum item comigo.")
        elif userInput == "magias":
#            if magias = []:
            print("Eu ainda não domino nenhuma magia, o que exatamente eu estou tentando fazer?")
            time.sleep(3)
        elif userInput == "ambiente":
            print("Você pode se aproximar do buraco, da água ou da porta:")
            print("Comandos:buraco,agua,porta")
            userInput = str(input())
            if userInput == "buraco":
                print("Você se aproxima do buraco e olha dentro dele")
                print("Tudo o que você consegue ver é a escuridao.")
                print("Esse lugar passa a sentenca do sofrimento eterno, do qual nunca se sai")
                print("Provavelmente esse lugar esta ligado ao Rei da Noite.")
                time.sleep(6)
            elif userInput == "agua":
                    print("Você se aproxima do corpo de água")
                    print("De alguma forma você sabe que deve jogar uma das coroas dentro do buraco")
                    print("Mas e agora, como decidir entre elas?")
                    print("Comandos: boiando, afundada")
                    userInput = str(input())
                    strelevante("É isso!")
                    if userInput == "boiando":
                        strelevante("Você retira a coroa boiando da água. Nada parece estranho")
                        strelevante("Ao carregá-la ate o buraco Você não sente nada de diferente")
                        strelevante("A coroa é jogada e desaparrece no breu")
                        time.sleep(5)
                        strelevante("Alguns segundos se passam")
                        strelevante("Uma risada pode ser ouvida ao fundo, macabra e penetrante")
                        strelevante("Você sente o chão se abrindo e cai em meio a escuridão")
                        break
                    elif userInput == "afundada":
                        strelevante("Você retira a coroa afundada da água. Nada parece estranho")
                        strelevante("Ao carregá-la ate o buraco Você não sente nada de diferente")
                        strelevante("A coroa é jogada e desaparrece no breu")
                        time.sleep(5)
                        strelevante("Alguns segundos se passam")
                        strelevante("E então a enorme porta se abre em sua frente, liberando a passagem.")
                        strelevante("À sua frente se apresenta uma escada, esse parece ser o unico caminho.")
                        strelevante("Você começa a descer a escada")
                        time.sleep(2)
                        strelevante("Eventualmente a porta atrás de você desaparece e a escada parece ainda não ter fim")
                        time.sleep(5)
                        strelevante("Muito tempo se passa")
                        time.sleep(0.5)
                        strelevante("O fim da escada se torna vísivel, de um lado um precipicio, do outro, ao longe, o caminho de saida.")
                        time.sleep(0.5)
                        strelevante("O chão parece ser de gelo, é muito escorregadio. Seria impossivel atravessar andando")
                        time.sleep(0.3)
                        strelevante("Você consegue alcançar a pedra.")
                        Saida = 1
                        break
                    
            elif userInput == "porta":
                print("Você se aproxima da porta, ela parece pesada demais para ser movida")
                print("A porta tem vários inscritos em uma língua que você nunca viu antes.")
                time.sleep(3)
            else:
                print("Opção Inválida")
                time.sleep(2)
            
        elif userInput == "concentrar":
            print("o Sacerdote disse algo sobre isso:")
            print("O Rei da Noite é o ser mais ganancioso sob os ceus.")
            print("Aqueles pegos em sua armadilha deverão deixar algo de valor em peso para saírem.")
            time.sleep(7)
        else:
            print("Opção Inválida")
            time.sleep(5)
    return Saida
	
def PunicaoRN(itens,magias):
    itens = itens
    magias = magias
    strelevante("Uma risada maléfica é o que Você escuta vindo da escuridao")
    time.sleep(1)
    strelevante("HAHAHAHAHAHAHAHAHAHA pequenino")
    strelevante("\'Achou mesmo que uma replica me satisfaria? hahaha\'")
    strelevante("\"Eu sou o Rei da Noite, ninguem nunca foi capaz de escapar da minha punição eterna hahahaha\"")
    time.sleep(6)
    strelevante("Você nao sabe quanto tempo se passou")
    time.sleep(1)
    strelevante("Nada a sua volta é visivel.")
    strelevante("Ao longe e possivel ver uma pedra que parece bem pequena.")
    time.sleep(1)
    strelevante("Essa parece ser a unica coisa identificável")
    time.sleep(0.8)
    while True:
        ex = 0
        os.system('cls')
        printrelevante()
        userInput = str(input("Selecione sua ação (itens, magias, ambiente, concentrar) ")).lower()
        if userInput == "itens":
            if itens != []:
                print ("Os itens que carrego comigo são:")
                #print("itens", ex)
                for m in itens:
                    print(m)
                while True:
                    if ex == 1:
                                break
                    userInput = str(input("Selecione um item ").lower().title())
                    if userInput not in itens:
                        print("Opcao inválida")
                    elif userInput == "Bloco De Metal":
                        print("Bom, acho que posso arremessar esse bloco....")
                        #print("Arremessar bloco? (sim/nao)")
                        while True:
                            userInput = str(input("Arremessar bloco? (sim/nao) "))
                            #print('Arremessar bloco',ex)
                            if userInput == "sim":
                                userInput = str(input("Em qual direcao? (da pedra/contraria) " ))
                                while True:
                                    if userInput =="da pedra":
                                        itens.pop(itens.index("Bloco De Metal"))
                                        strelevante("Você arremessa o bloco na direcao da pedra")
                                        strelevante("Você percebe que a pedra comeca a se afastar ")
                                        strelevante("\'ISSO NÃO PODE ESTAR ACONTECENDO\'")
                                        time.sleep(2)
                                        strelevante("\' HAHAHAHAHAHAHAAHAHAHAHAHAHA \'-  A risada do rei da noite ecoa na escuridao")
                                        strelevante("Você percebeu que sua aventura se encerrou aqui, o Rei da Noite te derrotou.")
                                        time.sleep(10)
                                        exit()
                                    elif userInput == "contraria":
                                        itens.pop(itens.index("Bloco de metal"))
                                        strelevante("Você arremessa o bloco na direcao contraria da pedra")
                                        strelevante("Você percebe que lentamente a pedra se aproxima de Você")
                                        time.sleep(0.3)
                                        strelevante("Ou melhor, Você se aproxima da pedra")
                                        strelevante("O processo é bem lento, provavelmente Você levara horas")
                                        time.sleep(5)
                                        strelevante("Você alcança a pedra e percebe que ela esta sob um chão de gelo")
                                        strelevante("Uma escada parece descer exatamente para o lugar onde Você se encontra agora")
                                        ex = 1
                                        return itens
                                    else:
                                        print("Opção Inválida")
                                        break
                            elif userInput == "nao":
                                ex = 1
                                break
                            else:
                                print("Opção Inválida")
                    elif ex == 1:
                        break
                    else:
                        print("\'Acho que "+userInput+" não vai me ajudar aqui não\'")
                        break
            else:
                print("Não estou carregando nenhum item comigo.")
        elif userInput == "magias":
            if magias == []:
                print("Eu ainda não domino nenhuma magia, o que exatamente eu estou tentando fazer?")
                time.sleep(5)
        elif userInput == "ambiente":
            print("O ambiente está vazio, um breu completo e apenas uma pedra ao longe")
            time.sleep(5)
        elif userInput == "concentrar":
            print("o Sacerdote disse algo sobre isso:")
            print("O Rei da Noite é o ser mais ganancioso sob os ceus.")
            print("Aqueles pegos em sua armadilha deverão deixar algo de valor em peso para sairem.")
            time.sleep(7)
        else:
            print("Opção Inválida")
			
def PuzzleGelo(itens,magias,Saida):
    itens = itens
    magias = magias
    t = 0
    ex = 0
    while True:
        os.system('cls')
        printrelevante()
        if ex == 1:
            break
        userInput = str(input("Selecione sua ação (itens, magias, ambiente, concentrar) ")).lower()
        if userInput == "itens":
            if itens != []:
                print ("Os itens que carrego comigo são:")
                for m in itens:
                    print(m)
                while True:
                    userInput = str(input("Selecione um item ").lower().title())
                    if userInput not in itens:
                        print("Opção Inválida")
                    else:
                        print("\'Acho que "+userInput+" não vai me ajudar aqui não\'")
                        print("Para ser sincero, acho que nenhum dos itens irá.")
                        break
            else:
                print("Não estou carregando nenhum item comigo.")
        elif userInput == "magias":
            if magias == []:
                print("Eu ainda não domino nenhuma magia, o que exatamente eu estou tentando fazer?")
        elif userInput == "ambiente":
            print("Você está proximo a pedra e a escada")
            while True:
                userInput = str(input("Selecione uma acao:(subir a escada,voltar) "))
                if userInput.startswith("emp") or userInput.startswith("Emp"):
                    strelevante("Você empurra a pedra")
                    time.sleep(1)
                    strelevante("Você percebe que esta se deslocando em direcao a saida")
                    ex = 1
                    break
                elif userInput == "subir a escada":
                    if Saida == 1:
                        print("Essa é a escada que Você acabou de descer")
                        time.sleep(5)
                    else:
                        print("A escadaria é enorme, Você gasta muito tempo para subi-la")
                        time.sleep(5)
                        print("Ao chegar no topo da escadaria, Você vê uma porta que parece muito a da primeira sala")
                        time.sleep(0.5)
                        print("Não parece que Você conseguiria abri-la")
                        print("Você espera para ver se algo acontece")
                        time.sleep(2)
                        print("talvez agora?")
                        time.sleep(2)
                        print("E agora?")
                        time.sleep(2)
                        print("Agora?")
                        time.sleep(2)
                        print("SHAZAM!")
                        time.sleep(2)
                        print("Parece que nada vai acontecer mesmo. Você decide que é melhor descer a escada de volta")
                        time.sleep(5)
                        Saida = 1
                elif userInput == "voltar":
                    break
                else:
                    print("Opção Inválida")
                    time.sleep(4)
            
        elif userInput == "concentrar":
            if t == 0:
                print("Talvez eu devesse explorar mais o ambiente")
                t = 1
                time.sleep(5)
            else:
                print("Acho que eu posso empurar a pedra para tentar me mover")
                time.sleep(7)
        else:
            print("Opção Inválida")
			
def PuzzleElevador(itens, magias):
    strelevante("Você caminha ate alcancar uma colina muito alta, não parece ser possivel escala-lo")
    strelevante("Você esta sobre uma tabua que parece estar presa por uma corda passando por uma roldana no teto")
    strelevante("Essa corda esta presa a uma pedra que esta sobre uma plataforma muito alta")
    strelevante("A sustentacao dessa plataforma é fina")
    while True:
        os.system('cls')
        printrelevante()
        ex = 0
        userInput = str(input("Selecione sua ação (itens, magias, ambiente, concentrar) ")).lower()
        if userInput == "itens":
            if itens != []:
                print ("Os itens que carrego comigo são:")
                for m in itens:
                    print(m)
                while True:
                    if ex == 1:
                            break
                    userInput = str(input("Selecione um item ").lower().title())
                    print(userInput)
                    if userInput not in itens:
                        print("Opcao inválida")
                    elif userInput.startswith("Espada"):
                        while True:
                            userItem = userInput
                            userInput = str(input("Cortar suporte? (sim/nao) "))
                            if userInput == "sim":
                                strelevante("Você usa a sua "+userItem+" para cortar o suporte.")
                                strelevante("Você corta a sustentacao, a pedra cai junto com a base e Você sobe")
                                time.sleep(1)
                                strelevante("Um pequeno salto é o suficiente para alcancar o topo da colina")
                                return
                            elif userInput == "nao":
                                print(" \'Hmmmm, deve ter outra solução. \' ")
                                ex = 1
                                break
                            else:
                                print("Opção Inválida")
                    else:
                        print("\'Acho que "+userInput+" não vai me ajudar aqui não\'")
                        break
            else:
                print("Não estou carregando nenhum item comigo.")
        elif userInput == "magias":
            if magias != []:
                print("Eu ainda não domino nenhuma magia, o que exatamente eu estou tentando fazer?")
            else:
                print("Eu ainda não domino nenhuma magia, o que exatamente eu estou tentando fazer?")
                time.sleep(5)
        elif userInput == "ambiente":
            print("Você está em cima de algo que parece um elevador.")
            time.sleep(2)
            print("O contra peso do elevador está preso por um suporte que pode ser cortado")
            time.sleep(6)
        elif userInput == "concentrar":
            print("Acho que consigo cortar esse suporte com minha espada")
            time.sleep(7)
        else:
            print("Opção Inválida")

if __name__ == '__main__':
    itens = ["Bloco De Metal","Espada Longa", "Espada Curta","Vembrassa"]
    magias = []
    print("Seja muito bem-vindo, Você está jogando \" A epopeia de Alalngar \".")
    time.sleep(1)
    print("Essa é a versão pre-alfa do jogo, que esta sendo desenvolvido por mim e minha enorme equipe.")
    time.sleep(1)
    print("Antes de começar a jogatina acho que vale a pena explicar como funciona o jogo")
    print("Esse jogo é um RPG de texto, simplificando Você deve escrever palavras quando solicitado para realizar acoes")
    print("Acredite, é mais facil do que parece")
    time.sleep(1)
    print("Algumas vezes todas as ações possíveis estarão explicitamente escritas na tela")
    time.sleep(1)
    print("Outras vezes as ações estarão escondidads e Você deverá advinhar a ação a ser tomada")
    time.sleep(1)
    print("Chega de falar")
    print("Bom jogo!!!")
    time.sleep(5)
    os.system('cls')
    strelevante("O reino de Ulk foi amaldicoado pelos deuses.")
    strelevante("Fome e pobreza assolam o reino. Você, Alalngar, o Heroi decide que apenas uma solucao é possível")
    strelevante("Enfrentar os deuses.")
    strelevante("Meshkiangasher II, o sacerdote, alertou-lhe")
    strelevante(" \' Isso é uma insanidade! \' ")
    strelevante("Apesar disso, ele indica o caminho de entrada para o territorio divino")
    strelevante("Uma caverna ao norte de Ulk, dentro da Floresta Proibida")
    strelevante(" \' Se alguém é capaz de fazer uma insanidade dessas, deve ser Você. \' ")
    strelevante("Com essas palavras, o Sacerdote entregou um Bloco de metal pesado para o herói dizendo")
    strelevante(" \' Espero que nao precise disso, mas e melhor ter e nao usar\'.")
    strelevante("O heroi entao se prepara e entra na caverna, sem certeza do futuro que lhe aguarda.")
    Saida = PuzzleOuro(itens,magias)
    if Saida != 1:
        itens = PunicaoRN(itens,magias)

    PuzzleGelo(itens,magias,Saida)
    PuzzleElevador(itens,magias)
    strelevante("A frente é possível ver que o tom verdejante dessa parte da caverna some, dando lugar a paredes de pedra azul brilhante")
    strelevante("Do alto da colina onde Você está é possível ver que a sala e um grande vale, do outro lado do vale Você consegue ver algo")
    strelevante("Seus olhos vermelhos, sua pele escura como a noite, a visão é de arrepiar")
    strelevante("Um dragão, é isso que Você esta vendo do outro lado da sala.Você sente seu sangue gelando, e um suor frio escorrer pelo seu rosto ")
    strelevante("O dragao olha diretamente para Você")
    strelevante("Hahahahahahaha, te chamam de \' o mais forte entre os humanos \', certo? ")
    strelevante("Bem vindo a terra dos deuses, aqui Você podera testar seus verdadeiros limites")
    strelevante("Isso se Você puder passar por mim, o rei da noite hahahahahah.")
    strelevante("Continua...")
    time.sleep(10)