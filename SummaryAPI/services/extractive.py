import streamlit as st
from azure.ai.textanalytics import ExtractSummaryAction

# Method for summarizing text
def extractive_summarization(client,input_text, max_sentence_count):

    poller = client.begin_analyze_actions(
        input_text,
        actions=[
            ExtractSummaryAction(max_sentence_count=max_sentence_count)
        ],
    )

    document_results = poller.result()
    for result in document_results:
        extract_summary_result = result[0]  # first document, first result
        if extract_summary_result.is_error:
            return f"...Is an error with code '{extract_summary_result.code}' and message '{extract_summary_result.message}'"
        else:
            return f"{' '.join([sentence.text for sentence in extract_summary_result.sentences])}"
        
        
        
     