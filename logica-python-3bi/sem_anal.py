comando = input("Digite o dia da semana: ")
match comando:
    case "Domingo":
        print("Hoje é domingo")
    case "Segunda":
        print("Hoje é segunda")
    case "Terça":
        print("Hoje é terça")
    case "Quarta":
        print("Hoje é quarta")
    case "Quinta":
        print("Hoje é quinta")
    case "Sexta":
        print("Hoje é sexta")
    case "Sábado":
        print("Hoje é sábado")
    case _:
        print("Não é um dia da semana")