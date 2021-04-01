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
async def on_member_join(member):
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


@bot.command()
async def resources(ctx):
    tut_message = """
<https://community.tribot.org/topic/6644-a-simple-tutorial-to-hashmaps/> - Tutorial on practical implementation of HashMap's in scripts

<https://explv.github.io/?centreX=3108&centreY=3321&centreZ=0&zoom=7> Explv's map for finding area's and tiles

<https://www.osrsbox.com/tools/> Tool for finding NPC or object ID's

<https://app.diagrams.net/?> good for planning out how your scripts should work logically :smile:

<https://youtube.com/channel/UCCDS_ii2C6nTXs9Y2E_YIyA> pretty cool channel, it's for Dreambot but you can take the concepts he shows and apply them to basically any botting client

<https://dreambot.org/forums/index.php?/topic/20611-how-to-create-custom-listeners/> this is for Dreambot but you can probably apply a lot of it to other clients

<https://dreambot.org/forums/index.php?/topic/2910-a-pug-tutorial-all-about-making-the-best-paint/> some of these can be applied to other clients :smile:

<https://dreambot.org/forums/index.php?/topic/4510-easily-saveload-script-settings/> if you want to have script settings using a GUI :smile:

<https://discourse.rspeer.org/t/how-to-implement-script-arguments-into-a-script-with-jcommander/3791> implement cli into your scripts :)

<https://community.tribot.org/topic/38966-efficient-scripting/> - Some good ways to learn how to structure your code

<https://osbot.org/forum/topic/91620-tutorial-decorating-entities-an-alternative-to-static-libraries> pretty nice :)

<https://osbot.org/forum/topic/155701-tutorial-make-your-script-send-discord-messages> if your client doesn't have a discord api

<https://osbot.org/forum/topic/157464-tutorial-push-notifications-using-telegram-example-code-and-more> meh, if you have Telegram then ig it would be nice

<https://osbot.org/forum/topic/81168-improved-interact> this is on OSBot but can be applied to other clients very easily

<https://osbot.org/forum/topic/41900-beginners-guide-to-separating-classes> for the noobies :)
"""
    tut_message2 = """
    <https://community.tribot.org/topic/65825-tutorial-singleton-pattern/> kinda nice to know stuff about singleton's :)

    <https://community.tribot.org/topic/79682-proper-banking-add-randomization-and-real-success-checks/> eh, seems a bit pointless but to each their own

    <https://osbot.org/forum/topic/91620-tutorial-decorating-entities-an-alternative-to-static-libraries/> actually really useful

    <https://osbot.org/forum/topic/163538-snippet-getting-item-prices/> if your client doesn't have a native way of getting GE prices for an item :smile:

    <https://dreambot.org/forums/index.php?/topic/5791-java-tutorial-series/>

    <https://dreambot.org/forums/index.php?/topic/17883-edu-basic-scripting-all-you-need-to-start-coding/>

    <https://oldschool.runescape.wiki/w/RuneScape:Real-time_Prices> very recent addition that just recently happened afaik :smile: enjoy!

    <https://dreambot.org/forums/index.php?/topic/10490-configlistener/> ConfigListener (Basically varbits, so you can apply the same thing to varbits)
        """
    await ctx.send(tut_message)
    await ctx.send(tut_message2)


bot.run("ODI1NDk1MTM1MzYxODI2ODg2.YF-wQQ.845G47anM2Kp2yA5GcvspSsjZh4")
