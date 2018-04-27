# -*- coding:utf-8 -*-
import numpy as np
import pickle as pickle
#import tensorflow as tf
import matplotlib.pyplot as plt
import math
import gym
env = gym.make('CartPole-v0')
env.reset()
random_episodes = 0
reward_sum = 0

""" OBSERVATION """
POS_CART = 2.4
VEL_CART = 2.5
ANG_PEND = 2   #valor em radianos
VEL_PEND = 2.5

TAM_INTERVALO_OBJS = 10
TAM_INTERVALO_VEL  = 10

numeroDevariaveis = env.observation_space.shape[0] #shape de 0 contem o array observation q possui todas as variaveis do problema

# QT_STATES = TAM_INTERVALO_ITENS_OBS^QT_ITENS(4)
#Box com 4 posições
box = np.zeros((4,numeroDevariaveis))
#print(Box)

# pos 0 --> posição do carrinho [-2.4, 2.4]
#box[0] = np.linspace(-POS_CART, POS_CART, TAM_INTERVALO_OBJS)
#print(box[0])

# pos 1 --> velocidade do carrinho (-inf, inf)
"""     Percebeu-se observando a execucao do arquivo original que a velocidade do cart varia entre -2 e 2.
        Por isso da definicao desse intervalo de valores para velocidade """
#box[1] = np.linspace(-VEL_CART,VEL_CART, TAM_INTERVALO_VEL)
#print(box[1])

#pos 2 --> ângulo pêndulo [~-41.8, ^41.8]
"""     Como no link explicando o problema, citava que um episodio terminava quando o angulo passava de 12º do centro,
        decidiu-se entao, demilitar o intervalo de valores para o angulo de -15º a 15º """
#box[2] = np.linspace(-ANG_PEND, ANG_PEND, TAM_INTERVALO_OBJS)
#print(box[2])
#pos 3 --> velocidade pêndulo (-inf, inf)
"""     Definição do intervalo segue a mesma ideia da velocidade do cart
        Porém, intervalo ai de -5 a 5"""
#box[3] = np.linspace(-VEL_PEND,VEL_PEND, TAM_INTERVALO_VEL)
#print(box[3])
""" FIM OBSERVATION """

#print(box)
""" ACTIONS """
actions = range(env.action_space.n)
""" FIM ACTIONS """


""" REWARD """
# Recompensa é 1 para cada passo dado, incluindo o passo de terminação
# """ FIM REWARD """
REWARD = 1 

""" ESTADO INICIAL """

# Todas as observations sao atribuidas a um valor aleatorio uniforme entre +- 0.05

""" FIM ESTADO INICIAL """

""" TERMINO DE UM EPISODIO """

# Episodio termina
#  se --> angulo do pendulo é maior que +-12º #um exemplo citou que o angulo seria 15º?????
# 	--> posicao do carrinho é maior que +- 2.4 ( o centro do carrinho atinge a borda da janela de exibicao
# 	--> duracao do episodio for maior que 200

""" FIM TERMINO DE UM EPISODIO """

""" RESOLUCAO DO PROBLEMA """

# Problema é resolvido quando a recompensa média é maior ou igual a 195.0 em 100 tentativas consecutivas

""" FIM RESOLUCAO DO PROBLEMA """

# state = np.zeros(4)
# for i in range(4):
#         state[i] = np.digitize(observation[i],box[i])
# print(state)




#inicia Qtable com valores todos zerados.
# funcao é chamada apenas na primeira vez que rodar o problema
def init_qtable(): 
    arq_Qtable = open('qtable.txt','w')
    for i in range(10**4):
        arq_Qtable.write("0.0,0.0,0.0,0.0;0,0\n")


#salva Qtable atual em um arquivo
# para posteriormente continuar o treinamento "de onde parou"
def save_qtable():
    Qtable = open('qtable.txt', 'w')
    
    qt_linhas = Qtable.shape[0]


def read_qtable():
    arq_qtable = open('qtable.txt')
    qtable = np.array([l.split(';') for l in arq_qtable.readlines()])
    
    qt_l,qt_c = qtable.shape
    
    observation = np.array([qtable[:,0]]) # ta pegando o observation do arquivo 
    action = np.array([qtable[:,1]]) # pegando acoes do arquivo

    print(observation)

    #splitar observation 


    
    return qtable




arq_Qtable = init_qtable()
qtable = read_qtable()

#data=np.array([d.split(',') for d in fdata.readlines()],dtype=float)

#print(qtable.shape[0])
#print(qtable.shape[1])

#print(qtable[0])



"""
#
# Aqui ponha o seu codigo para ler os valores dos estados, se houver
#
while random_episodes < 100:
    observation = env.reset()
    for t in range(200):
        env.render()
        #print(observation)
#
# Aqui ponho o seu codigo para salvar a observacao, estado
#
#
# Aqui ponha o seu codigo para escolher a melhor acao dependendo do estado atual
#
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print(observation)
        if done:
#
# Aqui ponha o seu codigo para atualizar os valores dos estados apos uma execucao
#
            print("Episode finished after {} timesteps".format(t+1))
            break
#
#   Aqui ponha o seu codigo para salvar os valores dos estados calculados
"""
