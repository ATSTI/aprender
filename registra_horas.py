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

horaRegistro = []

print (" ----------------------------------------")
print ("Entrada e saida do usuario")
print (" ----------------------------------------")

# Registra momento de entrada do usuario
print ("Digite <ENTER> para registrar entrada")
entrada=input()
inicio=datetime.now()
horaInicial= inicio.strftime("%H")
minInicial= inicio.strftime("%M")
print (f"entrada, {horaInicial}hrs{minInicial}min")
entradaH = horaInicial
entradaM = minInicial

# Registra momento de saida do usuario
print ("Digite <ENTER> para registrar saida")
saida=input()
fim=datetime.now()
horaFinal= fim.strftime("%H")
minFinal= fim.strftime("%M") 
print (f"saida, {horaFinal}hrs{minFinal}m")
saidaH = horaFinal
saidaM = minFinal

#calcula a quantidade de horas e minutos
horaRegistro= (int(saidaH) - int(entradaH))
minRegistro= (int(saidaM) - int(entradaM))

print ("Total de horas trabalhadas:")
print (f"{horaRegistro}hrs{minRegistro}m")
 