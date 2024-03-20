print(f"\n" + ("-"*60))
idade = int(input("\nInsira sua idade: "))
tempo = int(input("\nInsira o seu tempo de serviço: "))
if idade >= 65 or tempo >= 30:
    print("\nPode se aposentar !\n" + ("-"*60))
elif 0 > idade or 0> tempo:
    print("\nInsira um valor válido !\n" + ("-"*60))
elif idade>=60 and idade>=25:
    print("\nPode se aposentar !\n" + ("-"*60))
else:
    print(f"\nFaltam {65-idade} anos para se aposentar pela idade \nFaltam {30-tempo} anos para se aposentar pelo tempo de trabalho\n\n" + ("-"*60))