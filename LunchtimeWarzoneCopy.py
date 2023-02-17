
import asyncio
import os
import discord
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
import random
from datetime import datetime
import threading
import aiocron
import requests
from dotenv import load_dotenv
import openai
load_dotenv()

DISCORD_API_KEY = os.getenv('DISCORDAPI_KEY')
OPENAI_API_KEY = os.getenv('OPENAPI_KEY')

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)


GUILD = "Merry Band of Minorities" # server name3
##############

openai.api_key = OPENAI_API_KEY
model_engine = "text-davinci-003"

######################



@client.event
async def on_ready(): #event handler that handles the event when the Client has established a connection to discord and finsiehd prepping the data that discord has sent
    #on_ready() gets called once client is ready for further action
    print('We have logged in as {0.user}'.format(client))

    g = discord.utils.get(client.guilds, name = GUILD) #this tells it to join a guild we specified, in our case its good shit, this will be changed to the discord server

    
    channel = client.get_channel(380936459496062981) # This will load the channel ID I want to transmit in

    #await channel.send("Sup guys")
    print("We are in!!!!!!!!!!!!!!!!!")
    cron_min = aiocron.crontab('30 17 * * 1-5', func=checkWarzoneTime, args='', start=True) #cron job that will run every 1730 CEST


#When invoked, it will invoke the ChatGPT API to answer a question 
@client.command()
async def q(ctx, *, question: str): #question needs str as a type, or else the code fails
    print(f"The input is:  {question}\n")
    completion = openai.Completion.create(
    engine=model_engine,
    prompt=question,
    temperature=random.randrange(50, 90) / 100, # make it random how smart the bot should be
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    timeout=10
    )
    response = completion.choices[0].text
    await ctx.send(response)


@client.command()
async def shutdown(ctx):
    role = discord.utils.get(ctx.guild.roles, name="God")
    person = ctx.author.id #this gets your id
  

    if role in ctx.author.roles:
        await ctx.send("I am going to shut down")
        
        else:
            arrayGroups =  Array("A", "B", "C")
            var A = 5
            arrayA1 = Array("Study","Lie about","Love","Hate","orget","Cheat","Lose","Fear","Battle with","Live under","Hide from","Discover","Lose","Cheer for","Pray for","Ask for","Wish for","Cry for","Weep for","Enlist","Trust in","Expect","Show me","Show them","Rely on","Put your faith in","Bury","Dress up","Use","Employ","Go to war with","Think you are","Thank God for")
            arrayA2 = Array("the past","your heart","a pig","a donkey","your mother and father","your obligations","stupidity","hard things","excuses","mistakes","your past","your dreams","your brain","another's wife","another's lover","sex","truth","promises","broken promises","lies","giraffes","the yolk","the rod","the punishment","the results","your success","a frozen lake","a glass of mead","the pilgrims","failure","tales of heroes","open hearts","a kind heart","a kind ear","misconceptions","beliefs","religion","what got you here","what made you what you are","this mess","your pride","ignorance","a hurricane","guilt")
            arrayA3 = Array("if you would","and you'll","or you will","and you may as well","and you'll find you will","and","or")
            arrayA4 = Array("study","lie about","love","hate","forget","cheat","lose","fear","battle with","live under","hide from")
            arrayA5 =  Array("the past","your heart","a pig","a donkey","your mother and father","your obligations","stupidity","hard things","excuses","mistakes","your past","your dreams","your brain","another's wife","another's lover","sex","truth","promises","broken promises","lies","giraffes","the yolk","the rod","the punishment","the results","your success","a frozen lake","a glass of mead","the pilgrims","failure","tales of heroes","open hearts","a kind heart","a kind ear","misconceptions","beliefs","religion","what got you here","what made you what you are","this mess","your pride","ignorance","a screen door","a rooster","a hidden gift","a stubbed toe")

            var B = 5 
            arrayB1 = Array("Before you","Always","Never","You must","A wise man must","A fool must","An idiot should","You must never")
            arrayB2 = Array("embark on","take","find","discover","cheat","fear","hide","reveal","threaten","promote","pray for","expect")
            arrayB3 =  Array("a journey of revenge","a sinful thought","your mistakes","your drycleaning","your ugliness","your pride","toast","buttered toast")
            arrayB4 =  Array("without giving","without sharing","without inviting","without trading","without burying","without fighting")
            arrayB5 =  Array("two graves","an apple","a dog","a secret","a vampire","a killer","a gardener","a lunatic","a fool","a drunk","a swan","an angry bull","righteous indignation","folly","fools","a carp","the sands of time","lunacy")

            var C = 7
            arrayC1 =  Array("An eagle","A leopard","You","A man","A boy","A person","A woman","A girl","A horse","God","The devil","The postman","The milkman","A celebrity","A customer","A politician","A prophet","A rich man","A poor man","A leper","A lazy man","A fool","A wise man","A reasonable man","An old man","An old woman","A prisoner","A jester","A lost soul","A troubled mind","A sad heart","An angry man","A clown","A dictator","A sparrow","A caterpillar","A butterfly","An earthworm","A duck","A cardinal","A religious man","A priest","A monk","An evil man","A businessman","A atupid man","A dead man","An outsider","A friend","You","You","You","A blind man","A ferryman","A drunk")
            arrayC2 =  Array("can","might","may","could","can forget to","may always","may never")
            arrayC3 =  Array("fear","stumble upon","choke","eviscerate","appreciate","feel shame for","be ashamed of","take revenge upon","see","forget","hear","kick", "cry over", "enslave", "burn for", "wish upon", "do evil to", "jump over", "discover", "bring vengence upon", "understand", "escape", "die from", "kill for", "destroy", "live under", "rise against", "feel pity for", "pray to", "feel", "lay with", "hide from", "wish for", "discover", "sit on", "reason with", "love", "root for", "expect", "fully grasp", "hold", "sleep with", "be troubled by", "fail", "learn from", "dig deep within", "think about", "ruminate on", "feel accepted by", "nurture", "fall beneath", "rise above", "have dominion over", "be in the shadow of", "climb", "swing from", "leap onto", "mingle with", "lay down with", "frolic with", "run from", "hide in shame from", "be consumed by", "eat with", "devour", "be lost without", "be comfortable with", "share", "laugh at", "like", "fight for", "suffer for", "suffer from", "laugh about", "steal", "confide in", "dance with", "dance for", "dance under", "dream about","demonize", "give up", "tolerate", "banish", "forego", "trip over")
            arrayC4 =  Array("a pig", "an apple", "the sun", "a bucket", "a glass of water", "thunder", "lost hope", "a criminal", "a heart", "a mind", "the reason", "the truth", "a camel", "thirst", "hunger", "solitude", "the time", "an egg", "defeat", "sickness", "butter", "sugar", "a man", "a heart", "humbleness", "philosophy", "why", "the effect", "existence", "the weight", "the past", "good grooming", "politeness", "your home", "a rocket", "love", "the moon", "a river", "a creek", "an ocean", "the ocean", "a mountain", "weakness", "a canary", "a parrot", "a rainbow", "gold", "money", "a horse", "a barrel of fish", "a trout", "a peacock", "an enemy", "the enemy", "war", "misery", "a clown", "the barn", "a silo", "a cry for help", "help", "scorn", "ridicule", "insults", "an argument", "hell", "heaven", "manure", "insanity", "the sea","the process","the result","emptiness","blood","a button hole","a loaf of bread","a whale's belly","bad habits","a filthy tongue","a bed","a cactus","a shrew","stupidity","a simpleton","a woman","a boy","a girl","a dog","a father","a mother","a grandfather","balls","lemons","bitterness","an elephant","elephants","a gorilla","a shepherd","a carp","a halibut","a comedian","a nightmare","a finch","a larch","an eggplant","modesty","shame","a swine","patience", "virtue", "chastity", "rust", "sex", "dust", "unrequited love", "embarassment", "a soldier", "a stopwatch", "alcohol", "merriment", "family", "a hero", "money", "power", "wealth", "glory", "boredom", "stupidity", "demons","pride","lust","envy","sloth","a sloth","a turtle","a housecat","a lunatic","a grouse","a partridge","an apple tree","bloodlust","exasperation","life","death","lunacy","the buffalo","the snake","the worm","the larch","the lark","sweat","a feather","ineptitude","grease","a dog's bark","a cat's tongue","a forked tongue","the miller's wife","a blacksmith","a bird's beak","a duck's quack","an old man's elbow","a shadow","a lost cause","a pearl","a stubborn mule")
            arrayC5 =  Array("but never", "but must always", "but will never", "but will always", "but will not", "and","but may","but can","but must","but instead")
            arrayC6 =  Array("fear","stumble upon","choke","eviscerate","appreciate","feel shame for","be ashamed of","take revenge upon","see","forget","hear","kick", "cry over", "enslave", "burn for", "wish upon", "do evil to", "jump over", "discover", "bring vengence upon", "understand", "escape", "die from", "kill for", "destroy", "live under", "rise against", "feel pity for", "pray to", "feel", "lay with", "hide from", "wish for", "discover", "sit on", "reason with", "love", "root for", "expect", "fully grasp", "hold", "sleep with", "be troubled by", "fail", "learn from", "dig deep within", "think about", "ruminate on", "feel accepted by", "nurture", "fall beneath", "rise above", "have dominion over", "be in the shadow of", "climb", "swing from", "leap onto", "mingle with", "lay down with", "frolic with", "run from", "hide in shame from", "be consumed by", "eat with", "devour", "be lost without", "be comfortable with", "share", "laugh at", "like", "fight for", "suffer for", "suffer from", "laugh about", "steal", "confide in", "dance with", "dance for", "dance under", "dream about","demonize", "give up", "tolerate", "banish", "forego", "trip over")
            arrayC7 =  Array("a lost lamb","a scoundrel","a crooked politician","a salty pirate","a pig", "an apple", "the sun", "a bucket", "a glass of water", "thunder", "lost hope", "a criminal", "a heart", "a mind", "the reason", "the truth", "a camel", "thirst", "hunger", "solitude", "the time", "an egg", "defeat", "sickness", "butter", "sugar", "a man", "a heart", "humbleness", "philosophy", "why", "the effect", "existence", "the weight", "the past", "good grooming", "politeness", "your home", "a rocket", "love", "the moon", "a river", "a creek", "an ocean", "the ocean", "a mountain", "weakness", "a canary", "a parrot", "a rainbow", "gold", "money", "a horse", "a barrel of fish", "a trout", "a peacock", "an enemy", "the enemy", "war", "misery", "a clown", "the barn", "a silo", "a cry for help", "help", "scorn", "ridicule", "insults", "an argument", "hell", "heaven", "manure", "insanity", "the sea","the process","the result","emptiness","blood","a button hole","a loaf of bread","a whale's belly","bad habits","a filthy tongue","a bed","a cactus","a shrew","stupidity","a simpleton","a woman","a boy","a girl","a dog","a father","a mother","a grandfather","balls","lemons","bitterness","an elephant","elephants","a gorilla","a shepherd","a carp","a halibut","a comedian","a nightmare","a finch","a larch","an eggplant","modesty","shame","a swine","patience", "virtue", "chastity", "rust", "sex", "dust", "unrequited love", "embarassment", "a soldier", "a stopwatch", "alcohol", "merriment", "family", "a hero", "money", "power", "wealth", "glory", "boredom", "stupidity", "demons","pride","lust","envy","sloth","a sloth","a turtle","a housecat","a lunatic","a grouse","a partridge","an apple tree","bloodlust","exasperation","life","death","lunacy","the buffalo","the snake","the worm","the larch","the lark","sweat","a feather","ineptitude","grease","a dog's bark","a cat's tongue","a forked tongue","the miller's wife","a blacksmith","a bird's beak","a duck's quack","an old man's elbow","a shadow","a lost cause","a pearl","a stubborn mule")

            function GetArrayName(group, arraynum) #This function assords the array variables into one variable for Confucius saying
            var name = "array" + group + arraynum
            return name

            function LoadMenuItems() #This is what is returned on Bot shutdown
            if(generate==1)
            var group = arrayGroups[Math.floor(Math.random() * arrayGroups.len)]
            var strResult
            strResult = ""
            for(i=1 i<=eval(group) i++)
            strResult += eval(GetArrayName(group, i))[Math.floor(Math.random() * eval(GetArrayName(group, i)).len)] + " "
            ctx.send("strResult")
        exit()
    else:
        await ctx.send("Sorry you do not have the rights :( ")

#When invoke, it will ping the group for the warzone notification 
async def checkWarzoneTime():

    print("Called from checkWarzoneTime() \n")

    channel = client.get_channel(380936459496062981)
    g = discord.utils.get(client.guilds, name = GUILD) 
    roleMention = discord.utils.get(g.roles, id = 929444477515497513)
    poll = await channel.send(f"{roleMention.mention}Are you going to be there for lunchtime warzone? ")
    #await channel.send("Is it time\n")
    await poll.add_reaction("✅")
    await poll.add_reaction("❌")
         
      

#When invoked, it will invoke the DALL-E API from openapi to generate an image   
@client.command()
async def i(ctx, *, question: str): #question needs str as a type, or else the code fails
    response = openai.Image.create(
    prompt=question,
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    full_path = 'test' + '.jpg'
    f = open(full_path, 'wb')
    f.write(requests.get(image_url).content)
    f.close()
    await ctx.send(file=discord.File(full_path))

client.run(DISCORD_API_KEY)


