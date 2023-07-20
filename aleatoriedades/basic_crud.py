from os import system
from time import sleep

bd = dict()
prov = dict()
prov2 = dict()


def error():
    system("cls")
    print("Try again")
    sleep(2)


def visualizar():
    for cadastrado, infos in bd.items():
        print(cadastrado)
        for i, j in infos.items():
            print(f"    {i}: {j}")
    input()


def remove():
    nome = input("Nome: ").title().strip()
    system("cls")
    if nome in bd:
        try:
            del bd[nome]
            print("Deleted")
        except:
            print("Ocorreu algum erro")
    else:
        print("Esse cadastro não existe")

    sleep(2)


def atualizar():
    prov.clear()
    prov2.clear()
    nome = input("Nome: ").title().strip()
    prov["age"] = input("age: ")
    prov["sex"] = input("sex: ")
    prov2[nome] = prov.copy()
    system("cls")

    if nome in bd:
        print("Updated")
    else:
        print("Created")

    try:
        bd.update(prov2)

    except:
        print("Ocorreu algum erro")

    sleep(2)


def menu():
    while True:
        op = " "
        system("cls")
        print(f'{" BASIC CRUD ":=^31}')

        try:
            op = int(
                input(
                    "\n1 - Cadastrar\n2 - Visualizar\n3 - Atualizar\n4 - Remover\n5 - Sair\n\n>: "
                )
            )
        except:
            error()
            continue
        system("cls")

        if 0 < op < 6:
            if op == 1:
                atualizar()
            if op == 2:
                visualizar()
            if op == 3:
                atualizar()
            if op == 4:
                remove()
            if op == 5:
                print("Saindo")
                sleep(2)
                quit()
        else:
            error()
        continue


if __name__ == "__main__":
    menu()
