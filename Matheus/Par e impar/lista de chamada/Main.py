def main():
    quantAlunos = int(input("Digete a qantidade de alunos: "))

    while quantAlunos <1:
        print("Numero inválido, digite novamente")
        quantAlunos = int(input("Digete a quantidade de alunos: "))

    nomes = [""] * quantAlunos

    i = 0

    while i in range(len(nomes)):
        nomes [i] = input("Digete o nome do aluno: ")
        i += 1
    print(nomes)
    return 0
main()