# proyecto_7
#Análisis de Vehículos Usados con Streamlit
solución de proyecto sprint 7

Esta es una aplicación web interactiva desarrollada en Python utilizando la biblioteca Streamlit. Su propósito es facilitar la visualización y exploración de un conjunto de datos que contiene información sobre vehículos usados.
La aplicación permite a los usuarios visualizar el contenido del dataset y generar gráficos interactivos de forma sencilla, sin necesidad de conocimientos técnicos avanzados. Está pensada como una herramienta de apoyo para estudiantes, analistas o cualquier persona interesada en el análisis de datos del mercado automotor.

Funcionalidades de la aplicación

Muestra el dataset completo cargado desde un archivo CSV.
Permite generar un histograma de la columna "odometer", que representa el kilometraje de los vehículos.
Permite generar un gráfico de dispersión entre las columnas "odometer" (kilometraje) y "price" (precio).
Utiliza gráficos dinámicos construidos con la biblioteca Plotly.
La interfaz es completamente interactiva: los gráficos se generan solo si el usuario activa las opciones correspondientes mediante casillas de verificación.

Cómo ejecutar la aplicación

Asegúrate de tener Python instalado en tu sistema.
Instala las dependencias necesarias ejecutando el siguiente comando en la terminal:
pip install streamlit pandas plotly
Ejecuta el archivo principal de la aplicación con el siguiente comando:
streamlit run app.py
Se abrirá automáticamente una ventana en el navegador con la aplicación en funcionamiento. Si no se abre automáticamente, puedes acceder manualmente a la URL local que te muestra la terminal (generalmente http://localhost:8501).