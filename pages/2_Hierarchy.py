import streamlit as st
import pandas as pd
from pyarxaasBack import setReductHierarch, setIntervHierarch

attributes = pd.read_csv('finalWithPeople.csv')

st.write("Hierarchies")
chooseAtr3 = st.multiselect("choose attribute to generalize", attributes.columns.values.tolist())
if chooseAtr3:
    hierarchyType = st.selectbox("choose hierarchy", ("","Reduction", "Intervals", "Order"))
    if hierarchyType == "Reduction" :
        st.write(chooseAtr3[0])
        st.write(setReductHierarch(chooseAtr3[0]))

    if hierarchyType == "Intervals":
        intervalsText=st.text_area("Type your intervals (min, max, category name)")
        newlist=[]
        line = intervalsText.splitlines()
        for i in line:
            newlist.append(i.split(","))
        st.write(chooseAtr3[0])
        if intervalsText:
            setIntervHierarch(chooseAtr3[0],newlist)
            

    if hierarchyType == "Order":
        st.write("pending...")