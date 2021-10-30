import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
import time

st.title("Streamlit 超入門")

st.write("プログレスバーの表示")
"Start!!"
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.05)
"Done!"
    
#st.write("DataFrame")
#df = pd.DataFrame({
#    "1列目": [1, 2, 3, 4],
#    "2列目": [10, 20, 30, 40]
#})

# Draw Table
#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0), width=250, height=400)
#st.table(df) # static (unsortable)

# Draw chart
#df = pd.DataFrame(
#    np.random.rand(20, 3),
#    columns=["a", "b", "c"]
#)

#st.write("Line chart")
#st.line_chart(df)

#st.write("Area chart")
#st.area_chart(df)

#st.write("Bar chart")
#st.bar_chart(df)

#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=["lat", "lon"]
#)
#st.map(df)

# Interactive widget
# Check box

#if st.checkbox("Show Image"):
#    st.write("Display Image")
#    img = Image.open("koenigsegg_one.jpg")
#    st.image(img, caption="Koenigsegg One", use_column_width=True)

# Select box
#option = st.selectbox(
#    "あなたが好きな数字を教えてください",
#    [i for i in range(1, 10+1)]
#)

#"あなたの好きな数字は, " , option, "です。"

#st.sidebar.write("Interactive widgets")
#st.write("Interactive widgets")

# Text box
#text = st.sidebar.text_input("あなたの趣味を教えてください。")
#text = st.text_input("あなたの趣味を教えてください。")
#"あなたの趣味: " , text

# Slider
#condition = st.slider("あなたの今の調子は？", 0, 100, 50)
#condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
# min, max, init
#"コンディション: ", condition

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ほげぇ、ボタン押された〜")
        
expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")
