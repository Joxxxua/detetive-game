print("Escreva 1/Sim ou 0/Não")
telef = int(input("Telefonou para a vítima?"))
local = int(input("Esteve no local do crime?: "))
mora = int(input("Mora perto da vítima?: "))
devia = int(input("Devia para a vítima?: "))
trabalho = int(input("Já trabalhou para a vítima?: "))
total=telef+local+mora+devia+trabalho
if total == 2:
    print("Você é suspeito!")
elif total == 3 or total == 4:
    print("Você é cumplice")
elif total < 2 or total == 0:
    print("Você é inocente")
else:
    print("VOCÊ É O ASSASSNO!!!!!!!!!!!!!!!!!!!!!!")



        
    

