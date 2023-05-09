import streamlit as st

# Set page title
st.set_page_config(
    page_title="TermsBrief",
)

st.sidebar.image("assets/logo.png")

# Custom CSS styles
st.markdown(
    """
    <style>
    body {
        background-color: #1F1F1F;
    }
    .header {
        font-size: 48px;
        font-weight: bold;
        color: #FF8800;
        margin-bottom: 20px;
        text-align: center;
    }
    .subheader {
        font-size: 32px;
        color: #FFFFFF;
        margin-bottom: 10px;
        text-align: center;
    }
    .text {
        font-size: 24px;
        color: #DDDDDD;
        margin-bottom: 20px;
        text-align: center;
    }
    .gif {
        border-radius: 5px;
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
    }
    .emoji {
        width: 100px;
        margin-bottom: 20px;
        text-align: center;
    }
    .summary {
        font-size: 24px;
        color: #FFFFFF;
        background-color: #FF8800;
        border-radius: 5px;
        padding: 10px 20px;
        margin-top: 30px;
        text-align: center;
    }
    .infographic {
        margin-top: 30px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar content
st.sidebar.subheader("Made with ❤ by [Gunjan Agrawal](https://github.com/gunjan1622) and [Hemanth Sai](https.github.com/HemanthSai7)")

# Main content
st.markdown('<h1 class="header">Termsbrief</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subheader">Tired of reading those endless <strong>terms and conditions</strong> before agreeing to them?</h2>', unsafe_allow_html=True)

# Image and text columns
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown('<p class="text">Agreeing to <strong>terms and conditions</strong> with your eyes closed?</p>', unsafe_allow_html=True)
with col2:
    st.image('https://media.tenor.com/TatG54muuNYAAAAi/eyes-looking.gif', width=300, caption='Image source: Tenor')

st.markdown('<p class="text">Without thinking how someone can be stealing your personal information.</p>', unsafe_allow_html=True)

# Image column
mid_column, _ = st.columns([2, 1])
with mid_column:
    st.image('https://media.tenor.com/ZWHGB0dc7koAAAAi/theumbrellaacademy-theumbrellaacademyhazelandchacha.gif', width=400, caption='Image source: Tenor')

# Image and text columns
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.image('https://media.tenor.com/6ceOmdT7SHkAAAAi/emoji-emojis.gif', width=100, caption='Image source: Tenor')
with col2:
    st.markdown('<h2 class="subheader" style="text-align: center">Termsbrief is the perfect tool for making quick, simple summaries of important legal documents.</h2>', unsafe_allow_html=True)
with col3:
    st.image('https://media.tenor.com/6ceOmdT7SHkAAAAi/emoji-emojis.gif', width=100, caption='Image source: Tenor')