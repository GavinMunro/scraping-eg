#### Beautiful Soup 4, Flask and Docker example

The app monitors a Twitter account and outputs text from new tweets to stdout. 
The 5 most recent tweets are shown initially and new tweets then checked for every 10 mins.

The Twitter handle can be provided as a command-line argument by the user starting the program in console.

A simple REST API is exposed to dump all the tweets collected so far in JSON format via a simple curl command.

**Curl command to access API running in container:** 

$ curl http://127.0.0.1:8000/tweets

**Run command:** 

$ "docker run --name flask_app -d -p 8000:5000 -e FLASK_APP=flask_app flask_app:latest"
