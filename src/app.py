import streamlit as st

st.image("img/neurona.png", width = 400)

st.header("¡Hola neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
   st.header("Una neurona con una entrada y un peso")
   w = st.slider('Peso', 0.0, 5.0, key = 0)
   x = st.number_input('Introduzca el valor de la entrada', key = 1)
   if st.button('Calcular salida', key = 2):
      y = w * x
      st.write('La salida de la neurona es ', y)

with tab2:
   col1, col2 = st.columns(2)

   with col1:
      w0 = st.slider('Peso w₀', 0.0, 5.0, key = 3)
      x0 = st.number_input('Entrada x₀', key = 4)

   with col2:
      w1 = st.slider('Peso w₁', 0.0, 5.0, key = 6)
      x1 = st.number_input('Entrada x₁', key = 7)
   
   if st.button('Calcular salida', key = 5):
         y = (x0 *w0) + (x1 * w1)
         st.write('La salida de la neurona es ', y)
      

with tab3:
   col1, col2, col3 = st.columns(3)

   with col1:
      w0 = st.slider('Peso w₀', 0.0, 5.0, key = 8)
      x0 = st.number_input('Entrada x₀', key = 9)

   with col2:
      w1 = st.slider('Peso w₁', 0.0, 5.0, key = 10)
      x1 = st.number_input('Entrada x₁', key = 11)

   with col3:
      w2 = st.slider('Peso w₂', 0.0, 5.0, key = 12)
      x2 = st.number_input('Entrada x₂', key = 13)

   b = st.number_input('Introduzca el valor del sesgo', key = 14)
   if st.button('Calcular salida', key = 15):
         y = (x0 * w0) + (x1 * w1) + (x2 * w2) + b
         st.write('La salida de la neurona es ', y)
   

