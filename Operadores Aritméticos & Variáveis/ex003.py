""" 3. Conversão de tempo
Um vídeo dura 7.845 segundos. Converta esse tempo para o formato horas:minutos:segundos. """

#Parte da divisão inteira dos segundos por 3600
horas = 7845//3600

#Resto da divisão (segundos faltando)
segundos = 7845%3600

minutos_hora = segundos//60
segundos_hora = segundos%60

print(f"7.845 segundos = {horas} horas {minutos_hora} minutos e {segundos_hora} segundos")