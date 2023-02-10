# -*- coding: utf-8 -*-
"""Modelo SIR em Redes - GitHub.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17mPvL2zUb9Y3FfrEZMrDE92369W17ysF

# Modelo SIR aplicado em Redes
**Autores:**

[Lucas Henrique Amorim da Silva]()<br>
[Lucas Praxedes Fischer de Mattos]()<br>
[Rafael da Silva Medeiros]()<br>

**Data de Criação:** 04/08/2022<br>
**Ultima Modificação:** 10/02/2023<br>
**Descrição:** Projeto utilizado como avalição da unidade curricular (UC) Modelagem Computacional ministrada pelo Prof. Dr. Marcos Gonçalves Quiles na Universidade Federal de São Paulo.

## Descrição Geral do Sistema Simulado

O presente relatório realiza a simulção do modelo SIR implementado em redes. O objetivo é analisar como cada vertice da rede se comportará, variando suas probabilidades de migração.


### Equações do algoritmo:
- $\frac{dS_1}{dt} = -r_1S_1(I_1+γ_1‎ _2 I_2)$

- $\frac{dI_1}{dt} = r_1S_1(I_1+γ_1‎ _2 I_2) - α_1I_1$

- $\frac{dR_1}{dt} = α_1(I_1+γ_1‎ _2 I_2)$

## Parâmetros da Simulação

### Parâmetros gerais:

- $TMax$ = $365$ - Tempo máximo de simulação em dias
- $Infectados$ = $500$ - Nº de infectados inicialmente em cada modelo sir
- $N$ = $10$ - Quantidade de vertices (cidades)
"""

# Bibliotecas
import numpy as np
from matplotlib import pyplot as plt
import random
import networkx as nx

"""## Simulação 01 - Apenas uma cidade com infectados

### Parâmetros
"""

# Váriaveis de controle
DT = 0.01           # Variação do tempo
t = 0               # Tempo inicial
TMax = 365          # Tempo máximo para simulação (365 Dias)
N = 10              # Quantidade de vertices da rede (representado por cidades)

S = 0
I = 0
R = 0

# Infecção
gama = np.zeros((10, 10), dtype=np.float64)

# Listas para plot
sl = [S]            # Lista sucetiveis total
il = [I]            # Lista infectados total
rl = [R]            # Lista recuperados total
tl = [t]            # Lista Tempo

# Modelo SIR 

class cidades:
  def __init__(self, S, I, R, r, a):
    self.S = S      # Poulação Sucetivel
    self.I = I      # Poupulação Infectada
    self.R = R      # População Recuperada
    self.r = r      # Taxa de infecção
    self.a = a      # Taxa de recuperação
    self.il = [I]   # Numero de infectados de cada cidade

"""###Cálculos"""

redeGraph = nx.barabasi_albert_graph(N, 2, None) # Gerando o grafo

for i in range(10):
  for j in range(10):
    gama[i][j] = random.uniform(0.0001, 0.0005)

# Inicializa cada N cidade com 500 pessoas sucetiveis, 0 pessoas infectadas, 0 pessoas recuperadas, e uma taxa de infecção e recuperação aleatória
cidadeVet = [cidades(500, 0, 0, random.uniform(0.0001, 0.0005), random.uniform(0.01, 0.02)) for i in range(N)]

# Somente a cidade 5 estará infectada
cidadeVet[5].I = 250
cidadeVet[5].S = 250

for i in np.arange(DT,TMax,DT):
  VariacaoTotalS = 0
  VariacaoTotalI = 0
  VariacaoTotalR = 0
  MigratoriosInfectados = 0
  for j in range(N): 

    for k in range(N):
      if(redeGraph.has_edge(j, k)):
        if(random.random() < 0.8): # 80% de chance de alguem migrar para da cidade k para j
          MigratoriosInfectados += gama[k][j]*cidadeVet[k].I # Se a migrarem, há a possibilidade de infecção

    DS = (-cidadeVet[j].r*cidadeVet[j].S*(cidadeVet[j].I + MigratoriosInfectados)) * DT
    DI = (cidadeVet[j].r*cidadeVet[j].S*(cidadeVet[j].I + MigratoriosInfectados) - cidadeVet[j].a*cidadeVet[j].I) * DT
    DR = (cidadeVet[j].a*(cidadeVet[j].I + MigratoriosInfectados)) * DT

    cidadeVet[j].S += DS
    cidadeVet[j].I += DI
    cidadeVet[j].R += DR

    cidadeVet[j].il.append(cidadeVet[j].I)

    VariacaoTotalS += cidadeVet[j].S
    VariacaoTotalI += cidadeVet[j].I
    VariacaoTotalR += cidadeVet[j].R

  sl.append(VariacaoTotalS)
  il.append(VariacaoTotalI)
  rl.append(VariacaoTotalR)

  tl.append(t)
  t += DT

"""### Gráficos"""

plt.xlabel("Tempo (dias)")
plt.ylabel("População")
plt.plot
plt.plot(tl,il, label = "Infectados", color = "red")
plt.plot(tl,sl, label = "Sucetiveis", color = "blue")
plt.plot(tl, rl, label = "Recuperados", color = "green")
plt.legend(loc="best")
plt.show()

plt.xlabel("Tempo (dias)")
plt.ylabel("População")
plt.plot
plt.plot(tl,cidadeVet[0].il, label = "Infectados cidade 0", color = "red")
plt.plot(tl,cidadeVet[1].il, label = "Infectados cidade 1", color = "blue")
plt.plot(tl,cidadeVet[2].il, label = "Infectados cidade 2", color = "grey")
plt.plot(tl,cidadeVet[3].il, label = "Infectados cidade 3", color = "yellow")
plt.plot(tl,cidadeVet[4].il, label = "Infectados cidade 4", color = "green")
plt.plot(tl,cidadeVet[5].il, label = "Infectados cidade 5", color = "purple")
plt.plot(tl,cidadeVet[6].il, label = "Infectados cidade 6", color = "orange")
plt.plot(tl,cidadeVet[7].il, label = "Infectados cidade 7", color = "black")
plt.plot(tl,cidadeVet[8].il, label = "Infectados cidade 8", color = "pink")
plt.plot(tl,cidadeVet[9].il, label = "Infectados cidade 9", color = "lime")

plt.legend(loc="best")
plt.show()

"""Com apenas uma cidade infectada, podemos identificar os seguintes pontos:
- Há uma demora na infecção de todas as cidades, número de suscetíveis cai devagar
- Curva mais prolongada de infectados totais e um auge maior
- Concentração maior no meio do processo total de infecção

## Simulação 02 - Reduzindo a probabilidade de individuos migrarem de cidade

### Parâmetros
"""

# Váriaveis de controle
DT = 0.01           # Variação do tempo em dias
t = 0               # Tempo inicial
TMax = 365          # Tempo máximo para simulação (365 Dias)
N = 10              # Quantidade de vertices (representado por cidades)

S = 0
I = 0
R = 0

# Infecção
gama = gama = np.zeros((10, 10), dtype=np.float64)

# Listas para plot
sl = [S]            # Lista sucetiveis total
il = [I]            # Lista infectados total
rl = [R]            # Lista recuperados total
tl = [t]            # Lista Tempo

class cidades:
  def __init__(self, S, I, R, r, a):
    self.S = S      # Poulação Sucetivel
    self.I = I      # Poupulação Infectada
    self.R = R      # População Recuperada
    self.r = r      # Taxa de infecção
    self.a = a      # Taxa de recuperação
    self.il = [I]   # Numero de infectados da cidade

"""###Cálculos"""

redeGraph = nx.barabasi_albert_graph(N, 2, None) # Gerando o grafo


for i in range(10):
  for j in range(10):
    gama[i][j] = random.uniform(0.0001, 0.0005)

# Inicializa cada N cidade com 500 pessoas sucetiveis, 0 pessoas infectadas, 0 pessoas recuperadas, e uma taxa de infecção e recuperação aleatória
cidadeVet = [cidades(500, 0, 0, random.uniform(0.0001, 0.0005), random.uniform(0.01, 0.02)) for i in range(N)]

# Somente a cidade 5 estará infectada
cidadeVet[5].I = 250
cidadeVet[5].S = 250

for i in np.arange(DT,TMax,DT):
  VariacaoTotalS = 0
  VariacaoTotalI = 0
  VariacaoTotalR = 0
  MigratoriosInfectados = 0
  for j in range(N): 

    for k in range(N):
      if(redeGraph.has_edge(j, k)):
        if(random.random() < 0.01): # 1% de chance de alguem migrar para da cidade k para j
          MigratoriosInfectados += gama[k][j]*cidadeVet[k].I # Se a migrarem, há a possibilidade de infecção

    DS = (-cidadeVet[j].r*cidadeVet[j].S*(cidadeVet[j].I + MigratoriosInfectados)) * DT
    DI = (cidadeVet[j].r*cidadeVet[j].S*(cidadeVet[j].I + MigratoriosInfectados) - cidadeVet[j].a*cidadeVet[j].I) * DT
    DR = (cidadeVet[j].a*(cidadeVet[j].I + MigratoriosInfectados)) * DT

    cidadeVet[j].S += DS
    cidadeVet[j].I += DI
    cidadeVet[j].R += DR

    cidadeVet[j].il.append(cidadeVet[j].I)

    VariacaoTotalS += cidadeVet[j].S
    VariacaoTotalI += cidadeVet[j].I
    VariacaoTotalR += cidadeVet[j].R

  sl.append(VariacaoTotalS)
  il.append(VariacaoTotalI)
  rl.append(VariacaoTotalR)

  tl.append(t)
  t += DT

"""### Gráficos"""

plt.xlabel("Tempo (dias)")
plt.ylabel("População")
plt.plot
plt.plot(tl,il, label = "Infectados", color = "red")
plt.plot(tl,sl, label = "Sucetiveis", color = "blue")
plt.plot(tl, rl, label = "Recuperados", color = "green")
plt.legend(loc="best")
plt.show()

plt.xlabel("Tempo (dias)")
plt.ylabel("População")
plt.plot
plt.plot(tl,cidadeVet[0].il, label = "Infectados cidade 0", color = "red")
plt.plot(tl,cidadeVet[1].il, label = "Infectados cidade 1", color = "blue")
plt.plot(tl,cidadeVet[2].il, label = "Infectados cidade 2", color = "grey")
plt.plot(tl,cidadeVet[3].il, label = "Infectados cidade 3", color = "yellow")
plt.plot(tl,cidadeVet[4].il, label = "Infectados cidade 4", color = "green")
plt.plot(tl,cidadeVet[5].il, label = "Infectados cidade 5", color = "purple")
plt.plot(tl,cidadeVet[6].il, label = "Infectados cidade 6", color = "orange")
plt.plot(tl,cidadeVet[7].il, label = "Infectados cidade 7", color = "black")
plt.plot(tl,cidadeVet[8].il, label = "Infectados cidade 8", color = "pink")
plt.plot(tl,cidadeVet[9].il, label = "Infectados cidade 9", color = "lime")

plt.legend(loc="best")
plt.show()

"""Ao reduzir a probabilidade de migração entre as cidades, observa-se que:
- Demora na infecção de todas as cidades, mais que na simulação 1
- Curva mais prolongada de infectados totais e diferentes auges (alta variação)
- Concentração maior no meio do processo total de infecção com um pico prolongado

## Simulação 03 - Simulação sem interferência entre as cidades

### Parâmetros
"""

# Váriaveis de controle
DT = 0.01           # Variação do tempo
t = 0               # Tempo inicial
TMax = 365          # Tempo máximo para simulação (365 Dias)
N = 10              # Quantidade de vertices

S = 0
I = 0
R = 0

# Infecção
gama = gama = np.zeros((10, 10), dtype=np.float64)

# Listas para plot
sl = [S]            # Lista sucetiveis total
il = [I]            # Lista infectados total
rl = [R]            # Lista recuperados total
tl = [t]            # Lista Tempo

# Modelo SIR 

class cidades:
  def __init__(self, S, I, R, r, a):
    self.S = S      # Poulação Sucetivel
    self.I = I      # Poupulação Infectada
    self.R = R      # População Recuperada
    self.r = r      # Taxa de infecção
    self.a = a      # Taxa de recuperação
    self.il = [I]   # Numero de infectados de cada cidade

"""###Cálculos"""

redeGraph = nx.barabasi_albert_graph(N, 2, None) # Gerando o grafo


for i in range(10):
  for j in range(10):
    gama[i][j] = random.uniform(0.0001, 0.0005)

# Inicializa cada N cidade com 500 pessoas sucetiveis, 0 pessoas infectadas, 0 pessoas recuperadas, e uma taxa de infecção e recuperação aleatória
cidadeVet = [cidades(500, 0, 0, random.uniform(0.0001, 0.0005), random.uniform(0.01, 0.02)) for i in range(N)]

# As cidades 5, 0, 8 e 9 estarão infectadas
cidadeVet[5].I = 5
cidadeVet[5].S = 495

cidadeVet[0].I = 2
cidadeVet[0].S = 498

cidadeVet[8].I = 20
cidadeVet[8].S = 480

cidadeVet[9].I = 1
cidadeVet[9].S = 499

for i in np.arange(DT,TMax,DT):
  VariacaoTotalS = 0
  VariacaoTotalI = 0
  VariacaoTotalR = 0
  MigratoriosInfectados = 0
  for j in range(N): 

    for k in range(N):
      if(redeGraph.has_edge(j, k)):
        if(random.random() < 0): # 0% de chance de alguem migrar para da cidade k para j
          MigratoriosInfectados += gama[k][j]*cidadeVet[k].I # Se a migrarem, há a possibilidade de infecção

    DS = (-cidadeVet[j].r*cidadeVet[j].S*(cidadeVet[j].I + MigratoriosInfectados)) * DT
    DI = (cidadeVet[j].r*cidadeVet[j].S*(cidadeVet[j].I + MigratoriosInfectados) - cidadeVet[j].a*cidadeVet[j].I) * DT
    DR = (cidadeVet[j].a*(cidadeVet[j].I + MigratoriosInfectados)) * DT

    cidadeVet[j].S += DS
    cidadeVet[j].I += DI
    cidadeVet[j].R += DR

    cidadeVet[j].il.append(cidadeVet[j].I)

    VariacaoTotalS += cidadeVet[j].S
    VariacaoTotalI += cidadeVet[j].I
    VariacaoTotalR += cidadeVet[j].R

  sl.append(VariacaoTotalS)
  il.append(VariacaoTotalI)
  rl.append(VariacaoTotalR)

  tl.append(t)
  t += DT

"""### Gráficos"""

plt.xlabel("Tempo (dias)")
plt.ylabel("População")
plt.plot
plt.plot(tl,il, label = "Infectados", color = "red")
plt.plot(tl,sl, label = "Sucetiveis", color = "blue")
plt.plot(tl, rl, label = "Recuperados", color = "green")
plt.legend(loc="best")
plt.show()

plt.xlabel("Tempo (dias)")
plt.ylabel("População")
plt.plot
plt.plot(tl,cidadeVet[0].il, label = "Infectados cidade 0", color = "red")
plt.plot(tl,cidadeVet[1].il, label = "Infectados cidade 1", color = "blue")
plt.plot(tl,cidadeVet[2].il, label = "Infectados cidade 2", color = "grey")
plt.plot(tl,cidadeVet[3].il, label = "Infectados cidade 3", color = "yellow")
plt.plot(tl,cidadeVet[4].il, label = "Infectados cidade 4", color = "green")
plt.plot(tl,cidadeVet[5].il, label = "Infectados cidade 5", color = "purple")
plt.plot(tl,cidadeVet[6].il, label = "Infectados cidade 6", color = "orange")
plt.plot(tl,cidadeVet[7].il, label = "Infectados cidade 7", color = "black")
plt.plot(tl,cidadeVet[8].il, label = "Infectados cidade 8", color = "pink")
plt.plot(tl,cidadeVet[9].il, label = "Infectados cidade 9", color = "lime")

plt.legend(loc="best")
plt.show()

"""Com a probabilidade de migração nula, conclui-se que:
- Mesmo auges nas infecções das cidades infectadas inicialmente
- Curva mais curta e achatada de infectados totais e um auge menor, a infecção entre cidades (menor concentração de infectados)
- Número de suscetíveis cai rapidamente e para (nem todas as cidades estão infectadas)

## Simulação 04 - Todas as cidades infectadas

### Parâmetros
"""

# Váriaveis de controle
DT = 0.01           # Variação do tempo
t = 0               # Tempo inicial
TMax = 365          # Tempo máximo para simulação (365 Dias)
N = 10              # Quantidade de vertices

S = 0
I = 0
R = 0

# Infecção
gama = gama = np.zeros((10, 10), dtype=np.float64)

# Listas para plot
sl = [S]            # Lista sucetiveis total
il = [I]            # Lista infectados total
rl = [R]            # Lista recuperados total
tl = [t]            # Lista Tempo

# Modelo SIR 

class cidades:
  def __init__(self, S, I, R, r, a):
    self.S = S      # Poulação Sucetivel
    self.I = I      # Poupulação Infectada
    self.R = R      # População Recuperada
    self.r = r      # Taxa de infecção
    self.a = a      # Taxa de recuperação
    self.il = [I]   # Numero de infectados de cada cidade

"""###Cálculos"""

redeGraph = nx.barabasi_albert_graph(N, 2, None) # Gerando o grafo


for i in range(10):
  for j in range(10):
    gama[i][j] = random.uniform(0.0001, 0.0005)

# Inicializa cada N cidade com 500 pessoas sucetiveis, 0 pessoas infectadas, 0 pessoas recuperadas, e uma taxa de infecção e recuperação aleatória
cidadeVet = [cidades(500, 0, 0, random.uniform(0.0001, 0.0005), random.uniform(0.01, 0.02)) for i in range(N)]

# Todas cidades estão infectadas
cidadeVet[0].I = 100
cidadeVet[0].S = 400

cidadeVet[1].I = 2
cidadeVet[1].S = 498

cidadeVet[2].I = 500
cidadeVet[2].S = 0

cidadeVet[3].I = 17
cidadeVet[3].S = 483

cidadeVet[4].I = 44
cidadeVet[4].S = 456

cidadeVet[5].I = 250
cidadeVet[5].S = 250

cidadeVet[6].I = 129
cidadeVet[6].S = 371

cidadeVet[7].I = 200
cidadeVet[7].S = 300

cidadeVet[8].I = 403
cidadeVet[8].S = 97

cidadeVet[9].I = 0
cidadeVet[9].S = 500

for i in np.arange(DT,TMax,DT):
  VariacaoTotalS = 0
  VariacaoTotalI = 0
  VariacaoTotalR = 0
  MigratoriosInfectados = 0
  for j in range(N): 

    for k in range(N):
      if(redeGraph.has_edge(j, k)):
        if(random.random() < 0.02): # 2% de chance de alguem migrar para da cidade k para j
          MigratoriosInfectados += gama[k][j]*cidadeVet[k].I # Se a migrarem, há a possibilidade de infecção

    DS = (-cidadeVet[j].r*cidadeVet[j].S*(cidadeVet[j].I + MigratoriosInfectados)) * DT
    DI = (cidadeVet[j].r*cidadeVet[j].S*(cidadeVet[j].I + MigratoriosInfectados) - cidadeVet[j].a*cidadeVet[j].I) * DT
    DR = (cidadeVet[j].a*(cidadeVet[j].I + MigratoriosInfectados)) * DT

    cidadeVet[j].S += DS
    cidadeVet[j].I += DI
    cidadeVet[j].R += DR

    cidadeVet[j].il.append(cidadeVet[j].I)

    VariacaoTotalS += cidadeVet[j].S
    VariacaoTotalI += cidadeVet[j].I
    VariacaoTotalR += cidadeVet[j].R

  sl.append(VariacaoTotalS)
  il.append(VariacaoTotalI)
  rl.append(VariacaoTotalR)

  tl.append(t)
  t += DT

"""### Gráficos"""

plt.xlabel("Tempo (dias)")
plt.ylabel("População")
plt.plot
plt.plot(tl,il, label = "Infectados", color = "red")
plt.plot(tl,sl, label = "Sucetiveis", color = "blue")
plt.plot(tl, rl, label = "Recuperados", color = "green")
plt.legend(loc="best")
plt.show()

plt.xlabel("Tempo (dias)")
plt.ylabel("População")
plt.plot
plt.plot(tl,cidadeVet[0].il, label = "Infectados cidade 0", color = "red")
plt.plot(tl,cidadeVet[1].il, label = "Infectados cidade 1", color = "blue")
plt.plot(tl,cidadeVet[2].il, label = "Infectados cidade 2", color = "grey")
plt.plot(tl,cidadeVet[3].il, label = "Infectados cidade 3", color = "yellow")
plt.plot(tl,cidadeVet[4].il, label = "Infectados cidade 4", color = "green")
plt.plot(tl,cidadeVet[5].il, label = "Infectados cidade 5", color = "purple")
plt.plot(tl,cidadeVet[6].il, label = "Infectados cidade 6", color = "orange")
plt.plot(tl,cidadeVet[7].il, label = "Infectados cidade 7", color = "black")
plt.plot(tl,cidadeVet[8].il, label = "Infectados cidade 8", color = "pink")
plt.plot(tl,cidadeVet[9].il, label = "Infectados cidade 9", color = "lime")

plt.legend(loc="best")
plt.show()

"""Com todas as cidade com pelo menos 1 infectado, chegamos aos seguintes pontos:
- Pico grande no auge das infecções das cidades (concentração no início, infecção mais rápida quando conectados e ainda mais quando todos já estão infectados)
- Crescimento menor do número de infectados (todas cidades já estão infectadas quase no auge desde o início)
- Número de suscetíveis cai mais rapidamente (todas cidades já estão infectadas, então já têm menos pessoas para contaminar)
"""