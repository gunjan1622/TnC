from .utils.TextAnalytics import TextAnalytics
from .utils.DBConnection import DBConnection

# inits
try:
    textanalyticscon = TextAnalytics()
    dbconnection = DBConnection()
    print(f"Connection successful to database:{dbconnection.get_client()} and Connection successful to Text Analytics:{textanalyticscon.get_client()}")
except Exception as e:
    print(e)