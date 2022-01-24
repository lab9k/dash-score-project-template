from dash import dcc, Dash, Output, Input, State, callback_context
from dash.exceptions import PreventUpdate
from typing import List, Callable


class VariableStore:
    def __init__(self, app: Dash, store_id: str):
        self.store = store_id
        self.app = app

    def add_input_to_store(self, input_id: str, value_prop: str) -> 'VariableStore':
        @self.app.callback(
            Output(self.store, 'data'),
            Input(input_id, value_prop),
            State(self.store, 'data'))
        def temp(updated_value, data):
            if updated_value is None:
                raise PreventUpdate

            data = data or {}
            data[input_id] = updated_value
            return data

        return self

    def add_store_to_output(self,
                            store_var_ids: List[str],
                            output_id: str,
                            output_prop: str,
                            output_func: Callable) -> 'VariableStore':
        @self.app.callback(
            Output(output_id, output_prop),
            Input(self.store, 'modified_timestamp'),
            State(self.store, 'data')
        )
        def temp(updated_value, data):
            if updated_value is None:
                raise PreventUpdate

            data = data or {}

            callable_args = {key: data.get(val, None) for key, val in store_var_ids}

            returned_value = output_func(**callable_args)
            return returned_value

        return self


def initialize_memory_store(app: Dash, store_id: str) -> VariableStore:
    return VariableStore(app, store_id)
