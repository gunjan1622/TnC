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
            print("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
        else:
            print("Summary extracted: \n{}".format(
                " ".join([sentence.text for sentence in extract_summary_result.sentences]))
            )