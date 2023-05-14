import streamlit as st
from trubrics.integrations.streamlit import FeedbackCollector

from SummaryAPI.utils.DBQueries import DBQueries

st.title("Termbrief Feedback 🌟")
st.markdown("Feedback is a gift. Please help us improve Termbrief by sharing your thoughts. 🤗")

collector=FeedbackCollector()
with st.form("feedback"):
    q1=st.slider("How much do you love this app?",max_value=10,value=0)
    q2=st.text_input("What do you like about the app?")
    q3=st.text_input("How can we improve the app?")
    q4=st.text_input("Raise a specific issue")
    submit_button=st.form_submit_button("Submit")
    if q1 and q2 and q3 and q4:
        if submit_button:
            feedback=collector.st_feedback(
                "custom",
                user_response={
                    "How much do you love this app?":q1,
                    "What do you like about the app?":q2,
                    "How can we improve the app?":q3,
                    "Raise a specific issue":q4
                },
                path=None
            )
            DBQueries.insert_to_database("Termsbrief","Feedback",feedback.dict())
st.markdown("Thank you for your feedback! 🙏")

st.sidebar.success(f"Average Rating : {DBQueries.retrieve_average_rating('Termsbrief')} 🌟")

if not submit_button:
    st.stop()