import pandas as pd
from SummaryAPI.utils.DBConnection import DBConnection

# Define the rating table schema
rating_schema = """
CREATE TABLE IF NOT EXISTS ratings (
    id INT AUTOINCREMENT PRIMARY KEY,
    rating INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
# Execute the schema creation query on the database
session=DBConnection.authenticate_SF_session()
session.use_database("RATINGSDB")
session.sql(rating_schema).collect()

# Define the function to insert a rating into the database
def insert_rating(rating):
    with DBConnection.authenticate_SF_session() as conn:
        insert_query = f"INSERT INTO ratings (rating) VALUES ({rating})"
        conn.sql(insert_query).collect()

def get_stats():
    with DBConnection.authenticate_SF_session() as session:
        session.use_database("RATINGSDB")
        count_query = "SELECT COUNT(*) as count FROM ratings"
        result = session.sql(count_query).collect()
        num_responses = result[0][0]
        if num_responses > 0:
            avg_query = "SELECT AVG(rating) as average_rating FROM ratings"
            result = session.sql(avg_query).collect()
            avg_rating = result[0][0]
        else:
            avg_rating = 0.0
        return num_responses, avg_rating



