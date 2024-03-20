print(f"\n" + ("-"*60))
uni = int(input("\nInsira a sua universidade (1 - PUCPR / 2- UNICAMP): "))
if uni == 1:
    nota1 = float(input("\nInsira sua 1º nota: "))
    nota2 = float(input("\nInsira sua 2º nota: "))
    media = (nota1+nota2)/2
    if media >= 7.0:
        print("\nEstudante aprovado !\n" + ("-"*60))
    elif 4.0<=media<7.0:
        print("\nEstudante em exame !\n" + ("-"*60))
    else:
        print("\nEstudante reprovado !\n" + ("-"*60))
elif uni == 2:
    nota1 = float(input("\nInsira sua 1º nota: "))
    nota2 = float(input("\nInsira sua 2º nota: "))
    media = (nota1+nota2)/2
    if media >= 5.0:
        print("\nEstudante aprovado !\n" + ("-"*60))
    else:
        print("\nEstudante em exame !\n" + ("-"*60))
else:
    print("\nInsira um valor válido !\n" + ("-"*60))
