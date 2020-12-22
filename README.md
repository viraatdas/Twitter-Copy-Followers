# Twitter-Copy-Followers
Gets followers from one account and follows same people on another account

### How to use
- Rename `temp_env.py` to `env.py`
  - `mv temp_env.py env.py`
- Get the access and API tokens for the two accounts (one is the old account where you want to copy the followers from. The other is the new one that will copy the followers.
  - https://python-twitter.readthedocs.io/en/latest/getting_started.html
- Add the values in `env.py` accordingly
- Run `pipenv install`
- Run `python follow.py`

### Note
The Twitter API only allows 400 follows every 24 hours [POST friendships/create
](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-create). There is not way of getting around this apart from just running this over multiple days if you have more than 400 followers. 

For my purposes, I wanted to first follow people that follow me AND that I follow. I used an OrderedSet to add these people to be followed first. Anytime there is  an exception raised (most likely due to the number of people being followed), the list of remaining people that haven't been followed is serialized. When `follow.py` is run again, it resumes using the serialized structure to follow. 
