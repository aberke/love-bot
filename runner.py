""" Run the Bot """

from bot import bot
from bot.celeb_data import CELEB_DATA

love_bot = bot.LoveBot()

for screen_name in CELEB_DATA.keys():
    love_bot.handle_celebrity(screen_name)
