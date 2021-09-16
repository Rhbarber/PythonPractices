import os; discord_pass = os.environ['TOKEN'];

from discord_easy_commands import EasyBot

bot = EasyBot()

bot.setCommand("!test", "I'm alive!")

bot.run(discord_pass)