from discord.ext import commands
import random
import os
import urllib.request

INIT_CAP_CHANCE = 0.50  # initial probability to capitalize a letter

BOT_ENABLED = True


bot = commands.Bot(command_prefix="!spong")


@bot.command(name="ify")
async def _convert(ctx, *phrase):
    print("the fuck")
    unaltered = ''.join(phrase) if len(phrase) == 1 else ' '.join(phrase)
    lowered = unaltered.lower()
    alt_cased = []
    cap_chance = INIT_CAP_CHANCE
    for c in lowered:
        roll = random.random()
        if roll > cap_chance:
            alt_cased.append(c.upper())
        else:
            alt_cased.append(c)
    alt_cased = ''.join(alt_cased)
    print(alt_cased)
    if BOT_ENABLED:
        await ctx.send(alt_cased)
    return alt_cased

def internet_on():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib.request.URLError as err:
        return False

if internet_on():
    print("Got network!")
else:
    print("No network :( ")

token = os.environ.get("SPONGE_SECRET")
print(token)
bot.run(token)
