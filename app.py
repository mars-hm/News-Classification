import streamlit as st
import joblib

model=joblib.load("news-classification-model.pkl")

news_labels={"0": "Technical", "1": "Business", "2" : "Sports", "3" : "Entertainment", "4" : "Politics"}

st.title("News Classification")

user_input= st.text_area("Enter the News:")


if st.button("Predict"):
    print(user_input)
    predicted_label=model.predict([user_input])[0]
    print("Predicted Label:" + str(predicted_label))
    predicted_news_label=news_labels[str(predicted_label)]

    st.info(f"Predicted News Category: {predicted_news_label}")
