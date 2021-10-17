
import spacy
import spacy_streamlit
import streamlit as st
import wikipedia
ner=spacy.load("en_core_web_sm")


def scrapping(input1):
  result = wikipedia.search(input1)
  print(result)
  page = wikipedia.page(result[1])
  content = page.content
  print(content)
  return content



st.title('NER Recognizer\n', )
st.subheader("JALLURI PAVAN NAGA VENKATA KOUSHIK")

option = st.sidebar.selectbox('Navigation', ["Home", "Named Entity Recognition"])

if option == 'Home':
	st.write(
			"""
				## Project Description
				This is a NER tool developed by Koushik.
			"""
		)
elif option == "Named Entity Recognition":

	st.header("Enter the keyword for wikiidea that you want to analyze")
	st.markdown("**Random Sentence:** Tesla car")
	input1=st.text_area("enter keyword")
	content = scrapping(input1)

	#ner = en_core_web_sm.load()
	doc = ner(str(content))

	# Display 
	spacy_streamlit.visualize_ner(doc, labels=ner.get_pipe('ner').labels)
  # Bar graph

