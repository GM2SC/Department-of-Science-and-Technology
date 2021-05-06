# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:04:13 2021

@author: Prof. Denis C. L. Costa
Disciplina: Matemática Aplicada
Tema: Representação Gráfica
aula_03

"""
# Importando bibliotecas: numpy e matplotlib
# numpy --> Operações Matemáticas
# matplotlib --> Construção gráfica
import numpy as np
import matplotlib.pyplot as plt

# Função Linear ou função do 1° grau: f1 = ax + b
# Input --> a, b, x
# a --> coeficiente angular ; b --> coeficiente linear
# x --> Conjunto domínio: DataSet 
print('=========== Início do Programa ================')
a = 2
b = 3
print('a =', a)
print('b =', b)
# Comando linspace --> (início, fim, número de dados)
x = np.linspace(-2,4,10)
print('x =', x)
# Declarar a Função: output
f1 = a*x + b
print('f1 =', f1)

# Representação Gráfica: comando plot
# plot(DataSet - x, Output - f1, 'Cor e o tipo da linha')
plt.plot(x, f1, '-.m')
# Título dos eixos
plt.xlabel('Valores de x')
plt.ylabel('Valores de f1')
# Título do Gráfico
plt.title('Função Linear')
# Linha de grade --> grid
plt.grid(True)
plt.show() # Comando para apresentar o gráfico

# Sugestões de cores e tipos de linha:
# Cores: r --> vermelha; b --> azul; g --> verde;
# k --> preta; c --> azul claro; m --> lilás; y --> amarela
# tipos de linha: o; *; s (quadrado); ^,>,< (trângulo);
# d(losango); -. ; +     
    
    
    
    
    
    
    
    










