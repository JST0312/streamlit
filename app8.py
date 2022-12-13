import streamlit as st
from app_home import run_home_app
from app_eda  import run_eda_app
from app_ml import run_ml_app
def main():
    st.title('파일 분리 앱')

    #EXPLoratory Data Analysis  
    menu=['home','EDA','ML','About']

    choice=st.sidebar.selectbox('메뉴',menu)


    if choice=='home':
        run_home_app()
    elif choice=='EDA':
         run_eda_app()
    elif choice=='ML':
        run_ml_app()
    elif choice=='About':
        pass



if __name__=='__main__':
    main()