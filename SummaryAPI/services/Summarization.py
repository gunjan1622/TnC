import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
from SummaryAPI.utils.TextAnalytics import TextAnalytics

from .extractive import extractive_summarization
from .abstract import abstractive_summarization

class Summarization:
    
        def __init__(
                    self,
                    model):
            self.model = model

        def summarize(self,docs,max_sentence_count):
            if isinstance(docs, str):
                if docs:
                     docs = [docs]
                else:
                     return []
            if self.model == "Extractive":
                 return extractive_summarization(
                    TextAnalytics.get_client(),
                    docs,
                    max_sentence_count)    
            
            elif self.model == "Abstractive":
                return abstractive_summarization(
                     TextAnalytics.get_client(),
                     docs,
                     max_sentence_count)