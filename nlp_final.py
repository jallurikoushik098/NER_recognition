#importing all modules
import spacy
import spacy_streamlit
import streamlit as st
import wikipedia
import warnings
ner=spacy.load("en_core_web_sm")

warnings.filterwarnings(action='ignore')
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

# Scrapping the data using Wikipedia API
def scrapping(input1):
	try:
		result = wikipedia.search(input1,results=5)
                #print(result)
                page = wikipedia.page(result[1])
                content = page.content
                #print(content)
                return content
	except:
		pass
		
  '''result = wikipedia.search(input1,results=5)
  #print(result)
  page = wikipedia.page(result[1])
  content = page.content
  #print(content)
  return content'''



#Designing the APP
st.title('NER Recognizer\n', )
st.subheader("JALLURI PAVAN NAGA VENKATA KOUSHIK")

option = st.sidebar.selectbox('Navigation', ["Home", "Named Entity Recognition"])

if option == 'Home':
	st.write(
			"""
				## Project Description
				This is a NER tool developed by Koushik.Pls check out the navigition tab in left corner for the NER application and type the key word and press ctrl+enter. Pls ignore the warning and use the app.
			"""
		)
elif option == "Named Entity Recognition":

	st.header("Enter the keyword for wikiidea that you want to analyze")
	st.markdown("**Random idea:** Tesla car")
	#input1=st.text_area("enter keyword")
	input1=st.text_input("enter keyword")
	
	content = scrapping(input1)
	#applying spacy model for NER recognition
	doc = ner(str(content))

	# Display 
	spacy_streamlit.visualize_ner(doc, labels=ner.get_pipe('ner').labels)

