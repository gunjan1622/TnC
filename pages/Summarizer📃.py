import pandas as pd
import streamlit as st

from SummaryAPI.services.Summarization import Summarization
#from SummaryAPI.utils.rating import insert_rating, get_stats

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

st.sidebar.subheader("Made with ❤️ by [Gunjan Agrawal](https://github.com/gunjan1622)")

ratings = []
# def star_rating(label, key):
#     rating = st.slider(label, 0, 10, key=key, step=1)
#     return rating

# with st.sidebar.form(key='ratings'):
#     rating = star_rating('Rate this app:', 'rating')
#     ratings.append(rating)
#     insert_rating(rating)
#     num_responses, avg_rating = get_stats()    
#     submit_btn=st.form_submit_button(label='Rate')

#     if submit_btn:
#         st.sidebar.success("Thanks for your feedback!")
#         st.sidebar.write(f'Number of responses: {num_responses}')
#         st.sidebar.write(f'Average rating: {avg_rating:.2f}')

c30, c31, c32 = st.columns([50, 1, 3])

with c30:
    # st.image("logo.png", width=400)
    st.title("🧾 Terms and Conditions Summarization")
    st.header("")



with st.expander("ℹ️ - About this app", expanded=True):

    st.write(
        """  
- This app is a demo of the *Azure Text Analytics API*. This library contains the following features: Sentiment Analysis, Key Phrase Extraction, Named Entity Recognition, Language Detection, and Text Analytics. We are using the **Summarization** feature of the API.           
- **Extractive summarization:** Produces a summary by extracting sentences that collectively represent the most important or relevant information within the original content.
- **Abstractive summarization:** Produces a summary by generating summarized sentences from the document that capture the main idea.
- The app is built using the [Azure Cognitive Service for Language API](https://learn.microsoft.com/en-in/azure/cognitive-services/language-service/) and [Streamlit](https://streamlit.io/).
	    """
    )

    st.markdown("")

st.markdown("")
st.markdown("## 📌 Paste document ")

with st.form(key="my_form"):

    ce, c1, ce, c2, c3 = st.columns([0.07, 1, 0.07, 5, 0.07])
    with c1:
        ModelType = st.radio(
            "Choose your model",
            ["Extractive Summary", "Abstractive Summary"],
            help="At present, only extractive summarization method works. More to come as Microsoft will include more APIs!",
        )

        if ModelType == "Extractive Summary":

            @st.cache_data()
            def load_model():
                return Summarization(model="Extractive")
            summary_model = load_model()

        else:
            @st.cache_data()
            def load_model():
                return Summarization(model="Abstractive")
            summary_model = load_model()
            

        max_sentence_count = st.slider(
            "Maximum sentence count",
            min_value=1,
            max_value=20,
            value=2,
            help="You can choose the maximum sentence count to be generated in the summary.",
        )    

    with c2:
        doc = st.text_area(
            "Paste your text below",
            height=350,
        )

        submit_button = st.form_submit_button(label="✨ Generate Summary!")

if not submit_button:
    st.stop()    

with st.spinner("🔮 Generating summary..."):
    summary=summary_model.summarize(doc,max_sentence_count=max_sentence_count)  
    st.markdown("## 📝 Summary")
    st.success(summary)
    st.balloons()