import time
import asyncio
import argparse

from scrape import check_tweets


tweets = None


if __name__ == '__main__':
    """ An event loop is needed to poll Twitter every 10mins. """
    # loop = asyncio.get_event_loop()
    # # ToDo: add async def main if needed later
    # asyncio.run(main())
    # loop.run_forever()
    # loop.close()
    
    parser = argparse.ArgumentParser(description='The handle for the Twitter account')
    parser.add_argument('Handle', type=str)
    args = parser.parse_args()
    handle = args.Handle
    
    n = 0
    while True:
        """ Poll Twitter every 10mins for new tweets on an account. """
        n += 1  # Keep a counter so it doesn't actually run forever.
        check_tweets(handle, tweets)  # Call fn to get latest tweets.
        time.sleep(10 * 60)  # Wait 10mins
        if n > 6 * 24:
            break  # Quit after 24hrs
    print('Goodbye')
