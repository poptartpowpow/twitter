import tweepy
import csv
import time
import pandas as pd
import tweo
import configparser

#Authorize requests
config = configparser.ConfigParser()
config.read('config.ini')
bearer_token = config['Twitter']['bearer_token']
auth = tweepy.OAuth2BearerHandler(bearer_token)
api = tweepy.API(auth, wait_on_rate_limit=True, retry_count=3)


def get_twitter_followers(username): 

    #Create empty df & CSV
    empty_df = pd.DataFrame(columns=['ID', 'Username', 'Name', 'Location', 'City', 'State', 'Country', 'Verified status', 'Follower Count'])
    empty_df.to_csv('{}_followers.csv'.format(username))
       

    #Create a CSV with all followers of username
    user = api.get_user(screen_name=username)
    total_followers = user.followers_count
    print('OK')
    
    count = 0

    while True: 
        try:
            print('Initiating loop:')
            for follower in tweepy.Cursor(api.get_followers, screen_name=username).items(total_followers):
                #print('so far so good')

                parsed_location = tweo.parse_location(follower.location)

                follower_list = [count, follower.id, follower.screen_name, follower.name, follower.location, parsed_location['city'], parsed_location['state'], parsed_location['country'], follower.verified, follower.followers_count]
                follower_df = pd.DataFrame(data=follower_list).T

                #print(follower_df)

                follower_df.to_csv(('{}_followers.csv'.format(username)), sep=',', mode='a', header=False, index=False, chunksize=1)
                print('{follower} successfully appended. Count = {count}'.format(follower=follower.screen_name, count=count))
                count += 1
        
        except (tweepy.TweepyException, tweepy.HTTPException, tweepy.BadRequest, tweepy.Unauthorized, tweepy.Forbidden, tweepy.NotFound, tweepy.TooManyRequests, tweepy.TwitterServerError) as error:
            print(error)
            time.sleep(100)
            continue
        except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError) as connection_error:
            print (connection_error) 
            time.sleep(100)
            continue

        finally:
            if (count + 1) == total_followers:
                print('Operation success. All {total_followers} of {username} successfully appended to CSV.'.format(total_followers=total_followers, username=username))
            else:
                print('Operation failure :(')
            break



#RUN FOLLOWER FUNCTION BELOW---------------------------------------------------------------------------------------------
get_twitter_followers()