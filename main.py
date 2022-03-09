import streamlit as st
# from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()

bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.01)

# img = Image.open('angela.jpeg')
# st.image(img, caption="Angela")

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('クリックしましたね！')

expander1 = st.expander('あなたは誰？')
expander1.write('Angela')
expander2 = st.expander('どういう人？')
expander2.write('インストラクター')
expander3 = st.expander('年齢')
expander3.write('？')


# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
#
# 'あなたの趣味は、', text
# 'コンディション', condition
