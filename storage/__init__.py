from typing import Optional, List

from dash.dcc import Store


class Storage:
    def __init__(self):
        self.stores: List[Store] = []

    def add_memory_store(self, store_id: str):
        self.stores.append(Store(id=store_id, storage_type='memory'))

    def add_local_store(self, store_id: str):
        self.stores.append(Store(id=store_id, storage_type='local'))

    def add_session_store(self, store_id: str):
        self.stores.append(Store(id=store_id, storage_type='session'))


container = Storage()
