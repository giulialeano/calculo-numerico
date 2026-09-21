""" Leia uma temperatura em Celsius e mostre em Fahrenheit e em Kelvin.
(F = C × 9/5 + 32 e K = C + 273,15)"""

temp_celsius = float(input("Digite uma temperatura em celsius: "))
converter_fahrenheit = temp_celsius * 9/5 + 32
converter_celsius = temp_celsius + 273,15

print(f"Celsius: {temp_celsius} Cº")
print(f"Fahrenheit: {converter_fahrenheit} F")
print(f"Kelvin: {converter_celsius} K") 