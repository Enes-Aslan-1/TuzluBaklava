from discord import guild
from discord.ext import commands, tasks
from discord.ext.commands import Cog
import discord
import datetime

client = discord.Client()
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.bans = True

bot = commands.Bot(command_prefix= commands.when_mentioned_or("tb!"), intents = intents)
dosya = "/app/Karsilama.txt"

class Welcome(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message):
        messageid = str(message.guild.id)
        if message.content == "tb!karşılama":
            if message.author.guild_permissions.administrator:
                with open(dosya, 'a+') as f:
                    f.seek(0)
                    if messageid in f.read():
                        await message.channel.send("Zaten karşılama sistemi açık. Kapatmak için `tb!karşılama kapat` yazın.")
                    else:   
                        f.write(messageid)
                        await message.channel.send("Karşılama sistemi başarıyla açıldı.")
                    f.close()
            else:
                await message.channel.send("Üzgünüm ama sunucuyu yönetme iznin yok!")

        if message.content == "tb!karşılama kapat":
            if message.author.guild_permissions.administrator:
                with open(dosya,"r+") as f:
                    f.seek(0)
                    if messageid in f.read():
                        new_f = f.readlines()
                        f.seek(0)
                        for line in new_f:
                            if messageid not in line:
                                f.write(line)
                        f.truncate()
                        await message.channel.send("Karşılama sistemi başarıyla kapatıldı.")
                    else:
                        await message.channel.send("Zaten karşılama sistemi kapalı.")
            else:
                await message.channel.send("Üzgünüm ama sunucuyu yönetme iznin yok!")

    @Cog.listener()
    async def on_member_join(self, member):
        with open(dosya,"r+") as f:
            f.seek(0)
            if str(member.guild.id) in f.read():
                mesaj = discord.Embed(
                    title = f"{member.guild.name} sunucusuna hoş geldin!",
                    description = f"Bu sunucudaki {member.guild.member_count}. üyesin."
                )

                fields = [("Sahip", member.guild.owner, False),
                          ("Bölge", member.guild.region, False),
                          ("Kuruluş Tarihi", member.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                          ("Üyeler", len(member.guild.members), False),
                          ("Üyeler (Bot hariç)", len(list(filter(lambda m: not m.bot, member.guild.members))), False),
                          ("Botlar", len(list(filter(lambda m: m.bot, member.guild.members))), False)]

                for name, value, inline in fields:
                    mesaj.add_field(name=name, value=value, inline=inline)

                mesaj.set_thumbnail(url = member.guild.icon_url)
                mesaj.set_footer(icon_url = "https://cdn.shopify.com/s/files/1/0259/9003/7582/products/baklava-with-walnuts_590x.jpg?v=1605787978", text = "TuzluBaklava")
                mesaj.timestamp = datetime.datetime.now()
                mesaj.set_author(name ='Hoşgeldin' , icon_url = member.avatar_url)

                await member.send(embed = mesaj)


def setup(bot):
    bot.add_cog(Welcome(bot))
