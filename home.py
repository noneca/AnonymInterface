import streamlit as st
import streamlit.components.v1 as com
import pandas as pd
from makeTemplates import newTemplate, dictAccess,newTemplate2

df = pd.read_csv("finalWithPeople.csv")

com.html("<div><h1> this is my interface </h1>")

templs = dictAccess()
templateTmp = st.multiselect("Choose template", templs)
if templateTmp:
    st.write(templs[templateTmp[0]])
    st.write(df[templs[templateTmp[0]]])
    st.session_state.template=df[templs[templateTmp[0]]]



st.write("Make a new template")
attributes = pd.read_csv('finalWithPeople.csv')
chooseAtr = st.multiselect("choose columns", attributes.columns.values.tolist())
tmplName = st.text_input("template name")
if st.button("Submit your template"):
    newTemplate2(tmplName, chooseAtr)

##st.write(df)
