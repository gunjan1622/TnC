""" Import Important Packages"""
import os
from dotenv import load_dotenv
load_dotenv()

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

class TextAnalytics:
    """TextAnalytics Class. It ensures only one instance of the class is 
       created and it is accessible from everywhere. It is used in the 
       design of logging classes, Configuration classes where we need to have 
       only one instance of the class. There is no need to create multiple 
       instances of each operation across all components of application.

    Raises:
           Exception: It raises an exception if the client instance is not created.
    """
    __client = None #This is the client variable that is used to connect to the database
    flag_client = False

    try:
        # Authenticate the client using your key and endpoint 
        @staticmethod
        def authenticate_client():
            key = os.environ["API_KEY"]
            endpoint = os.environ["ENDPOINT"]
            ta_credential = AzureKeyCredential(key)
            text_analytics_client = TextAnalyticsClient(
                    endpoint=endpoint, 
                    credential=ta_credential)
            return text_analytics_client
        
    except Exception as e:
        raise Exception(f"Error while authenticating the client: {e}")

    def __init__(self):
        """This is the constructor of the class. It is used to create the client 
        variable. It also checks if the client instance is already created. 
        If the client instance is already created, then it does not create a 
        new client instance.
        """
        if TextAnalytics.__client is not None:
            raise Exception("This class is a singleton!")
        else:    
            TextAnalytics.__client = TextAnalytics.authenticate_client()
            TextAnalytics.flag_client = True

    @staticmethod  # A static method is a method that is called without creating an instance of the class.
    def get_client():
        """The get_client() function is used to get the client instance.

        Returns:
            TextAnalytics.__client: It returns the client instance.
        """
        return TextAnalytics.__client