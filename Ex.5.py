print(f"\n"+("-"*60))
gen = int(input("\nQual o seu gênero (1- homem / 2- mulher)?: "))
if gen<1 or gen>2: 
    print(f"\nErro, insira um número válido para o gênero !\n" + ("-"*60))
    quit
if gen == 1:
    h = float(input("\nQual a sua altura em Metros (ex.: 1.75m)?: "))
    print(f"\nO seu peso ideal (em Kg) é: {((72.7 * h) - 58):.2f}\n" + ("-"*60))
elif gen == 2:
    h = float(input("\nQual a sua altura em Metros (ex.: 1.75m)?: "))
    print(f"\nO seu peso ideal (em Kg) é: {((62.1 * h) - 44.7):.2f}\n" + ("-"*60))