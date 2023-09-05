nome1 = str(input("digite seu nome: "))
idade1 = int(input("Digite o ano de nascimento: "))
nome2 = str(input("digite seu nome: "))
idade2 = int(input("Digite o ano de nascimento: "))


if 2023 - idade1 >= 18:
    print(f"{nome1} tem {2023-idade1} anos.")
else:
    print(f"{nome1} não tem mais que 18 anos")

if 2023 - idade1 >= 18:
    print(f"{nome2} {2023-idade2} anos.")
else:
    print(f"{nome2} não tem mais de 18 anos")
