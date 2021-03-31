import discord
from discord.ext import commands
from discord.utils import get
import traceback

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print("[INFO] No errors encountered during startup")

@bot.event
async def on_member_join( member):
    role = get(member.guild.roles, name="Member")
    try:
        await member.add_roles(role)
        print(f"[INFO] Gave {member} the {role} role successfully")

    except:
        print("[ERROR] + " + traceback.print_exc())


@bot.command()
async def docs(ctx):
    docs = """
    Client Javadocs: 
EPICBOT: https://epicbot.com/javadocs/
TRIBOT: http://www.docs.tribot.org/tribot/latest/
POWBOT: https://powbot.org/docs/
DREAMBOT: https://dreambot.org/javadocs/
    """
    await ctx.send(docs)

@bot.command()
async def invite(ctx):
    link = "https://discord.gg/RwgKpds7dc"
    await ctx.send(link)

@bot.command()
async def rules(ctx):
    rules = """
    ```
RULES

- No racial slurs of any kind (even as a joke. This includes memes) you will be warned once and then banned.
- Please try and keep your conversation related to the channel
- Don't be a dick to new programmers/scripters or anyone. We all started from no knowledge at some point.
- No posting of advertisements or market of ANY kind, you may recommend a client to someone if someone asks the question, otherwise none. You will be banned
- No IP grabber links. You will be banned.
- Please search and do your own research before trying to ask for help when it comes to basic Java language problems. This helps you and and others not ask/need to answer very simple questions. If you do not understand something then that's fine, but don't ask "What's a string" and expect people to answer you or give you a serious answer. We aren't going to spoonfeed you answers and you shouldn't expect that. We're here to help, not to hold your hand through writing your scripts. This won't result in a ban or a kick or anything, this is just a disclaimer that if you ask a stupid question w/o doing your own research, then you're going to receive meme answers.

- Read your client's docs first before coming here, prevents a lot of questions from being answered that could've been answered on your own.
- No politics/anything related to political movements or events, past or present. We don't care about your political views in here, if you'd like to talk about it do it in your DMs.
- No excessive pinging of roles/other members, i.e you've pinged them 5 times in the past hour (this doesn't apply if you're replying to recent messages)
    ```
    """
    await ctx.send(rules)

@bot.command()
async def spoon(ctx):
    message = "We aren't going to spoonfeed you answers and you shouldn't expect that. We're here to help, not to hold your hand through writing your scripts"
    await ctx.send(message)


bot.run("ODI1NDk1MTM1MzYxODI2ODg2.YF-wQQ.845G47anM2Kp2yA5GcvspSsjZh4")