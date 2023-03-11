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


# input_text = [
#         "The extractive summarization feature uses natural language processing techniques to locate key sentences in an unstructured text document. "
#         "These sentences collectively convey the main idea of the document. This feature is provided as an API for developers. " 
#         "They can use it to build intelligent solutions based on the relevant information extracted to support various use cases. "
#         "In the public preview, extractive summarization supports several languages. It is based on pretrained multilingual transformer models, part of our quest for holistic representations. "
#         "It draws its strength from transfer learning across monolingual and harness the shared nature of languages to produce models of improved quality and efficiency. "
#     ]
# extractive_summarization(client=DBConnection.get_client(),input_text=input_text, max_sentence_count=5)