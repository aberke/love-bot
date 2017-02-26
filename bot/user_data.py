""" File containing Twitter user data for Love Bot to read and use """


SCIENCE_TWEETS = [
    (
        "Hey @{lover_username1} @{lover_username2}\n"
        "You both RTed this\n"
        "It must be fate\n"
        "The universe wants you\n"
        "To go on a date\n"
        " {tweet_url}"
    ), (
        "Hey @{lover_username1} @{lover_username2} your cosmic fandom for "
        "science and Tyson might imply a bit more chemistry {tweet_url}"
    ), (
        "Hey @{lover_username1} @{lover_username2} the world is 197 million sq"
        " miles but the same tweet brought you two together {tweet_url}"
    )
]

USER_DATA = {
    "jennschiffer": {
        "tweet_templates": [(
            "Hey @{lover_username1} @{lover_username2}! You both RTed this?? "
            "Jenn seems rad. You three should fall in love. I'm a bot."
            " {tweet_url}"
        )]
    },
    "neiltyson": {
        "tweet_templates": SCIENCE_TWEETS
    },
    "BillNye": {
        "tweet_templates": SCIENCE_TWEETS,
    },
    "AlexandraBerke": {
        "tweet_templates": [(
            "Hey @{lover_username1} @{lover_username2}! You both RTed this?? "
            "Alex seems rad. You three should fall in love. I'm a bot."
            " {tweet_url}"
        )]
    }
}
