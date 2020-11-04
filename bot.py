import discord
import json
import akinator
import os
import re
import time
import datetime
import traceback
import random
from itertools import cycle
import asyncio
from discord.ext import commands, tasks 
from pip._vendor import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import redditlink
from io import BytesIO
import wikipediaAPI

prefix_ = '-'
client = commands.Bot(command_prefix=prefix_)
bot = client
client.remove_command("help")

@client.event
async def on_connect():
    print('Connected to Discord')

status = cycle(['-help','-music', 'with Life', 'Alone🚶','commands','-helpmusic','CORNHUB🌽','Stupid commands','in 69+ servers'])

@tasks.loop(seconds=300)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


@bot.event
async def on_ready():
    change_status.start()
    print('<------------------------------>')
    print('EPAX\'s Bot is ready')
    print(f'Using Discord.py Version {discord.__version__}')
    print('<------------------------------>')



    

@client.event
async def on_message(msg):
    channel = msg.channel
    if msg.author == bot.user:
        return
    else:
        
        if 'F' ==  msg.content:
            await msg.channel.send("F")
        if 'f' ==  msg.content:
            await msg.channel.send("f")
        if "chotu" == msg.content:
            await msg.channel.send(f"Hey! I am Chotu Type {prefix_}help for commands")   

    await client.process_commands(msg)
    
@bot.event
async def on_command_error(ctx,error):
  if isinstance(error,commands.CheckFailure):
    embed = discord.Embed(title = ':x: oops! You do not have permission to use this command.', color = discord.Colour.red())
    await ctx.send(embed = embed)
  elif isinstance(error,commands.MissingRequiredArgument):
    embed = discord.Embed(title = ':x:You are missing the required arguements. Please check if your command requires an addition arguement.', color = discord.Colour.red())
    await ctx.send(embed = embed)
  elif isinstance(error, commands.CommandNotFound):
    pass

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency*1000)}ms')


######################################################
###################INFO###############################   
#######################################################

@client.command()
async def avatar( ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    embed=discord.Embed(title=f'{avamember} avatar!!')
    embed.set_image(url=userAvatarUrl)
    await ctx.send(embed=embed)
@client.command(aliases = ['channelstats'])
async def channelinfo(ctx,channel:discord.TextChannel):
    nsfw = bot.get_channel(channel.id).is_nsfw()
    news = bot.get_channel(channel.id).is_news()
    embed = discord.Embed(title = 'Channel Infromation: ' + str(channel),
    colour = discord.Colour.from_rgb(54, 151, 255))
    embed.add_field(name = 'Channel Name: ', value = str(channel.name))
    embed.add_field(name = "Channel's NSFW Status: ", value = str(nsfw))
    embed.add_field(name = "Channel's id: " , value = str(channel.id))
    embed.add_field(name = 'Channel Created At: ', value = str(channel.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
    embed.add_field(name = 'Channel Type: ', value = str(channel.type))
    embed.add_field(name = "Channel's Announcement Status: ", value = str(news))
    await ctx.send(embed = embed)
@client.command(aliases = ['guild'])
async def server(ctx):
        findbots = sum(1 for member in ctx.guild.members if member.bot)
        embed = discord.Embed(title = 'Infomation about ' + ctx.guild.name + '.', colour = discord.Colour.from_rgb(54,151,255))
        embed.set_thumbnail(url = str(ctx.guild.icon_url))
        embed.add_field(name = "Guild's name: ", value = ctx.guild.name)
        embed.add_field(name = "Guild's owner: ", value = str(ctx.guild.owner))
        embed.add_field(name = "Guild's verification level: ", value = str(ctx.guild.verification_level))
        embed.add_field(name = "Guild's id: ", value = str(ctx.guild.id))
        embed.add_field(name = "Guild's member count: ", value = str(ctx.guild.member_count))
        embed.add_field(name="Bots", value=findbots, inline=True)
        embed.add_field(name = "Guild created at: ", value = str(ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
        await ctx.send(embed =  embed)
        
@client.command(aliases=['idea', 'tell', 'suggestion'])
async def suggest(ctx, *, suggestion = None):
    await ctx.message.delete()
        #729711188392280154 production id
    channel = bot.get_channel(729711188392280154)
    embed = discord.Embed(title = f"Suggestion from: {ctx.author}", color = discord.Colour.blue())
    embed.set_author(name = f"{ctx.author}", icon_url = ctx.author.avatar_url)
    embed.add_field(name = "Author's Suggestion: ", value = str(suggestion))
    msg = await channel.send(embed = embed)
    await msg.add_reaction('\U00002705')
    await msg.add_reaction('❌')
    embed = discord.Embed(title = f"{ctx.author}, your suggestion has been successfully submitted! Check #💡suggestions")
    msg2 = await ctx.send(embed = embed)
    await asyncio.sleep(10)
    await msg2.delete()
    
@client.command(aliases=['whois', 'userinfo'])
async def user(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    pos = sum(m.joined_at < member.joined_at for m in ctx.guild.members if m.joined_at is not None)
    roles = [role for role in member.roles]
    embed = discord.Embed(color=member.color, timestamp=datetime.datetime.utcnow())
    embed.set_author(name=f"{member}", icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"))
    embed.add_field(name='Registered at:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p'))
    embed.add_field(name='Bot?', value=f'{member.bot}')
    embed.add_field(name='Status?', value=f'{member.status}')
    embed.add_field(name='Top Role?', value=f'{member.top_role}')
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles[:1]]))
    embed.add_field(name='Join position', value=pos)
    embed.add_field(name='user id', value= member.id)
    embed.set_footer(icon_url=member.avatar_url, text=f'Requested By: {ctx.author.name}')
    await ctx.send(embed=embed)



###################################################################
###################################################################
###############IMAGE IMAGE IMAGE IMAGE ############################

@client.command()
async def slap(ctx, user : discord.Member = None) :
    
    user1 = ctx.author
    user2 = user
    if user == None:
        user2 = ctx.author
    
    slap = Image.open("slap.jpg")
            
    asset1 = user1.avatar_url_as(size = 256)
    asset2 = user2.avatar_url_as(size = 256)
    data1 = BytesIO(await asset1.read())
    data2 = BytesIO(await asset2.read())
    pfp1  = Image.open(data1)
    pfp1 = pfp1.resize((72,72))
    slap.paste(pfp1,(131,11))
    slap.save("slap1.jpg")
    pfp2  = Image.open(data2)
    pfp2 = pfp2.resize((72,72))
    slap.paste(pfp2,(11,33))
    slap.save("slap1.jpg")
    await ctx.send(file = discord.File("slap1.jpg"))

@client.command()
async def worthless(ctx, user : discord.Member = None) :
    if user == None:
        user = ctx.author
    worthless = Image.open("worthless.jpg")        
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp  = Image.open(data)
    pfp = pfp.resize((120,120))
    worthless.paste(pfp,(148,76))
    worthless.save("gay1.jpg")
    await ctx.send(file = discord.File("gay1.jpg"))



@client.command(aliases= ['kq'])
async def keepquiet(ctx, user : discord.Member = None) :
    if user == None:
        user = ctx.author
    stop = Image.open("stop.jpg")        
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp  = Image.open(data)
    pfp = pfp.resize((220,220))
    stop.paste(pfp,(695,42))
    stop.save("gay1.jpg")
    await ctx.send(file = discord.File("gay1.jpg"))


@client.command()
async def fart(ctx, user : discord.Member = None) :
    if user == None:
        user = ctx.author
    fart = Image.open("fart.jpg")        
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp  = Image.open(data)
    pfp = pfp.resize((200,200))
    fart.paste(pfp,(532,120))
    fart.save("gay1.jpg")
    await ctx.send(file = discord.File("gay1.jpg"))

@client.command()
async def pee(ctx, user : discord.Member = None) :
    if user == None:
        user = ctx.author
    pee = Image.open("pee.jpg")        
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp  = Image.open(data)
    pfp = pfp.resize((210,210))
    pee.paste(pfp,(432,61))
    pee.save("gay1.jpg")
    await ctx.send(file = discord.File("gay1.jpg"))

@client.command()
async def coffindance(ctx, user : discord.Member = None) :
    if user == None:
        user = ctx.author
    pee = Image.open("coffindance.jpg")        
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp  = Image.open(data)
    pfp = pfp.resize((127,127))
    pee.paste(pfp,(196,32))
    pee.save("gay1.jpg")
    await ctx.send(file = discord.File("gay1.jpg"))



@client.command()
async def smash(ctx, user : discord.Member = None) :
    if user == None:
        user2 = ctx.author
    user1 = ctx.author
    user2 = user
    
    smash = Image.open("smash.jpg")
            
    asset1 = user1.avatar_url_as(size = 256)
    asset2 = user2.avatar_url_as(size = 256)
    data1 = BytesIO(await asset1.read())
    data2 = BytesIO(await asset2.read())
    pfp1  = Image.open(data1)
    pfp1 = pfp1.resize((91,91))
    smash.paste(pfp1,(122,167))
    smash.save("slap1.jpg")
    pfp2  = Image.open(data2)
    pfp2 = pfp2.resize((88,88))
    smash.paste(pfp2,(326,290))
    smash.save("slap1.jpg")
    await ctx.send(file = discord.File("slap1.jpg"))



@client.command()
async def wanted(ctx, user : discord.Member = None) :
    if user == None:
        user = ctx.author
    wanted = Image.open("wantted.jpg")
            
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp  = Image.open(data)
    pfp = pfp.resize((300,300))
    wanted.paste(pfp,(81,224))
    wanted.save("profile.jpg")
    await ctx.send(file = discord.File("profile.jpg"))

@client.command()
async def gay(ctx, user : discord.Member = None) :
    if user == None:
        user = ctx.author
    gay = Image.open("gay.jpg")
            
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp  = Image.open(data)
    pfp = pfp.resize((199,199))
    gay.paste(pfp,(32,96))
    gay.save("gay1.jpg")
    await ctx.send(file = discord.File("gay1.jpg"))

##############################################
##############################################
##########################################
##############MEME###########################

@client.command()
async def csmeme(ctx):
    l = redditlink.randmeme('ProgrammerHumor')
    
    em = discord.Embed(title = l[1], color = discord.Colour.red())
    em.set_image(url = l[0])
    await ctx.send(embed= em)



    
@client.command()
async def desimeme(ctx):
    l = redditlink.randmeme('desimemes')
    em = discord.Embed(title = l[1], color = discord.Colour.blue())
    em.set_image(url = l[0])
    await ctx.send(embed= em)

@client.command(aliases = ['memes','MEME'])
async def meme(ctx):
    l = redditlink.randmeme('meme')
    em = discord.Embed(title = l[1], color = discord.Colour.green())
    em.set_image(url = l[0])
    await ctx.send(embed= em)

@client.command(aliases = ['nr','mass'])
async def plenty(ctx,num : int = 5,* , name : str = None ):
    if ctx.channel.is_nsfw():
        if name == None:
            
            await ctx.send(f"{ctx.author}\"please mention number of posts and subreddit name to pull data\" eg : plenty 10 dankmeme")
        else :
            if num > 69 :
                await ctx.send("You crossed the limit , `max = 69` ")
            else:
                for i in range(num):

                    l = redditlink.randmeme(name)
                    url = l[0]

                    if url[-4:] == ".jpg" :
                        em = discord.Embed(title = l[1], color = discord.Colour.green())
                        em.set_image(url = l[0])
                        await ctx.send(embed= em)

                    elif url[-4:] == ".png" :
                        em = discord.Embed(title = l[1], color = discord.Colour.green())
                        em.set_image(url = l[0])
                        await ctx.send(embed= em)

                    else:
                        em = discord.Embed(title = l[1], color = discord.Colour.red()) 
                        await ctx.send(embed= em)
                        await ctx.send(l[0])
    else:
        em = discord.Embed(title = "NSFW not allowed here" , description = "Hey Dummy Use NSFW commands in a NSFW marked channel",color = discord.Color.dark_red() )
        em.set_image(url = 'https://i.imgur.com/oe4iK5i.gif')
        await ctx.send(embed = em)


@client.command(aliases = ['r', 'nsfw'])
async def reddit(ctx,name : str = None ):
    if ctx.channel.is_nsfw():
        if name == None:
            await ctx.send(f"{ctx.author}\"please mention subreddit name to pull data\" eg : reddit dankmeme")
        else :
            l = redditlink.randmeme(name)
            url = l[0]

            if url[-4:] == ".jpg" :
                em = discord.Embed(title = l[1], color = discord.Colour.green())
                em.set_image(url = l[0])
                await ctx.send(embed= em)
                
            elif url[-4:] == ".png" :
                em = discord.Embed(title = l[1], color = discord.Colour.green())
                em.set_image(url = l[0])
                await ctx.send(embed= em)
            
            else:
                em = discord.Embed(title = l[1], color = discord.Colour.red()) 
                await ctx.send(embed= em)
                await ctx.send(l[0])
                
    else:
        em = discord.Embed(title = "NSFW not allowed here" , description = "Hey Dummy Use NSFW commands in a NSFW marked channel",color = discord.Color.dark_red() )
        em.set_image(url = 'https://i.imgur.com/oe4iK5i.gif')
        await ctx.send(embed = em)




@client.command(aliases = ['animememes','anime'])
async def animememe(ctx):
    l = redditlink.randmeme('animememes')
    em = discord.Embed(title = l[1], color = discord.Colour.green())
    em.set_image(url = l[0])
    await ctx.send(embed= em)


@client.command(aliases = ['animewp','animewp1'])
async def animewallpaper(ctx):
    l = redditlink.randmeme('AnimeWallpapersSFW')
    em = discord.Embed(title = l[1], color = discord.Colour.purple())
    em.set_image(url = l[0])
    await ctx.send(embed= em)

@client.command(aliases = ['wp','wall'])
async def wallpaper(ctx):
    l = redditlink.randmeme('WQHD_Wallpaper')
    em = discord.Embed(title = l[1], color = discord.Colour.purple())
    em.set_image(url = l[0])
    await ctx.send(embed= em)

@client.command(aliases = ['gamewp','gamewall'])
async def gamewallpaper(ctx):
    l = redditlink.randmeme('videogamewallpapers')
    url = l[0]

    if url[-4:] == ".jpg" :
        em = discord.Embed(title = l[1], color = discord.Colour.green())
        em.set_image(url = l[0])
        await ctx.send(embed= em)
        
    elif url[-4:] == ".png" :
        em = discord.Embed(title = l[1], color = discord.Colour.green())
        em.set_image(url = l[0])
        await ctx.send(embed= em)
    
    else:
        em = discord.Embed(title = l[1], color = discord.Colour.red()) 
        await ctx.send(embed= em)
        await ctx.send(l[0])    




@client.command(aliases = ['dank','dankmemes'])
async def dankmeme(ctx):
    l = redditlink.randmeme('dankmemes')
    em = discord.Embed(title = l[1], color = discord.Colour.purple())
    em.set_image(url = l[0])
    await ctx.send(embed= em)
@client.command(aliases = ['bot link','link'])  
async def botlink(ctx):
    await ctx.send('https://discord.com/api/oauth2/authorize?client_id=772372193963016202&permissions=0&scope=bot')

######################################
#######################################
################FUN####################

@client.command()
async def story(ctx):
    em = discord.Embed(title = ":partying_face:  Story Time :partying_face: " ,description = random.choice(redditlink.stories) ,color = discord.Colour.dark_purple()  )
    await ctx.send(embed = em)


@client.command()
async def penis(ctx , member : discord.Member):
    em = discord.Embed(color = discord.Colour.blue() , title= "PeePee size calculator")
    x = ['','==','','=','','====','','=','======','==========================','===',"===============","========","===","===================","===","==========================="]
    em.add_field(name = f"{member.display_name}s penis:eggplant:",value = f"8{random.choice(x)}D")
    await ctx.send(embed = em)


@client.command(aliases = ['mock','laugh','drunk','drunkify'])
async def camel(ctx,*,msg):
    msg = list(msg)
    converted = []
    for x in msg:
        try:
            qt = random.randint(0,1)
            if qt == 1:
                convert = x.upper()
                converted.append(convert)
            elif qt == 0:
                convert = x.lower()
                converted.append(convert)
        except:
            pass
    final = ''.join(converted)
    await ctx.send(final)









@client.command(aliases=['8ball','test','ask'])
async def _8ball(ctx, *, question):
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later."
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        em = discord.Embed(title = 'Magic 8ball!',colour = discord.Colour.orange())
        em.add_field(name=f"**Question:** {question}", value=f"**Answer:** {random.choice(responses)}")
        await ctx.send(embed = em)


@client.command(aliases = [ 'how gay', 'gaypercent'])
async def howgay(ctx,member : discord.Member):
    num = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,100]
    per = random.choice(num)
    
    if per >= 50 :
        gay = 'GAY'
    else:
        gay = "Not Gay"
    em = discord.Embed(title = member.display_name , description = ":two_men_holding_hands: gay result:" , color = discord.Colour.red() )
    em.add_field(name = gay , value= f"{member.display_name} is :rainbow_flag: {str(per)}% gay " )
    em.set_thumbnail(url = member.avatar_url)
    
    await ctx.send(embed = em)


@client.command()
async def kill(ctx, user : discord.Member = None) :
    if user == None:
        user = ctx.author
    await ctx.send(f'{user.display_name} {random.choice(redditlink.kills)}')

@client.command()
async def say(ctx,*,msg):
        await ctx.channel.purge(amount = 1)
        await ctx.send(msg)

@client.command()
async def reverse(ctx,*,msg):
        try:
            msg = list(msg)
            msg.reverse()
            send = ''.join(msg)
            await ctx.send(send)
        except Exception:
            traceback.print_exc()


@client.command(aliases = ['pass','generator','password','passwordgenerator'])
async def _pass(ctx,amt : int = 8):
    try:
        nwpss = []
        lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z','!','@',
        '#','$','%','^','&','*','(',')','-','_','+','=','{',",",'}',']',
        '[',';',':','<','>','?','/','1','2','3','4','5','6','7','8','9','0'
        ,'`','~','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'
        ,'Q','R','S','T','U','V','W','X','Y','Z']
        for x in range(amt):
            newpass = random.choice(lst)
            nwpss.append(newpass)
        fnpss = ''.join(nwpss)
        await ctx.send(f'{ctx.author} attempting to send you the genereated password in dms.')
        await ctx.author.send(f':white_check_mark:Password Generated: {fnpss}')
    except Exception as e:
            print(e)

        
@client.command()    
async def whisper(ctx, member : discord.Member, *,content):
            embed=discord.Embed(color=discord.Colour.orange())
            embed=discord.Embed(title='Someone Whispered To You!')
            embed.add_field(name='Message: '+ str(content), value="From"  + str(ctx.author.mention))
            await member.send(embed=embed)
            await ctx.message.delete()

@client.command()
async def sayname(ctx, *,  avamember : discord.Member=None):
    await ctx.send(f"Your name is {ctx.author.mention}")



@client.command()
async def count(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    messages = await channel.history(limit=None).flatten()
    count = len(messages)
    embed = discord.Embed(
        title="Total Messages",
        colour=0x2859b8,
    description=f"There were {count} messages in {channel.mention}")
    await ctx.send(embed=embed)



########################                    ########################
#####################                        DALEK        #####################
###############               DALEK     DALEK                       ############### 
####################               DALEK                  ####################


@client.command()
async def beer( ctx , user: discord.Member = None, reason: commands.clean_content = ""):
    if not user or user.id == ctx.author.id:
        return await ctx.send(f"{ctx.author.name}: paaaarty!:tada::beer:")
    if user.id == bot.user.id:
        return await ctx.send("drinks beer with you* :beers:")
    if user.bot:
        return await ctx.send(f"lol {ctx.author.name}lol")
    beer_offer = f"{user.name}, you got a :beer: offer from {ctx.author.name}"
    beer_offer = beer_offer + f"\n\nReason: {reason}" if reason else beer_offer
    msg = await ctx.send(beer_offer)        
    def reaction_check(m):
        if m.message_id == msg.id and m.user_id == user.id and str(m.emoji) == "🍻":
            return True
        return False
    try:
        await msg.add_reaction("🍻")
        await bot.wait_for('reaction_add', timeout=30.0, check=reaction_check)
        await msg.edit(content=f"{user.name} and {ctx.author.name} are enjoying a lovely beer together :beers:")
    except asyncio.TimeoutError:
        await msg.delete()
        await ctx.send(f"well, doesn't seem like {user.name} wanted a beer with you {ctx.author.name} ;-;")
    except discord.Forbidden:
        beer_offer = f"{user.name}, you got a :beer: from {ctx.author.name}"
        beer_offer = beer_offer + f"\n\nReason: {reason}" if reason else beer_offer
        await msg.edit(content=beer_offer)
    
@client.command()
async def amiadmin(ctx):
    if ctx.author.guild_permissions.administrator == True:
        await ctx.send(f'Yes {ctx.author.name} you are an admin! :white_check_mark:')
    elif ctx.author.id == 579326961038524446:
        await ctx.send('Yes Happy Days you are an admin! :white_check_mark:')
    else:
        await ctx.send(f'no, heck off {ctx.author.name}')
        
@client.command()
async def dm(ctx, user_id: int, *, message: str):
    user = bot.get_user(user_id)
    if not user:
        return await ctx.send(f"Could not find any UserID matching {user_id}")
    try:
        await user.send(message)
        await ctx.send(f":envelope: Sent a DM to {user_id}")
    except discord.Forbidden:
        await ctx.send("This user might be having DMs blocked or it's a bot account...")
        
@client.command()
async def dalekping(ctx):
    before = time.monotonic()
    before_ws = int(round(bot.latency * 1000, 1))
    message = await ctx.send(":ping_pong: Pong")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f":ping_pong: WS: {before_ws}ms  |  REST: {int(ping)}ms")

#######################################################################
########################################GAMES
#############################################GAMES ###############   
##################################################GAMES###################


@client.command()
async def rps(ctx ,num : int = 0):
    val = ['Rock','Paper','Scissor']
    if num == 0:
        em = discord.Embed(color = discord.Colour.dark_orange(), title = f"🔥*ROCK PAPER SCISSOR**🔥 \n\n TYPE :\nFor Rock✊   : `{prefix_}rps 1` \nFor Paper✋  : `{prefix_}rps 2` \nFor Seissor✌️ : `{prefix_}rps 3` ")

        await ctx.send(embed = em)
        return
    elif num == 1 :
        userval = 'Rock'
    elif num == 2 :
        userval = 'Paper'
    elif num == 3 :
        userval = 'Scissor'
    else :
        em = discord.Embed(color = discord.Colour.dark_orange(), title = f"🔥*ROCK PAPER SCISSOR**🔥 \n\n TYPE :\nFor Rock✊   : `{prefix_}rps 1` \nFor Paper✋  : `{prefix_}rps 2` \nFor Seissor✌️ : `{prefix_}rps 3` ")

        await ctx.send(embed = em)
        return
    botval = random.choice(val)
    if userval == 'Rock':
        if botval == 'Rock':
            em = discord.Embed(color = discord.Colour.orange(), title = "Tie!\n We Both slected Rock LoL\n 🤜🤛 ")
            await ctx.send(embed = em)
        elif botval == 'Paper':
            em = discord.Embed(color = discord.Colour.orange(), title = "Lost!\n Looser i selected Paper😝\n 🤜🤚 ")
            await ctx.send(embed = em)
        elif botval == 'Scissor':
            em = discord.Embed(color = discord.Colour.orange(), title = "Won!\n Hey you won i selected Scissor🖖\n 🤜✌️ ")
            await ctx.send(embed = em)
    elif userval == 'Paper':
        if botval == 'Rock':
            em = discord.Embed(color = discord.Colour.orange(), title = "Won!\n Hey you won i selected Rock👊 \n ✋🤛 ")
            await ctx.send(embed = em)
        elif botval == 'Paper':
            em = discord.Embed(color = discord.Colour.orange(), title = "Tie!\n OOPS we both selected Paper😅 \n 🤚✋ ")
            await ctx.send(embed = em)
        elif botval == 'Scissor':
            em = discord.Embed(color = discord.Colour.orange(), title ="Lost!\n Looser i selected Scissor😝\n 🤚✌️ ")
            await ctx.send(embed = em)
    elif userval == 'Scissor':
        if botval == 'Rock':
            em = discord.Embed(color = discord.Colour.orange(), title = "Lost!\n You lost! i selected selected Rock👊 \n ✌️🤛 ")
            await ctx.send(embed = em)
        elif botval == 'Paper':
            em = discord.Embed(color = discord.Colour.orange(), title = "Won!!\n Congo you won i selected Paper\n ✌️✋ ")
            await ctx.send(embed = em)
        elif botval == 'Scissor':
            em = discord.Embed(color = discord.Colour.orange(), title ="Tie!\n Two Scissors😲😅 \n ✌️✌️ ")
            await ctx.send(embed = em)
            
        
            


    

         



     















########################                    ########################
#####################                              #####################
###############               web                      ############### 
####################                                 ####################


@client.command(aliases = ['wikipedia'])
async def wiki(ctx,* , querry_ : str ):
    l = wikipediaAPI.finder(querry_)
    em = discord.Embed(title = l[1] ,color=discord.Color(0xf58742))
    em.set_footer(text = l[0])
    em2 = discord.Embed( color = discord.Color(0xf58742) )
    
    em2.set_footer(text= f'Recommended searches : ' + f'{l[2][1:-1]}'[1:-1])
    await ctx.send(embed= em)
    await ctx.send(embed= em2)





###############################################     mod
#################################################    mod
###################################################    mod
####################################################### mod
##########################################################   mod
########################################################
@client.command()
@commands.has_permissions(manage_channels = True)
async def lock(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)
    await ctx.message.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    embed = discord.Embed(title = 'This channel has been locked by: ' + str(ctx.message.author))
    await ctx.send(embed=embed)
    
@client.command()
async def nick(ctx,member:discord.Member,name):
    await member.edit(nick = name)
    embed = discord.Embed(title = 'Nick Name Successfully Changed!')
    await ctx.send(embed = embed)
@client.command()
@commands.has_permissions(manage_channels = True)
async def unlock(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)
    await ctx.message.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    embed = discord.Embed(title = 'This channel has been unlocked by: ' + str(ctx.message.author))
    await ctx.send(embed=embed)
@client.command()
async def slowmode(ctx,time:int):
    try:
        if time == 0:
            embed = discord.Embed(title = 'Slowmode turned off')
            await ctx.send(embed = embed)
            await ctx.channel.edit(slowmode_delay = 0)
        elif time > 21600:
            embed = discord.Embed(title = 'You cannot have a slowmode above 6hrs.')
            await ctx.send(embed = embed)
        else:
            await ctx.channel.edit(slowmode_delay = time)
            embed = discord.Embed(title = f'Slowmode set to {time} seconds.')
            await ctx.send(embed = embed)
    except Exception:
        traceback.print_exc()
        
    
@client.command()
async def softban(ctx, member:discord.Member,*, reason = 'No reason provided'):
    await member.ban(reason = reason)
    await member.unban(reason = reason)
    embed = discord.Embed(title = f'Successfully softbanned {member}')
    await ctx.send(embed = embed)


@client.command()
async def tempban(ctx,member:discord.Member,time,*,reason = 'No Reason Provided'):
    with open('guild.json','r') as f:
        channels = json.load(f)
    indicator = time[-1]
    if indicator == "m" or indicator == "s" or indicator == 'h' or indicator == 'd':
        pass
    else:
        await ctx.send('Incorrect Time Format.')
    embed = discord.Embed(title = f'{member} has been temp banned for {time}.')
    await ctx.send(embed = embed)
    await member.ban(reason = reason)
    chanid = channels[str(ctx.guild.id)]['admin'][0]['adid']
    channel = bot.get_channel(chanid)
    embed = discord.Embed(title = 'Member Tempbanned!', color = discord.Colour.red())
    embed.add_field(name = f'{member} was tempbanned({time}) from {ctx.guild.name} for: ',value = f'{reason}')
    await channel.send(embed = embed)
    time = time[:-1]
    if indicator == 'm':
        await asyncio.sleep(int(time) * 60)
    elif indicator == 'h':
        await asyncio.sleep(int(time) * 3600)
    elif indicator == 's':
        await asyncio.sleep(int(time))
    elif indicator == 'd':
        await asyncio.sleep(int(time) * 86400)
    await member.unban(reason = 'Timer has expired.')   


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount : int):
    await ctx.channel.purge(limit = amount)



@client.command()
@commands.has_permissions(ban_members = True)
async def ban( ctx, member : discord.Member=None, *, reason = None):
    if member is None:
        em = discord.Embed(title = 'Please specify a member.')
        await ctx.send(embed = em)
        return
    await member.ban(reason = reason)
    em = discord.Embed(title = f'You banned {member}')
    await ctx.send(embed = em)
    
    embed = discord.Embed(title='You have been banned from The Coding Community', description=f'Banned by {member}')
    embed.add_field(name='Reason:', value=f'{reason}')
    await member.send(embed=embed)
@client.command()
@commands.has_permissions(ban_members = True)
async def unban( ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            em = discord.Embed(title = f'You Unbanned {user.mention}')
            await ctx.send(embed = em)
            return            
@client.command()
@commands.has_permissions(administrator=True)
async def kick( ctx, member:discord.Member = None,*,reason = 'No reason provided'):
    if not member:
        em = discord.Embed(title = 'Please specify a member.')
        await ctx.send(embed = em)
        return
    await member.kick()
    em = discord.Embed(title = f'You kicked {member}')
    await ctx.send(embed = em)
    embed = discord.Embed(title='You have been kicked from The Coding Community', description=f'Kicked by {member}')
    embed.add_field(name='Reason:', value=f'{reason}')
    await member.send(embed=embed)
@client.command()
@commands.has_permissions(kick_members = True )
async def mute(ctx, member:discord.Member = None,time:str = None,*,reason = 'No reason provided'):
    try:
        while True:
            try:
                if member == None:
                    em = discord.Embed(title = 'Please specify a member.')
                    await ctx.send(embed = em)
                    return
                if member == ctx.message.author:
                    embed = discord.Embed(title = 'No you may not mute yourself.')
                    await ctx.send(embed = embed)
                    break
                else:
                    indicator = time[-1]
                    if indicator == "m" or indicator == "s" or indicator == 'h' or indicator == 'd':
                        pass
                    else:
                        await ctx.send('Incorrect Time Format.')
                        break
                    muted_give = discord.utils.get(ctx.guild.roles, name = 'Muted')
                    await member.add_roles(muted_give)
                    embed = discord.Embed(title = str(member) + ' was successfully muted by: ' + str(ctx.author) + ' for ' + str(time) + ' Reason:' + str(reason))
                    await ctx.send(embed = embed)
                    time = time[:-1]
                    if indicator == 'm':
                        await asyncio.sleep(int(time) * 60)
                    elif indicator == 'h':
                        await asyncio.sleep(int(time) * 3600)
                    elif indicator == 's':
                        await asyncio.sleep(int(time))
                    elif indicator == 'd':
                        await asyncio.sleep(int(time) * 86400)
                    else: 
                        pass
                    await member.remove_roles(muted_give)
                    break
            except AttributeError:
                muted = await ctx.guild.create_role(name = "Muted")
                await ctx.message.channel.set_permissions(ctx.guild.get_role(muted.id), send_messages = False)
    except Exception:
        traceback.print_exc()
@client.command()
@commands.has_permissions(manage_guild=True)
async def warn(ctx , member : discord.Member ,* , reason = "No reason Provided"):
    with open('warnings.json','r') as f:
        warns = json.load(f)
    if str(ctx.guild.id) not in warns:
        warns[str(ctx.guild.id)] = {}
    if str(member.id) not in warns[str(ctx.guild.id)]:
        warns[str(ctx.guild.id)][str(member.id)] = {}
        warns[str(ctx.guild.id)][str(member.id)]["warns"] = 1
        warns[str(ctx.guild.id)][str(member.id)]["warnings"] = [reason]
    else:
        warns[str(ctx.guild.id)][str(member.id)]["warnings"].append(reason)
    with open('warnings.json','w') as f:
        json.dump(warns , f)
        await ctx.send(f"{member.mention} was warned for: {reason}")
        
        embed = discord.Embed(title='You have been warned in The Coding Community', description=f'You received a warning from {member}')
        embed.add_field(name='Reason:', value=f'{reason}')
        await member.send(embed=embed)
        
@client.command()
@commands.has_permissions(manage_guild=True)
async def removewarn(ctx, member: discord.Member, num: int, *, reason='No reason provided.'):
    with open('warnings.json' , 'r') as f:
        warns = json.load(f)
    num -= 1
    warns[str(ctx.guild.id)][str(member.id)]["warns"] -= 1
    warns[str(ctx.guild.id)][str(member.id)]["warnings"].pop(num)
    with open('warnings.json' , 'w') as f:
        json.dump(warns , f)
        await ctx.send('Warn has been removed!')
        embed = discord.Embed(title='Your warn in The Coding Community has been removed', description=f'Your warning was removed by {ctx.author}')
        await member.send(embed=embed)
        
@client.command()
@commands.has_permissions(manage_messages=True)
async def warns(ctx , member : discord.Member):
    with open('warnings.json', 'r') as f:
        warns = json.load(f)
    num = 1
    warnings = discord.Embed(title = f"{member}\'s warns")
    for warn in warns[str(ctx.guild.id)][str(member.id)]["warnings"]:
        warnings.add_field(name = f"Warn {num}" , value = warn)
        num += 1
    await ctx.send(embed = warnings)


###############################################     help
#################################################    help
###################################################    help
#######################################################  help
##########################################################hlep
########################################################


@client.group(invoke_without_command = True , aliases = ["commands" , "command"])
async def help( ctx):
            embed=discord.Embed(color =discord.Colour.purple() ,title='Bot Commands', description=f'\n\n`{prefix_}helpmemes`:joy:  ➣ For meme commands!\n`{prefix_}helpimages`:camera_with_flash:  ➣ For Fun Troll image commmands!\n`{prefix_}helpposts`:frame_photo:  ➣ For Wallpapers and more!\n`{prefix_}helpmod` :hammer_pick:  ➣ For moderation commands\n`{prefix_}helpfun` :zany_face:  ➣ For Epic fun commands\n`{prefix_}helpinfo` :information_source:  ➣ For infomation commands\n`{prefix_}helpmusic`:musical_note:  ➣ For the music commands\n`{prefix_}helputils`:electric_plug:  ➣ For random utility commands\n`{prefix_}helprandom`🃏  ➣ for random commands that dont fit in.\n`{prefix_}helpnsfw 🔞`  ➣ Adult content and more (use in NSFW channels only)')
            await ctx.send(embed=embed)



@client.command(aliases = ["play","music"])
async def helpmusic( ctx):
            embed1=discord.Embed(title = ":headphones:Music:" , description = "`@Chotu lyrics [song name]` - shows the lyrics to the currently-playing song \n `@Chotu nowplaying` - shows the song that is currently playing \n `@Chotu play <title|URL|subcommand>` - plays the provided song \n `@Chotu playlists` - shows the available playlists \n `@Chotu queue [pagenum]` - shows the current queue \n `@Chotu remove <position|ALL>` - removes a song from the queue \n `@Chotu search <query>` - searches Youtube for a provided query \n `@Chotu scsearch <query>` - searches Soundcloud for a provided query \n `@Chotu shuffle` - shuffles songs you have added \n `@Chotu skip` - votes to skip the current song \n",color = discord.Colour.dark_gold())
            embed2 = discord.Embed(title = "🔊DJ:" , description ="`@Chotu forceremove <user>` - removes all entries by a user from the queue \n `@Chotu forceskip` - skips the current song \n `@Chotu movetrack` <from> <to> - move a track in the current queue to a different position \n `@Chotu pause` - pauses the current song \n `@Chotu playnext <title|URL>`- plays a single song next \n `@Chotu repeat [on|off]` - re-adds music to the queue when finished \n `@Chotu skipto <position>` - skips to the specified song  \n `@Chotu stop` - stops the current song and clears the queue \n `@Chotu volume [0-150]` - sets or shows volume \nFor additional help, contact !ΞPAX㋡#2215 " ,color = discord.Colour.dark_blue())
            await ctx.send(embed=embed1)
            await ctx.send(embed=embed2)
@client.command()
async def helpmod( ctx):
            embed=discord.Embed(title=':hammer_pick: Moderation Commands :hammer_pick:', description=f'\n\n`{prefix_}clear` - This command clears a spesified  ammount of messages from a text channel\n`{prefix_}mute` - Mutes the spesified player\n`{prefix_}unmute` - This command unmutes a user.\n`{prefix_}kick` - Kicks a spesified user\n`{prefix_}ban` - This command bans a user.\n`{prefix_}unban` - This command bans a user.\n`{prefix_}lockdown` - This locksdown a certain channel.\n`{prefix_}warn` - This warns the user. \n`{prefix_}removewarn` - This removes a warn.\n`{prefix_}warns` - This shows warns.\n`{prefix_}lock` - locks a channel\n`{prefix_}unlock` - unlocks a channel\n`{prefix_}slowmode` - sets channel slowmode' , color = discord.Colour.dark_red())
            await ctx.send(embed=embed)


@client.command()
async def helpinfo(ctx):
            embed=discord.Embed(title = f' :information_source:NFO commands \n `{prefix_}avatar` `{prefix_}count` `{prefix_}channelinfo ` `{prefix_}amiadmin` `{prefix_}user` `{prefix_}server` ',color = discord.Colour.red())
            await ctx.send(embed=embed)



#fun help command
@client.command()
async def helpfun( ctx):
            embed=discord.Embed(color = discord.Colour.green(),title=':zany_face: Fun Commands :zany_face:', description=f'\n\n`{prefix_}kill` - use this to kill someone!\n`{prefix_}story` - some cool stories!\n`{prefix_}whisper` - Tell something to your friend secretly!\n`{prefix_}rps` - Play Rock Paper Scissor with me!\n`{prefix_}beer` - have some beer!\n`{prefix_}` - !\n`{prefix_}howgay` - use this to check gayness of your friend or test your self!\n`{prefix_}8ball` - This command you say _8ball then ask your question!\n`{prefix_}whisper` - lets you send a dm to someone.\n`{prefix_}mock` - lets you camelfy a word!\n`{prefix_}reverse` - lets you reverse a word!\n`{prefix_}password` - generates you a random password\n`{prefix_}sayname` - says the users name!')
            await ctx.send(embed=embed)

@client.command()
async def helputils( ctx):
            embed=discord.Embed(title='utility commands!', description=f'\n\n`{prefix_}checkthanks - checks a users thanks!\n `{prefix_}thxlb` - lets you see the thanks leaderboard\n{prefix_}thx - lets you thank a user')
            await ctx.send(embed=embed)


@client.command(aliases = ['helpimage'])
async def helpimages( ctx):
            embed=discord.Embed(title=':camera_with_flash: Images Commands :camera_with_flash: \n' f'`{prefix_}wanted` `{prefix_}gay` `{prefix_}slap` `{prefix_}fart` `{prefix_}smash` `{prefix_}keepquiet` `{prefix_}worthless` `{prefix_}coffindance` `{prefix_}pee` `{prefix_}shit`  ',color = discord.Colour.blurple())
            await ctx.send(embed=embed)


@client.command(aliases = ['helpmeme'])
async def helpmemes( ctx):
            embed=discord.Embed(title=':joy: MeMe Commands :joy: :   \n' f'`{prefix_}meme` `{prefix_}csmeme` `{prefix_}desimeme` `{prefix_}dankmeme` `{prefix_}desimeme` `{prefix_}reddit <subreddit_Name>`  ',color = discord.Colour.green())
            await ctx.send(embed=embed)


    
@client.command()
async def helprandom( ctx):
            embed=discord.Embed(title='RaNdOm CoMMands : \n' f'`{prefix_}wiki` `{prefix_}password` `{prefix_}botlink` `{prefix_}story` `{prefix_}`',color = discord.Colour.blurple())
            await ctx.send(embed=embed)

@client.command()
async def helpcurrency(ctx):
            embed=discord.Embed(color=discord.Colour.orange())
            embed=discord.Embed(title = 'Coming Soon!!')
            await ctx.send(embed=embed)


@client.command()
async def helpposts(ctx):
            embed=discord.Embed(color=discord.Colour.orange())
            embed=discord.Embed(title = f':frame_photo: PhotoS FoR YoU :frame_photo: \n', description =f'`{prefix_}animewp` - some cool anime wallpapers for you!\n `{prefix_}wp` - 4k and HD wallpapers!\n `{prefix_}gamewp` - 4K Game wallpapers!\n')
            await ctx.send(embed=embed)




@client.command()
@commands.has_permissions(administrator=True)
async def spam(ctx,num : int, *, msg):
    for i in range(num):
        await ctx.send(msg)
    

@client.command()
async def helpnsfw(ctx):
            embed=discord.Embed(color = discord.Colour.red())
            embed=discord.Embed(title=':sweat_drops: NSFW commands:sweat_drops: ', description= f'`{prefix_}reddt` or `{prefix_}r`- to get post from any subreddit eg : {prefix_}r boobs , {prefix_}r discord etc \n `{prefix_}plenty` or `{prefix_}nr`  - to get large no of memes or any subreddit content eg : {prefix_}plenty 20 desimemes!\n\n\n\n  some famous commands : `{prefix_}r boobs` `{prefix_}r pussy` `{prefix_}r booty` `{prefix_}r porn`')
            
            await ctx.send(embed=embed)


client.run('NzcyMzcyMTkzOTYzMDE2MjAy.X55tqQ.erInlV7y4oL4k6kpKrxXctCyzv8')






#NzcyMzcyMTkzOTYzMDE2MjAy.X55tqQ.erInlV7y4oL4k6kpKrxXctCyzv8