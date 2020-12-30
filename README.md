# scraping-eg
This is an exercise/example of webscraping using Beautiful Soup 4 and Flask

Program monitors a Twitter account and outputs text from new tweets to stdout, 5 most recent tweets right after execution and checks for new tweets every 10 mins.

The Twitter handle can be provided as a command-line argument by the user starting the program in console.

Exposes a simple API to dump all the tweets collected so far in JSON format via a simple curl command.
