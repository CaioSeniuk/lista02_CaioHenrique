print(f"\n" + ("-"*60))
idade = int(input("\nInsira a sua idade: "))
if 1 <= idade < 15:
    print(f"\nIdade inválida !\nÉ necessário ser maior de 15 (quinze) anos.\n\n" + ("-")*60)
elif idade >= 15:
    peso = float(input("Insira o seu peso (em Kg): "))
    if peso > 120:
        print("\nAcesso bloqueado! Limite de peso de 120Kg.\n")
    elif peso < 0:
        print("\nInsira um peso real !\n")
    else:
        print("\nAcesso Liberado! Bom-passeio.\n\n" + ("-")*60)
else: 
    print("\nIdade inválida! Insira uma idade real.\n")