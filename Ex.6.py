print(f"\n" + ("-"*60))
P = 0
I = 0
print(f"\nPrograma que verifica se um número é par ou ímpar: ")
num = int(input("\nInsira um número inteiro e positivo: "))
if num % 2 == 0:
    P = num
    print(f"\nVariável P: {P} é par\nVariável I: {I}\n" + ("-"*60))
else:
    I = num
    print(f"\nVariável P: {P}\nVariável I: {I} é ímpar\n" + ("-"*60))
    