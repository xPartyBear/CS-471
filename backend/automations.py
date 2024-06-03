import psycopg2
import constants
from datetime import date, datetime, timedelta
import random

import pypokedex
import requests as r

print(date.today())

#insert into puzzle_data (game_date, pokedex_num) values (TO_DATE('05/30/2024','MM/DD/YYYY'), 132);
#delete from puzzle_data;	

#print(pypokedex.get(name="venusaur-mega"))

def get_stage_num(name, chain, i=1):
    if(chain['species']['name']==name):
        return i
    if(len(chain['evolves_to']) == 0 or chain['evolves_to'] == None):
        return 0
    for j in range(0, len(chain['evolves_to'])):
        res = get_stage_num(name, chain['evolves_to'][j], i+1)
        if(res > 0):
            return res


def generate_puzzles(count):
    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
    cur = db.cursor()
    today = date.today()
    options = [m['name'] for m in r.get('https://pokeapi.co/api/v2/pokemon?limit=100000').json()['results']]
    #print(options)
    samples = random.sample(options,count)
    for i in range(0, count):
        d = today + timedelta(i)
        dS = d.strftime("%Y-%m-%d")
        #get initial information
        pokemon = pypokedex.get(name=samples[i])
        name = samples[i] # not sent to the database but really useful for a lot of other calculations
        dex_num = pokemon.dex 
        type1 = pokemon.types[0]
        type2 = 'None' if len(pokemon.types)==1 else pokemon.types[1]
        abilities = ''
        for j in range(0,len(pokemon.abilities)):
            abilities += pokemon.abilities[j][0]
            if(j < len(pokemon.abilities)-1):
                abilities += '/'
        height_weight = str(pokemon.height / 10) + "m / " + str(pokemon.weight / 10) + "kg"
        #data to get egg_types and regions and evo stuff

        #species getter
        res = r.get(f'''https://pokeapi.co/api/v2/pokemon/{samples[i]}''').json()
        species_name = res['species']['name']
        form = name.replace((species_name + '-'),'') if not name.replace((species_name),'') == '' else 'None'

        additionalData = r.get(f'''https://pokeapi.co/api/v2/pokemon-species/{species_name}''').json()
        egg_types = ''
        for k in range(0,len(additionalData['egg_groups'])):
            egg_types += additionalData['egg_groups'][k]['name']
            if(k < len(additionalData['egg_groups'])-1):
                egg_types += '/'

        evo_chainURL = additionalData['evolution_chain']['url'] 
        res = r.get(evo_chainURL).json()
        evo_stage = get_stage_num(species_name,res['chain'])
        mixed = 'Mixed' if len(res['chain']['evolves_to']) > 1 else 'None'
        if len(res['chain']['evolves_to']) == 1:
            evo_method = res['chain']['evolves_to'][0]['evolution_details'][0]['trigger']['name'] 
        else:
            evo_method = mixed


        generationURL = additionalData['generation']['url']
        res = r.get(generationURL).json()
        region = res['main_region']['name']

        cur.execute(f'''INSERT INTO {constants.PUZZLE_TABLE} (game_date, pokedex_num, type1, type2, abilities, height_weight, egg_type, region, form, evo_stage, evo_method) VALUES (TO_DATE('{dS}','YYYY-MM-DD'),{dex_num},'{type1}','{type2}','{abilities}','{height_weight}','{egg_types}','{region}','{form}','{evo_stage}','{evo_method}');''')
        print(f'''date: {d}  dex_num: {dex_num} type1: '{type1}' type2: '{type2}' abilities: '{abilities}' height_weight: '{height_weight}' egg_type: '{egg_types}' region: '{region}' form: '{form}' evo_stage: '{evo_stage}' evo_method: '{evo_method}')''')
        db.commit()
    cur.close()
    db.close()

if __name__ == '__main__':
    #change this value to increase or decrease the amount of puzzles you look to generate
    generate_puzzles(100)

    