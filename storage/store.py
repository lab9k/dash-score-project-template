from dash import dcc, Dash, Output, Input, State, callback_context
from dash.exceptions import PreventUpdate
from typing import List, Callable


class VariableStore:
    def __init__(self, app: Dash):
        self.app = app
        self.store_ids: List[str] = []

    def add_input_to_store(self, input_id: str, value_prop: str) -> 'VariableStore':
        store_id = f'{input_id}-store'
        self.store_ids.append(store_id)

        @self.app.callback(
            Output(store_id, 'data'),
            Input(input_id, value_prop),
            State(store_id, 'data'))
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
        store_ids = [f'{x}-store' for x in store_var_ids]

        inputs = {x: Input(x, 'modified_timestamp') for x in store_ids}

        @self.app.callback(
            output=[Output(output_id, output_prop)],
            inputs=inputs,
            state={f'{x}-state': State(x, 'data') for x in store_ids}
        )
        def temp(**kwargs):
            y = [(k, v) for k, v in kwargs.items()]
            found_states = list(filter(lambda tp: tp[0].endswith('-state'), y))
            if len(inputs) == len(list(filter(lambda x: x is None, found_states))):
                raise PreventUpdate

            states_dicts = [y[1] for y in found_states]
            states = {}
            for sd in states_dicts:
                states.update(sd)

            callable_args = [states.get(v, None) for v in store_var_ids]
            return output_func(*callable_args)

        return self


def initialize_memory_store(app: Dash) -> VariableStore:
    return VariableStore(app)
