import geocoder
import folium
import get_locations
import requests

def get_coords(location):
    '''
    (str) --> list
    This function takes the name of location as argument
    and returns the list of real numbers coordinates
    >>> get_coords("New York")
    [40.71455000000003, -74.00713999999994]
    '''
    coords = geocoder.arcgis(location)
    return coords.latlng

def main(dct):
    '''

    This function creates the map with markers of filming locations
    and if film_count and city are True, shows the choropleth of filming
    locations count in country and cities with the most films
    '''

    m = folium.Map(zoom_start=10)
    if dct == None:
        return None
    for friend in dct.keys():
        if dct[friend]:
            try:
                folium.Marker(location=get_coords(dct[friend]),
                     popup=str(friend)
                      ).add_to(m)
            except:
                pass
    return 1


    m.save('templates/locations.html')


