import streamlit as st
import pandas as pd
import numpy as np
import metodos.normalizarDados as nmd
import metodos.algoritmo_edas as ed

import io

exemploDados = {
  "Opções": ['Alternativa A', 'Alternativa B', 'Alternativa C'],
  "Critério A": [50, 40, 85],
  "Critério B": [60, 20, 50],
  "Critério C": [40, 30, 70]
}
df = pd.DataFrame(exemploDados)

normalizados = pd.DataFrame([])
listaNormalizar = []
istacategorias = [] 
listaNormalizarMaior = [] 
listaNormalizarMenor = []
pesos = 1

def main():
    global df, listaNormalizar, normalizados, pesos
    global listacategorias, listaNormalizarMaior, listaNormalizarMenor

    st.set_page_config(
        page_title="ApoioDecisao",
        page_icon='📈'
    )

    st.title('Evaluation based on distance from average solution (EDAS)')
    st.sidebar.success('Menu')

    st.sidebar.subheader("Escolha seu arquivo")
    cont = st.container()
    col1, col2, col3 = st.columns(3)
    cont2 = st.container()
    col4, col5, col6, col7, col8 = st.columns(5)
    
    
    cont3 = st.container()
    cont4 = st.container()
    cont5 = st.container()
    
    
    arquivoUpload = st.sidebar.file_uploader(label="Upload arquivo de xlsx",  ) 
    
    if arquivoUpload is not None:
       
        try:
            df = pd.read_excel(arquivoUpload, engine = "openpyxl")
        except Exception as e:
            print(e)
            df = pd.read_csv(arquivoUpload)
        try:
            cont.dataframe(df)
        except Exception as e:
            print(e)
            st.write('Por favor faça o upload dos seus dados')
        opcoes1 = col1.multiselect('Selecione as colunas de controle', df.columns)
        listacategorias = opcoes1
        opcoes2 = col2.multiselect('Normalizar MAIOR MELHOR', df.drop(opcoes1, axis=1).columns)
        listaNormalizarMaior = opcoes2

        opcoes3 = col3.multiselect('Normalizar MENOR MELHOR',  df.drop(opcoes1+opcoes2, axis=1).columns)
        listaNormalizarMenor = opcoes3
        
        btnCalcular = cont4.button('Calcular')
        
        if btnCalcular: 
            try:
                normalizados = nmd.normalizar(df[listacategorias], 
                                              df[listaNormalizarMaior],
                                              df[listaNormalizarMenor])
                
                print(normalizados.head())
                print()
                print(pesos)
                print()
                metododp2 =  ed.edas(normalizados[listacategorias],
                                 normalizados[listaNormalizarMaior+listaNormalizarMenor],
                                 pesos
                                 )
                print(metododp2.head())
                cont5.dataframe(metododp2.style.highlight_max(axis=0))
                    
                st.download_button(
                        label= "Baixar resultados",
                        data= criar_excel(metododp2),
                        file_name ='resultados.xlsx',
                        mime="application/vnd.ms-excel",)               
                
                                 
            except Exception as e:
                st.write('Por favor confira as colunas selecionadas.')
        
def criar_excel(dados):
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer) as writer:
        dados.to_excel(writer)
    return buffer

def LstPesosConstante(tam):
    colunas = tam.columns
    wth = list([1]*len(tam.columns))
    dfConstante = pd.DataFrame(wth).transpose()
    dfConstante.columns = colunas
    dfConstante.index = ['Pesos']
    
    
    return dfConstante, wth

if __name__ == '__main__':
    main()
        