# !/usr/bin/python
# Calcula quantos dias de vida uma pessoa teve dado o dia, mes e ano de seu nascimento.
# Autor: Ewerton Tiago de Azevedo
# Analise e Desenvolvimento de Sistemas - IFF Campos dos Goytacazes
# Data: 12-03-2010
 
 
from datetime import datetime
import locale
 
#configuracoes do usuario
 
locale.setlocale(locale.LC_ALL, "")
 
hoje=datetime.today()
 
anoAtual= hoje.strftime("%Y")
mesAtual= hoje.strftime("%m")
diaAtual= hoje.strftime("%d")

Datasfaturas = []

print (" ----------------------------------------")
print ("Escolha o dia de vencimento e em quantas parcelas será feito:")
print
print
print ("Dia para vencer:"),
dia=input()
print ("Quantidades de parcelas:"),
print("OBS: Digite separadamente em quantas parcelas será feito, ex: [1,2,3]")
mes=input("")

anoAtual=int(anoAtual)
mesAtual=int(mesAtual)
diaAtual=int(diaAtual)
mesProximo=int(mesAtual+1)

if len(mes) > 1:
    print
    print ("Data de venc das parcelas:"),
    for prc in eval(mes):
        if int(dia) > diaAtual:
            prcA = mesAtual + prc
            if prcA > 12:
                print(f"{dia}/{prcA-12}/{anoAtual+1}")
            else:
                print(f"{dia}/{prcA}/{anoAtual}")
        if int(dia) <= diaAtual:
            prcP = mesAtual + prc
            if prcP > 12:
                print(f"{dia}/{prcP-12}/{anoAtual+1}")
            else:
                print(f"{dia}/{prcP}/{anoAtual}")
else:
    print ("Data de vencimento:"),
    if int(dia) > diaAtual:
        print(f"{dia}/{mesAtual}/{anoAtual}")
    if int(dia) <= diaAtual:
        print(f"{dia}/{mesProximo}/{anoAtual}")


