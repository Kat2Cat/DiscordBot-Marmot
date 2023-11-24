import discord
from discord import app_commands
from discord.ext import commands

class msg_filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if 'http://' in message.content or 'https://' in message.content:
            await message.reply(f'請勿在此頻道發送連結', mention_author=True, delete_after=5)
            await message.delete()
            channel = message.channel
            embed = discord.Embed(title="警告", description=f"請勿在 {channel.mention} 發送連結", color=0xff0000)
            embed = embed.set_footer(text=f"一隻土撥鼠MrMarmot", icon_url="https://yt3.googleusercontent.com/JdnJOYl62WdIhiP5XAx0pF94oWO5AiBuJhONTgjL77I877tJVfLXJU_8nuhBz94CXt-q0vVptFo=s176-c-k-c0x00ffffff-no-rj")
            await message.author.send(embed=embed)
        
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(msg_filter(bot))