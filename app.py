import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
    temperature=0.3
)

st.title("Essay Abridger")

essay = st.text_area("Paste your essay here")

if st.button("Generate Abridgement"):

    prompt = ChatPromptTemplate.from_template(
        """
        Convert the following essay into a concise abridgement.

        Essay:
        {essay}

        Abridgement:
        """
    )

    chain = prompt | llm

    result = chain.invoke({
        "essay": essay
    })

    st.subheader("Abridgement")
    st.write(result.content)