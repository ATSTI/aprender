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

dataNascimento = []

print (" ----------------------------------------")
print ("Atenção : digite conforme a forma abaixo.")
print (" ----------------------------------------")
print ("Digite sua data de nascimento no formato: dia<ENTER>mes<ENTER>ano<ENTER> ")
print (" Para mes digite apenas 1 e nao 01, 2 e nao 02")
print
print ("Data de Nascimento: "),
dia=input()
mes=input()
ano=input()
dataNascimento.append(dia)
dataNascimento.append(mes)
dataNascimento.append(ano)
 
print "Data de Nascimento: ", dataNascimento, "\n"
 
#Converte a data para inteiro
 
anoAtual=int(anoAtual)
mesAtual=int(mesAtual)
diaAtual=int(diaAtual)
 
# Verifica a idade do usuario
 
idade=anoAtual-dataNascimento[2]
 
 
if mesAtual > dataNascimento[1]:
   idade=idade
 
elif dataNascimento[1] == mesAtual and diaAtual >= dataNascimento[0]:
   idade=idade
 
else:
   idade= idade-1
 
 
quantidadeAnosBissextos= idade/4
 
 
idadeEmDias=(idade*365)+quantidadeAnosBissextos
 
 
print "Sua idade em dias:",idadeEmDias,
