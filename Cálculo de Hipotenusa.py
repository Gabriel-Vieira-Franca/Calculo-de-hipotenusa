import math
# Definindo os comprimentos dos catetos
cateto_a = float(input("Insira o cateto A: "))
cateto_b = float(input("Insira o cateto B: "))
# Calculando o quadrado da hipotenusa
quadrado_hipotenusa = cateto_a ** 2 + cateto_b ** 2
# Calculando a hipotenusa usando a raiz quadrada
hipotenusa = math.sqrt(quadrado_hipotenusa)
# Imprimindo o resultado
print("---------------")
print(f"A hipotenusa é: {hipotenusa}")