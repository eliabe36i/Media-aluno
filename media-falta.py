
n1 = float(input("digite nota 1 "))
n2= float(input("digite nota 2 "))
n3= float(input("digite nota 3 "))



media= (n1+n2+n3)/3

print("Amedia é {:2.2f}".format(media))

if (media<5):
    print("aluno Reprovado")
elif(media>=5) and (media<7):
    print("aluno de recuperação")
else:
    print("aluno aprovado")

    falta=int(input("Digite o numero de faltas "))
    if(falta>=25):
        print("Aluno Reprovado Por falta ")
    elif(falta<25):
        print("Frequencia ok")

