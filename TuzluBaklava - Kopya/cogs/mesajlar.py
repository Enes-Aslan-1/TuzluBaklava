import discord
import random
import feedparser
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from covid import Covid
from KekikSpatula import Doviz
from KekikSpatula import HavaDurumu
import requests
import praw
from datetime import datetime
from google_trans_new import google_translator
import os
import wikipedia
from instaloader import Instaloader, Profile
from discord.ext.commands import Cog
import time

L = Instaloader()

LANGUAGES = {
    'af': 'Afrika Dili',
    'sq': 'Arnavutça',
    'am': 'Amharca',
    'ar': 'Arapça',
    'hy': 'Ermenice',
    'az': 'Azerbaycan Dili',
    'eu': 'Baskça',
    'be': 'Belarusça',
    'bn': 'Bengalce',
    'bs': 'Bosnakça',
    'bg': 'Bulgarca',
    'ca': 'Katalanca',
    'ceb': 'Cebuano',
    'ny': 'Chicheva',
    'zh-cn': 'Çince (Basitleştirilmiş)',
    'zh-tw': 'Çince (Gelenekse)',
    'co': 'Korsika',
    'hr': 'Hırvatça',
    'cs': 'Çekce',
    'da': 'Danca',
    'nl': 'Hollandaca',
    'en': 'İngilizce',
    'eo': 'esperanto',
    'et': 'Estonca',
    'tl': 'filipino',
    'fi': 'Fince',
    'fr': 'Fransızca',
    'fy': 'Frizce',
    'gl': 'Galyiçyaca',
    'ka': 'Gürce',
    'de': 'Almanca',
    'el': 'Yunanca',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'İbranice',
    'he': 'İbranice',
    'hi': 'Hintçe',
    'hmn': 'hmong',
    'hu': 'Macarca',
    'is': 'İzlandaca',
    'ig': 'igbo',
    'id': 'Endonezya Dili',
    'ga': 'İrlanda Dili',
    'it': 'İtalyanca',
    'ja': 'Japonca',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'Korece',
    'ku': 'Kürtçe (kurmanji)',
    'ky': 'Kırgızca',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'Letonca',
    'lt': 'Litvanyaca',
    'lb': 'Lüksemburgca',
    'mk': 'Makedonca',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'Maltaca',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'Moğolca',
    'my': 'myanmar (burmese)',
    'ne': 'Nepalce',
    'no': 'Norveççe',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'Farsça',
    'pl': 'Lehçe',
    'pt': 'Portekizce',
    'pa': 'punjabi',
    'ro': 'Romence',
    'ru': 'Rusça',
    'sm': 'samoan',
    'gd': 'İskoç Galcesi',
    'sr': 'Sırpça',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'Slovakça',
    'sl': 'Slovence',
    'so': 'somali',
    'es': 'İspanyolca',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'İsveççe',
    'tg': 'tajik',
    'ta': 'tamil',
    'tt': 'Tatarca',
    'te': 'telugu',
    'th': 'Tayca',
    'tr': 'Türkçe',
    'tk': 'Türkmence',
    'uk': 'Ukrayna',
    'ur': 'urdu',
    'ug': 'Uygurca',
    'uz': 'Özbekçe',
    'vi': 'Vietnamca',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu',
}

translator = google_translator()

yazıtura = ["yazı", "tura"]
covid = Covid(source="worldometers")
covid.get_data()

reddit = praw.Reddit(client_id='vRYVGceTPhRrwg', client_secret='Oibl0EtDsuNqH30UPT1CkBFz804', user_agent='EnesinBotu')

cevaplar = ['Doğru \N{WHITE HEAVY CHECK MARK}', 'Yalan \N{CROSS MARK}']

truth_items = ['Telefonunda en son attığın mesaj nedir ?', 'En son söylediğin yalan nedir?', 'Şişeden bir cin çıksa üç dileğin ne olurdu?', 'Şimdiye kadar bir başkasına söylediğin en acımasızca şey neydi?', 'Dünyadaki herhangi birini Türkiye’nin başkanı yapabilseydin bu kim olurdu?', 'Bir aynanın önünde yaptığın en çılgınca şey nedir?', 'Bu hayatta en çok kimi kıskanıyorsun?', 'Bu hayatta en çok kimi kıskanıyorsun?', 'Şimdiye kadar bir başkasına söylediğin en acımasızca şey neydi?', 'Hangi ünlü yerinde olmak isterdin?', 'Ömrünün sonuna kadar dinlemek için tek bir şarkı seçebilecek olsaydın hangisini seçerdin ?', 'Dışarıda yaşadığın en utanç verici an neydi ?', 'Tuvaletini yaparken düşündüğün bir kaç şey söyler misin ?', 'Sokakta yere bir şey düşürdüğünde hiç bir şey olmamış gibi alıp ağzına attın mı ?', 'Bir sabah karşı cins olarak uyansaydın ilk yapacağın şey ne olurdu ?', 'Eğer birden fazla eşle evlenebilseydin ? Kimleri seçerdin ?', 'Telefonunda arattığın en son şey nedir ?', 'Duştayken işer misin ?', 'En kötü huyun nedir ?', 'En gıcık olduğun şey nedir ?', 'Hiç aldatıldın mı ?', 'Hiç osurup suçu başkasına attın mı ?'
, 'Hayalindeki kız/erkek nasıl biri ?', 'Herhangi bir ünlü ile evlenseydin, kim olurdu?', 'Yaptığın en çapkın şey nedir?', 'Bir sınavdan aldığın en kötü puan neydi?', 'Sınıfımızdaki en iyi 5 erkek kim? Onları sırala.', 'Hiç yerden bir şey yedin mi?', 'Hiç tabağını yaladın mı?', 'Hiç terinin tadına baktın mı?', 'Hayatının en büyük hatası neydi?', 'Hiç geçmişte bir şey çaldın mı?', 'Kaç kez öpüştün?', 'Hangi garip kokuyu seversin?', 'Birisi kapınızın önünde 2.000.000 TL ile dolu bir çanta bırakırsa ne yapardınız?', 'Eşinizi tek bir soruya göre seçmek zorunda olsaydınız, hangi soruyu sorardınız?', 'Kendinize özel bir organ tasarlayabilseydin, hangi organ ve vücudun neresinde olurdu?', 'Yaptığınız en iğrenç şaka nedir?', 'İsminizi değiştirmek zorunda olsaydınız, yeni ismin ne olurdu?', 'Yakalanmadan söylediğin en büyük yalan nedir?', 'Bir ünlü Instagram’da seni takip etseydi bu ünlünün kim olmasını isterdin?', 'Erkek arkadaşının ya da kız arkadaşının seninle aynı üniversiteye gitmesini ister misin?']

sorular = ['Saklamanız söylendiği bir sırrı hiç anlattınız mı?', 'Hiç en iyi arkadaşına yalan söyledin mi?', ' Size 5000 lira verilse, oyunuzu satar mısınız?', 'Toplum baskısı, dini kurallar ve cezalar olmasaydı, adam öldürür müydünüz?', 'Sinirlendiğinde ortalığı yakıp yıkıp, insanlara sesini yükselttiğin hatta ve hatta küfrettiğin oluyor mu?', 'Arkadaşlarınla buluşmak istemediğinde onlara sık sık yalan söylediğin oluyor mu?', 'Sevdiğin insanla ailen kesinlikle evlenmeni istemiyor. Onları dinler misin?', 'En yakın arkadaşının eski sevgilisiyle evlenir miydin?', 'Birine aşık olduğun genelde ilk adımı karşındaki kişiden mi beklersin?', 'En iyi arkadaşına bile söylemediğin sırların var mı?']

dare_items = ['Yeri öp', 'Sarhoş taklidi yap', 'Birini ara ve karadeniz şivesiyle konuş', 'Kendi elin ile tutkulu bir şekilde öpüş (Korona olursanız benden değil)']

client = discord.Client()
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.bans = True

class Mesajlar(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == 782279138537898044:
            return

        if message.content.startswith('tb!yalan'):
            await message.channel.send(f'{random.choice(sorular)} Sadece 10 saniyen var.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.choice(cevaplar)
            guess = await client.wait_for('message', timeout=10.0)            
            await message.channel.send(answer)
            return


        if message.content.startswith('tb!deprem'):        
            url=('http://koeri.boun.edu.tr/rss/')
            haberler=feedparser.parse(url)
            i=0
            for x in haberler.entries:
                i+=1
                embed = discord.Embed(title='BÜYÜKLÜK / YER / ZAMAN', description=x.title)
                await message.channel.send(content=None, embed=embed)
                if i==5 :
                    break
            return

        if message.content == "tb!yazıtura":
            embed = discord.Embed(title=f'{message.author.name} parayı fırlattı.', value="⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/784106804749140081/23582839171_4e2343645d65907a8f97_512.png')
            embed.add_field(name=f'Para havada döndü veeeee {str(random.choice(yazıtura))} geldi', value="🪙")
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.channel.send (embed = embed)
            return

        if message.content.startswith ("tb!aşk"):
            x = message.content.split(" ")
            print(x[2])
            y = x[2]
            z = ""
            if y == z:
                await message.channel.send("İlk etiket ile ikinci etiket arasına boşluk koymayın. Zaten kendisi koyuyor.")
                return
            await message.channel.send ('%s ile %s arasındaki aşk :' % (x[1], x[2]) + f' Yüzde {str(random.randint(1,100))}')
            return

        if message.content.startswith ("tb!çeviri"):
            x = message.content.split(" ", 2)
            if x[1] not in LANGUAGES:
                embed = discord.Embed(title="Dil kodunu yanlış yazdınız.", description="İşte [dil kodları listesi](https://drive.google.com/file/d/17FL-LwxwXog6qLQVrm-xa7OR6WQt3IyB/view?usp=sharing).")
                embed.set_footer(text="Kodun kullanım şekli tb!çeviri <dilkodu> <çevirelecek dil>")
                await message.channel.send(embed=embed)
                return
            translate_text = translator.translate(x[2],lang_tgt=x[1])
            detect_result = translator.detect(x[2])
            embed = discord.Embed(title='Tuzlu Baklava Çeviri', value="⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/784433517614334022/ZrNeuKthBirZN7rrXPN1JmUbaG8ICy3kZSHt-WgSnREsJzo2txzCzjIoChlevMIQEAs180-rw.png')
            embed.add_field(name='Çevirilen yazı :', value=x[2], inline=False)
            embed.add_field(name='Çeviri :', value=translate_text, inline=False)
            embed.add_field(name='Çevirilen Dil :', value=LANGUAGES[detect_result[0]], inline=False)
            embed.add_field(name='Çeviri Dili :', value=LANGUAGES[x[1]], inline=False)
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.channel.send (embed = embed)
            return

        if message.content == 'tb!döviz2':
            doviz = Doviz()
            await message.channel.send(doviz.tablo())

        if message.content.startswith('tb!haber'):        
            url=('https://www.aa.com.tr/tr/rss/default?cat=guncel')
            haberler=feedparser.parse(url)
            i=0
            for x in haberler.entries:
                i+=1
                embed = discord.Embed(title=x.title, description=x.description)
                await message.channel.send(content=None, embed=embed)
                if i==5 :
                    break

        if message.content == 'tb!döviz':
            pasteURL6 = "http://tr.investing.com/currencies/usd-try"
            data6 = urlopen(Request(pasteURL6, headers={'User-Agent': 'Mozilla'})).read()
            parse6 = BeautifulSoup(data6, "html.parser" )
            for dolar in parse6.find_all('span', id="last_last"):
                liste6 = list(dolar)

            pasteURL1 = "https://tr.investing.com/currencies/chf-try"
            data1 = urlopen(Request(pasteURL1, headers={'User-Agent': 'Mozilla'})).read()
            parse1 = BeautifulSoup(data1, "html.parser" )
            for frank in parse1.find_all('span', id="last_last"):
                liste1 = list(frank)
                    
            pasteURL2 = "https://tr.investing.com/currencies/gbp-try"
            data2 = urlopen(Request(pasteURL2, headers={'User-Agent': 'Mozilla'})).read()
            parse2 = BeautifulSoup(data2, "html.parser" )
            for sterlin in parse2.find_all('span', id="last_last"):
                liste2 = list(sterlin)

            pasteURL3 = "http://tr.investing.com/currencies/eur-try"
            data3 = urlopen(Request(pasteURL3, headers={'User-Agent': 'Mozilla'})).read()
            parse3 = BeautifulSoup(data3, "html.parser" )
            for euro in parse3.find_all('span', id="last_last"):
                liste3 = list(euro)

            pasteURL4 = "https://tr.investing.com/currencies/gau-try"
            data4 = urlopen(Request(pasteURL4, headers={'User-Agent': 'Mozilla'})).read()
            parse4 = BeautifulSoup(data4, "html.parser" )
            for graltın in parse4.find_all('span', id="last_last"):
                liste4 = list(graltın)

            pasteURL5 = "https://tr.investing.com/currencies/btc-try"
            data5 = urlopen(Request(pasteURL5, headers={'User-Agent': 'Mozilla'})).read()
            parse5 = BeautifulSoup(data5, "html.parser" )
            for bitcoin in parse5.find_all('span', id="last_last"):
                liste5 = list(bitcoin)
            embed = discord.Embed(title="Güncel Dolar Kuru: " + str(liste6), description=time.strftime("%X %d/%m/%Y"))
            embed.add_field(name="Güncel Euro Kuru: " + str(liste3), value=time.strftime("%X %d/%m/%Y"))
            embed.add_field(name="Güncel Altın Kuru: " + str(liste4), value=time.strftime("%X %d/%m/%Y"))
            embed.add_field(name="Güncel Sterlin Kuru: " + str(liste2), value=time.strftime("%X %d/%m/%Y"))
            embed.add_field(name="Güncel Frank Kuru: " + str(liste1), value=time.strftime("%X %d/%m/%Y"))
            embed.add_field(name="Güncel Bitcoin Kuru: " + str(liste5), value=time.strftime("%X %d/%m/%Y"))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content.startswith('tb!bitcoin'):
            pasteURL5 = "https://tr.investing.com/currencies/btc-try"
            data5 = urlopen(Request(pasteURL5, headers={'User-Agent': 'Mozilla'})).read()
            parse5 = BeautifulSoup(data5, "html.parser" )
            for bitcoin in parse5.find_all('span', id="last_last"):
                liste5 = list(bitcoin)
            embed = discord.Embed(title="Güncel Bitcoin Kuru: " + str(liste5), description=time.strftime("%X %d/%m/%Y"))
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='Piyasaların kapalı olduğu gün ve saatlerde veri akışı bulunmamaktadır.')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779835417087311872/sorunun-cozumu-dolar-bulmak_.png')
            await message.channel.send(content=None, embed=embed)
            return

        if message.content.startswith('tb!gr altın'):
            url = "https://piyasa.paratic.com/altin/gram/"
            response = requests.get(url).content
            soup = BeautifulSoup(response,"html.parser")
            dolarveri = soup.find("div", attrs={"class":"ng_price ng_price_alis"})
            dolarveri1 = soup.find("div", attrs={"class":"ng_price ng_price_satis"})
            dolarveri2 = soup.find("div", attrs={"class":"ng_price ng_price_degisim"})
            embed = discord.Embed(title="Güncel Gram Altın Verileri: ", description="💵💵💵💵💵💵💵💵")
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='Piyasaların kapalı olduğu gün ve saatlerde veri akışı bulunmamaktadır.')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779835417087311872/sorunun-cozumu-dolar-bulmak_.png')
            embed.add_field(name=dolarveri.text, value="💵💵💵💵")
            embed.add_field(name=dolarveri1.text, value="💵💵💵💵")
            embed.add_field(name=dolarveri2.text, value="💵💵💵💵")
            await message.channel.send(content=None, embed=embed)
            return
                
        if message.content.startswith('tb!euro'):
            url = "https://piyasa.paratic.com/doviz/euro/"
            response = requests.get(url).content
            soup = BeautifulSoup(response,"html.parser")
            dolarveri = soup.find("div", attrs={"class":"ng_price ng_price_alis"})
            dolarveri1 = soup.find("div", attrs={"class":"ng_price ng_price_satis"})
            dolarveri2 = soup.find("div", attrs={"class":"ng_price ng_price_degisim"})
            embed = discord.Embed(title="Güncel Euro Verileri: ", description="💵💵💵💵💵💵💵💵")
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='Piyasaların kapalı olduğu gün ve saatlerde veri akışı bulunmamaktadır.')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779835417087311872/sorunun-cozumu-dolar-bulmak_.png')
            embed.add_field(name=dolarveri.text, value="💵💵💵💵")
            embed.add_field(name=dolarveri1.text, value="💵💵💵💵")
            embed.add_field(name=dolarveri2.text, value="💵💵💵💵")
            await message.channel.send(content=None, embed=embed)
            return
                
        if message.content.startswith('tb!sterlin'):
            url = "https://piyasa.paratic.com/doviz/sterlin/"
            response = requests.get(url).content
            soup = BeautifulSoup(response,"html.parser")
            dolarveri = soup.find("div", attrs={"class":"ng_price ng_price_alis"})
            dolarveri1 = soup.find("div", attrs={"class":"ng_price ng_price_satis"})
            dolarveri2 = soup.find("div", attrs={"class":"ng_price ng_price_degisim"})
            embed = discord.Embed(title="Güncel Sterlin Verileri: ", description="💵💵💵💵💵💵💵💵")
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='Piyasaların kapalı olduğu gün ve saatlerde veri akışı bulunmamaktadır.')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779835417087311872/sorunun-cozumu-dolar-bulmak_.png')
            embed.add_field(name=dolarveri.text, value="💵💵💵💵")
            embed.add_field(name=dolarveri1.text, value="💵💵💵💵")
            embed.add_field(name=dolarveri2.text, value="💵💵💵💵")
            await message.channel.send(content=None, embed=embed)
            return

        if message.content.startswith('tb!frank'):
            url = "https://piyasa.paratic.com/doviz/isvicre-frangi/"
            response = requests.get(url).content
            soup = BeautifulSoup(response,"html.parser")
            dolarveri = soup.find("div", attrs={"class":"ng_price ng_price_alis"})
            dolarveri1 = soup.find("div", attrs={"class":"ng_price ng_price_satis"})
            dolarveri2 = soup.find("div", attrs={"class":"ng_price ng_price_degisim"})
            embed = discord.Embed(title="Güncel Frank Verileri: ", description="💵💵💵💵💵💵💵💵")
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='Piyasaların kapalı olduğu gün ve saatlerde veri akışı bulunmamaktadır.')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779835417087311872/sorunun-cozumu-dolar-bulmak_.png')
            embed.add_field(name=dolarveri.text, value="💵💵💵💵")
            embed.add_field(name=dolarveri1.text, value="💵💵💵💵")
            embed.add_field(name=dolarveri2.text, value="💵💵💵💵")
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == "euro kaç tl":
            pasteURL = "http://tr.investing.com/currencies/eur-try"
            data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
            parse = BeautifulSoup(data, "html.parser" )
            for dolar in parse.find_all('span', id="last_last"):
                liste = list(dolar)
                await message.channel.send("Güncel Euro Kuru: " + str(liste))
            return


        if message.content == "dolar kaç tl":
            pasteURL = "http://tr.investing.com/currencies/usd-try"
            data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
            parse = BeautifulSoup(data, "html.parser" )
            for dolar in parse.find_all('span', id="last_last"):
                liste = list(dolar)
                await message.channel.send("Güncel Dolar Kuru: " + str(liste))
            return

        if message.content.startswith('tb!dolar'):
            url = "https://piyasa.paratic.com/doviz/dolar/"
            response = requests.get(url).content
            soup = BeautifulSoup(response,"html.parser")
            dolarveri = soup.find("div", attrs={"class":"ng_price ng_price_alis"})
            dolarveri1 = soup.find("div", attrs={"class":"ng_price ng_price_satis"})
            dolarveri2 = soup.find("div", attrs={"class":"ng_price ng_price_degisim"})
            embed = discord.Embed(title="Güncel Dolar Verileri: ", description="💵💵💵💵💵💵💵💵")
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='Piyasaların kapalı olduğu gün ve saatlerde veri akışı bulunmamaktadır.')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779835417087311872/sorunun-cozumu-dolar-bulmak_.png')
            embed.add_field(name=dolarveri.text, value="💵💵💵💵")
            embed.add_field(name=dolarveri1.text, value="💵💵💵💵")
            embed.add_field(name=dolarveri2.text, value="💵💵💵💵")
            await message.channel.send(content=None, embed=embed)
            return   

        if message.content == 'tb!korona TR':
            tr_cases = covid.get_status_by_country_name("turkey")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Türkiye Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779984520555921439/800px-Flag_of_Turkey.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona US':
            tr_cases = covid.get_status_by_country_name("usa")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Amerika Birleşik Devletleri Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779983844363206666/1200px-Flag_of_the_United_States.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona DE':
            tr_cases = covid.get_status_by_country_name("germany")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Almanya Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779983567123251201/Flag_of_Germany.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona AZ':
            tr_cases = covid.get_status_by_country_name("azerbaijan")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Azerbaycan Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779982815751962664/Flag_of_Azerbaijan.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona BE':
            tr_cases = covid.get_status_by_country_name("belgium")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Belçika Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779982565041635348/1.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona BR':
            tr_cases = covid.get_status_by_country_name("brazil")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Brezilya Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779980219662467092/flag-400.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona AM':
            tr_cases = covid.get_status_by_country_name("armenia")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Ermenistan Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779979557906284544/1200px-Flag_of_Armenia.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona FR':
            tr_cases = covid.get_status_by_country_name("france")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Fransa Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779977510061604874/1200px-Flag_of_France.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona FI':
            tr_cases = covid.get_status_by_country_name("finland")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Finlandiya Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779976762045890560/flag-400.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona NL':
            tr_cases = covid.get_status_by_country_name("netherlands")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Hollanda Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779976507799765002/flag-of-the-netherlands.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona MX':
            tr_cases = covid.get_status_by_country_name("mexico")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Meksika Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779976164197269504/flag-of-mexico.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona PT':
            tr_cases = covid.get_status_by_country_name("portugal")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Portekiz Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779975764702527519/1280px-Flag_of_Portugal.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona RU':
            tr_cases = covid.get_status_by_country_name("russia")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Rusya Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779974726658293760/1200px-Flag_of_Russia.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona IT':
            tr_cases = covid.get_status_by_country_name("italy")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="İtalya Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779972854384295946/italy-flag__19720.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona SE':
            tr_cases = covid.get_status_by_country_name("sweden")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="İsveç Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779971932220817408/sweden.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona CH':
            tr_cases = covid.get_status_by_country_name("switzerland")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="İsviçre Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779971550665244682/switzerland-flag-small.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona GB':
            tr_cases = covid.get_status_by_country_name("uk")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Birleşmiş Krallık Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779970537266348032/7-2-united-kingdom-flag-png-image.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona EU':
            tr_cases = covid.get_status_by_country_name("europe")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Avrupa Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779968912929718272/european-union-eu-large-country-flag-5-x-3-.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona DÜNYA':
            tr_cases = covid.get_status_by_country_name("world")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Dünya Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779981258322083890/3uCD4xxY_400x400.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona IN':
            tr_cases = covid.get_status_by_country_name("india")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Hindistan Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779967112617656340/288_2.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona GR':
            tr_cases = covid.get_status_by_country_name("greece")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Yunanistan Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779966424500273182/Flag_of_Greece.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona JP':
            tr_cases = covid.get_status_by_country_name("japan")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Japonya Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779965926111445022/682baee52deeb0bfb7e2356c4e711edf.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content == 'tb!korona BG':
            tr_cases = covid.get_status_by_country_name("bulgaria")
            tr_onaylanmış = (tr_cases['confirmed'])
            tr_ölümler = (tr_cases['deaths'])
            tr_iyileşenler = (tr_cases['recovered'])
            tr_kritik = (tr_cases['critical'])
            tr_toplam_test = (tr_cases['total_tests'])
            tr_popülasyon = (tr_cases['population'])

            embed = discord.Embed(title="Bulgaristan Koronavirus Verileri", description="Kaynak worlometers'dir.")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779828797099999232/bulgarbayrag.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(text='0 olan veriler bilinmeyen verilerdir.')
            embed.add_field(name="Toplam Vaka Sayısı : ",  value = str(tr_onaylanmış))
            embed.add_field(name="Toplam Ölüm Sayısı : ",  value = str(tr_ölümler))
            embed.add_field(name="Toplam İyileşen Sayısı : ",  value = str(tr_iyileşenler))
            embed.add_field(name="Toplam Kritik Sayısı : ",  value = str(tr_kritik))
            embed.add_field(name="Toplam Test Sayısı : ",  value = str(tr_toplam_test))
            embed.add_field(name="Toplam İnsan Sayısı : ",  value = str(tr_popülasyon))
            await message.channel.send(content=None, embed=embed)
            return

        if message.content.startswith('tb!hdurumu'):
            x = message.content.split(" ")
            hava = HavaDurumu(x[1], 'Merkez')
            await message.channel.send (hava.tablo())
            return

        if message.content.startswith('tb!doğruluk'):
            await message.channel.send(random.choice(truth_items))
            return

        if message.content.startswith('tb!cesaret'):
            await message.channel.send(random.choice(dare_items))
            return

        if message.content == 'tb!zar':
            embed = discord.Embed(title=f'{message.author.name} zar attı.', value="⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇")
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779822209769275412/zar1.gif')
            embed.add_field(name=f'Zar attın ve gelen sayı : {str(random.randint(1,6))}', value="1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣")
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.channel.send (embed = embed)

        if message.content.startswith('tb!yapımcı'):
            await message.channel.send('<@619600347744436254>')
            await message.channel.send('Enes Aslan #3380')
            return

        if message.content == 'tb!davet':
            await message.channel.send ('https://discord.com/api/oauth2/authorize?client_id=770241810827575307&permissions=8&scope=bot')
            return

        if message.content == 'tb!sunucu':
            await message.channel.send('discord.gg/Uw9Js5FxaW')
            return

        if message.content.startswith("tb!reddituser"):
            veri = message.content.split(" ")
            zaman = reddit.redditor(veri[1]).created_utc  
            name = reddit.redditor(veri[1]).name
            ids = reddit.redditor(veri[1]).id
            link_karma = reddit.redditor(veri[1]).link_karma
            comment_karma = reddit.redditor(veri[1]).comment_karma
            total_karma = link_karma + comment_karma
            embed = discord.Embed(title=name, description=ids, colour=discord.Colour.from_rgb(255, 69, 0))
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/783967501389135892/redditlogo.png')
            embed.add_field(name='Hesabın Açılış Tarihi:', value=datetime.utcfromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S') + ' UTC', inline=False)
            embed.add_field(name="Link Karma:", value=link_karma, inline=False)
            embed.add_field(name="Comment Karma:", value=comment_karma, inline=False)
            embed.add_field(name="Toplam Karma:", value=total_karma, inline=False)
            await message.channel.send(embed=embed)
            return

        if message.content.startswith("tb!subnew"):
            sbreddit = message.content.split(" ")
            subreddit_new = reddit.subreddit(sbreddit[1]).new(limit=5)
            for post in subreddit_new:
                embed = discord.Embed(title=post.title, description=post.id, colour=discord.Colour.from_rgb(255, 69, 0))
                embed.add_field(name="Gönderi Sahibi:", value=post.author, inline=False)
                embed.add_field(name='Gönderinin Atılış Tarihi:', value=datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S') + ' UTC', inline=False)
                embed.add_field(name="Upvote Oranı:", value=post.upvote_ratio, inline=False)
                embed.add_field(name="Gönderi Skoru:", value=post.score, inline=False)
                embed.add_field(name="Gönderi URLsi", value=post.url, inline=False)
                await message.channel.send(embed=embed)
            return

        if message.content.startswith("tb!subhot"):
            sbreddit = message.content.split(" ")
            subreddit_new = reddit.subreddit(sbreddit[1]).hot(limit=5)
            for post in subreddit_new:
                embed = discord.Embed(title=post.title, description=post.id, colour=discord.Colour.from_rgb(255, 69, 0))
                embed.add_field(name="Gönderi Sahibi:", value=post.author, inline=False)
                embed.add_field(name='Gönderinin Atılış Tarihi:', value=datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S') + ' UTC', inline=False)
                embed.add_field(name="Upvote Oranı:", value=post.upvote_ratio, inline=False)
                embed.add_field(name="Gönderi Skoru:", value=post.score, inline=False)
                embed.add_field(name="Gönderi URLsi", value=post.url, inline=False)
                await message.channel.send(embed=embed)
            return

        if message.content.startswith("tb!subinfo"):
            sbreddit = message.content.split(" ")
            subreddit = reddit.subreddit(sbreddit[1])
            embed = discord.Embed(title=subreddit.display_name, description=subreddit.description, colour=discord.Colour.from_rgb(255, 69, 0))
            embed.add_field(name="Üye Sayısı:", value=subreddit.subscribers, inline=False)
            embed.add_field(name='Sayfanın Kuruluş Tarihi:', value=datetime.utcfromtimestamp(subreddit.created_utc).strftime('%Y-%m-%d %H:%M:%S') + ' UTC', inline=False)
            await message.channel.send(embed=embed)
            return

        if message.content == "tb!meme":
            memepages = reddit.subreddit("meme+memes").random()
            embed = discord.Embed(title='Random atman için 3 saniyen var.', value="⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇")
            embed.add_field(name='Gönderen :', value=memepages.author, inline=True)
            embed.add_field(name='Başlık :', value=memepages.title, inline=True)
            embed.set_image(url=memepages.url)
            await message.channel.send (embed = embed)

        if message.content.startswith("tb!tkm"):
            hamle1 = message.content.split(" ")
            hamleler = ['taş', "kağıt", "makas"]
            hamle2 = hamleler[random.randint(0,2)]
            await message.channel.send("Benim hamlem " + hamle2)
            if hamle1[1] == hamle2:
                await message.channel.send("Berabere!")
            elif hamle1[1] == "taş":
                if hamle2 == "kağıt":
                    await message.channel.send('Tuzlu Baklava Kazandı!')
                    return
                else:
                    await message.channel.send(f'{message.author} Kazandı!')
                    return
            elif hamle1[1] == "kağıt":
                if hamle2 == "makas":
                    await message.channel.send('Tuzlu Baklava Kazandı!')
                    return
                else:
                    await message.channel.send(f'{message.author} Kazandı!')
                    return
            elif hamle1[1] == "makas":
                if hamle2 == "taş":
                    await message.channel.send('Tuzlu Baklava Kazandı!')
                    return
                else:
                    await message.channel.send(f'{message.author} Kazandı!')  
                    return
            else:
                await message.channel.send("Sanırım hamleni yanlış yazdın. Unutma hamle küçük harf ile başlayacak.")

        if message.content == "tb!biyoloji":
            if message.channel.id == 626290531827449856:
                await message.channel.send("""
            > Ders: **BİYOLOJİ**

    **ID:** 3206022147
    **ŞiFRE:** Bhyal.2020

    **İyi** dersler**.** :slight_smile:
            """)

        if message.content == "tb!edebiyat":
            if message.channel.id == 626290531827449856:
                await message.channel.send("""
            > Ders: **EDEBİYAT**

    **ID:** 3736324469
    **ŞiFRE:** Bhyal.2020

    **İyi** dersler**.** :slight_smile:
            """)

        if message.content == "tb!matematik":
            if message.channel.id == 626290531827449856:
                await message.channel.send("""
            > Ders: **MATEMATİK**

    **ID:** 9105319455
    **ŞiFRE:** Bhyal.2020

    **İyi** dersler**.** :slight_smile:
            """)

        if message.content == "tb!fizik":
            if message.channel.id == 626290531827449856:
                await message.channel.send("""
            > Ders: **FİZİK**

    **ID:** 6171286202
    **ŞiFRE:** Bhyal.2020

    **İyi** dersler**.** :slight_smile:
            """)

        if message.content == "tb!tarih":
            if message.channel.id == 626290531827449856:
                await message.channel.send("""
            > Ders: **TARİH**

    **ID:** 9158178363
    **ŞiFRE:** Bhyal.2020

    **İyi** dersler**.** :slight_smile:
            """)

        if message.content == "tb!coğrafya":
            if message.channel.id == 626290531827449856:
                await message.channel.send("""
            > Ders: **COĞRAFYA**

    **ID:** 9710660759
    **ŞiFRE:** Bhyal.2020

    **İyi** dersler**.** :slight_smile:
            """)

        if message.content == "tb!din":
            if message.channel.id == 626290531827449856:
                await message.channel.send("""
            > Ders: **DİN**

    **ID:** 2397793797
    **ŞiFRE:** Bhyal.2020

    **İyi** dersler**.** :slight_smile:
            """)

        if message.content == "tb!bilişim":
            if message.channel.id == 626290531827449856:
                await message.channel.send("""
            > Ders: **BİLİŞİM**

    **ID:** 6396985435
    **ŞiFRE:** Bhyal.2020

    **İyi** dersler**.** :slight_smile:
            """)

        if message.content == "tb!resim":
            if message.channel.id == 626290531827449856:
                await message.channel.send("""
            > Ders: **RESİM**

    **ID:** 7744885665
    **ŞiFRE:** Bhyal.2020

    **İyi** dersler**.** :slight_smile:
            """)

        if message.content == "tb!felsefe":
            if message.channel.id == 626290531827449856:
                await message.channel.send("""
            > Ders: **FELSEFE**

    **ID:** 7237089775
    **ŞiFRE:** Bhyal.2020

    **İyi** dersler**.** :slight_smile:
            """)

        if message.content == "tb!çizelge":
            await message.channel.send(file=discord.File(os.path.join(os.path.dirname(__file__), 'çizelge.png')))

        if message.content.startswith("tb!tekrarla"):
            bölüm = message.content.split(" ",1)
            await message.channel.send(bölüm[1])

        if message.content.startswith("tb!wiki"):
            bölüm = message.content.split(" ",1)
            wikipedia.set_lang("tr")
            await message.channel.send(wikipedia.summary(bölüm[1])[0:2000])
            await message.channel.send(wikipedia.summary(bölüm[1])[2000:4000])
            await message.channel.send(wikipedia.summary(bölüm[1])[4000:6000])

        if message.content.startswith("tb!hdsondurum"):
            bölüm = message.content.split(" ")
            bölüm1 = bölüm[1].replace("ı", "i")
            bölüm1 = bölüm[1].replace("ü", "u")
            bölüm1 = bölüm[1].replace("ş", "s")
            bölüm1 = bölüm[1].replace("ç", "c")
            bölüm1 = bölüm[1].replace("ö", "o")
            bölüm1 = bölüm[1].replace("ğ", "g")
            url = ("https://www.mgm.gov.tr/sunum/sondurum-show-2.aspx?m=" + bölüm1.upper() + "&rC=111&rZ=fff")
            await message.channel.send(url)

        if message.content.startswith("tb!hd5günlük"):
            bölüm = message.content.split(" ")
            bölüm1 = bölüm[1].replace("ı", "i")
            bölüm1 = bölüm[1].replace("ü", "u")
            bölüm1 = bölüm[1].replace("ş", "s")
            bölüm1 = bölüm[1].replace("ç", "c")
            bölüm1 = bölüm[1].replace("ö", "o")
            bölüm1 = bölüm[1].replace("ğ", "g")
            url = ("https://www.mgm.gov.tr/sunum/tahmin-show-2.aspx?m=" + bölüm1.upper() + "&basla=1&bitir=5")
            await message.channel.send(url)

        if message.content.startswith("tb!insta"):
            username = message.content.split(" ")
            profile = Profile.from_username(L.context, username[1])
            gizlilik = "Gizli" if profile.is_private == True else "Gizli Değil"
            onay = "Onaylı" if profile.is_verified == True else "Onaylı Değil"
            embed = discord.Embed(title=profile.full_name, value="\u200b")
            embed.add_field(name='Takipçi Sayısı :', value=profile.followers, inline=True)
            embed.add_field(name='Takip edilen sayısı :', value=profile.followees, inline=True)
            embed.add_field(name='Biografi :', value=profile.biography, inline=True)
            embed.add_field(name='Gizli mi? :', value=gizlilik, inline=True)
            embed.add_field(name='IGTV sayısı :', value=profile.igtvcount, inline=True)
            embed.add_field(name='Onaylı mı? :', value=onay, inline=True)
            embed.set_footer(text="https://www.instagram.com/" + username[1])
            embed.set_thumbnail(url=profile.profile_pic_url)
            await message.channel.send (embed = embed)

def setup(bot):
	bot.add_cog(Mesajlar(bot))