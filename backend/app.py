import constants
import psycopg2
import pypokedex
from flask import Flask, request
from flask_cors import CORS
import accounts

import requests as r
from flask import jsonify

import time

import os
import json

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

def get_img(name):
    print(f'''finding pokedex image for {name}''')
    data = pypokedex.get(name=name)
    return '' if data.sprites[0]['default'] == None else data.sprites[0]['default']

complete_pokedex = []
dex_path = './dex_data.json'
if not os.path.exists(dex_path):
    json_data = r.get('https://pokeapi.co/api/v2/pokemon?limit=100000').json()['results']
    restart = 0
    while(restart < len(json_data)):
        for i in range(restart,len(json_data)):
            try:
                complete_pokedex.append({"name": json_data[i]['name'], "imgSrc":get_img(json_data[i]['name'])})
            except:
                print(f'''pypokedex stalled on {json_data[i]['name']} pokedex image''')
                time.sleep(1)
                restart = i
                break
        if(i >= len(json_data)-1):
            restart = i + 1
            break
    # complete_pokedex = [{"name": i['name'], "imgSrc":get_img(i['name'])} for i in json_data]
    f = open(dex_path, 'w+')
    f.write(json.dumps(complete_pokedex))
    f.close()
else: 
    f = open(dex_path, 'r')
    complete_pokedex = json.loads(f.read())
    f.close()

print('pokedex loading complete!')

@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/get_daily/<day>")
def get_daily(day):
    # TODO: Get the daily Pokemon
    return "To get daily Pokemon for " + day


@app.route("/get_leaderboard/<leaderboard_type>", methods=['POST'])
@app.route("/get_leaderboard/<leaderboard_type>/<limit>", methods=['POST'])
def get_leaderboard(leaderboard_type, limit=10):
    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
    cur = db.cursor()
    cur.execute(f'''SELECT * FROM {constants.USER_STAT_TABLE};''')
    res = cur.fetchall()

    cur.execute(f'''SELECT * FROM {constants.USER_STAT_TABLE} WHERE last_game_played=CURRENT_DATE;''')
    resDaily = cur.fetchall()

    cur.execute(f'''SELECT id, username FROM public.{constants.USER_TABLE}''')
    idData=cur.fetchall()

    cur.close()
    db.close()
    
    idToUsername = {i[0]: i[1] for i in idData}

    scores = {}
    leaderboard = []

    if leaderboard_type == "daily":
        for user in resDaily:
            scores[idToUsername[user[0]]] = int(user[4])  # Daily score
        #daily score needs to be checked if that last played was updated
        leaderboard = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    elif leaderboard_type == "lifetime":
        for user in res:
            scores[idToUsername[user[0]]] = int(user[5])  # Lifetime score
        leaderboard = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    
    return jsonify(leaderboard[:limit])


@app.route("/set_leaderboard/<username>/<score>", methods=['POST'])
def set_leaderboard(username, score):
    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
    cur = db.cursor()
    cur.execute(f'''SELECT * FROM {constants.USER_STAT_TABLE};''')
    res = cur.fetchall()

    cur.execute(f'''SELECT * FROM "{constants.USER_TABLE}" WHERE username = %s;''', (username,))
    account = cur.fetchone()

    has_stats = False
    last_score = 0

    for user_score in res:
        if user_score[0] == account[0]:
            has_stats = True
            last_score = int(user_score[5])
            break

    if has_stats:
        cur.execute(
            f'''UPDATE "{constants.USER_STAT_TABLE}" 
            SET daily_score = {score}, 
            lifetime_score = {str(last_score + int(score))}
            last_game_played = CURRENT_DATE
            WHERE id = {account[0]};''')
        db.commit()
    else:
        cur.execute(
            f'''INSERT INTO "{constants.USER_STAT_TABLE}" (id, daily_score, lifetime_score, last_game_played) 
            VALUES ({account[0]}, %s, %s, CURRENT_DATE);''',
            (score, str(last_score + int(score)),))
        db.commit()

    cur.close()
    db.close()

    return jsonify(res="Score updated!", data={"daily_score": score, "lifetime_score": str(last_score + int(score))})


@app.route("/get_mon/<dex_num>")
@app.route("/get_mon/<dex_num>/<attribute>")
def dex(dex_num, attribute=None):
    pokemon = pypokedex.get(dex=int(dex_num))
    pokemon_json = {
        "dex": pokemon.dex,
        "name": pokemon.name,
        "types": pokemon.types,
        "abilities": pokemon.abilities,
        "height": str(pokemon.height / 10) + " m",
        "weight": str(pokemon.weight / 10) + "kg",
        "sprites": pokemon.sprites,
    }
    if attribute is not None:
        return pokemon_json[attribute]
    return pokemon_json


@app.route('/get-pokemon', methods=['POST'])
def get_pokemon():
    data = request.get_json()
    date = data['date']

    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
    cur = db.cursor()
    cur.execute(f'''SELECT pokedex_num FROM {constants.PUZZLE_TABLE} WHERE game_date=TO_DATE(%s,'MM-DD-YYYY');''',
                (date,))

    res = cur.fetchone()

    cur.close()
    db.close()
    dex_num = res[0]
    print(dex_num)
    simple_data = pypokedex.get(dex=int(dex_num))
    finalRes = {"name": simple_data.name, "imgSrc": simple_data.sprites[0]['default']}
    print(finalRes)
    return finalRes



@app.route("/filter_mons", methods=['POST'])
def filter_dex():
    data = request.get_json()
    f = data['filter']
    if (f == ''):
        return {'result': []}
    # need to manually get all the pokemon informtion using this command
    filtered = list(filter(lambda i: f.lower() in i['name'].lower(), complete_pokedex))
    return {'result': filtered}


@app.route("/get_info", methods=['POST'])
def get_info():
    data = request.get_json()
    date = data['date']
    info = data['info']

    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
    cur = db.cursor()

    cur.execute(f'''SELECT {info} FROM {constants.PUZZLE_TABLE} WHERE game_date=TO_DATE(%s,'MM-DD-YYYY');''', (date,))

    res = cur.fetchone()

    cur.close()
    db.close()

    return res[0]


@app.route('/guess_pokemon', methods=['POST'])
def guess_pokemon():
    failedToFetch = False
    data = request.get_json()
    date = data['date']
    guess = data['guessName']
    pokemon = pypokedex.get(name=guess)
    dex = pokemon.dex
    print(dex)

    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
    cur = db.cursor()

    cur.execute(
        f'''SELECT * FROM {constants.PUZZLE_TABLE} WHERE game_date = TO_DATE(%s,'MM-DD-YYYY') AND pokedex_num = {dex};''',
        (date,))

    res = cur.fetchone()
    print(res)

    cur.close()
    db.close()
    return {"res": (not res == None)}


@app.route("/get_db", methods=['GET'])
def get_db():
    # Connect to postgres DB
    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
    cur = db.cursor()

    # Select all products from the table
    cur.execute(f'''SELECT * FROM {constants.PUZZLE_TABLE}''')

    # Fetch the data
    data = cur.fetchall()

    # close the cursor and connection
    cur.close()
    db.close()
    return data


@app.route("/login", methods=['POST'])
def login():
    return accounts.login(request)


@app.route("/signup", methods=['POST'])
def signup():
    return accounts.signup(request)


@app.route('/reset', methods=['POST'])
def password_reset():
    return accounts.password_reset(request)


if __name__ == "__main__":
    db = psycopg2.connect(dbname=constants.DATABASE_NAME,
                          user=constants.DATABASE_USER,
                          host=constants.DATABASE_HOST,
                          password=constants.DATABASE_PASSWORD,
                          port=constants.DATABASE_PORT)
    cur = db.cursor()
    cur.execute(f'''CREATE TABLE IF NOT EXISTS "{constants.USER_TABLE}" (id bigserial PRIMARY KEY,
                                                                         username varchar(100), 
                                                                         password varchar(100),
                                                                         email varchar(100),
                                                                         last_played date);''')

    cur.execute(f'''CREATE TABLE IF NOT EXISTS {constants.PUZZLE_TABLE} (game_date date DEFAULT CURRENT_DATE,
                                                                         pokedex_num integer, 
                                                                         type1 varchar(100),
                                                                         type2 varchar(100),
                                                                         abilities varchar(100),
                                                                         evo_method varchar(100),
                                                                         evo_stage varchar(100),
                                                                         height_weight varchar(100),
                                                                         species varchar(100),
                                                                         egg_type varchar(100),
                                                                         region varchar(100),
                                                                         form varchar(100),
                                                                         PRIMARY KEY (game_date, pokedex_num));''')

    cur.execute(f'''CREATE TABLE IF NOT EXISTS {constants.USER_STAT_TABLE} (id bigserial PRIMARY KEY,
                                                                            last_game_played date, 
                                                                            current_streak integer,
                                                                            longest_streak varchar(100),
                                                                            daily_score varchar(100),
                                                                            lifetime_score varchar(100));''')

    # commit the changes
    db.commit()

    # close the cursor and connection
    cur.close()
    db.close()
    app.run(debug=True)
