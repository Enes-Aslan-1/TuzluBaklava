from discord.ext.commands.bot import when_mentioned_or
import discord
from discord.ext import commands
from discord.ext.commands import Cog

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.bans = True

bot = commands.Bot(command_prefix= when_mentioned_or("tb!"), intents = intents)

class Admin(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member} banlandı!')

    # The below code unbans player.
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} ın banı kaldırıldı!')
                return

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member} kicklendi!')


def setup(bot):
	bot.add_cog(Admin(bot))