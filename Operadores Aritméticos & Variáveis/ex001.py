"""1. Conta de energia elétrica
Uma casa consome, em média, 350 kWh por mês. 
A tarifa é de R$ 0,92 por kWh, mas há uma taxa fixa de R$ 25,00 
independente do consumo. Calcule o valor total da conta e quanto 
seria pago se o consumo dobrasse. """

media_consumo = 350
tarifa = 0.92
taxa_fixa = 25.00

valor_total = media_consumo * tarifa + taxa_fixa
valor_dobrado = (media_consumo * 2) * tarifa + taxa_fixa

print(f"Valor total da conta: R$ {valor_total:.2f}")
print(f"Valor total da conta com consumo dobrado: R$ {valor_dobrado:.2f}")