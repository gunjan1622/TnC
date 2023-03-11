import streamlit as st

from SummaryAPI.services.Summarization import Summarization

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
            ["Extractive Summary", "Abstractive Summary"],
            help="At present, you can choose extractive summarization method. More to come!",
        )

        if ModelType == "Extractive Summary":

            @st.cache(allow_output_mutation=True)
            def load_model():
                return Summarization(model="Extractive")
            summary_model = load_model()

        else:
            @st.cache(allow_output_mutation=True)
            def load_model():
                return Summarization(model="Abstractive")
            summary_model = load_model()
            

        max_sentence_count = st.slider(
            "# of results",
            min_value=1,
            max_value=30,
            value=2,
            help="You can choose the maximum sentence count for the summary.",
        )    

    with c2:
        doc = st.text_area(
            "Paste your text below (max 500 words)",
            height=510,
        )

        MAX_WORDS = 500
        import re
        res = len(re.findall(r"\w+", doc))
        if res > MAX_WORDS:
            st.warning(
                "⚠️ Your text contains "
                + str(res)
                + " words."
                + " Only the first 500 words will be reviewed. Stay tuned as increased allowance is coming! 😊"
            )

            doc = doc[:MAX_WORDS]

        submit_button = st.form_submit_button(label="✨ Get me the data!")

if not submit_button:
    st.stop()    

summary=summary_model.summarize(doc,max_sentence_count=max_sentence_count)              


        