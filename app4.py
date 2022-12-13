import streamlit as st
import pandas as pd

def main():
    df=pd.read_csv('streamlit_data/iris.csv')


   
    if st.  button ('데이터프레임 보기') :
         st .dataframe( df )


# 버튼을 클릭하면 데이터프레임이 보이도록 만들기
# ui요소들을 처리하는 방법
# 버튼 라디오버튼 셀렉트박스 멀티 셀렉트 슬라이더

    name= 'Mike'

    if st.button('대문자로') :
        st.text(name.upper())
        
    if st.button('소문자로') :
        st.text(name.lower())

    status=st.radio('정렬을 선택하세요',['오름차순정렬,내림차순정렬'])
    
    if status =='오름차순정렬':
        # df의 petal_length컬럼을 오름차순으로 정렬해서 보여주세요

       st.dataframe( df.sort_values('petal_lenfth'))
    elif status == '내림차순정렬' :
        #df 의 petal_lenfth컬럼을 내림차순으로 정렬해서 보여주세요

         st.dataframe( df.sort_values('petal_length',ascending=False))

    

    # 체크밥ㄱ스를 체크하면 데이터프레임이 나오고
    # 해제하면 데이터프레임 나오지않게

    if  st.checkbox('show/hide') :
        st.dataframe(df)
    else:
        st.write('')

        #셀렉트박스 : 여러개중에 한개 선택
        language=['python','c','java','php','go']

        my_choice= st.selectbox('좋아하는 단어를 선택하시오',language)
        # 유저가 선택하면 해당언어를 다음처럼 표시해준다
        #저는 python언어를 가장 좋아합니다
        # 저는 fava언어를 가장좋아합니다

    st.text ('저는'+ my_choice +'언어룰 가장좋아합니다.')

# 만약 유저가 선택한 언어가 파이썬이나 go언어이면
# 배우기 쉽습니다 라고 화면에 보여주고 
# 자바나 씨언어를 선택하면


    selected_list= st.multiselect('원하는 컬럼을 선택하세요',df.columns)
    print(selected_list)


# 유저가 컬럼을 선택하면 해당컬럼을 화면에 보여주고
# 유저가 아무컬럼도 선택하지 않으면 데이터프레임 보여주지 않는다
    if len(selected_list)==0:
      st.text('')
    
    else:

         st.dataframe(df[selected_list])

age=st. slider('나이',1,100)

st.text('당신이 선택한 나이는'+ str(age) +'입니다')
st.slider('데이터',1,100,step=5)
st.slider('데이터',1,200,value=5)
st.slider('데이터',0.0,1.0,step=0.1)

with st.expander('hello'):
    st.text('안녕하세요!')


if __name__=='__main__':
    main()