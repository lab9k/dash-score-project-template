from dash import html, dcc

def pagetitletile(pagetitle:str):
    content = html.Div(className = 'px-2 py-2', children=[
        html.Div(
            className = 'bg-primary text-white px-3 py-2',
            children = [html.H5(pagetitle)]
            )
        ])
    return content

def subtitletile(subtitle:str):
    content = html.Div(className = 'px-2 pt-2', children=[
        html.Div(
            className = 'text-primary px-3 py-0',
            children = [html.H5(subtitle)]
            )
        ])
    return content

def infotile(infotxt:str):
    content = html.Div(className = 'px-2 py-2', children=[
        html.Div(
            className = 'bg-white px-3 py-2',
            children = [html.P(infotxt)]
            )
        ])
    return content

def tile(tiletitle:str, className='', children = None):
    if children is None:
        children = []
    content = html.Div(className = 'px-2 py-2', children=[
        html.Div(
            className = className + ' shadow bg-white px-3 py-2', 
            children = [
                html.H6(className='text-primary', 
                          children=[tiletitle]),
                ] + children
            )
        ])
    return content

def filtertile(tiletitle:str=None, className='', children = None):
    if children is None:
        children = []
    if tiletitle is not None:
        children = [html.H6(
            className='text-primary', 
            children=[tiletitle]
            )] + children
    content = html.Div(className = 'px-2 py-2', children=[
        html.Div(
            className = className + 'px-3 py-0', 
            children = children
            )
        ])
    return content

def plottile(tiletitle:str, className='', **kwargs):
    content = html.Div(className = 'px-2 py-2', children=[
        html.Div(
            className = className + ' shadow bg-white', 
            children = [
                html.H6(className='text-primary px-3 pt-2', 
                          children=[tiletitle]),
                dcc.Graph(**kwargs)
            ])
        ])
    return content

def maptile(tiletitle:str, className='', mapfigure=None):
    content = html.Div(className = 'px-2 py-2', children=[
        html.Div(
            className = className + ' shadow bg-white', 
            children = [
                mapfigure,
                html.Div(className = 'zindex-dropdown position-relative top-0 start-0 pt-3 pl-5',
                         children=[
                             html.H6(tiletitle, 
                                     className='text-primary px-3 pt-2 bg-white'
                                     )]
                         ),
            ])
        ])
    return content