import json

import requests
from discord.ext import commands


class RandomSentences:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="zio_random")
    async def zio_rand_sentence(self):
        r = requests.get('http://www.bestemmie.org/api/bestemmie/random')
        bestemmia = json.loads(r.text)[0]
        await self.bot.say(bestemmia.get("bestemmia_low"))

    @commands.command(name="zio_default")
    async def zio_default_sentence(self):
        await self.bot.say("mannaggialamadonna amici!!")

    @commands.command(name="babbo_default")
    async def babbo_default_sentence(self):
        await self.bot.say("Devo cagare!")


def setup(bot):
    bot.add_cog(RandomSentences(bot))
