import streamlit as st
import spacy
from spacy import displacy
import en_core_web_sm
nlp = en_core_web_sm.load()
# from pprint import pprint
from newspaper import Article

st.title("NAMED ENTITY RECOGNIZER")
text = st.text_area("Enter your paragraph here:")
st.markdown("### OR")
url=st.text_input("Enter your URL here:")
button=st.button("SUBMIT")
   
def textfunc(text):
    doc = nlp(text)
    ent_html = displacy.render(doc, style="ent", jupyter=False)
    st.markdown(ent_html, unsafe_allow_html=True)

def urlfunc(url):
    article = Article(url)
    article.download()
    article.parse()
    doc = nlp(article.text)
    ent_html=displacy.render(doc, style="ent", jupyter=False)
    st.markdown(ent_html,unsafe_allow_html=True)

if button:
    if text and url:
        st.warning("Please enter any one input only.")
    elif url:
        urlfunc(url)
        st.text("    ")
        st.success("Successfully analyzed the article!") 
    elif text:
        textfunc(text)
        st.text("   ")
        st.success("Successfully analyzed the article!") 
    else:
        st.warning("Please enter an input.")
