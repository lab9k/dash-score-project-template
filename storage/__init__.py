from typing import Optional

from dash import Dash

from .store import initialize_memory_store, VariableStore


class Storage:
    def __init__(self):
        self.memory_store: Optional[VariableStore] = None

    def initialize(self, app: Dash):
        self.memory_store = initialize_memory_store(app)


container = Storage()
