from discord.ext import commands
import random
import os
import asyncio

INIT_CAP_CHANCE = 0.50  # initial probability to capitalize a letter
PER_CHAR_INCREASE = 0.15  # increase chance of case swap by this amount
BOT_ENABLED = False

bot = commands.Bot(command_prefix="!spong")


@bot.command(name="ify")
async def _convert(ctx, *phrase):
    unaltered = ''.join(phrase) if len(phrase) == 1 else ' '.join(phrase)
    lowered = unaltered.lower()
    alt_cased = []
    cap_chance = INIT_CAP_CHANCE
    for c in lowered:
        roll = random.random()
        if roll > cap_chance:
            alt_cased.append(c.upper())
            cap_chance = INIT_CAP_CHANCE
        else:
            alt_cased.append(c)
            cap_chance -= PER_CHAR_INCREASE
    alt_cased = ''.join(alt_cased)
    print(alt_cased)
    if BOT_ENABLED:
        await ctx.send(alt_cased)
    return alt_cased

if BOT_ENABLED:
    token = os.environ.get("SPONGE_SECRET")
    bot.run(token)
else:
    asyncio.run(_convert(None, "this", "is", "the", "test", "phrase"))
