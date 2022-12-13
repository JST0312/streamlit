import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import altair as alt



def main():
    df=pd.read_csv('streamlit_data/lang_data.csv')


    st.dataframe(df.head())

    column_menu = df.columns[1:]
    
    choice_list=st.multiselect('프로그래밍 언어를 선택하시오',)

    if len(choice_list) !=0:


        #유저가 선택한 언어만 차트르 그린다
        df_selected=df[choice_list]

        ## 스트림릿에서 제공하는 라인차트
        st.line_chart(df_selected)

        ## 스트림릿에서 제공하는 영역차트
        st.area_chart(df_selected)
        
        ## 스트림릿에서 제공하는 바차트
        st.bar_chart(df_selected)


  
    df2=pd.read_csv('streamlit_data/iris.csv')
    ### altair라이브러리의 mark_cicle함수 사용법
    alt.Chat(df2).mark_circle().encode(
        x='petal_length',
        y='petal_width',
        colot='species'

    )
    

if __name__=='__main__':
    main()
