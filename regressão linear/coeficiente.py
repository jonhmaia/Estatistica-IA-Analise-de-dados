import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Seus dados
preco_venda = [400000, 370000, 382500, 300000, 305000, 320000, 321000, 445000, 377500, 460000, 265000, 299000, 385000, 430000, 214900, 475000, 280000, 457000, 210000, 272500, 268000, 300000, 477000, 292000, 379000, 295000, 499000, 292000, 305000, 520000, 308000, 316000, 355500, 225000, 270000, 253000, 310000, 300000, 295000, 478000]
comodos = [2.27, 0.75, 1.00, 0.43, 3.60, 1.70, 0.81, 2.00, 1.50, 1.09, 1.60, 0.42, 0.89, 4.79, 0.25, 11.58, 0.46, 1.84, 0.94, 1.39, 0.83, 0.57, 1.10, 0.52, 1.00, 0.90, 5.98, 2.93, 0.33, 1.53, 0.63, 2.00, 0.44, 0.62, 0.68, 0.68, 1.69, 0.83, 2.90, 2.14]

# Calcula a regressão linear
slope, intercept, R, p_value, std_err = linregress(preco_venda, comodos)

# Cria uma função para a linha de regressão
def regression_line(x):
    return slope * x + intercept

# Cria o gráfico de dispersão
plt.scatter(preco_venda, comodos, label='Dados Originais')

# Adiciona a linha de regressão ao gráfico
plt.plot(preco_venda, regression_line(np.array(preco_venda)), color='red', label='Reta de Regressão')

# Adiciona o coeficiente de determinação ao gráfico
plt.text(min(preco_venda), max(comodos), f'R² = {R**2:.2f}', ha='left', va='bottom', color='blue')

# Adiciona rótulos e título
plt.xlabel('Preço Venda')
plt.ylabel('comodos')
plt.title('Gráfico de Dispersão com Reta de Regressão')
print(f"Equação de Regressão Linear: comodos
 = {intercept:.2f} + {slope:.2f} * Preço Venda")
print(f"Coeficiente de Determinação (R²): {R**2:.2f}")
if R == 1:
    print("O modelo explica 100% da variação na variável dependente. Ajuste perfeito.")
elif R > 0.7:
    print("O modelo tem um bom ajuste,uma alta proporção da variação na variável dependente.")
elif R > 0.5:
    print("O modelo tem um ajuste razoável,  uma proporção moderada da variação na variável dependente.")
else:
    print("O modelo tem um ajuste fraco,  uma baixa proporção da variação na variável dependente.")
# Exibe a legenda
plt.legend()

# Exibe o gráfico
plt.show()
import numpy as np
from scipy.stats import linregress

# Dados fornecidos
preco_venda = [400000, 370000, 382500, 300000, 305000, 320000, 321000, 445000, 377500, 460000, 265000, 299000, 385000, 430000, 214900, 475000, 280000, 457000, 210000, 272500, 268000, 300000, 477000, 292000, 379000, 295000, 499000, 292000, 305000, 520000, 308000, 316000, 355500, 225000, 270000, 253000, 310000, 300000, 295000, 478000]
comodos = [9, 8, 9, 8, 6, 7, 8, 9, 9, 10, 6, 7, 9, 8, 5, 7, 8, 11, 7, 6, 4, 9, 10, 8, 10, 6, 6, 7, 8, 11, 8, 7, 10, 6, 6, 6, 6, 8, 6, 8]

# Calcula a regressão linear
slope, intercept, R, p_value, std_err = linregress(preco_venda, comodos
)

# Cria uma função para a linha de regressão
def regression_line(x):
    return slope * x + intercept

# Cria o gráfico de dispersão
plt.scatter(preco_venda, comodos
, label='Dados Originais')

# Adiciona a linha de regressão ao gráfico
plt.plot(preco_venda, regression_line(np.array(preco_venda)), color='red', label='Reta de Regressão')

# Adiciona o coeficiente de determinação ao gráfico
plt.text(min(preco_venda), max(comodos
), f'R² = {R**2:.2f}', ha='left', va='bottom', color='blue')

# Adiciona rótulos e título
plt.xlabel('Preço Venda')
plt.ylabel('comodos')
plt.title('Gráfico de Dispersão com Reta de Regressão')
print(f"Equação de Regressão Linear: comodos
 = {intercept:.2f} + {slope:.2f} * Preço Venda")
print(f"Coeficiente de Determinação (R²): {R**2:.2f}")
if R == 1:
    print("O modelo explica 100% da variação na variável dependente. Ajuste perfeito.")
elif R > 0.7:
    print("O modelo tem um bom ajuste,uma alta proporção da variação na variável dependente.")
elif R > 0.5:
    print("O modelo tem um ajuste razoável,  uma proporção moderada da variação na variável dependente.")
else:
    print("O modelo tem um ajuste fraco,  uma baixa proporção da variação na variável dependente.")
# Exibe a legenda
plt.legend()

# Exibe o gráfico
plt.show()