from TuzluBaklava.TuzluBaklava import get_prefix
from typing import Optional
import asyncio
import discord
from discord import Embed
from discord.utils import get
from discord.ext.menus import MenuPages, ListPageSource
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.bans = True
client = discord.Client()
bot = commands.Bot(command_prefix= get_prefix, intents = intents, help_command=None)

class enes(Cog):
	def __init__(self, bot):
		self.bot = bot

	@bot.command()
	async def help(self, ctx):
		sosyal = discord.Embed(
			title = "Prefix = tb!",
			description = "TuzluBaklava Sosyal Komutları"
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
		eğlence = discord.Embed(
			title = "Prefix = tb!",
			description = "TuzluBaklava Eğlence Komutları"
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
		
		bilgi = discord.Embed(
			title = "Prefix = tb!",
			description = "TuzluBaklava Bilgi Komutları"
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
			name = "tb!çeviri <Dil Kodları> <Çevirilecek Yazı>",
			value = "Çevirilecek yazıyı girilen dile çevirir.",
			inline = False
		)

		
		pages = [sosyal, bilgi, eğlence]

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
				if i < 2:
					i += 1
					await message.edit(embed = pages[i])
			elif str(reaction) == '⏭':
				i = 2
				await message.edit(embed = pages[i])
			
			try:
				reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = check)
				await message.remove_reaction(reaction, user)
			except:
				break

		await message.clear_reactions()


def setup(bot):
	bot.add_cog(enes(bot))