import dash_leaflet as dl


dflt_mapcenter=[56.46738142611407, 4.270427975709105]
dflt_zoom=5



def lfmap_lyrs(layers:dict=None, legend:bool=True):
    # Initiate layers dict
    if layers == None:
        layers = {}
    for key in ['baselayers', 'overlayers']:
        if not key in layers.keys():
            layers[key]=[]
    if layers['baselayers'] == []:
        layers['baselayers']=[]
        attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        layers['baselayers'].append({'layer':dl.TileLayer(attribution=attribution), 'name':'OpenStreetMap', 'checked':True, 'legend':True})
        attribution = '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
        layers['baselayers'].append({'layer':dl.TileLayer(url='https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png', 
                                                          maxZoom=20,
                                                          attribution=attribution), 
                                     'name':'Stadia Dark', 'checked':False, 'legend':True})
        
    # Generate mapchildren and legend
    if legend is False:
        lyrs = [baselayer['layer'] for baselayer in layers['baselayers']]
        lyrs = lyrs + [overlayer['layer'] for overlayer in layers['overlayers']]
        mapchildren = [*lyrs]
    else:
        nonlegendbase = [baselayer['layer'] for baselayer in layers['baselayers'] if baselayer['legend']==False]
        legendlyrs = dl.LayersControl(
            [dl.BaseLayer(baselayer['layer'], 
                          name = baselayer['name'], 
                          checked= baselayer['checked']
                          ) for baselayer in layers['baselayers'] if baselayer['legend']==True] +
            [dl.Overlay(overlayer['layer'], 
                        name = overlayer['name'], 
                        checked= overlayer['checked']
                        ) for overlayer in layers['overlayers'] if overlayer['legend']==True]
            )
        nonlegendlyrs = [overlayer['layer'] for overlayer in layers['overlayers'] if overlayer['legend']==False]
        mapchildren = [*nonlegendbase, legendlyrs, *nonlegendlyrs]
    return mapchildren

def lfmap_fig(comp_id:str, mapchildren=[dl.TileLayer()], center=dflt_mapcenter, zoom=dflt_zoom):
    # Create map    
    mapfig = dl.Map(center=center, zoom=zoom,
                    children=mapchildren,
                    id=comp_id,
                    className='w-100 h-100',
                    style={'min-width': '400px', 'min-height': '500px'}
                    )
            
    return mapfig
