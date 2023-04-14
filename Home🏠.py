import streamlit as st


st.set_page_config(
    page_title="TermsBrief",
)
st.sidebar.subheader("Made with ❤️ by [Gunjan Agrawal](https://github.com/gunjan1622) and [Hemanth Sai](https.github.com/HemanthSai7)")
#st.sidebar.markdown("### *Summarizer, a project of my bestie Gunjuuuuu*")
st.header('TERMSBRIEF')
st.markdown('Tired of reading those endless **:orange[terms and conditions]** before agreeing to them?')
#st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")
col1, col2 = st.columns([1.5, 1])
with col1:
    st.markdown('Agreeing to **:green[terms and conditions]** with your eyes closed?')
with col2:
    st.image('https://media.tenor.com/TatG54muuNYAAAAi/eyes-looking.gif', width=47)

st.markdown('Without thinking how someone can be stealing your personal information.')

_left, mid, _right = st.columns([0.3, 1, 0.1])
with mid:
    st.image('https://media.tenor.com/ZWHGB0dc7koAAAAi/theumbrellaacademy-theumbrellaacademyhazelandchacha.gif', width=170)

col1, col2, col3= st.columns([0.5, 1.5, 0.5])
with col1:
    st.image('https://media.tenor.com/6ceOmdT7SHkAAAAi/emoji-emojis.gif', width=47)
with col2:
    st.markdown('**:orange[Termsbreif  is the perfect tool for making quick, simple summaries of important legal documents.]**')
with col3:
    st.image('https://media.tenor.com/6ceOmdT7SHkAAAAi/emoji-emojis.gif', width=47)

st.markdown('**:white[Simply  paste your text in the given area and choose the summary option u want,  to create your own summary in seconds. And Voila, u protected urself from someone else governing your personal information.]**')

