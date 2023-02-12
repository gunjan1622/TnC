import os
import json
import numpy as np
import pandas as pd
import streamlit as st

from SummaryAPI.utils import DBConnection
from SummaryAPI.services.abstract import abstractive_summarization 
from SummaryAPI.services.extractive import extractive_summarization

st.set_page_config(
    page_title="The Fine Art of Summarization",
    page_icon="📝",
)
def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


_max_width_()

c30, c31, c32 = st.columns([2.5, 1, 3])

with c30:
    # st.image("logo.png", width=400)
    st.title("🔑 Summarization")
    st.header("")



with st.expander("ℹ️ - About this app", expanded=True):

    st.write(
        """     
-   The *BERT Keyword Extractor* app is an easy-to-use interface built in Streamlit for the amazing [KeyBERT](https://github.com/MaartenGr/KeyBERT) library from Maarten Grootendorst!
-   It uses a minimal keyword extraction technique that leverages multiple NLP embeddings and relies on [Transformers] (https://huggingface.co/transformers/) 🤗 to create keywords/keyphrases that are most similar to a document.
	    """
    )

    st.markdown("")

st.markdown("")
st.markdown("## **📌 Paste document **")
with st.form(key="my_form"):


    ce, c1, ce, c2, c3 = st.columns([0.07, 1, 0.07, 5, 0.07])
    with c1:
        ModelType = st.radio(
            "Choose your model",
            ["Abstractive Summary", "Extractive Summary"],
            help="At present, you can choose extractive summarization method. More to come!",
        )
        
        top_N = st.slider(
            "# of results",
            min_value=1,
            max_value=30,
            value=10,
            help="You can choose the number of keywords/keyphrases to display. Between 1 and 30, default number is 10.",
        )

        if ModelType == "Default (Extractive))":
            # kw_model = KeyBERT(model=roberta)

            @st.cache(allow_output_mutation=True)
            def load_model():
                return extractive_summarization(client,input_text, max_sentence_count) 
            kw_model = load_model()

        else:
            @st.cache(allow_output_mutation=True)
            def load_model():
                return KeyBERT("distilbert-base-nli-mean-tokens")

            kw_model = load_model()

        