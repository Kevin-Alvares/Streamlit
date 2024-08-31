import streamlit as st

st.write("Hello, *World!* :sunglasses:")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

st.subheader("These subheaders have rotating dividers", divider=True)