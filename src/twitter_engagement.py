def twitter_api_auth(api_key, api_secret_key, access_token, access_token_secret):
    import tweepy 

    auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth)

    return api

def twitter_engagement(user, yaml_path):
    import yaml
    import tweepy
    from datetime import datetime, timedelta

    with open(yaml_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    
    api = twitter_api_auth(config['twitter_api']['api_key'],config['twitter_api']['api_secret_key'],
                           config['twitter_api']['access_token'],config['twitter_api']['access_token_secret']) 
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    end_date_str = end_date.strftime('%Y-%m-%d')
    start_date_str = start_date.strftime('&Y-%m-%d')

    tweets = tweepy.Cursor(api.user_timeline, screen_name=user,since=start_date_str, until=end_date_str).items()

    #for tweet in tweets:
        #user_data