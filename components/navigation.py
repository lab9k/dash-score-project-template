from typing import List

from dash import html

from utils.routing import PathUtil


def _navbar_toggler():
    return html.Button(
        className='navbar-toggler', type='button',
        **{'data-bs-toggle': "collapse", 'data-bs-target': "#navbarSupportedContent",
           'aria-controls': "navbarSupportedContent", 'aria-expanded': "false", 'aria-label': "Toggle navigation"},
        children=[
            html.Span(className='navbar-toggler-icon')
        ]
    )


def navbar(routes: List[PathUtil]):
    links = []
    for path in routes:
        links.append(html.Li(className='nav-item', children=[
            html.A(className='nav-link active',
                   href=path.url(), children=[path.pieces[-2]])
        ]))
    return html.Nav(className='navbar navbar-expand-lg navbar-light bg-light',
                    children=[
                        html.Div(className='container-fluid',
                                 children=[
                                     html.A(className='navbar-brand', href='/', children=[
                                         html.Img(src='/assets/img/favicon-32x32.png', alt='logo stad gent', width=32,
                                                  height=32, className='d-inline-block'),
                                         "Dashboard Stad Gent"
                                     ]),
                                     _navbar_toggler(),
                                     html.Div(className='collapse navbar-collapse', id='navbarSupportedContent',
                                              children=[
                                                  html.Ul(
                                                      className='navbar-nav me-auto mb-2 mb-lg-0',
                                                      children=[
                                                          html.Li(className='nav-item',
                                                                  children=[
                                                                      html.A(className='nav-link active',
                                                                             href='/',
                                                                             children=['Home'])
                                                                  ]),
                                                          *links
                                                      ])
                                              ])
                                 ])
                    ])


def sidebar():
    return html.Div()