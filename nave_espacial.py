##variáveis globais
combustivel =  110
tripulantes = []

##funções

def viajar(): ##gasto de combustível
    global combustivel ##modifica a variável externa

    if (combustivel >= 30):
        combustivel = combustivel - 30
        print(f"\nA nave viajou 🚀!")

    else:
        print("\nCombustível insufuciente. Abasteça! ⚠️")


def abastecer(): ##ganho de combustível
    global combustivel

    combustivel = 110 
    print(f"\nTanque abastecido⛽!")


def status_nave(): ##quantidade de combustível e tripulantes

    print("\n--------STATUS DA NAVE-------")
    print(f"Temos {combustivel}L de combustível.")
    print(f"Tripulantes da nave: {tripulantes}\n")


def registrarTripulante():

    novoTripulante = input("\nInsira o nome do novo tripulante: ")
    tripulantes.append(novoTripulante)
    print("Novo tripulante inserido com sucesso!! 🧑🏻‍🚀\n")



##Criar um menu

print("\n------MENU INTERATIVO------")
print("Selecione um aopção:")

while True: ##roda para sempre
    # print("Bem vindo a nave espacial! 🚀")
   
    print("\n1- Mostrar status da nave \n2- Viajar  \n3- Abastecer \n4- Adicionar novo tripulante  \n5- Sair do menu")

    opcao = input("R: ")
    
    if opcao == "1":
        status_nave()

    elif opcao == "2":
        viajar()

    elif opcao == "3":
        abastecer()

    elif opcao == "4":
        registrarTripulante()

    elif opcao == "5":
        print("Viagem encerrada!")
        break

