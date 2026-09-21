"""7. Distância entre dois pontos
Leia as coordenadas (x₁, y₁) e (x₂, y₂) e mostre a distância euclidiana entre eles. (Dica: raiz quadrada é ** 0.5.)"""

coord_x1 = float(input("x1: "))
coord_y1 = float(input("y1: "))
coord_x2 = float(input("x2: "))
coord_y2 = float(input("y2: "))

print(f"Sendo assim, temos: ({coord_x1}, {coord_y1}) e ({coord_x2}, {coord_y2})")

distancia = ((coord_x2 - coord_x1)**2 - (coord_y2 - coord_y1)**2)**0.5
print(f"A distância entre os pontos é {distancia} metros.")
