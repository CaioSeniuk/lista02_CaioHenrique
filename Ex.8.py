print(f"\n" + ("-"*60))
idade = int(input("\nInsira a sua idade: "))
if  0 <= idade < 16:
    print(f"\nNão eleitor !\n\n" + ("-")*60)
elif 16 <= idade < 18 or idade >= 65:
    print(f"\nEleitor facultativo !\n\n" + ("-"*60))
elif 18 <= idade < 65:
    print (f"\nEleitor obrigatório !\n\n" + ("-"*60))
else:
    print("\nErro !\nInsira uma idade válida.\n" + ("-"*60))