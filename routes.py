import importlib
from typing import List

import dash
from dash.dependencies import Input, Output

from components import notfound
from utils.routing import find_module_names_in_path, walk_package, LayoutPath


def _find_layouts():
    page_names: List[LayoutPath] = []
    package_structure = walk_package('pages')
    for package in package_structure:
        top_files = find_module_names_in_path(package)
        # pages/<top_files>/layout.py ??
        if 'layout' in top_files:
            # layout exists, so no sublayouts should exist
            layout_path = [*package.pieces, 'layout']
            page_names.append(LayoutPath(layout_path))
        else:
            sub_packages = walk_package(package.fs_path())
            for sub in sub_packages:
                sub.prepend_piece('pages')
                sub_files = find_module_names_in_path(sub)
                # pages/<top_files>/<sub_files>/layout.py ??
                if 'layout' in sub_files:
                    # sub module is a layout module
                    layout_path = [*sub.pieces, 'layout']
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
        return notfound
