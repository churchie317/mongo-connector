# filename: my_doc_manager.py
import requests as rq
from mongo_connector.doc_managers.doc_manager_base import DocManagerBase


class DocManager(DocManagerBase):

    def __init__(self, url, **kwargs):
        print("Starting document manager...")

    def stop(self):
        print("Stopping document manager...")

    def upsert(self, doc, namespace, timestamp):
        print("Upsert called...")
        rq.get("http://localhost:8080")
        print(doc)
        print(namespace)
        print(timestamp)

    def bulk_upsert(self, docs, namespace, timestamp):
        print("Bulk upsert called...")
        print(docs)
        print(namespace)
        print(timestamp)

    def update(self, document_id, update_spec, namespace, timestamp):
        print("Update called...")
        print(document_id)
        print(update_spec)
        print(namespace)
        print(timestamp)

    def remove(self, document_id, namespace, timestamp):
        print("Remove called...")
        print(document_id)
        print(namespace)
        print(timestamp)

    def search(self, start_ts, end_ts):
        print("Search called...")
        print(start_ts)
        print(end_ts)

    def commit(self):
        print("Search called...")

    def get_last_doc(self):
        return None

    def handle_command(self, doc, namespace, timestamp):
        print("Handle command called...")
