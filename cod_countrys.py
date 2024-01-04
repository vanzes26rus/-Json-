from pygal_maps_world.maps import COUNTRIES

# for country_cod in sorted(COUNTRIES.keys()):
#     print(country_cod, COUNTRIES[country_cod])

def cod_country(country_name):
    '''Возвращает код страны'''
    for cod, name in COUNTRIES.items():
        if name == country_name:
            return cod
    return None

