from datetime import datetime
from typing import Optional
import discord
from discord import Embed, Member, Profile
from discord.ext.commands import Cog
from discord.ext.commands import command

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.bans = True
intents.presences = True

class Info2(Cog):
	def __init__(self, bot):
		self.bot = bot

	@command(name="userinfo", aliases=["memberinfo", "ui", "mi"])
	async def user_info(self, ctx, target: Optional[Member]):
		target = target or ctx.author
		title = ""
		value = ""

		if target.bot == True:
			title = title + "<:Bot:806827787708268624>"

		if target.public_flags.hypesquad_bravery == True:
			title = title + "<:Bravery:806813433672499231>"

		if target.public_flags.hypesquad_balance == True:
			title = title + "<:Balance:806814996415512576>"
		
		if target.public_flags.hypesquad_brilliance == True:
			title = title + "<:Brilliance:806816169901817897>"
			
		if target.public_flags.staff == True:
			title = title + "<:Staff:806819511189110805>"
		
		if target.public_flags.partner == True:
			title = title + "<:Partner:806819513374605323>"

		if target.public_flags.early_verified_bot_developer == True:
			title = title + "<:EarlyVerifiedBotDeveloper:806819511209689088>"

		targetavatar = str(target.avatar_url)
		if "gif" in targetavatar:
			title = title + "<:Nitro:806974063649357864>"

		if target.public_flags.bug_hunter_level_2 == True:
			title = title + "<:BugHunterLevel2:806819511067475988>"

		if target.public_flags.bug_hunter == True:
			title = title + "<:BugHunter:806819510782263317>"

		if target.id == target.guild.owner_id:
			value = value + "<:ServerOwner:806832320978878484>"	

		if str(target.status) == "online":
			value = value + "<:Online:806829176417288242>"

		if str(target.status) == "offline":
			value = value + "<:Offline:806829176324620288>"

		if str(target.status) == "idle":
			value = value + "<:Idle:806829176282677279>"

		if str(target.status) == "dnd":
			value = value + "<:dnd:806829194918494219>"	

		value1 =  value + " " + target.mention + " "+ target.name + "#" + target.discriminator

		embed = Embed(title="Kullanıcı Bilgisi",
					  description=title,
					  colour=target.colour,
					  timestamp=datetime.utcnow())

		embed.set_thumbnail(url=target.avatar_url)

		embed.add_field(name = "İsim", value = value1)

		embed.set_author(icon_url= "https://cdn.shopify.com/s/files/1/0259/9003/7582/products/baklava-with-walnuts_590x.jpg?v=1605787978", name="TuzluBaklava")

		fields = [("ID", target.id, False),
				  ("En Yetkili Rolü", target.top_role.mention, False),
				  ("Status", str(target.status).title(), False),
				  ("Aktiflik", f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}", False),
				  ("Oluşturulma Tarihi", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
				  ("Katılma Tarihi", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False),
				  ("Takviye Yapıyor mu?", bool(target.premium_since), False)]

		for name, value, inline in fields:
			embed.add_field(name=name, value=value, inline=inline)

		await ctx.send(embed=embed)

	@command(name="serverinfo", aliases=["guildinfo", "si", "gi"])
	async def server_info(self, ctx):
		embed = Embed(title="Server Bilgisi",
					  colour=ctx.guild.owner.colour,
					  timestamp=datetime.utcnow())

		embed.set_thumbnail(url=ctx.guild.icon_url)

		embed.set_author(icon_url= "https://cdn.shopify.com/s/files/1/0259/9003/7582/products/baklava-with-walnuts_590x.jpg?v=1605787978", name="TuzluBaklava")

		statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

		fields = [("ID", ctx.guild.id, True),
				  ("Sahip", ctx.guild.owner, True),
				  ("Bölge", ctx.guild.region, True),
				  ("Kuruluş Tarihi", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
				  ("Üyeler", len(ctx.guild.members), True),
				  ("Üyeler (Bot hariç)", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
				  ("Botlar", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
				  ("Statuses", f"<:Online:806829176417288242> {statuses[0]} <:Idle:806829176282677279> {statuses[1]} <:dnd:806829194918494219> {statuses[2]} <:Offline:806829176324620288> {statuses[3]}", True),
				  ("Banlanan kişi sayısı", len(await ctx.guild.bans()), True),
				  ("Yazı Kanalları", len(ctx.guild.text_channels), True),
				  ("Ses Kanalları", len(ctx.guild.voice_channels), True),
				  ("Kategoriler", len(ctx.guild.categories), True),
				  ("Roller", len(ctx.guild.roles), True),
				  ("Davetler", len(await ctx.guild.invites()), True),
				  ("\u200b", "\u200b", True)]

		for name, value, inline in fields:
			embed.add_field(name=name, value=value, inline=inline)

		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Info2(bot))