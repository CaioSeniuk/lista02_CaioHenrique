print(f"\n"+("-"*60))
nota = float(input("\nInsira a nota do estudante: "))
if 4 <= nota < 7:
    print("\nEstudante em recuperação !\n" + ("-"*60))
elif 0 <= nota < 4:
    print("\nEstudante reprovado !\n" + ("-"*60))
elif nota < 0 or nota > 10:
    print("\nInsira uma nota válida !\n" + ("-"*60))
else:
    print("\nEstudante aprovado !\n" + ("-"*60))