#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:20:48 2024

@author: deeptarkaroy
"""
import pandas as pd
import streamlit as st
import pickle 
from streamlit_option_menu import option_menu

model =pd.read_pickle(open("abcd","rb"))

model_circular=pickle.load(open("efgh","rb"))


with st.sidebar:
     
    selected=option_menu("Axial Capacity Prediction of CFSST Columns",
                         ["Rectangular CFSST Columns",
                          "Circular CFSST Columns"],default_index=0)
    
    
if (selected=="Rectangular CFSST Columns"):
    #model =pd.read_pickle(open("abcd","rb"))
    
    st.title("**GUI for Rectangular CFSST Columns** ")
    st.subheader("Input Parameters")
    
    def user_input_features():
       Grade_SS=st.number_input("  Grade_SS",1,23,3) 
       B=st.number_input("  B (mm)",40,250,124)
       H=st.number_input("H (mm)",49,250,120)
       t=st.number_input("  t (mm)",1,12,3)
       L=st.number_input("  L (mm)",150,850,377)
       LB=st.number_input(" L/B",1.5,7.46,3.15)
       Eo=st.number_input(" Eo (MPa)",18000,217000,199730)
       f=st.number_input("  f_0.2 (MPa)",258,598,433)
       fu=st.number_input(" fu (MPa)",409,961,674)
       n=st.number_input("  n",3.0,12.4,5.97)
       fc_cyl=st.number_input("f c_cyl (MPa)",21.5,114.6,48.14)
       data={"Grade_SS":Grade_SS,"B (mm)":B,"H (mm)":H,"t (mm)":t,"L (mm)":L,"L/B":LB,"Eo (MPa)":Eo,"f_0.2 (MPa)":f,"fu (MPa)":fu,"n":n,"fc_cyl (MPa)":fc_cyl}
       features =pd.DataFrame(data,index=[0])
       return features
   
    data_df=user_input_features()
    

    prediction=model.predict(data_df)

    
    #Grade_SS=st.text_input("Grade_SS"), 
    #B=st.text_input("B (mm)"),
    #H=st.text_input("H (mm)"),
    #t=st.text_input("t (mm)"),
    #L=st.text_input("  L (mm)"),
    #LB=st.text_input(" L/B"),
    #Eo=st.text_input(" Eo (MPa)"),
    #f=st.text_input("  f_0.2 (MPa)")
    #fu=st.text_input(" fu (MPa)")
    #n=st.text_input("  n")
    #fc_cyl=st.text_input("f c_cyl (MPa)")   
    
    
    st.subheader("Axial Capacity of CFSST Column (kN)")
    st.write("%.2f" % prediction)
   

#if (selected=="Circular CFSST Columns"):
else:
    st.title("**GUI for Circular CFSST Columns** "
           )
    #model_circular=pickle.load(open("efgh","rb"))
    
    
    st.subheader("Input Parameters")
    
    def user_features():
     Grade_SS=st.number_input("Grade_SS",1,6,3)
     D=st.number_input("D (mm)",50.0,324.1,100.02)
     t=st.number_input("t (mm)",1,11,7)
     L=st.number_input("  L (mm)",150,975,600)
     LD=st.number_input(" L/D",2,4,3)
     Eo=st.number_input(" Eo (MPa)",173900,203500,180000)
     f=st.number_input("  f_0.2 (MPa)",259,789,300)
     fu=st.number_input(" fu (MPa)",400,750,450)
     n=st.number_input("  n",3,9,5)
     fc_cyl=st.number_input("fc_cyl (MPa)",20,120,50)   
     Data={"Grade_SS":Grade_SS," D (mm) ":D,"t (mm)":t,"L (mm)":L,"L/D":LD,"Eo (MPa)":Eo,"f_0.2 (MPa)":f,"fu (MPa)":fu,"n":n,"fc_cyl (MPa)":fc_cyl}
     feature=pd.DataFrame(Data,index=[0])
     return feature
    
    pred=user_features()
    

    pred_new=model_circular.predict(pred)
    st.subheader("Axial Capacity of CFSST Column (kN)")
    st.write("%.2f" % pred_new)