import os
import traceback
from discord.ext import commands

description = """
Hello! I am the pagliachatbot
"""

command_prefix = "?"

extensions = [
    'bot.cogs.ping',
    'bot.cogs.pagliacci_random_sentences'
]


class PagliachatBot(commands.Bot):
    """
    Bot For Pagliacci!
    """

    def __init__(self):
        super().__init__(
            command_prefix=command_prefix, description=description,
            pm_help=True, help_attrs=dict(hidden=True)
        )
        for extension in extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                print('Failed to load extension {}.'.format(extension))  # , file=sys.stderr)
                traceback.print_exc()

    def run(self):
        super().run(os.environ.get("BOT_TOKEN", None), reconnect=True)


def run_bot():
    bot = PagliachatBot()
    bot.run()


if __name__ == "__main__":
    run_bot()
