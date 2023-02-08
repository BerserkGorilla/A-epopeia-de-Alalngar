#-*- coding: utf-8 -*
import time

def PuzzleOuro(itens,magias):
    itens = itens
    magias = magias
    print("O corredor da caverna é escuro, apertado e umido")
    time.sleep(0.4)
    print("Um som estrondoso acontece em suas costas, uma pedra fechou a entrada")
    print("Sua única opção é seguir em frente, mas o sacerdote avisou-lhe")
    time.sleep(0.5)
    print("Você chega a um lugar estranho, duas coroas douradas se encontram em um pequeno corpo de água a sua direita.")
    print("Uma das coroas está boiando, enquanto a outra se encontra no fundo do corpo.")
    print("Ao lado desse poço existe um buraco quadrado com cerca de um metro de lado.")
    userInput = ""
    Saida = 0
    while True:
        print("Selecione sua ação (itens, magias, ambiente, concentrar)")
        userInput = str(str(input()))
        if userInput == "itens":
            if itens != []:
                print ("Os itens que carrego comigo são:")
                for m in itens:
                    print(m)
                while True:
                    userInput = str(input())
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
        elif userInput == "ambiente":
            print("Você pode se aproximar do buraco, da água ou da porta:")
            print("Comandos:buraco,agua,porta")
            userInput = str(input())
            if userInput == "buraco":
                print("Você se aproxima do buraco e olha dentro dele")
                print("Tudo o que você consegue ver é a escuridao.")
                print("Esse lugar passa a sentenca do sofrimento eterno, do qual nunca se sai")
                print("Provavelmente esse lugar esta ligado ao Rei da Noite.")
            elif userInput == "agua":
                    print("Você se aproxima do corpo de água")
                    print("De alguma forma você sabe que deve jogar uma das coroas dentro do buraco")
                    print("Mas e agora, como decidir entre elas?")
                    print("Comandos: boiando, afundada")
                    userInput = str(input())
                    print("É isso!")
                    if userInput == "boiando":
                        print("Você retira a coroa boiando da água. Nada parece estranho")
                        print("Ao carregá-la ate o buraco Você não sente nada de diferente")
                        print("A coroa é jogada e desaparrece no breu")
                        time.sleep(5)
                        print("Alguns segundos se passam")
                        print("Uma risada pode ser ouvida ao fundo, macabra e penetrante")
                        print("Você sente o chão se abrindo e cai em meio a escuridão")
                        break
                    elif userInput == "afundada":
                        print("Você retira a coroa afundada da água. Nada parece estranho")
                        print("Ao carregá-la ate o buraco Você não sente nada de diferente")
                        print("A coroa é jogada e desaparrece no breu")
                        time.sleep(5)
                        print("Alguns segundos se passam")
                        print("E então a enorme porta se abre em sua frente, liberando a passagem.")
                        print("À sua frente se apresenta uma escada, esse parece ser o unico caminho.")
                        print("Você comeca a descer a escada")
                        time.sleep(2)
                        print("Eventualmente a porta atrás de você desaparece e a escada parece ainda nao ter fim")
                        time.sleep(5)
                        print("Muito tempo se passa")
                        time.sleep(0.5)
                        print("O fim da escada se torna vísivel, de um lado um precipicio, do outro, ao longe, o caminho de saida.")
                        time.sleep(0.5)
                        print("O chão parece ser de gelo, é muito escorregadio. Seria impossivel atravessar andando")
                        time.sleep(0.3)
                        print("Você consegue alcancar a pedra.")
                        Saida = 1
                        break
                    
            elif userInput == "porta":
                print("Você se aproxima da porta, ela parece pesada demais para ser movida")
                print("A porta tem vários inscritos em uma língua que você nunca viu antes.")
            else:
                print("Opção Inválida")
            
        elif userInput == "concentrar":
            print("o Sacerdote disse algo sobre isso:")
            print("O Rei da Noite é o ser mais ganancioso sob os ceus.")
            print("Aqueles pegos em sua armadilha deverão deixar algo de valor em peso para saírem.")
        else:
            print("Opção Inválida")
    return Saida
	
def PunicaoRN(itens,magias):
    itens = itens
    magias = magias
    print("Uma risada maléfica é o que Você escuta vindo da escuridao")
    time.sleep(1)
    print("HAHAHAHAHAHAHAHAHAHA pequenino")
    print("\'Achou mesmo que uma replica me satisfaria? hahaha\'")
    print("\"Eu sou o Rei da Noite, ninguem nunca foi capaz de escapar da minha punição eterna hahahaha\"")
    time.sleep(6)
    print("Você nao sabe quanto tempo se passou")
    time.sleep(1)
    print("Nada a sua volta é visivel.")
    print("Ao longe e possivel ver uma pedra que parece bem pequena.")
    time.sleep(1)
    print("Essa parece ser a unica coisa identificável")
    time.sleep(0.8)
    while True:
        ex = 0
        userInput = str(input("Selecione sua ação (itens, magias, ambiente, concentrar) "))
        if userInput == "itens":
            if itens != []:
                print ("Os itens que carrego comigo são:")
                #print("itens", ex)
                for m in itens:
                    print(m)
                while True:
                    if ex == 1:
                                break
                    userInput = str(input("Selecione um item "))
                    if userInput not in itens:
                        print("Opcao inválida")
                    elif userInput == "Bloco de metal":
                        print("Bom, acho que posso arremessar esse bloco....")
                        #print("Arremessar bloco? (sim/nao)")
                        while True:
                            userInput = str(input("Arremessar bloco? (sim/nao) "))
                            #print('Arremessar bloco',ex)
                            if userInput == "sim":
                                userInput = str(input("Em qual direcao? (da pedra/contraria)" ))
                                while True:
                                    if userInput =="da pedra":
                                        itens.pop(itens.index("Bloco de metal"))
                                        print("Você arremessa o bloco na direcao da pedra")
                                        print("Você percebe que a pedra comeca a se afastar ")
                                        print("\'ISSO NÃO PODE ESTAR ACONTECENDO\'")
                                        time.sleep(2)
                                        print("\' HAHAHAHAHAHAHAAHAHAHAHAHAHA \'-  A risada do rei da noite ecoa na escuridao")
                                        print("Você percebeu que sua aventura se encerrou aqui, o Rei da Noite te derrotou.")
                                        time.sleep(10)
                                        exit()
                                    elif userInput == "contraria":
                                        itens.pop(itens.index("Bloco de metal"))
                                        print("Você arremessa o bloco na direcao contraria da pedra")
                                        print("Você percebe que lentamente a pedra se aproxima de Você")
                                        time.sleep(0.3)
                                        print("Ou melhor, Você se aproxima da pedra")
                                        print("O processo é bem lento, provavelmente Você levara horas")
                                        time.sleep(5)
                                        print("Você alcança a pedra e percebe que ela esta sob um chão de gelo")
                                        print("Uma escada parece descer exatamente para o lugar onde Você se encontra agora")
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
        elif userInput == "ambiente":
            print("O ambiente está vazio, um breu completo e apenas uma pedra ao longe")
        elif userInput == "concentrar":
            print("o Sacerdote disse algo sobre isso:")
            print("O Rei da Noite é o ser mais ganancioso sob os ceus.")
            print("Aqueles pegos em sua armadilha deverão deixar algo de valor em peso para sairem.")
        else:
            print("Opção Inválida")
			
def PuzzleGelo(itens,magias,Saida):
    itens = itens
    magias = magias
    t = 0
    ex = 0
    while True:
        if ex == 1:
            break
        userInput = str(input("Selecione sua ação (itens, magias, ambiente, concentrar)"))
        if userInput == "itens":
            if itens != []:
                print ("Os itens que carrego comigo são:")
                for m in itens:
                    print(m)
                while True:
                    userInput = str(input())
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
            print("Você esta proximo a pedra e a escada")
            t = 1
            while True:
                userInput = str(input("Selecione uma acao:(subir a escada,voltar) "))
                if userInput.startswith("emp") or userInput.startswith("Emp"):
                    print("Você empurra a pedra")
                    time.sleep(1)
                    print("Você percebe que esta se deslocando em direcao a saida")
                    ex = 1
                    break
                elif userInput == "subir a escada":
                    if Saida == 1:
                        print("Essa é a escada que Você acabou de descer")
                    else:
                        print("A escadaria e enorme, Você gasta muito tempo para subi-la")
                        time.sleep(5)
                        print("Ao chegar no topo da escadaria, Você ve uma porta que parece muito a da primeira sala")
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
            
        elif userInput == "concentrar":
            if t == 0:
                print("Talvez eu devesse explorar mais o ambiente")
            else:
                print("Acho que eu posso empurar a pedra para tentar me mover")
        else:
            print("Opção Inválida")
			
def PuzzleElevador(itens, magias):
    print("Você caminha ate alcancar uma colina muito alta, nao parece ser possivel escala-lo")
    time.sleep(1)
    print("Você esta sobre uma tabua que parece estar presa por uma corda passando por uma roldana no teto")
    print("Essa corda esta presa a uma pedra que esta sobre uma plataforma muito alta")
    print("A sustentacao dessa plataforma é fina")
    while True:
        ex = 0
        userInput = str(input("Selecione sua ação (itens, magias, ambiente, concentrar) "))
        if userInput == "itens":
            if itens != []:
                print ("Os itens que carrego comigo são:")
                for m in itens:
                    print(m)
                while True:
                    if ex == 1:
                            break
                    userInput = str(input("Selecione um item "))
                    if userInput not in itens:
                        print("Opcao inválida")
                    elif userInput.startswith("Espada"):
                        while True:
                            userItem = userInput
                            userInput = str(input("Cortar suporte? (sim/nao) "))
                            if userInput == "sim":
                                print("Você usa a sua "+userItem+" para cortar o suporte.")
                                print("Você corta a sustentacao, a pedra cai junto com a base e Você sobe")
                                time.sleep(1)
                                print("Um pequeno salto é o suficiente para alcancar o topo da colina")
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
        elif userInput == "ambiente":
            print("Você está em cima de algo que parece um elevador.")
            time.sleep(0.8)
            print("O contra peso do elevador está preso por um suporte que pode ser cortado")
        elif userInput == "concentrar":
            print("Acho que consigo cortar com minha espada esse suporte")
        else:
            print("Opção Inválida")

if __name__ == '__main__':
    itens = ["Bloco de metal","Espada longa", "Espada curta","Vembrassa"]
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
    print("O reino de Ulk foi amaldicoado pelos deuses.")
    print("Fome e pobreza assolam o reino. Você, Alalngar, o Heroi decide que apenas uma solucao e possivel")
    time.sleep(1)
    print("Enfrentar os deuses.")
    time.sleep(1)
    print("Meshkiangasher, o sacerdote, alertou-lhe")
    print(" \' Isso é uma insanidade! \' ")
    time.sleep(1)
    print("Apesar disso, ele indica o caminho de entrada para o territorio divino")
    time.sleep(1)
    print("Uma caverna ao norte de Ulk, dentro da Floresta Proibida")
    time.sleep(1)
    print(" \' Se alguém é capaz de fazer uma insanidade dessas, deve ser Você. \' ")
    time.sleep(1)
    print("Com essas palavras, o Sacerdote entregou um Bloco de metal pesado para o herói dizendo")
    print(" \' Espero que nao precise disso, mas e melhor ter e nao usar\'.")
    print("O heroi entao se prepara e entra na caverna, sem certeza do futuro que lhe aguarda.")
    Saida = PuzzleOuro(itens,magias)
    if Saida != 1:
        itens = PunicaoRN(itens,magias)

    PuzzleGelo(itens,magias,Saida)
    print("Você caminha ate alcancar uma colina muito alta, nao parece ser possivel escala-lo")
    time.sleep(1)
    print("Você esta sobre uma tabua que parece estar presa por uma corda passando por uma roldana no teto")
    print("Essa corda esta presa a uma pedra que esta sobre uma plataforma muito alta")
    print("A sustentacao dessa plataforma é fina, e Você conseguiria cortar com sua espada longa ")
    PuzzleElevador(itens,magias)
    time.sleep(1)
    print("A frente é possível ver que o tom verdejante dessa parte da caverna some, dando lugar a paredes de pedra azul brilhante")
    time.sleep(1)
    print("Do alto da colina onde Você está é possível ver que a sala e um grande vale, do outro lado do vale Você consegue ver algo")
    time.sleep(1)
    print("Seus olhos vermelhos, sua pele escura como a noite, a visão é de arrepiar")
    time.sleep(1)
    print("Um dragão, é isso que Você esta vendo do outro lado da sala.Você sente seu sangue gelando, e um suor frio escorrer pelo seu rosto ")
    time.sleep(1)
    print("O dragao olha diretamente para Você")
    time.sleep(1)
    print("Hahahahahahaha, te chamam de \' o mais forte entre os humanos \', certo? ")
    time.sleep(1)
    print("Bem vindo a terra dos deuses, aqui Você podera testar seus verdadeiros limites")
    time.sleep(1)
    print("Isso se Você puder passar por mim, o rei da noite hahahahahah.")
    time.sleep(2)
    print("Continua...")
    time.sleep(10)