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
    print('navbar called')
    links = []
    for path in routes:
        if path.is_page():
            links.append(html.Li(className='nav-item', children=[
                html.A(className='nav-link active',
                       href=path.url(), children=[path.pieces[-2]])
            ]))
        else:
            links.append(html.Li(className='nav-item', children=[
                html.A(className='nav-link active',
                       href=path.children[0].url(), children=[f'{path.pieces[-1]}'])
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
                                     html.Div(className='collapse navbar-collapse justify-content-end', id='navbarSupportedContent',
                                              children=[
                                                  html.Ul(
                                                      className='navbar-nav',
                                                      children=[
                                                          # html.Li(className='nav-item',
                                                          #         children=[
                                                          #             html.A(className='nav-link active',
                                                          #                    href='/',
                                                          #                    children=['Home'])
                                                          #         ]),
                                                          *links
                                                      ])
                                              ])
                                 ])
                    ])


def sidebar(paths: List[PathUtil]):
    return html.Div(className='d-flex flex-column p-3 sticky-top', children=[
        html.Ul(className='nav nav-pills flex-column mb-auto', children=[
            html.Li(children=[
                html.A(className='nav-item', href=x.url(), children=[x.pieces[-2]])
            ]) for x in paths
        ])
    ])
