import streamlit as st
import requests

st.markdown('<h1 style="text-align:center;color:white;font-weight:bolder;font-size:100px;background: -webkit-linear-gradient(#e20b0b,#ec720e,#46a3e0,#093ff0); -webkit-background-clip: text;-webkit-text-fill-color: transparent;">Semantic Search Engine</h1>',unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;color:white;">A search Engine that searches with meaning</h2>',unsafe_allow_html=True)

API_URL = st.sidebar.text_input("Enter API URL")

print(API_URL)

query = st.text_area("Enter Query..")

if st.button ('Search'):
    if API_URL == "":
        st.write("[ERROR] Please specify API URL in sidebar")
        pass
	
    else:
		# get translated text from api

        returned_docs = requests.get(API_URL+"/search?query="+query)


        if returned_docs.status_code == 200:
            temp_docs = returned_docs.text.split('\n')
            for docs in temp_docs:
                st.write(docs)
                st.markdown('<br>',unsafe_allow_html=True)

		
        elif returned_docs.status_code == 404:
		
        	st.write("\n### Link not found, please specify correct APL link")

link = '[DOCS!](http://github.com)'
st.markdown(link, unsafe_allow_html=True)
