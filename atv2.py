#!/usr/bin/env python
# coding: utf-8

# # Inteligência Artificial e Aprendizado de Máquina - Prática 02
# 
# ## Introdução ao Aprendizado de Máquina

# In[ ]:

# Bibliotecas inicialmente necessárias

from itertools import product
import random
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import math

params = {'legend.fontsize': 20,
          'figure.figsize': (15,5),
          'axes.labelsize': 20,
          'axes.titlesize': 20,
          'xtick.labelsize': 20,
          'ytick.labelsize': 20}


# **Questão 1)** Dados repassados pelos analistas de perfis:

# In[ ]:

newdot = [((random.random() * 2.0) + 1.0, (random.random() * 2.0) + 1.0)]

dots_1 = [(random.random() * 2.0, random.random() * 2.0) for _ in range(10)]

dots_2 = [((random.random() * 2.0) + 2.0, (random.random() * 2.0) + 2.0) for _ in range(10)]

r = 0.3

# Função da Distância
def distancia(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def classificar_ponto(centro, dots_1, dots_2, r):
    contador_comedia = 0
    contador_drama = 0
    
    for ponto in dots_1:
        if distancia(centro, ponto) <= r:
            contador_comedia += 1
    
    for ponto in dots_2:
        if distancia(centro, ponto) <= r:
            contador_drama += 1

    print("====Novo Cliente====")
    print("Pontos de Comédia dentro da circunferência:", contador_comedia)
    print("Pontos de Drama dentro da circunferência:", contador_drama)

    if contador_comedia > contador_drama:
        return "COMÉDIA (azul)\n"
    elif contador_drama > contador_comedia:
        return "DRAMA (vermelho)\n"
    else:
        return "Empate - não é possível classificar com este raio\n"



resultado = classificar_ponto(newdot[0], dots_1, dots_2, r)

print("Conclusão:", resultado)


# Criar figura e eixo
fig, ax = plt.subplots()

pylab.rcParams.update(params)

# Plotar pontos azuis e vermelhos
for i in range(len(dots_1)):
    ax.plot(dots_1[i][0], dots_1[i][1], c='blue', marker='o')
    ax.plot(dots_2[i][0], dots_2[i][1], c='red', marker='o')

# Plotar ponto amarelo (centro da circunferência)
ax.plot(newdot[0][0], newdot[0][1], c='yellow', marker='s', markersize=12)

# Criar circunferência com centro no ponto amarelo
circulo = plt.Circle(
    (newdot[0][0], newdot[0][1]),  
    r,                             
    color='yellow',
    fill=False,
    linewidth=2
)
# Adicionar circunferência ao gráfico
ax.add_patch(circulo)

# Legenda
ax.legend(['Comédia','Drama'])

# Mostrar gráfico
plt.show()






# **Questão 2)** O perfil do novo cliente:

# In[ ]:

# Usuário escolhe o raio
r = float(input("Digite o valor do raio r: "))

resultado = classificar_ponto(newdot[0], dots_1, dots_2, r)

print("Conclusão:", resultado)

# Criar figura e eixo
fig, ax = plt.subplots()
pylab.rcParams.update(params)


for i in range(len(dots_1)):
    
    pylab.rcParams.update(params)
    plt.plot(dots_1[i][0], dots_1[i][1], c = 'blue', marker = 'o')
    plt.plot(dots_2[i][0], dots_2[i][1], c = 'red', marker = 'o')
    
plt.plot(newdot[0][0], newdot[0][1], c = 'green', marker = 's', markersize = 12)

# Criar circunferência com centro no ponto amarelo
circulo = plt.Circle(
    (newdot[0][0], newdot[0][1]),  
    r,                             
    color='green',
    fill=False,
    linewidth=2
)
# Adicionar circunferência ao gráfico
ax.add_patch(circulo)

plt.legend(['Comédia','Drama'])    
plt.show()


        
# **Questão 3)** Dados envolvendo os filmes de Ficção Científica e Ação:

# In[ ]:
ficcao = [((random.random() * 2.0) + 0.5, (random.random() * 2.0) + 1.0) for _ in range(25)]
acao = [((random.random() * 2.0)+1.0, (random.random()*2.0)+1.5) for _ in range(25)] 
newdots = [((random.random()*2.0)+1.0, (random.random()*2.0)+1.5) for _ in range(3)]

def classificar_genero(centro, ficcao, acao, r):
    contador_ficcao = 0
    contador_acao = 0

    for ponto in ficcao:
        if distancia(centro, ponto) <= r:
            contador_ficcao += 1

    for ponto in acao:
        if distancia(centro, ponto) <= r:
            contador_acao += 1

    print("====Novo Cliente====")
    print("Pontos de Ficção Científica dentro da circunferência:", contador_ficcao)
    print("Pontos de Ação dentro da circunferência:", contador_acao)

    if contador_ficcao > contador_acao:
        return "FICÇÃO (azul)\n"
    elif contador_acao > contador_ficcao:
        return "AÇÃO (laranja)\n"
    else:
        return "Empate - não é possível classificar com este raio\n"
   

    
# In[ ]:

r = float(input("Digite o valor do raio para a Questão 3: "))

for i, cliente in enumerate(newdots):
    resultado = classificar_genero(cliente, ficcao, acao, r)
    print(f"Cliente {i+1} pertence ao grupo: {resultado}")


fig, ax = plt.subplots()
pylab.rcParams.update(params)

# Plotar pontos fixos
for i in range(len(ficcao)):
    ax.plot(ficcao[i][0], ficcao[i][1], c='navy', marker='o')
    ax.plot(acao[i][0], acao[i][1], c='darkorange', marker='o')

# Para cada novo cliente
for cliente in newdots:
    
    ax.plot(cliente[0], cliente[1], c='cyan', marker='s', markersize=12)
    
    circulo = plt.Circle(
        (cliente[0], cliente[1]),
        r,
        color='cyan',
        fill=False,
        linewidth=2
    )
    
    ax.add_patch(circulo)

ax.legend(['Ficção Científica','Ação'])
plt.show()