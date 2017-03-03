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


CELEB_DATA = {
    # Abbi from Broad City
    "abbijacobson": {
        "tweet_templates": [(
            "Hey @{lover_username1} @{lover_username2}! You both RTed this?? "
            "Abbi is rad. You three should fall in love. I won't tell Ilana."
            " {tweet_url}"
        ), (
            "Hey @{lover_username1} @{lover_username2} - "
            "You both RT'd this? Ya I'm a bot. "
            "Still, you might have more in common that an "
            "appreciation for Abbi.. {tweet_url}"
        ), (
            "Hey @{lover_username1} @{lover_username2} - "
            "Ya Abbi is cool I'll let you two take it from here.."
            " This is a bot. {tweet_url}"
        ), (
            "Hey @{lover_username1} @{lover_username2}\n"
            "Roses are red\n"
            "Violets are blue\n"
            "You both RT'd Abbi\n"
            "Here's an internet intro for you\n"
            "{tweet_url}"
        )]
    },
    # Science nerds <3
    "neiltyson": {
        "tweet_templates": SCIENCE_TWEETS
    },
    "BillNye": {
        "tweet_templates": SCIENCE_TWEETS,
    },
    # "jennschiffer": {
    #     "tweet_templates": [(
    #         "Hey @{lover_username1} @{lover_username2}! You both RTed this?? "
    #         "Jenn seems rad. You three should fall in love. I'm a bot."
    #         " {tweet_url}"
    #     ), (
    #         "Hey @{lover_username1} @{lover_username2} - "
    #         "You both think Jenn is cool? I'll let you two take it from here.."
    #         " This isn't Jenn. {tweet_url}"
    #     ), (
    #         "Hey @{lover_username1} @{lover_username2}\n"
    #         "Roses are red\n"
    #         "Violets are blue\n"
    #         "You both RT'd this\n"
    #         "Here's an internet intro for you\n"
    #         "{tweet_url}"
    #     )]
    # },
}
