from discord.ext.commands.bot import when_mentioned_or
from discord.ext import commands, tasks
from discord.ext.commands import Cog
import discord

client = discord.Client()
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.bans = True

küfürler = ['amına', 'orospu', 'oç', 'piç', 'pezevenk', 'sik', 'sikerim', 'sikeyim', 'sikim', 'ibne', 'yavşak', 'amcık', 'am', 'yarrak', 'yarak', 'sikiş']
bot = commands.Bot(command_prefix= when_mentioned_or("tb!"), intents = intents)
myFile = "/app/Servers.txt"

class KüfürEngel(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message):
        messageid = str(message.guild.id)
        if message.content == "tb!küfürengel":
            if message.author.guild_permissions.manage_messages:
                with open(myFile, 'a+') as f:
                    f.seek(0)
                    if messageid in f.read():
                        await message.channel.send("Zaten küfür engel açık. Kapatmak için `tb!küfürengel kapat` yazın.")
                    else:   
                        f.write(messageid)
                        await message.channel.send("Küfür engel sistemi başarıyla açıldı.")
                    f.close()
            else:
                await message.channel.send("Üzgünüm ama sunucuda mesajları yönetme iznin yok!")

        if message.content in küfürler:
            with open(myFile, 'a+') as f:
                f.seek(0)
                if messageid in f.read():
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} küfür etmemelisin.")
                f.close()

        if message.content == "tb!küfürengel kapat":
            if message.author.guild_permissions.manage_messages:
                with open(myFile,"r+") as f:
                    f.seek(0)
                    if messageid in f.read():
                        new_f = f.readlines()
                        f.seek(0)
                        for line in new_f:
                            if messageid not in line:
                                f.write(line)
                        f.truncate()
                        await message.channel.send("Küfür engel sistemi başarıyla kapatıldı.")
                    else:
                        await message.channel.send("Zaten küfür engel sistemi kapalı.")
            else:
                await message.channel.send("Üzgünüm ama sunucuda mesajları yönetme iznin yok!")    

        if message.content.startswith("tb!sil"):
            silenecek = message.content.split(" ")
            if int(silenecek[1]) > 100:
                await message.channel.send("100den fazla mesaj silemezsiniz.")
            else:
                deleted = await message.channel.purge(limit=int(silenecek[1]))
                await message.channel.send('{} mesaj silindi.'.format(len(deleted)))

def setup(bot):
	bot.add_cog(KüfürEngel(bot))