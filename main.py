import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('Interactive Widgets')

st.write('プログレスバーの表示')
'Start!!'
latest_iteration=st.empty()
bar = st.progress(0)


for i in range(100):
  latest_iteration.text(f'iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.01)


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに画像を表示')
if button:
  right_column.write('右カラムです')
# if st.checkbox('写真を表示'):
  img = Image.open('ajisai.jpeg')
  right_column.image(img, caption='紫陽花', use_column_width=True)
  
expander = st.expander('問い合わせ1')
expander.write('問い合わせ１回答')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ２回答')

  


# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味:',text 
  
# condition = st.sidebar.slider('あなたの今の調子は？', 0,100,50)

# 'コンディション：', condition

