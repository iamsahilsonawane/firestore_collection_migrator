import sys
import firebase_admin
from firebase_admin import credentials, initialize_app, firestore

from_cred = credentials.Certificate("service_accounts/from.json")
to_cred = credentials.Certificate("service_accounts/to.json")

default_app = initialize_app(from_cred, name="from-app")
other_app = initialize_app(to_cret, name="to-app")

from_db = firestore.client(default_app)
to_db = firestore.client(other_app)

collection_ref = from_db.collection(sys.argv[0])
destination_collection_ref = to_db.collection(sys.argv[0])

# transfer documents
for doc in collection_ref.stream():
    destination_collection_ref.document(doc.id).set(doc.to_dict())
