from datetime import datetime
import discord
from discord.ext import commands, tasks
import asyncio
from discord.ext.commands import HelpCommand
from discord import Member
from typing import Optional
from itertools import cycle
intents = discord.Intents.default()
from discord.utils import find
intents.members = True
intents.messages = True
intents.bans = True
intents.presences = True

extensions = ["cogs.info2", "cogs.küfürengel", "cogs.messages", "cogs.admin", "cogs.welcome"]

küfürler = ['amına', 'orospu', 'oç', 'piç', 'pezevenk', 'sik', 'sikerim', 'sikeyim', 'sikim', 'ibne', 'yavşak', 'amcık', 'am', 'yarrak', 'yarak', 'sikiş']

myFile = "/app/Servers.txt"
zaman = datetime.now()
client = discord.Client()
bot = commands.Bot(command_prefix= commands.when_mentioned_or("tb!"), intents = intents, help_command=None)

activeServers = bot.guilds
sum = 0
for s in activeServers:
    sum += len(s.members)

async def status_task():
    while True:
        servers = len(bot.guilds)
        members = 0
        for guild in bot.guilds:
            members += guild.member_count - 1

        await bot.change_presence(activity = discord.Activity(
            type = discord.ActivityType.watching,
            name = f'{servers} sunucuda {members} kullanıcıya hizmet veriyor.'
        ))
        await asyncio.sleep(10)
        await bot.change_presence(activity = discord.Activity(
            type = discord.ActivityType.listening,
            name = f'{servers} sunucuda {members} kullanıcıya hizmet veriyor.'
        ))
        await asyncio.sleep(10)
        await bot.change_presence(activity = discord.Activity(
            type = discord.ActivityType.playing,
            name = f'{servers} sunucuda {members} kullanıcıya hizmet veriyor.'
        ))
        await asyncio.sleep(10)
        await bot.change_presence(activity = discord.Activity(
            type = discord.ActivityType.competing,
            name = f'{servers} sunucuda {members} kullanıcıya hizmet veriyor.'
        ))
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print('{0.user} olarak giriş yapıldı.'.format(bot))
    bot.loop.create_task(status_task())


@bot.command()
async def yardım(ctx):
    sosyal = discord.Embed(
        title = "Prefix `tb!`",
        description = "TuzluBaklava Sosyal Komutları",
        timestap = zaman.strftime("%X %d/%m/%G"),
        colour = discord.Colour.from_rgb(0, 71, 152) 
    )
    sosyal.add_field(
        name = "insta <Kullanıcı Adı>",
        value = "Girilen kullanıcı hakkında bilgi verir.",
        inline = False
    )
    sosyal.add_field(
        name = "subhot <Subreddit İsmi>",
        value = "Girilen kullanıcı hakkında bilgi verir.",
        inline = False
    )
    sosyal.add_field(
        name = "subnew <Subreddit İsmi>",
        value = "Girilen kullanıcı hakkında bilgi verir.",
        inline = False
    )
    sosyal.add_field(
        name = "subinfo <Subreddit İsmi>",
        value = "Girilen kullanıcı hakkında bilgi verir.",
        inline = False
    )
    sosyal.add_field(
        name = "reddituser <Reddit Kullanıcı İsmi>",
        value = "Girilen kullanıcı hakkında bilgi verir.",
        inline = False
    )
    
    sosyal.set_thumbnail(url=ctx.guild.icon_url)
    sosyal.set_author(icon_url= "https://cdn.shopify.com/s/files/1/0259/9003/7582/products/baklava-with-walnuts_590x.jpg?v=1605787978", name="TuzluBaklava")
    sosyal.timestamp = datetime.now()
    sosyal.set_footer(text='\u200b',icon_url=ctx.author.avatar_url)

    eğlence = discord.Embed(
        title = "Prefix `tb!`",
        description = "TuzluBaklava Eğlence Komutları",
        timestap = zaman.strftime("%X %d/%m/%G"),
        colour = discord.Colour.from_rgb(0, 71, 152)
    )
    eğlence.add_field(
        name = "zar",
        value = "Zar atar.",
        inline = False
    )
    eğlence.add_field(
        name = "aşk <İlk Kişi> <İkinci kişi>",
        value = "Etiketlenen iki kişi arasındaki aşkı ölçer.",
        inline = False
    )
    eğlence.add_field(
        name = "tkm <Hamle>",
        value = "Zar atar.",
        inline = False
    )
    eğlence.add_field(
        name = "meme",
        value = "Rastgele meme yollar.",
        inline = False
    )
    eğlence.add_field(
        name = "tekrarla <Tekrarlanacak Mesaj>",
        value = "Zar atar.",
        inline = False
    )
    eğlence.add_field(
        name = "yazıtura",
        value = "Yazı tura atar.",
        inline = False
    )
    eğlence.add_field(
        name = "doğruluk",
        value = "Doğruluk sorusu gönderir.",
        inline = False
    )
    eğlence.add_field(
        name = "cesaret",
        value = "Cesaret için mesaj gönderir.",
        inline = False
    )
    
    eğlence.set_thumbnail(url=ctx.guild.icon_url)
    eğlence.set_author(icon_url= "https://cdn.shopify.com/s/files/1/0259/9003/7582/products/baklava-with-walnuts_590x.jpg?v=1605787978", name="TuzluBaklava")
    eğlence.timestamp = datetime.now()
    eğlence.set_footer(text='\u200b',icon_url=ctx.author.avatar_url)

    kur = discord.Embed(
        title = "Prefix `tb!`",
        description = "TuzluBaklava Kur Komutları",
        timestap = zaman.strftime("%X %d/%m/%G"),
        colour = discord.Colour.from_rgb(0, 71, 152)
    )
    kur.add_field(
        name = "dolar",
        value = "Güncel dolar verisi gönderir.",
        inline = False
    )
    kur.add_field(
        name = "euro",
        value = "Güncel euro verisi gönderir.",
        inline = False
    )
    kur.add_field(
        name = "sterlin",
        value = "Güncel sterlin verisi gönderir.",
        inline = False
    )
    kur.add_field(
        name = "frank",
        value = "Güncel frank verisi gönderir.",
        inline = False
    )
    kur.add_field(
        name = "bitcoin",
        value = "Güncel bitcoin verisi gönderir.",
        inline = False
    )
    kur.add_field(
        name = "gr altın",
        value = "Güncel gram altın verisi gönderir.",
        inline = False
    )

    kur.set_thumbnail(url=ctx.guild.icon_url)
    kur.set_author(icon_url= "https://cdn.shopify.com/s/files/1/0259/9003/7582/products/baklava-with-walnuts_590x.jpg?v=1605787978", name="TuzluBaklava")
    kur.timestamp = datetime.now()
    kur.set_footer(text='\u200b',icon_url=ctx.author.avatar_url)

    bilgi = discord.Embed(
        title = "Prefix `tb!`",
        description = "TuzluBaklava Bilgi Komutları",
        timestap = zaman.strftime("%X %d/%m/%G"),
        colour = discord.Colour.from_rgb(0, 71, 152)
    )
    bilgi.add_field(
        name = "korona <Ülke Kodu>",
        value = "Girilen ülkenin koronavirüs verilerini gösterir.",
        inline = False
    )
    bilgi.add_field(
        name = "deprem",
        value = "Türkiye'deki son 5 depremi gönderir. (Kaynak = [Kandilli Rasathanesi](http://www.koeri.boun.edu.tr/scripts/lst4.asp))",
        inline = False
    )
    bilgi.add_field(
        name = "haber",
        value = "Son 5 haberi gönderir. (Kaynak = [Anadolu Ajansı](https://www.aa.com.tr/tr/))",
        inline = False
    )
    bilgi.add_field(
        name = "hdurumu <Şehir İsmi>",
        value = "Girilen şehirdeki hava durumunu gösterir.(Kaynak = Google)",
        inline = False
    )
    bilgi.add_field(
        name = "hd5günlük",
        value = "5 günlük hava durumunu gönderir.Eğer çalışmazsa türkçe harfler kullanmadan yazınız. (Mahalleleri desteklemez.) (Kaynak = [MGM] (https://www.mgm.gov.tr))",
        inline = False
    )
    bilgi.add_field(
        name = "hdsondurum",
        value = "Son hava durumunu gönderir. Eğer çalışmazsa türkçe harfler kullanmadan yazınız. (İlçe ve mahalleleri desteklemez.) (Kaynak = [MGM] (https://www.mgm.gov.tr))",
        inline = False
    )
    bilgi.add_field(
        name = "wiki <Aratılcak Terim>",
        value = "Wikipediada aratılan terimin tanımı gönderir.",
        inline = False
    )
    bilgi.add_field(
        name = "çeviri <Dil Kodları> <Çevirilecek Yazı>",
        value = "Çevirilecek yazıyı girilen dile çevirir.",
        inline = False
    )
    bilgi.add_field(
        name = "userinfo , ui , memberinfo ya da mi",
        value = "Kullanıcı hakkında bilgi verir.",
        inline = False
    )
    bilgi.add_field(
        name = "serverinfo ya da si",
        value = "Sunucu hakkında bilgi verir.",
        inline = False
    )

    bilgi.set_thumbnail(url=ctx.guild.icon_url)
    bilgi.set_author(icon_url= "https://cdn.shopify.com/s/files/1/0259/9003/7582/products/baklava-with-walnuts_590x.jpg?v=1605787978", name="TuzluBaklava")
    bilgi.timestamp = datetime.now()
    bilgi.set_footer(text='\u200b',icon_url=ctx.author.avatar_url)

    bott = discord.Embed(
        title = "Prefix `tb!`",
        description = "TuzluBaklava Bot Komutları",
        timestap = zaman.strftime("%X %d/%m/%G"),
        colour = discord.Colour.from_rgb(0, 71, 152)
    )
    bott.add_field(
        name = "davet",
        value = "Bot davet linkini gönderir.",
        inline = False
    )
    bott.add_field(
    name = "ping",
    value = "Botun ping değerini gönderir.",
    inline = False
    )

    bott.set_thumbnail(url=ctx.guild.icon_url)
    bott.set_author(icon_url= "https://cdn.shopify.com/s/files/1/0259/9003/7582/products/baklava-with-walnuts_590x.jpg?v=1605787978", name="TuzluBaklava")
    bott.timestamp = datetime.now()
    bott.set_footer(text='\u200b',icon_url=ctx.author.avatar_url)

    admin = discord.Embed(
        title = "Prefix `tb!`",
        description = "TuzluBaklava Bot Komutları",
        timestap = zaman.strftime("%X %d/%m/%G"),
        colour = discord.Colour.from_rgb(0, 71, 152)
    )
    admin.add_field(
    name = "ban",
    value = "Etiketlenen kullanıcı banlar.(Bu komut için yetkiye ihtiyacınız vardır.)",
    inline = False
    )
    admin.add_field(
    name = "unban",
    value = "Etiketlenen kullanıcının banını kaldırır.(Bu komut için yetkiye ihtiyacınız vardır.)",
    inline = False
    )
    admin.add_field(
    name = "kick",
    value = "Etiketlenen kullanıcı kickler.(Bu komut için yetkiye ihtiyacınız vardır.)",
    inline = False
    )
    admin.add_field(
    name = "küfürengel",
    value = "Küfür engel sistemini açar.",
    inline = False
    )
    admin.add_field(
    name = "küfürengel kapat",
    value = "Küfür engel sistemini kapatır.",
    inline = False
    )
    admin.add_field(
    name = "karşılama",
    value = "Her gelen üyeye hoşgeldin mesajı atar.",
    inline = False
    )
    admin.add_field(
    name = "karşılama kapat",
    value = "Karşılama sistemini kapatır.",
    inline = False
    )

    admin.set_thumbnail(url=ctx.guild.icon_url)
    admin.set_author(icon_url= "https://cdn.shopify.com/s/files/1/0259/9003/7582/products/baklava-with-walnuts_590x.jpg?v=1605787978", name="TuzluBaklava")
    admin.timestamp = datetime.now()
    admin.set_footer(text='\u200b',icon_url=ctx.author.avatar_url)


    pages = [sosyal, bilgi, eğlence, kur, bott, admin]

    message = await ctx.send(embed = sosyal)
    await message.add_reaction('⏮')
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    await message.add_reaction('⏭')

    def check(reaction, user):
        return user == ctx.author

    i = 0
    reaction = None

    while True:
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed = pages[i])
        elif str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '▶':
            if i < 5:
                i += 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '⏭':
            i = 5
            await message.edit(embed = pages[i])
        
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions()


@bot.command(brief = "Ping")
async def ping(ctx):
    await ctx.send('Pong! {0} ms'.format(round(bot.latency, 1)))

@bot.event
async def on_guild_join(guild):      
    general = find(lambda x: x.name == 'genel',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send("""Tuzlu Baklavayı kullanığınız için teşekkür ederiz. 
        
    tb!yardım yazarak komutlara ulaşabilirsiniz. Şikayet veya öneri için Enes Aslan#8852'ye yazın.
        """)
    elif general == None:
        sohbet = find(lambda x: x.name == 'sohbet',  guild.text_channels)
        if sohbet and sohbet.permissions_for(guild.me).send_messages:
            await sohbet.send("""Tuzlu Baklavayı kullanığınız için teşekkür ederiz.             

    tb!yardım yazarak komutlara ulaşabilirsiniz. Şikayet veya öneri için Enes Aslan#8852'ye yazın.
            """)
        if guild.system_channel != None:
            await guild.system_channel.send("""Tuzlu Baklavayı kullanığınız için teşekkür ederiz. 
            
    tb!yardım yazarak komutlara ulaşabilirsiniz. Şikayet veya öneri için Enes Aslan#8852'ye yazın.
            """)


bot.load_extension("cogs.mesajlar")
bot.load_extension("cogs.info2")
bot.load_extension("cogs.admin")
bot.load_extension("cogs.küfürengel")

bot.run("NzcwMjQxODEwODI3NTc1MzA3.X5atlg.ZHCZ_fc6O8DxlciopLJkbmu3nDg")