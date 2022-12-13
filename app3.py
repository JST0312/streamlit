# 판다스의 데이터프레임을 웹화면으로 보여주는 방법

import streamlit as st
import pandas as pd


def main() :

   st.title('아이리스 꽃 데이터')                                       
   
   df = pd.read_csv('streamlit_Data/iris.csv')
   st.datafrme(df)

   species = df['species'].unique()

if __name__=='__main__':   
    main()