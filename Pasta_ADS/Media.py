nota1=float(input("Informe a primeira nota: "))
nota2=float(input("informe a segunda nota: "))
 
#calcular media
media_final= (nota1+nota2)/2

#verificação
if media_final >= 7.0:
    print ("A média: %.1f - Aprovado " % media_final)
else:
    print("A média: %.1f - Reprovado " % media_final)
