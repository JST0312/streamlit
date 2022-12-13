# 파일을 업로드 하는 방법


import streamlit as st
import pandas as pd
import os
from datetime import date,datetime
from PIL import Image

# 함수정의
# 디렉토리 (폴더)명과 파일을 알려주면
# 해당 디렉토리에 파일을 저장해 주는 함수
def save_uploaded_file(directory,file):
    #1 디렉토리가 있는지 확인하여 없으면 먼저 디렉토리부터 만든다
    if not os.path.exists(directory):
        os.makedirs(directory)

    #2디렉토리가 있으니 파일을 저장한다
    with open(os.path.join(directory,file.name),'wb')as f:
        f.write(file.getbuffer())

    #3 파일 저장이 성공했으니 화면에 성공했다고 보여주면서 리턴
    return st.success('{}에{}파일이 저장되었습니다'.format(directory,file.name))





def main():
    st.title('파일 업로드 프로젝트')

    menu=['image','csv','About']

    choice= st.sidebar.selectbox('메뉴',menu)

    if choice== 'image':
        st.subheader('이미지 파일 업로드')

        file =st.file_uploader('이미지를 업로드 하세요',type=['jpg','jpeg','peng'])

        if file is not None:
           # st.text(file.name)
           #st.text(file.size)
           #st.text(file.type)

           # 파일명을 일관성있게 회사의  파일명 규칙대로 바꾼다
           # 현재시간을 조합하여 파일명을 만들면 유니크하게 파일명을 지울수있다

           current_time=datetime.now()
           current_time=current_time.isoformat().replace(':','_')
           file.name=current_time+'jpg'

           #바꾼파일명으로 파일을 서버에 저장한다
           save_uploaded_file('tmp',file)

           # csv파일은 판다스로 읽어서 화면에 보여준다
           df=pd.read_csv(file)
           st.dataframe(df)

           #파일을 웹 화면에 나오게  
           img=Image.open(file)
           st.image(img)












        

        




if __name__=='__main__':
    main()