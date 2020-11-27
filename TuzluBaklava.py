import discord
import random
from DovizKurlari import DovizKurlari
import feedparser
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from discord.ext import commands, tasks
from itertools import cycle
import time
from covid import Covid
from KekikSpatula import Doviz
from KekikSpatula import HavaDurumu

ornek = DovizKurlari()

covid = Covid(source="worldometers")
covid.get_data()

cevaplar = ['Doğru \N{WHITE HEAVY CHECK MARK}', 'Yalan \N{CROSS MARK}']

etiket = '<@770241810827575307>'

truth_items = ['Telefonunda en son attığın mesaj nedir ?', 'En son söylediğin yalan nedir?', 'Şişeden bir cin çıksa üç dileğin ne olurdu?', 'Şimdiye kadar bir başkasına söylediğin en acımasızca şey neydi?', 'Dünyadaki herhangi birini Türkiye’nin başkanı yapabilseydin bu kim olurdu?', 'Bir aynanın önünde yaptığın en çılgınca şey nedir?', 'Bu hayatta en çok kimi kıskanıyorsun?', 'Bu hayatta en çok kimi kıskanıyorsun?', 'Şimdiye kadar bir başkasına söylediğin en acımasızca şey neydi?', 'Hangi ünlü yerinde olmak isterdin?', 'Ömrünün sonuna kadar dinlemek için tek bir şarkı seçebilecek olsaydın hangisini seçerdin ?', 'Dışarıda yaşadığın en utanç verici an neydi ?', 'Tuvaletini yaparken düşündüğün bir kaç şey söyler misin ?', 'Sokakta yere bir şey düşürdüğünde hiç bir şey olmamış gibi alıp ağzına attın mı ?', 'Bir sabah karşı cins olarak uyansaydın ilk yapacağın şey ne olurdu ?', 'Eğer birden fazla eşle evlenebilseydin ? Kimleri seçerdin ?', 'Telefonunda arattığın en son şey nedir ?', 'Duştayken işer misin ?', 'En kötü huyun nedir ?', 'En gıcık olduğun şey nedir ?', 'Hiç aldatıldın mı ?', 'Hiç osurup suçu başkasına attın mı ?'
, 'Hayalindeki kız/erkek nasıl biri ?', 'Herhangi bir ünlü ile evlenseydin, kim olurdu?', 'Yaptığın en çapkın şey nedir?', 'Bir sınavdan aldığın en kötü puan neydi?', 'Sınıfımızdaki en iyi 5 erkek kim? Onları sırala.', 'Hiç yerden bir şey yedin mi?', 'Hiç tabağını yaladın mı?', 'Hiç terinin tadına baktın mı?', 'Hayatının en büyük hatası neydi?', 'Hiç geçmişte bir şey çaldın mı?', 'Kaç kez öpüştün?', 'Hangi garip kokuyu seversin?', 'Birisi kapınızın önünde 2.000.000 TL ile dolu bir çanta bırakırsa ne yapardınız?', 'Eşinizi tek bir soruya göre seçmek zorunda olsaydınız, hangi soruyu sorardınız?', 'Kendinize özel bir organ tasarlayabilseydin, hangi organ ve vücudun neresinde olurdu?', 'Yaptığınız en iğrenç şaka nedir?', 'İsminizi değiştirmek zorunda olsaydınız, yeni ismin ne olurdu?', 'Yakalanmadan söylediğin en büyük yalan nedir?', 'Bir ünlü Instagram’da seni takip etseydi bu ünlünün kim olmasını isterdin?', 'Erkek arkadaşının ya da kız arkadaşının seninle aynı üniversiteye gitmesini ister misin?']

sorular = ['Saklamanız söylendiği bir sırrı hiç anlattınız mı?', 'Hiç en iyi arkadaşına yalan söyledin mi?', ' Size 5000 lira verilse, oyunuzu satar mısınız?', 'Toplum baskısı, dini kurallar ve cezalar olmasaydı, adam öldürür müydünüz?', 'Sinirlendiğinde ortalığı yakıp yıkıp, insanlara sesini yükselttiğin hatta ve hatta küfrettiğin oluyor mu?', 'Arkadaşlarınla buluşmak istemediğinde onlara sık sık yalan söylediğin oluyor mu?', 'Sevdiğin insanla ailen kesinlikle evlenmeni istemiyor. Onları dinler misin?', 'En yakın arkadaşının eski sevgilisiyle evlenir miydin?', 'Birine aşık olduğun genelde ilk adımı karşındaki kişiden mi beklersin?', 'En iyi arkadaşına bile söylemediğin sırların var mı?']

dare_items = ['Yeri öp', 'Sarhoş taklidi yap', 'Birini ara ve karadeniz şivesiyle konuş', 'Kendi elin ile tutkulu bir şekilde öpüş (Korona olursanız benden değil)']

türkisj_mizha = ['Ben hikâye yazarım Ebru Destan.', 'Yılanlardan korkma, yılmayanlardan kork.', 'Geçen gün taksi çevirdim hala dönüyor.', 'u/EnesAslan1', 'Bekarlık sultanlıktır, fakat er ya da geç demokrasiye geçilir', ' Aklımı kaçırdım, 100.000 TL fidye istiyorum.', 'Ben ekmek yedim Will Smith']

status = cycle(['$yardım', 'Bot biraz yavaş'])

ğ = (int(float(ornek.DegerSor("EUR","ForexBuying"))))

ü = 2324

ö = (ü //ğ)

ç = (int(float(ornek.DegerSor("USD","ForexBuying"))))

q = (int(float(ornek.DegerSor("CHF","ForexBuying"))))

e = (ü //q)

f = (ğ // q)

client = discord.Client()

@client.event
async def on_ready():
    change_status.start()
    print('{0.user} olarak giriş yapıldı.'.format(client))

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author.id == client.user.id:
        return

    if message.content.startswith('$yalan'):
        await message.channel.send(f'{random.choice(sorular)} Sadece 10 saniyen var.')

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        answer = random.choice(cevaplar)
        guess = await client.wait_for('message', timeout=10.0)            
        await message.channel.send(answer)

    if message.content.startswith('$deprem'):        
        url=('http://koeri.boun.edu.tr/rss/')
        haberler=feedparser.parse(url)
        i=0
        for x in haberler.entries:
            i+=1
            embed = discord.Embed(title='BÜYÜKLÜK / YER / ZAMAN', description=x.title)
            await message.channel.send(content=None, embed=embed)
            if i==5 :
                break

    if message.content == '$döviz2':
        doviz = Doviz()
        await message.channel.send(doviz.tablo())

    if message.content == "sa":
        await message.channel.send("cami mi lan burası")

    if message.content == "napim":
        with open('napim.mp4', 'rb') as fp:
            await message.channel.send(file=discord.File(fp, 'napim2.mp4'))

    if message.content == "bruh":
        await message.add_reaction("🇧")
        await message.add_reaction("🇷")
        await message.add_reaction("🇺")
        await message.add_reaction("🇭")
        with open('tenor.gif', 'rb') as fp:
            await message.channel.send(file=discord.File(fp, 'new_filename.gif'))

    if message.content.startswith('$haber'):        
        url=('https://www.aa.com.tr/tr/rss/default?cat=guncel')
        haberler=feedparser.parse(url)
        i=0
        for x in haberler.entries:
            i+=1
            embed = discord.Embed(title=x.title, description=x.description)
            await message.channel.send(content=None, embed=embed)
            if i==5 :
                break

    if message.content == '$döviz':
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

    if message.content.startswith('$bitcoin'):
        pasteURL = "https://tr.investing.com/currencies/btc-try"
        data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
        parse = BeautifulSoup(data, "html.parser" )
        for dolar in parse.find_all('span', id="last_last"):
            liste = list(dolar)
            embed = discord.Embed(title="Güncel Bitcoin Kuru: " + str(liste), description=time.strftime("%X %d/%m/%Y"))
            await message.channel.send(content=None, embed=embed)

    if message.content.startswith('$gr altın'):
        pasteURL = "https://tr.investing.com/currencies/gau-try"
        data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
        parse = BeautifulSoup(data, "html.parser" )
        for dolar in parse.find_all('span', id="last_last"):
            liste = list(dolar)
            embed = discord.Embed(title="Güncel Gram Altın Kuru: " + str(liste), description=time.strftime("%X %d/%m/%Y"))
            await message.channel.send(content=None, embed=embed)
            
    if message.content.startswith('$euro'):
        pasteURL = "http://tr.investing.com/currencies/eur-try"
        data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
        parse = BeautifulSoup(data, "html.parser" )
        for dolar in parse.find_all('span', id="last_last"):
            liste = list(dolar)
            embed = discord.Embed(title="Güncel Euro Kuru: " + str(liste), description=time.strftime("%X %d/%m/%Y"))
            await message.channel.send(content=None, embed=embed)
            
    if message.content.startswith('$sterlin'):
        pasteURL = "https://tr.investing.com/currencies/gbp-try"
        data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
        parse = BeautifulSoup(data, "html.parser" )
        for dolar in parse.find_all('span', id="last_last"):
            liste = list(dolar)
            embed = discord.Embed(title="Güncel Sterlin Kuru: " + str(liste), description=time.strftime("%X %d/%m/%Y"))
            await message.channel.send(content=None, embed=embed)

    if message.content.startswith('$frank'):
        pasteURL = "https://tr.investing.com/currencies/chf-try"
        data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
        parse = BeautifulSoup(data, "html.parser" )
        for dolar in parse.find_all('span', id="last_last"):
            liste = list(dolar)
            embed = discord.Embed(title="Güncel Frank Kuru: " + str(liste), description=time.strftime("%X %d/%m/%Y"))
            await message.channel.send(content=None, embed=embed)

    if message.content == "euro kaç tl":
        pasteURL = "http://tr.investing.com/currencies/eur-try"
        data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
        parse = BeautifulSoup(data, "html.parser" )
        for dolar in parse.find_all('span', id="last_last"):
            liste = list(dolar)
            await message.channel.send("Güncel Euro Kuru: " + str(liste))


    if message.content == "dolar kaç tl":
        pasteURL = "http://tr.investing.com/currencies/usd-try"
        data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
        parse = BeautifulSoup(data, "html.parser" )
        for dolar in parse.find_all('span', id="last_last"):
            liste = list(dolar)
            await message.channel.send("Güncel Dolar Kuru: " + str(liste))

    if message.content.startswith('$dolar'):
        pasteURL = "http://tr.investing.com/currencies/usd-try"
        data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
        parse = BeautifulSoup(data, "html.parser" )
        for dolar in parse.find_all('span', id="last_last"):
            liste = list(dolar)
            embed = discord.Embed(title="Güncel Dolar Kuru: " + str(liste), description=time.strftime("%X %d/%m/%Y"))
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779835417087311872/sorunun-cozumu-dolar-bulmak_.png')
            await message.channel.send(content=None, embed=embed)

    if message.content == '$korona TR':
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

    if message.content == '$korona US':
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

    if message.content == '$korona DE':
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

    if message.content == '$korona AZ':
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

    if message.content == '$korona BE':
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

    if message.content == '$korona BR':
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

    if message.content == '$korona AM':
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

    if message.content == '$korona FR':
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

    if message.content == '$korona FI':
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

    if message.content == '$korona NL':
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

    if message.content == '$korona MX':
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

    if message.content == '$korona PT':
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

    if message.content == '$korona RU':
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

    if message.content == '$korona IT':
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

    if message.content == '$korona SE':
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

    if message.content == '$korona CH':
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

    if message.content == '$korona GB':
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

    if message.content == '$korona EU':
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

    if message.content == '$korona DÜNYA':
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

    if message.content == '$korona IN':
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

    if message.content == '$korona GR':
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

    if message.content == '$korona JP':
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

    if message.content == '$korona BG':
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

    if message.content.startswith('$hdurumu İST'):
        hava = HavaDurumu('İstanbul', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu AĞR'):
        hava = HavaDurumu('Ağrı', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu BURDUR'):
        hava = HavaDurumu('Burdur', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu SİV'):
        hava = HavaDurumu('Sivas', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ADA'):
        hava = HavaDurumu('Adana', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ANK'):
        hava = HavaDurumu('Ankara', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ANT'):
        hava = HavaDurumu('Antalya', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu AYD'):
        hava = HavaDurumu('Aydın', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu BAL'):
        hava = HavaDurumu('Balıkesir', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu BUR'):
        hava = HavaDurumu('Bursa', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu DEN'):
        hava = HavaDurumu('Denizli', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu DİY'):
        hava = HavaDurumu('Diyarbakır', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ERZ'):
        hava = HavaDurumu('Erzurum', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ESK'):
        hava = HavaDurumu('Eskişehir', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu GAZ'):
        hava = HavaDurumu('Gaziantep', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu HAT'):
        hava = HavaDurumu('Hatay', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu İZM'):
        hava = HavaDurumu('İzmir', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu KAH'):
        hava = HavaDurumu('Kahramanmaraş', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu KAY'):
        hava = HavaDurumu('Kayseri', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu KOC'):
        hava = HavaDurumu('Kocaeli', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu KON'):
        hava = HavaDurumu('Konya', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu MAL'):
        hava = HavaDurumu('Malatya', 'Merkez')        
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu MAN'):
        hava = HavaDurumu('Manisa', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu MAR'):
        hava = HavaDurumu('Mardin', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu MER'):
        hava = HavaDurumu('Mersin', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu MUĞ'):
        hava = HavaDurumu('Muğla', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ORD'):
        hava = HavaDurumu('Ordu', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu SAK'):
        hava = HavaDurumu('Sakarya', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu SAM'):
        hava = HavaDurumu('Samsun', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ŞAN'):
        hava = HavaDurumu('Şanlıurfa', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu TEK'):
        hava = HavaDurumu('Tekirdağ', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu TRA'):
        hava = HavaDurumu('Trabzon', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu VAN'):
        hava = HavaDurumu('Van', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ZON'):
        hava = HavaDurumu('Zonguldak', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ADI'):
        hava = HavaDurumu('Adıyaman', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu AFY'):
        hava = HavaDurumu('Afyonkarahisar', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu AMA'):
        hava = HavaDurumu('Amasya', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ART'):
        hava = HavaDurumu('Artvin', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu BİL'):
        hava = HavaDurumu('Bilecik', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu BİN'):
        hava = HavaDurumu('Bingöl', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu BİT'):
        hava = HavaDurumu('Bitlis', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu BOL'):
        hava = HavaDurumu('Bolu', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ÇAN'):
        hava = HavaDurumu('Çanakkale', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ÇANK'):
        hava = HavaDurumu('Çankırı', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ÇOR'):
        hava = HavaDurumu('Çorum', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu EDİ'):
        hava = HavaDurumu('Edirne', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ELA'):
        hava = HavaDurumu('Elazığ', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ERZİ'):
        hava = HavaDurumu('Erzincan', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu GİR'):
        hava = HavaDurumu('Giresun', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu GÜM'):
        hava = HavaDurumu('Gümüşhane', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu HAK'):
        hava = HavaDurumu('Hakkari', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ISP'):
        hava = HavaDurumu('Isparta', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu KAR'):
        hava = HavaDurumu('Kars', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$hdurumu ARD'):
        hava = HavaDurumu('Ardahan', 'Merkez')
        await message.channel.send (hava.tablo())

    if message.content.startswith('$doğruluk'):
        await message.channel.send(random.choice(truth_items))

    if message.content.startswith('$türksihj-mizha'):
        await message.channel.send(random.choice(türkisj_mizha))

    if message.content.startswith('$cesaret'):
        await message.channel.send(random.choice(dare_items))

    if message.content == '$zar':
        embed = discord.Embed(title=f'{message.author.name} zar attı.', value="⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇")
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/771298832650338356/779822209769275412/zar1.gif')
        embed.add_field(name=f'Zar attın ve gelen sayı : {str(random.randint(1,6))}', value="1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣")
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        await message.channel.send (embed = embed)

    if message.content.startswith('$asgari maaş IE'):
        await message.channel.send("İRLANDA ASGARİ MAAŞI= 1658 Euro" )
        await message.channel.send("İRLANDA TL BAZINDAN ASGARİ MAAŞI= "+ str(1658 *ğ))
        await message.channel.send("İRLANDA ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(1658 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş NL'):
        await message.channel.send("HOLLANDA ASGARİ MAAŞI= 1680 Euro" )
        await message.channel.send("HOLLANDA TL BAZINDAN ASGARİ MAAŞI= "+ str(1680 *ğ))
        await message.channel.send("HOLLANDA ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(1680 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş FR'):
        await message.channel.send("FRANSA ASGARİ MAAŞI= 1539 Euro" )
        await message.channel.send("FRANSA TL BAZINDAN ASGARİ MAAŞI= "+ str(1539 *ğ))
        await message.channel.send("FRANSA ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(1539 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş DE'):
        await message.channel.send("ALMANYA ASGARİ MAAŞI= 1498 Euro" )
        await message.channel.send("ALMANYA TL BAZINDAN ASGARİ MAAŞI= "+str(1498 *ğ))
        await message.channel.send("ALMANYA ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(1498 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş BE'):
        await message.channel.send("BELÇİKA ASGARİ MAAŞI= 1600 Euro" )
        await message.channel.send("BELÇİKA TL BAZINDAN ASGARİ MAAŞI= "+str(1600 *ğ))
        await message.channel.send("BELÇİKA ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(1600 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş IT'):
        await message.channel.send("İTALYA ASGARİ MAAŞI= 1376 Euro" )
        await message.channel.send("İTALYA TL BAZINDAN ASGARİ MAAŞI= "+str(1376 *ğ))
        await message.channel.send("İTALYA ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(1376 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş BG'):
        await message.channel.send("BULGARİSTAN ASGARİ MAAŞI= 312 Euro" )
        await message.channel.send("BULGARİSTAN TL BAZINDAN ASGARİ MAAŞI= "+str(312 *ğ))
        await message.channel.send("BULGARİSTAN ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(312 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş GR'):
        await message.channel.send("YUNANİSTAN ASGARİ MAAŞI= 758 Euro" )
        await message.channel.send("YUNANİSTAN TL BAZINDAN ASGARİ MAAŞI= "+str(758 *ğ))
        await message.channel.send("YUNANİSTAN ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(758 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş AM'):
        await message.channel.send("ERMENİSTAN ASGARİ MAAŞI= 115 Euro / 55.499 Ermenistan Dramı" )
        await message.channel.send("ERMENİSTAN TL BAZINDAN ASGARİ MAAŞI= "+str(115 *ğ))
        await message.channel.send("ERMENİSTAN ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(115 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş GE'):
        await message.channel.send("GÜRCİSTAN ASGARİ MAAŞI= 85 Euro / 326 Gel" )
        await message.channel.send("GÜRCİSTAN TL BAZINDAN ASGARİ MAAŞI= "+str(85 *ğ))
        await message.channel.send("GÜRCİSTAN ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(85 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş DK'):
        await message.channel.send("DANİMARKA ASGARİ MAAŞI= 5376 Euro" )
        await message.channel.send("DANİMARKA TL BAZINDAN ASGARİ MAAŞI= "+str(5376 *ğ))
        await message.channel.send("DANİMARKA ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(5376 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş SE'):
        await message.channel.send("İSVEÇ ASGARİ MAAŞI= İsveç'te asgari maaş uygulaması yoktur. \n İsveç'te ortalama maaş = 2500 Euro" )
        await message.channel.send("İSVEÇ TL BAZINDAN ASGARİ MAAŞI= "+str(2500 *ğ))
        await message.channel.send("İSVEÇ ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(2500 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş NO'):
        await message.channel.send("NORVEÇ ORTALAMA MAAŞ = 2500 Euro" )
        await message.channel.send("NORVEÇ TL BAZINDAN ORTALAMA MAAŞI= "+str(2500 *ğ))
        await message.channel.send("NORVEÇ ORTALAMA MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(2500 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş PT'):
        await message.channel.send("PORTEKİZ ASGARİ MAAŞI= 740 Euro" )
        await message.channel.send("PORTEKİZ TL BAZINDAN ASGARİ MAAŞI= "+str(740 *ğ))
        await message.channel.send("PORTEKİZ ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(740 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş AZ'):
        await message.channel.send("AZERBAYCAN ASGARİ MAAŞI= 272 Euro / 541 Manat" )
        await message.channel.send("AZERBAYCAN TL BAZINDAN ASGARİ MAAŞI= "+str(272 *ğ))
        await message.channel.send("AZERBAYCAN ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(272 //ö) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş CH'):
        await message.channel.send("İSVİÇRE ASGARİ MAAŞI= 4100 İsviçre Frangı / "+ str(4100 *f) + ' Euro')
        await message.channel.send("İSVİÇRE TL BAZINDAN ASGARİ MAAŞI= "+str(758 *q))
        await message.channel.send("İSVİÇRE ASGARİ MAAŞININ TRDEKİ ASGARİ MAAŞA ORANI= " + str(758 //e) + (' (Yuvarlanmıştır)'))

    if message.content.startswith('$asgari maaş TR'):
        await message.channel.send("TÜRKİYE ASGARİ MAAŞI= 2324 Türk Lirası / "+ str(ö) + ' Euro')

    if message.content.startswith('$yapımcı'):
        await message.channel.send('<@619600347744436254>')
        await message.channel.send('Enes Aslan #3380')

    if message.content.startswith('$insta'):
        await message.channel.send('https://www.instagram.com/enes07.07aslan/')

    if message.content.startswith("youtube.com/watch?v=dQw4w9WgXcQ"):
        await message.channel.send ("DİKKAT BU BİR RİCKROLL")

    if message.content == '$botdavet':
        await message.channel.send ('https://discord.com/api/oauth2/authorize?client_id=770241810827575307&permissions=8&scope=bot')

    if message.content == "$yardım":
        embed = discord.Embed(title="DİKKAT BU BOT VERİLERİ CANLI VE GÜNCEL OLARAK ALDIĞI İÇİN 5-10 SANİYE GECİKEBİLİR.", description="KOMUTU VERDİKTEN SONRA 10 SANİYE BEKLEYİN")
        embed.add_field(name="$euro", value="Euro'nun kaç Türk Lirası'na tekabül ettiğini gösterir.")
        embed.add_field(name="$gr altın", value="Gram Altının kaç Türk Lirası'na tekabül ettiğini gösterir.")
        embed.add_field(name="$sterlin", value="Sterlinin kaç Türk Lirası'na tekabül ettiğini gösterir..")
        embed.add_field(name="$dolar", value="Dolar'ın kaç Türk Lirası'na tekabül ettiğini gösterir.")
        embed.add_field(name="$bitcoin", value="Bitcoinin kaç Türk Lirası'na tekabül ettiğini gösterir.")
        embed.add_field(name="$yapımcı", value="Botun sabihini gösterir.(Gerçi kim olduğunu biliyorsun.)")
        embed.add_field(name="$zar", value="Zar atarmaya yarar.")
        embed.add_field(name="$doğruluk", value="Doğruluk sorusu sorar.")
        embed.add_field(name="$cesaret", value="Cesarette ne yapacağını söyler")
        embed.add_field(name="$türksihj-mizha", value="Mizahta dünya markası olan biz Türklerden bir espri gönderir.")
        embed.add_field(name="$hdurumu <Şehrian ilk üç harfi>", value="Girilen şehrin hava durumunu gösterir. (Şimdilik 30 büyükşehir ve Zonguldak var.)")
        embed.add_field(name="$haber", value="Güncel haberleri gönderir.")
        embed.add_field(name="$deprem", value="Son depremleri gönderir.")
        embed.add_field(name="$asgari maaş <Ülke Kodu>", value="Girilen ülkenin asgari maaşı hakkında bilgi verir.")
        embed.add_field(name="$korona <Ülke Kodu>", value="Girilen ülkedeki korona verileri hakkında bilgi verir.")
        embed.add_field(name="$yalan", value="Yalan makinesi.")
        await message.channel.send(content=None, embed=embed)

client.run('NzcwMjQxODEwODI3NTc1MzA3.X5atlg.tB1rEVPnLMtzh_6OvSNt9qAI3oc')



