import os
from pathlib import Path  # python3 only

from dotenv import load_dotenv
from flask import Flask, request, redirect, session, url_for

import scrape


app = Flask(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


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
            <li><a href="/person">Twitter Author</a></li>
            <br/>
            <li><a href="/tweets">GET Tweets</a></li>
        </ul>
    </center>
    </p>
    '''
    return index_page


handle = 'BorisJohnson'  # ToDo: Create a from for input of this.


@app.route("/tweets")
def tweets():
    data = scrape.check_tweets(handle, [])
    json_data = '{' + \
        '"Author": ' + '"' + handle + '",' + \
        '"Tweets": "' + str(data) + '"}'
    print(json_data)  # debug
    return json_data


if __name__ == "__main__":
    # This allows us to use a plain HTTP callback. For local testing purposes.
    # NEVER SET THIS VARIABLE IN PRODUCTION.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    app.secret_key = os.urandom(24)
    app.run(debug=True)
