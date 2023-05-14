from .DBConnection import DBConnection

class DBQueries:

    @classmethod
    def insert_to_database(cls,db_name,coll_name,data):
        con = DBConnection.get_client()
        mydb = con[db_name]
        mycol = mydb[coll_name]

        if isinstance(data, list):
            return mycol.insert_many(data)
        else:
            return mycol.insert_one(data)
        
    @classmethod
    def retrieve_average_rating(cls,db_name):
        total_rating=0
        con=DBConnection.get_client()
        mydb=con[db_name]
        
        for col in mydb.list_collection_names():
            mycol=mydb[col]
            pipeline=[
                {
                    '$group':{
                        '_id':None,
                        'average_rating':{
                            '$avg':'$user_response.How much do you love this app?'
                        }
                    }
                }
            ]
            result=mycol.aggregate(pipeline)
            for i in result:
                total_rating=i['average_rating']
        return total_rating