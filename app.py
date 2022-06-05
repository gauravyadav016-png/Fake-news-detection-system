import streamlit as st
import joblib
st.title('Fake News Detection System')
ip=st.text_input("Enter the Text :")
ip=[ip]
ip=tfidf_vectorizer.transform(ip)
op=text_model.predict(aaa)
if st.button('Predict'):
    st.title("This News is:")
    st.title(op[0])
