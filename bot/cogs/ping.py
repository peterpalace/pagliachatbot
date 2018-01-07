from discord.ext import commands


class Ping:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self):
        """
        Simple command to test the bot
        :return: Pong!
        """
        await self.bot.say(":ping_pong: Pong!")


def setup(bot):
    bot.add_cog(Ping(bot))
