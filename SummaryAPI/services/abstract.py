from azure.ai.textanalytics import AbstractSummaryAction

def abstractive_summarization(client,input_text, max_sentence_count):

    poller = client.begin_analyze_actions(
        input_text,
        actions=[
            AbstractSummaryAction(max_sentence_count=max_sentence_count),
        ],
    )

    document_results = poller.result()
    for abstract_summary_results in document_results:
        for result in abstract_summary_results:
            if result.kind == "AbstractiveSummarization":
                print("Summaries abstracted:")
                [print(f"{summary.text}\n") for summary in result.summaries]
            elif result.is_error is True:
                print("...Is an error with code '{}' and message '{}'".format(
                    result.code, result.message
                ))

