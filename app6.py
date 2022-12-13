import streamlit as st



def main():
    #텍스트를 입력받는 방법
    name= st.text_input('이름을 입력하세요')    

    st.title (name)   

    name2= st.text_input('이름입력!',max_chars=5)
    st.title(name2)

    message=st.text_area('메세지를 입력하게요',height=10)
    st.text(message)

    year=st.number_input('출생년도를 입력하세요 ',1000,3000)
    st.text(year)


    number= st.number_input('실수를 입력하세요',0.5,100.0,step=0.3)

    #날짜 입력받는 방법
    my_data=st.date_input('약속날짜입력')

    st.write(my_data)
    #시간입력받은 방법
    my_time=st.time_input('약속시간선택')
    st.write(my_time)

    st.text( my_time.strftime('%H%M'))

    #비밀번호 입력받는 방법

    password=st.text_input('비밀번호 입력',type='password')
 
    st.text(password)
    #색깔입력
    color=st.color_picker('색을 선택하세여')
        
    st.text(color)
if __name__=='__main__':
    main()