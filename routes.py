import importlib
from typing import List, Dict

import dash
from dash.dependencies import Input, Output

from components import notfound
from environment import settings
from utils.routing import find_module_names_in_path, walk_package, PathUtil


def _find_layouts_and_init_callbacks(app: dash.Dash):
    page_names: List[PathUtil] = []
    package_structure = walk_package('pages')
    for package in package_structure:
        top_files = find_module_names_in_path(package)
        # pages/<top_files>/layout.py ??
        if 'callbacks' in top_files:
            print(f'registering callbacks for {package}')
            # noinspection PyUnresolvedReferences
            importlib.import_module(PathUtil([*package.pieces, 'callbacks']).mod_path()).callbacks(app)
        if 'layout' in top_files:
            # layout exists, so no sublayouts should exist
            layout_path = [*package.pieces, 'layout']
            page_names.append(PathUtil(layout_path))
        else:
            sub_packages = walk_package(package.fs_path())
            for sub in sub_packages:
                sub.prepend_piece('pages')
                sub_files = find_module_names_in_path(sub)
                # pages/<top_files>/<sub_files>/layout.py ??
                if 'callbacks' in sub_files:
                    print(f'registering callbacks for {sub}')
                    # noinspection PyUnresolvedReferences
                    importlib.import_module(PathUtil([*sub.pieces, 'callbacks']).mod_path()).callbacks(app)
                if 'layout' in sub_files:
                    # sub module is a layout module
                    layout_path = [*sub.pieces, 'layout']
                    page_names.append(PathUtil(layout_path))

    return page_names


def create_render_function(app: dash.Dash) -> List[PathUtil]:
    pages = _find_layouts_and_init_callbacks(app)
    modules = {x.url(): {'module': importlib.import_module(x.mod_path()),
                         'path': x} for x in pages}

    print(f'Starting webserver with the following paths: {modules}')

    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname in modules:
            return modules[pathname]['module'].layout
        if settings.DEFAULT_URL in modules:
            return modules[settings.DEFAULT_URL]['module'].layout
        return notfound

    return pages
