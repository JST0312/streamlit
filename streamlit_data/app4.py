import streamlit as sp
import pandas as pd

def main():
    df=pd.read_csv('streamlit_data/iris.csv')


   
   
   
   
   
   
   
        if  st.button ('데이터프레임 보기') :
         st .dataframe(df)


# 버튼을 클릭하면 데이터프레임이 보이도록 만들기
# ui요소들을 처리하는 방법
# 버튼 라디오버튼 셀렉트박스 멀티 셀렉트 슬라이더




if __name__=='__main__':
    main()