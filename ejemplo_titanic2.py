import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("database_titanic.csv")

st.write("""
# Mi primera aplicación interactiva
## Gráficos usando la base de datos del Titanic
""")

with st.sidebar:
    st.write("# Opciones")
    
    div = st.slider('Número de bins:', 1, 10, 2)
    
    st.write("Bins=", div)

fig, ax = plt.subplots(1, 3, figsize=(15, 4))

ax[0].hist(df["Age"].dropna(), bins=div, color='skyblue')
ax[0].set_xlabel("Edad")
ax[0].set_ylabel("Frecuencia")
ax[0].set_title("Histograma de edades")

df_male = df[df["Sex"] == "male"]
cant_male = len(df_male)
df_female = df[df["Sex"] == "female"]
cant_female = len(df_female)

ax[1].bar(["Masculino", "Femenino"], [cant_male, cant_female], color=['darkblue', 'pink'])
ax[1].set_xlabel("Sexo")
ax[1].set_ylabel("Cantidad Total")
ax[1].set_title("Conteo por Sexo")

df_survivors = df[df['Survived'] == 1]
survivors_by_sex = df_survivors.groupby('Sex')['Survived'].count()

surv_male = survivors_by_sex.get('male', 0)
surv_female = survivors_by_sex.get('female', 0)

ax[2].bar(["Masculino", "Femenino"], [surv_male, surv_female], color=['blue', 'red'])
ax[2].set_xlabel("Sexo")
ax[2].set_ylabel("Cantidad de Sobrevivientes")
ax[2].set_title("Sobrevivientes por Sexo")

st.pyplot(fig)

st.write("## Vista de los Datos")
st.table(df)