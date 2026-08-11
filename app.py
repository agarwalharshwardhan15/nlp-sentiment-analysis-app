import streamlit as st
from sentiment_model import analyze_sentiment

st.title("NLP Sentiment Analysis App")
st.write("Enter any text below to check its sentiment.")

user_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        sentiment, score = analyze_sentiment(user_input)
        st.subheader(f"Sentiment: {sentiment}")
        st.write(f"Polarity Score: {score:.2f}")