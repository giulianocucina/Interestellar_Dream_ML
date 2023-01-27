from os import path
import streamlit as st
import pandas as pd
st.title("Bienvenidos al Hyperespacio")
st.sidebar.write("Lista de Pasajeros")


#Read the CSV file into a dataframe
df = pd.read_csv(r"C:\Users\gcuci\Desktop\Interestellar Project\data\test.csv")

#Select the column you want to display
column_name = 'Name'
st.sidebar.dataframe(df[column_name],width=400)
numero_pasajero = st.sidebar.number_input("Escoje el numero de pasajero",min_value=1,max_value=4276,step=1)

#Select the index number of the row you want to display
index_number = numero_pasajero

selected_row = df.iloc[index_number]

#Iterate over the columns in the selected row
for column, value in selected_row.iteritems():
   if column != df.columns[-1]:
        st.write(f"{column} : {value}")

transporte = pd.read_csv(r"C:\Users\gcuci\Desktop\Interestellar Project\data\resultados.csv")
prediccion = st.button("Predecir")
if prediccion:
    if transporte['Transported'][index_number]:
      st.write(f" el pasajero SI logro llegar al destino")
    else:
       st.write(f" el pasajero NO logro llegar al destino")

