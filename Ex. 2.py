print(f"\n" + ("-"*60))
a = float(input("\nInforme a: "))
b = float(input("\nInforme b: "))
c = float(input("\nInforme c: "))

delta = b**2 - (4*a*c)
if delta > 0:
    print(f"\nComo delta é: {delta}, as raízes são reais e distintas\n" + ("-"*60))
elif delta == 0: 
    print(f"\nComo delta é : {delta}, as raízes são reais e iguais\n" + ("-"*60))
else:
    print(f"\nComo delta é: {delta}, as raízes são imaginárias conjugadas\n" + ("-"*60))