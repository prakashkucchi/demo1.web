import streamlit as st


st.title("welcome to melebaby moni:", )
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0)
fname = st.text_input("Enter your father name:")
Adress = st.text_area("Enter your adress:")
classdata = st.selectbox("enter your class:", (1,2,3,4,5,6,7,8,9))

button = st.button("done")
if button:
    st.markdown(f"""
name:{name}
father:{fname}
address:{Adress}
classs:{classdata}""")



