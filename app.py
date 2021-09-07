import streamlit as st
import pandas as pd
import lasio

st.title("Aplicación de Registros de Pozos")
st.sidebar.title('Menú')
opciones_inicio=st.sidebar.radio("Selecione una opción",["Inicio","Datos","Cálculos"])

#archivo_las=lasio.read("Archivo_Las\LGAE-040.las")
archivo_las=lasio.read("LGAE-040.las")
df=archivo_las.df()


if opciones_inicio=="Inicio":
	st.write("Ingreso al Inicio")
	st.write(df)
if opciones_inicio=="Datos":
	st.write("Ingreso a Datos")
	barra_deslizadora=st.slider("Selecione un valor",1,100,30)
	st.write("Valor Seleccionado es:",barra_deslizadora)
	ingreso_numero=st.number_input("Ingrese un valor:", min_value=1.00, max_value=1000.00, value=300.00)
if opciones_inicio=="Cálculos":
	st.write("Ingreso a Cálculos")
	seleccion=st.selectbox("Seleccione una opción:",[1,2,3,"A"])
	check1=st.checkbox("Activar")
	if check1==True:
		st.write("Check Activo")
archivo_subido=st.sidebar.file_uploader("Cargar Archivo Excel", type=[".xls",".xlsx"])

if archivo_subido is not None:
	df2=pd.read_excel(archivo_subido)
	st.write(df2)
