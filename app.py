import discord

from utils.model import model
from utils.nyaa import nyaa

bot = discord.Bot()


def create_embed(comment, prediction = False, human_prediction = False, user = False):
    if comment:
        title = comment["title"]
        comment_text = comment["comment"]["text"]
        release = comment["release"]
        comment_id = comment["comment"]["id"]

        username = comment["user"]["username"]
        avatar = comment["user"]["avatar"]

        if not prediction:
            prediction = model.predict(comment_text)

        embed = discord.Embed(
            title=title,
            description=comment_text,
            url=f"https://nyaa.si/view/{release}#{comment_id}",
        )
        embed.add_field(name="prediction", value=prediction)

        if embed and human_prediction and user:
            embed.add_field(name="human validation", value=f"{human_prediction} (by  {user})")

        embed.set_author(name=username, icon_url=avatar)

        return embed, prediction
    

    return False


class btnView(discord.ui.View):
    def __init__(self, comment, prediction, user):
        super().__init__(timeout=None)
        self.comment = comment
        self.prediction = prediction
        self.user = user

    @discord.ui.button(label="Negative", style=discord.ButtonStyle.danger, emoji="😤")
    async def negative_callback(self, button, interaction):
        model.train(self.comment["comment"]["text"], "negative")
        embed, _ = create_embed(self.comment, self.prediction, "negative", self.user)
        await interaction.response.edit_message(embed=embed, view=None)

    @discord.ui.button(label="Positive", style=discord.ButtonStyle.success, emoji="😀")
    async def positive_callback(self, button, interaction):
        model.train(self.comment["comment"]["text"], "positive")
        embed, _ = create_embed(self.comment, self.prediction, "positive", self.user)
        await interaction.response.edit_message(embed=embed, view=None)


@bot.slash_command()
async def comment(ctx):
    comment = nyaa.comment.get()
    if comment:
        embed, prediction = create_embed(comment)
        if embed:
            await ctx.respond(embed=embed, view=btnView(comment, prediction, ctx.author.mention))


bot.run("")
