import json

import pygal.style
from pygal import maps

import pygal_maps_world.maps
from cod_countrys import cod_country

cc_populations = {}
pop_1 = {}
pop_2 = {}
pop_3 = {}
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
# Построение словаря с данными численности населения.
    for meaning in pop_data:
        if meaning['Year'] == '2010':
            population = int(float(meaning['Value']))
            country_name = meaning['Country Name']
            code = cod_country(country_name)
# группировка стран по 3 уровням насиления
            if code:
                cc_populations[code] = population
            else:
                print(f"Error:{country_name}: {population}.")
            for cc, pop in cc_populations.items():
                if pop < 1000000000:
                    pop_1[cc] = pop
                elif pop > 1000000000:
                    pop_2[cc] = pop
                else:
                    pop_3[cc] = pop


st = pygal.style.LightColorizedStyle
stail_1 = pygal.style.RotateStyle('#000099', base_style=st)
# Изменение цветов стран
wm = pygal_maps_world.maps.World(style=stail_1)
wm.title = 'Числинность насиления'
wm.add('насиление < 1 млд', pop_1)
wm.add('насиление > 1 млд', pop_2)
wm.add('насиление < 10 мл', pop_3)
wm.render_to_file('americas.svg')