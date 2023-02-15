CONNECTION_STRING = getpass.getpass( prompt="mongodb://mongoday3:jvhIsl8HBuvAgi2DHz0xYGT9CJHGZX2dpyckkl7sP8FwEkN6qbgj5zuPtNm7dnTc1OrKMLQ4Xu3hACDbuCWwwA==@mongoday3.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@mongoday3@ " )

DATABASE = "mongodb" 
COLLECTION = "mongo" 
FIELD = "Day"

##CREATE FUNCTION
def insert_sample_document(collection):
    """Insert a sample document and return the contents of its _id field"""
    document_id = collection.insert_one(
        {FIELD: randint(50, 500)}
    ).inserted_id
    print("Inserted document with _id {}".format(document_id))
    return document_id

def create_database_unsharded_collection(client):
    """Create sample database with shared throughput if it doesn't exist and
    an unsharded collection
    """
    db = client[DATABASE]
    # Create database if it doesn't exist
    if DB_NAME not in client.list_database_names():
        # Database with 400 RU throughput that can be shared across the
        # DB's collections
        db.command({"customAction": "CreateDatabase", "offerThroughput": 400})
        print("Created db {} with shared throughput".format(DATABASE))
    # Create collection if it doesn't exist
    if COLLECTION not in db.list_collection_names():
        # Creates a unsharded collection that uses the DBs shared throughput
        db.command(
            {
                "customAction": "CreateCollection",
                "collection": COLLECTION,
            }
        )
        print("Created collection {}".format(COLLECTION))
    return db[COLLECTION]


def main():
    """Connect to the API for MongoDB, create DB and collection, perform
    CRUD operations
    """
    client = pymongo.MongoClient(CONNECTION_STRING)
    try:
        client.server_info()  # validate connection string
    except pymongo.errors.ServerSelectionTimeoutError:
        raise TimeoutError(
            "Invalid API for MongoDB connection string \
                or timed out when attempting to connect"
        )
    collection = create_database_unsharded_collection(client)
    #document_id = insert_sample_document(collection)

if __name__ == "__main__":
    main()




