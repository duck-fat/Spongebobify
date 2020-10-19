from discord.ext import commands
import random
import os

INIT_CAP_CHANCE = 0.50  # initial probability to capitalize a letter
IMGFLIP_MEME_ID = 102156234  # meme ID for imgflip meme generator

BOT_ENABLED = True


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
        else:
            alt_cased.append(c)
    alt_cased = ''.join(alt_cased)
    print(alt_cased)
    if BOT_ENABLED:
        await ctx.send(alt_cased)
    return alt_cased


@bot.command(name="epic")
async def _generate_img(ctx, *text):
    pass


@bot.command(name="e help")
async def _print_help(ctx):
    help_text = [
        "!spongify <text> to put your text into mocking case, a la the Mocking Spongebob meme.",
        "!spongepic <text1>/<text2> to generate a Mocking Spongebob image macro.",
        "!sponge help to generate this help text."
    ]
    ctx.send('<br>'.join(help_text))


token = os.environ.get("SPONGE_SECRET")
bot.run(token)
