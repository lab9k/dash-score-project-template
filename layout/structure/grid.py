from abc import ABCMeta, abstractmethod
from typing import List
from dash.development.base_component import Component as HtmlComponent
from dash import html


class _Grid(metaclass=ABCMeta):

    def __init__(self, children: List['_Grid'] = None, content: HtmlComponent = None):
        if content is not None and children is not None:
            raise ValueError('one of the properties "content" or "children" should be None')
        self.children = children if children is not None else []
        self.content = content

    @abstractmethod
    def get_layout(self, include_container=True) -> HtmlComponent:
        pass


class Column(_Grid):
    def get_layout(self, include_container=True) -> HtmlComponent:
        content = [x.get_layout(False) for x in self.children]
        if len(content) == 0 and self.content is not None:
            content = self.content
        if include_container:
            return html.Div(className='container', children=[html.Div(className='col', children=content)])
        return html.Div(className='col', children=content)


class Row(_Grid):
    def get_layout(self, include_container=True) -> HtmlComponent:
        content = [x.get_layout(False) for x in self.children]
        if len(content) == 0 and self.content is not None:
            content = self.content
        if include_container:
            return html.Div(className='container', children=[html.Div(className='row', children=content)])
        return html.Div(className='row', children=content)
