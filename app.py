import pandas as pd
import plotly.express as px
import streamlit as st
# titulo sobre que realiza este api
st.header("Análisis de vehículos usados")
# descripcion de que realiza esta Api
st.write("""
Esta aplicación permite visualizar datos de vehículos usados a partir de un conjunto de datos cargado.  
Puedes explorar el contenido del dataset y, si lo deseas, generar visualizaciones interactivas como:
- 📊 Un histograma del kilometraje (`odometer`) de los vehículos.
- 📈 Un gráfico de dispersión que relaciona el precio (`price`) con el kilometraje (`odometer`).
         
Estas herramientas ayudan a entender mejor la distribución de los datos y detectar patrones de interés.
""")
# se cargan los datos
ruta = "vehicles_us.csv"
car_data = pd.read_csv(ruta)
# se realiza una carga y visualizacion del dataset utilizado para mayor confiabilidad
st.subheader("Vista previa del dataset")
st.dataframe(car_data)
# se solicita al usuario que seleccion lo que necesite
st.write('Por favor selecciona el grafico que necesitas')

# Checkbox para gráfico de histograma
build_histogram = st.checkbox('Construir un histograma')
# si la casilla de verificación está seleccionada
if build_histogram:
    st.write('Se construye gráfico de histograma')
    fig = px.histogram(car_data, x="odometer",
                       title='histograma para la columna odómetro')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')
# si la casilla de verificación está seleccionada
if build_scatter:
    st.write('Se construye gráfico de dispersión entre precio y kilometraje')
    fig2 = px.scatter(car_data, x="odometer", y="price",
                      title="Precio vs. Kilometraje")
    st.plotly_chart(fig2, use_container_width=True)
