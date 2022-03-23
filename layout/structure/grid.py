from abc import ABCMeta, abstractmethod
from typing import List, Dict
from dash.development.base_component import Component as HtmlComponent
from dash import html


class _Grid(metaclass=ABCMeta):
    t: str

    def __init__(self, children: List['_Grid'] = None, content: HtmlComponent = None, styles: Dict[str, str] = None,
                 extra_classes: List[str] = None):
        if content is not None and children is not None:
            raise ValueError('one of the properties "content" or "children" should be None')
        self.children: List['_Grid'] = children if children is not None else []
        self.content = content
        self.styles: Dict[str, str] = styles or {}
        self.extra_classes: List[str] = extra_classes or []

    def get_layout(self, include_container=True) -> HtmlComponent:
        content = [x.get_layout(False) for x in self.children]
        if len(content) == 0 and self.content is not None:
            content = self.content
        this = html.Div(className=f'{self.t} {" ".join(self.extra_classes)}', children=content, style=self.styles)
        if include_container:
            return html.Div(className='container-fluid min-vh-100 bg-light', children=[this])
        return this


class Column(_Grid):
    t = 'col'


class Row(_Grid):
    t = 'row'
