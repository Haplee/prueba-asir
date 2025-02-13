import streamlit as st

st.title("🎈 Mi app")
st.write("Vamos a empezar con estoo.")

st.write("Practicando mi nueva app")

st.header("Esto es una cabezera")

cantidad=st.slider("Elija un valor")

print(f' el identificador de cantidad es {id(cantidad)}')


for i in range(cantidad):
    st.button(f'Botón{i}')
    st.checkbox (f'Opcion{i}')