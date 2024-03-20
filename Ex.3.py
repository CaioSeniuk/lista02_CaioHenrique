print(f"\n"+("-"*60))
temp = int(input("\nQual a temperatura (em ºC) do dia de hoje?: "))
if temp < 15: 
    print("\nEstá frio !\n" + ("-"*60))
elif 15 <= temp <= 25:
    print("\nTemperatura agradável ! \n" + ("-"*60))
else:
    print("\nEstá calor !\n" + ("-"*60))