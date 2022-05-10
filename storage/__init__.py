from typing import Optional, List

from dash.dcc import Store


class Storage:
    def __init__(self):
        self.stores: List[Store] = []

    def add_memory_store(self, store_id: str, data: dict = None):
        self.stores.append(Store(id=store_id, storage_type='memory', data=data))

    def add_local_store(self, store_id: str, data: dict = None):
        self.stores.append(Store(id=store_id, storage_type='local', data=data))

    def add_session_store(self, store_id: str, data: dict = None):
        self.stores.append(Store(id=store_id, storage_type='session', data=data))


container = Storage()
