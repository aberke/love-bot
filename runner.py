""" Run the Bot """

from bot import bot
from bot.user_data import USER_DATA

love_bot = bot.LoveBot()

for username in USER_DATA.keys():
    love_bot.handle_celebrity(username)
