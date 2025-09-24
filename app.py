import streamlit as st
from deep_translator import GoogleTranslator

st.markdown("""
    <style>
        body {
            background-color: #f0f8ff; /* Azul claro */
            color: #333333;
        }

        .stTextArea textarea {
            background-color: #ffffff;
            color: #000000;
        }

        .stButton > button {
            background-color: #007acc;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 1em;
            transition: background-color 0.3s;
        }

        .stButton > button:hover {
            background-color: #005f99;
        }

        .stMultiSelect div {
            background-color: #ffffff;
        }

        .title {
            text-align: center;
            font-size: 3em;
            color: #007acc;
            font-weight: bold;
        }

        hr {
            border-top: 1px solid #cccccc;
        }
    </style>
""", unsafe_allow_html=True)

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






