# -*- coding: utf-8 -*-
"""
Created on Mon May 29 10:51:08 2023
Atualizado 25-06-2026

@author: Adhmir Renan Voltolini Gomes
"""
# -*- coding: utf-8 -*-

import pandas as pd


def nMaiorMelhor(df):
    """
    Min-Max
    Quanto maior melhor
    """
    return (df - df.min()) / (df.max() - df.min())


def nMenorMelhor(df):
    """
    Min-Max invertido
    Quanto menor melhor
    """
    return (df.max() - df) / (df.max() - df.min())


def normalizar(categorias=None,
               maior_melhor=None,
               menor_melhor=None):

    partes = []

    if categorias is not None and not categorias.empty:
        partes.append(categorias)

    if maior_melhor is not None and not maior_melhor.empty:
        partes.append(nMaiorMelhor(maior_melhor))

    if menor_melhor is not None and not menor_melhor.empty:
        partes.append(nMenorMelhor(menor_melhor))

    return pd.concat(partes, axis=1) if partes else pd.DataFrame()
