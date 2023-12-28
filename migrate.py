import sys
import firebase_admin
from firebase_admin import credentials, initialize_app, firestore

dev_cred = credentials.Certificate("service_accounts/from.json")
prod_cred = credentials.Certificate("service_accounts/to.json")

default_app = initialize_app(dev_cred, name="from-app")
other_app = initialize_app(prod_cred, name="to-app")

dev_db = firestore.client(default_app)
prod_db = firestore.client(other_app)

collection_ref = dev_db.collection(sys.argv[0])
destination_collection_ref = prod_db.collection(sys.argv[0])

# transfer documents
for doc in collection_ref.stream():
    destination_collection_ref.document(doc.id).set(doc.to_dict())
