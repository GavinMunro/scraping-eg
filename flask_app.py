import os
import time
from pathlib import Path  # python3 only

import sqlite3
from dotenv import load_dotenv
from flask import Flask, request, redirect, session, url_for, g

import scrape


app = Flask(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
 
CUR_DIR = Path(__file__).absolute().parents[0]  # ie. the containing folder of the absolute path to this file.
DB = str(CUR_DIR / Path('database.db'))  # To be used by Sqlite


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB)
        db.row_factory = sqlite3.Row
    return db


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.teardown_appcontext
def close_conn(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    db = get_db()
    cur = db.execute(query, args)
    rv = cur.fetchall()
    # print(cur.description)  # debug
    cur.close()
    db.commit()
    return (rv[0] if rv else None) if one else rv


@app.route("/")
def index():
    """Index page contains only one function to start off - responds with JSON
    list of tweets posting using the nominated Twitter handle.
    """
    index_page = '''
    <p>
    <center>
    <h2>Tweets By Author</h2>
        <ul>
            <li><a href="/author">Twitter Author</a></li>
            <br/>
            <li><a href="/tweets">GET Tweets</a></li>
        </ul>
    </center>
    </p>
    '''
    return index_page


handle = 'BorisJohnson'  # ToDo: Create a from for input of this.


@app.route("/author")
def author():
    return handle


@app.route("/tweets")
def tweets():
    tweet_list = [t["tweet"] for t in query_db('SELECT * FROM tweets;')]
    fresh_data = scrape.check_tweets(handle, tweet_list)
    for t in fresh_data:
        if str(t) not in tweet_list:
            _ = query_db(
                "INSERT INTO tweets (author, tweet) VALUES (?, ?);",
                (handle, t)
            )
    time.sleep(2)
    tweet_list = [t["tweet"] for t in query_db('SELECT * FROM tweets;')]
    if not tweet_list:
        return None
    json_data = '{' + \
        '"Author": ' + '"' + handle + '",' + \
        '"Tweets": ' + '["' + tweet_list[0] + '"' + ''.join([', "' + str(t) + '"' for t in tweet_list[1:]]) + ']}'
    return json_data


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True)
