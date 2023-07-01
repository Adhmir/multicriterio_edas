# -*- coding: utf-8 -*-
"""
Created on Mon May 29 10:51:08 2023

@author: Adhmir Renan Voltolini Gomes
"""
import pandas as pd

def nMaiorMelhor(x):
        
    for i in range(len(x.columns)):
        def_norm = x.copy()
        for j in range(len(x)):
            # Pega o valor da linha e coluna
            xij = x.iloc[j,i:i+1].values
            #Pega o máximo da coluna normalizado, sempre do df que não é modificado
            max_coluna = def_norm[def_norm.columns[i:i+1]].max()
            #Pega o grau de liberdade
            min_coluna = def_norm[def_norm.columns[i:i+1]].min()
            #Pega o valor, diminui da soma menos o valor e divide pelo grau de liberdade
            primeiro_valor = ((xij-min_coluna)/(max_coluna-min_coluna))
            # substitui o valor
            x.iloc[j,i:i+1] = primeiro_valor
     
    #df_norm = (x-x.min())/(x.max()-x.min())
    return x


def nMenorMelhor(x):
        
    for i in range(len(x.columns)):
        def_norm = x.copy()
        for j in range(len(x)):
            # Pega o valor da linha e coluna
            xij = x.iloc[j,i:i+1].values
            #Pega o máximo da coluna normalizado, sempre do df que não é modificado
            max_coluna = def_norm[def_norm.columns[i:i+1]].max()
            #Pega o grau de liberdade
            min_coluna = def_norm[def_norm.columns[i:i+1]].min()
            #Pega o valor, diminui da soma menos o valor e divide pelo grau de liberdade
            primeiro_valor = ((max_coluna-xij)/(max_coluna-min_coluna))
            # substitui o valor
            x.iloc[j,i:i+1] = primeiro_valor
    #df_norm = (x-x.min())/(x.max()-x.min())
   
    return x


def normalizar(categorias, maior_melhor,menor_melhor):
    if len(categorias.columns) != 0:
        if (len(maior_melhor.columns) == 0) and (len(menor_melhor.columns) == 0):
            dfnormalizado = categorias.copy()
            dfnormalizado.columns = categorias.columns
        
            print('\n\nlistas vazias')
            
        elif (len(maior_melhor.columns) != 0) and (len(menor_melhor.columns) == 0):
            dfmaior = nMaiorMelhor(maior_melhor)
            dfnormalizado = pd.concat([categorias,dfmaior], axis=1, ignore_index=True)
            colunas = list(categorias.columns)+list(dfmaior.columns)
            dfnormalizado.columns = colunas
            print('\n\napenas quanto maior melhor')
            
        elif (len(maior_melhor.columns) == 0) and (len(menor_melhor.columns) != 0):
            dfmenor = nMenorMelhor(menor_melhor)
            dfnormalizado = pd.concat([categorias,dfmenor], axis=1, ignore_index=True)
            colunas = list(categorias.columns)+list(dfmenor.columns)
            dfnormalizado.columns = colunas
            
            print('\n\napenas quanto menor melhor')
            
        elif (len(maior_melhor.columns) != 0) and (len(menor_melhor.columns) != 0):
            dfmaior = nMaiorMelhor(maior_melhor)
            dfmenor = nMenorMelhor(menor_melhor)
            dfnormalizado = pd.concat([categorias,dfmaior, dfmenor], axis=1, ignore_index=True)
            colunas = list(categorias.columns)+list(dfmaior.columns)+list(dfmenor.columns)
            dfnormalizado.columns = colunas
            print('\n\nambos tipos de normalização, quanto maior melhor, quanto menor melhor')
    else:
        if (len(maior_melhor.columns) == 0) and (len(menor_melhor.columns) == 0):
            dfnormalizado = categorias.copy()
            dfnormalizado.columns = categorias.columns
        
            print('\n\nlistas vazias')
            
        elif (len(maior_melhor.columns) != 0) and (len(menor_melhor.columns) == 0):
            dfmaior = nMaiorMelhor(maior_melhor)
            dfnormalizado = dfmaior.copy()
            colunas = list(dfmaior.columns)
            dfnormalizado.columns = colunas
            print('\n\napenas quanto maior melhor')
            
        elif (len(maior_melhor.columns) == 0) and (len(menor_melhor.columns) != 0):
            dfmenor = nMenorMelhor(menor_melhor)
            dfnormalizado = dfmenor.copy()
            colunas = list(dfmenor.columns)
            dfnormalizado.columns = colunas
            
            print('\n\napenas quanto menor melhor')
            
        elif (len(maior_melhor.columns) != 0) and (len(menor_melhor.columns) != 0):
            dfmaior = nMaiorMelhor(maior_melhor)
            dfmenor = nMenorMelhor(menor_melhor)
            dfnormalizado = pd.concat([dfmaior, dfmenor], axis=1, ignore_index=True)
            colunas = list(dfmaior.columns)+list(dfmenor.columns)
            dfnormalizado.columns = colunas
            print('\n\nambos tipos de normalização, quanto maior melhor, quanto menor melhor')
    return dfnormalizado



'''
df1 = pd.DataFrame([['s',1,2],
                     ['s',3,4],
                     ['s',5,6],
                     ['s',7,8],
                     ['s',9,10],
                     ['t',31,32],
                     ['t',44,55],
                     ['t',22,11],
                     ['t',33,77],
                     ['t',66,54]],
                   columns=['categoria', 'numberA', 'numberB'])


"""
Apenas categorias
"""
categorias= df1.copy()
maior_melhor = pd.DataFrame([])
menor_melhor = pd.DataFrame([])
X1_cat = normalizar(categorias, maior_melhor,menor_melhor)
 
"""
Apenas quanto maior melhor
"""
categorias= df1.copy()
categorias = df1.drop(['numberA'], axis=1)
maior_melhor = pd.DataFrame(df1['numberA'].copy())
menor_melhor = pd.DataFrame([]) 
X2_maior = normalizar(categorias, maior_melhor,menor_melhor)

"""
Apenas quanto menor melhor
"""
categorias= df1.copy()
categorias = df1.drop(['numberB'], axis=1)
menor_melhor = pd.DataFrame(df1['numberB'].copy())
maior_melhor = pd.DataFrame([]) 
X3_menor = normalizar(categorias, maior_melhor,menor_melhor)

"""
AMBOS
"""
categorias= df1.copy()
categorias = df1.drop(['numberA','numberB'], axis=1).copy()
maior_melhor = pd.DataFrame(df1['numberA'].copy())
menor_melhor = pd.DataFrame(df1['numberB'].copy()) 
X4_ambos = normalizar(categorias, maior_melhor,menor_melhor) 
'''

