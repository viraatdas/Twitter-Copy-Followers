import pickle
from ordered_set import OrderedSet
import twitter
from env import *
import os
import time


FILENAME = "people_to_follow_list.pkl"

def follow_people(people_to_follow):
    # api of the account that will follow the new accounts 
    new_account = twitter.Api(consumer_key=API_KEY_2,
                        consumer_secret=API_KEY_SECRET_2,
                        access_token_key=ACCESS_TOKEN_2,
                        access_token_secret=ACCESS_TOKEN_SECRET_2)

    print("**************** NEW ACCOUNT CREDENTIALS ********************************")
    print(new_account.VerifyCredentials())
    print("**************** END NEW ACCOUNT API CREDENTIALS ********************************")
    
    i = 0
    while i < len(people_to_follow):
        twitter_id = people_to_follow[i]
        try:
            new_account.CreateFriendship(user_id=twitter_id)
            time.sleep(0.25)
            i+=1
        except:
            with open(FILENAME, "wb") as handle:
                # edge case handling when i is 0
                if i == 0:
                    i = 1
                remaining_people_to_follow = people_to_follow[i-1:]
                pickle.dump(remaining_people_to_follow, handle)
                return
            
def create_people_to_follow():
    # api of the account you want to copy the "followers" and "following"
    old_account = twitter.Api(consumer_key=API_KEY_1,
                        consumer_secret=API_KEY_SECRET_1,
                        access_token_key=ACCESS_TOKEN_1,
                        access_token_secret=ACCESS_TOKEN_SECRET_1)

    print("**************** OLD ACCOUNT CREDENTIALS ********************************")
    print(old_account.VerifyCredentials())
    print("**************** END OLD ACCOUNT CREDENTIALS ********************************")
    

    """
    Since there is a limit on how many people we can friend in a day, 
    we will priortize people that we follow AND people that follow us.

    We'll do this in two parts by first presorting people who follow us 
    and removing people that we don't follow. Afterwards, we add people 
    we follow. 

    We serialize a structure after session of friend to make sure that this doesn't change when 
    we follow more people. 
    """
    # Get ID of everyone following api_1
    followers_id = OrderedSet(old_account.GetFollowerIDs())
    following_id = OrderedSet(old_account.GetFriendIDs())

    # these are people you are following AND they are following you
    people_to_follow = followers_id - followers_id.difference(following_id)

    # adding the rest of the people you follow 
    # order will be preserved because we are 
    # using an ordered set
    people_to_follow |= following_id

    # convert this to a list
    people_to_follow = list(people_to_follow)
    
    follow_people(people_to_follow)

def follow_from_pickled_list():
    with open(FILENAME, "rb") as handle:
        people_to_follow = pickle.load(handle)
    follow_people(people_to_follow)


if __name__ == "__main__":
    if not os.path.exists(FILENAME):
        create_people_to_follow()
    else:
        follow_from_pickled_list()
