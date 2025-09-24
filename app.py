import streamlit as st
from deep_translator import GoogleTranslator

<style>
background-color:pink,
</style>

st.title("Tradutor com Deep Translator")

#Área de textos
texto = st.text_area(" Digite sua frase em português:", 
                     "Olá! Estou aprendendo a programar em Python e a usar modelos de inteligência artificial.")

# Seleção de idiomas
linguas = {
    "Inglês": "en",
    "Espanhol": "es",
    "Francês": "fr",
    "Alemão": "de",
    "Italiano": "it"
}

idiomas_escolhidos = st.multiselect("Selecione os idiomas de destino:", list(linguas.keys()), ["Inglês", "Espanhol"])

#traduzir
if st.button("Traduzir"):
    if texto.strip() == "":
        st.warning("Digite uma frase para traduzir!")
    else:
        for nome in idiomas_escolhidos:
            codigo = linguas[nome]
            traducao = GoogleTranslator(source='pt', target=codigo).translate(texto)
            st.subheader(f'➡ Tradução para {nome} ({codigo})')
            st.write(f'**Original:** {texto}')
            st.write(f'**Traduzido:** {traducao}')
            st.write("---")




