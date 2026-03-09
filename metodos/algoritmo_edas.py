# -*- coding: utf-8 -*-
"""
ATUALIZADO on Mon Mar  9 15:55:17 2026

@author: adh_r
"""

# -*- coding: utf-8 -*-
"""
VERSÃO ANTIGA
Created on Mon Jun 28 18:14:41 2021
@author: Adhmir Renan Voltolini Gomes
"""

"""
Evaluation Based on Distance from Average Solution (EDAS)

O método EDAS (Ghorabaee et al., 2015) seleciona a melhor alternativa
com base na distância em relação à solução média (AV).

São calculadas duas medidas:

PDA – Positive Distance from Average
NDA – Negative Distance from Average

Alternativas com maiores PDA e menores NDA são consideradas melhores.

Etapas do método:

1) Construção da matriz de decisão (X)
2) Cálculo da solução média para cada critério
3) Cálculo das distâncias positivas e negativas
4) Cálculo dos índices SPI e SNI
5) Determinação do score EDAS e ranking final
"""

import pandas as pd
import numpy as np


# ---------------------------------------------------------
# PDA - Positive Distance from Average
# ---------------------------------------------------------
def pda(x):

    x = x.copy().astype(float)

    for i in range(len(x.columns)):

        media_coluna = x.iloc[:, i].mean()

        for j in range(len(x)):

            xij = x.iloc[j, i]

            valor = max(0, (xij - media_coluna)) / media_coluna

            x.iloc[j, i] = valor

    return x


# ---------------------------------------------------------
# NDA - Negative Distance from Average
# ---------------------------------------------------------
def nda(x):

    x = x.copy().astype(float)

    for i in range(len(x.columns)):

        media_coluna = x.iloc[:, i].mean()

        for j in range(len(x)):

            xij = x.iloc[j, i]

            valor = max(0, (media_coluna - xij)) / media_coluna

            x.iloc[j, i] = valor

    return x


# ---------------------------------------------------------
# SPI e SNI
# ---------------------------------------------------------
def spi_sni(pda_df, nda_df, pesos):

    pesos = np.array(pesos)

    # SPI
    spi = (pda_df * pesos).sum(axis=1)

    # SNI
    sni = (nda_df * pesos).sum(axis=1)

    spi = spi.reset_index(drop=True)
    sni = sni.reset_index(drop=True)

    spi.name = "spi"
    sni.name = "sni"

    # normalização
    spi_norm = spi / spi.max()
    sni_norm = 1 - (sni / sni.max())

    df = pd.concat([spi_norm, sni_norm], axis=1)

    df.columns = ["spi", "sni"]

    return df


# ---------------------------------------------------------
# EDAS completo
# ---------------------------------------------------------
def edas(categoria, x, pesos):

    x = x.copy().astype(float)

    # PDA
    x_pda = pda(x.copy()).reset_index(drop=True)

    # NDA
    x_nda = nda(x.copy()).reset_index(drop=True)

    # SPI e SNI
    df_spi_sni = spi_sni(x_pda, x_nda, pesos).reset_index(drop=True)

    # score EDAS
    df_spi_sni["EDAS"] = 0.5 * (df_spi_sni["spi"] + df_spi_sni["sni"])

    # ranking
    df_spi_sni["Ranking"] = df_spi_sni["EDAS"].rank(method="min", ascending=False)

    resultado = pd.concat(
        [
            categoria.reset_index(drop=True),
            x.reset_index(drop=True),
            x_pda.add_suffix("_PDA"),
            x_nda.add_suffix("_NDA"),
            df_spi_sni
        ],
        axis=1
    )

    return resultado


