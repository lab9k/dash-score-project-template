import importlib
import pkgutil
from dataclasses import dataclass
from typing import List

import dash
from dash.dependencies import Input, Output

from components import notfound


@dataclass
class LayoutPath:
    pieces: List[str]

    def fs_path(self) -> str:
        return '/'.join(self.pieces)

    def mod_path(self) -> str:
        return '.'.join(self.pieces)

    def url(self) -> str:
        pieces = self.pieces.copy()
        pieces.remove('pages')
        pieces.remove('layout')
        return '/'.join(['', *pieces])


def _find_layouts():
    page_names: List[LayoutPath] = []
    for top_loader, top_module_name, top_is_pkg in pkgutil.walk_packages(['pages']):
        top_mod_path = f'{top_loader.path}/{top_module_name}'
        top_files = [name for _, name, _ in pkgutil.iter_modules([top_mod_path])]
        if 'layout' in top_files:
            # layout exists, so no sublayouts should exist
            layout_path = ['pages', top_module_name, 'layout']
            page_names.append(LayoutPath(layout_path))
        else:
            for sub_loader, sub_mod_name, sub_is_pkg in pkgutil.walk_packages(['/'.join(['pages', top_module_name])]):
                sub_mod_path = f'{sub_loader.path}/{sub_mod_name}'
                sub_files = [name for _, name, _ in pkgutil.iter_modules([sub_mod_path])]
                if 'layout' in sub_files:
                    # sub module is a layout
                    layout_path = ['pages', top_module_name, sub_mod_name, 'layout']
                    page_names.append(LayoutPath(layout_path))

    return page_names


def create_render_function(app: dash.Dash):
    pages = _find_layouts()
    modules = {x.url(): importlib.import_module(x.mod_path()) for x in pages}

    print(f'Starting webserver with the following paths: {modules}')

    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname in modules:
            return modules[pathname].layout
        return notfound.NotFoundPage


if __name__ == '__main__':
    names = _find_layouts()
    print(names)
