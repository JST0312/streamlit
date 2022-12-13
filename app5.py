import streamlit as st

# 이미지 처리를 위한 라이브러리
from PIL import Image

def main():
   img= Image.open('streamlit_data/image_03.jpg')


   st.image(img)
   st.image(img,use_column_width=True)    
   Image_url = 'https://post-phinf.pstatic.net/MjAyMjExMjlfMTY1/MDAxNjY5NzEzNDU0NDIy.OuVd29TSw5pJX--ET-e1_8ElG9Xo03NrF73x1jWndHQg.hTGreMHlMoyXZECqUHklsJFok5DKoeFQM4gRjfEsnUwg.JPEG/6e130cd6316eb17a7f5c10e4e5d83746.jpg?type=w1200'

  
   st.image(Image_url)



video_file=open('streamlit_data/secret_of_success.mp4','rb')

st.video(video_file)






if __name__ == '__main__':
    main()