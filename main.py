import random
import asyncio
from accfolder import account
from TRPG import attributetrpg
import discord
import platform
import os
from discord.ext import commands
from alive import alive
from datetime import datetime 
from asyncio import sleep as aiosleep


bot = commands.Bot(command_prefix=commands.when_mentioned_or('nayu '), case_insensitive=True )
bot.remove_command("help")

utctime = datetime.utcnow()


#Test Playground

#End Playground

#Bank
@bot.command()
async def bank(ctx, regi: str = None):
    if regi is None:
        if account.bal(ctx.message.author.id) is None:
            embed=discord.Embed(title="❌ Account is not registered!", description="It seems like your Account is not Registered or Unreadable!", color=0x0000ff)
            embed.add_field(name="Try this:", value="-Register your account by typing `nayu bank register`.\n-Try again later.\n-Report Bug if this problem still occurs.", inline=True)
            await ctx.send(embed=embed)
            return
        else:
            embed = discord.Embed(title="Bank Account info:",
                                  colour=discord.Colour(0xf5a623),
                                  description="Your balance is: `{}`".format(
                                      account.bal(ctx.message.author.id)))
            await ctx.send(embed=embed)
            return
    elif regi == "register":
      if account.register(ctx.message.author.id) is None:
          await ctx.send("Your Account is already Registered. Type `nayu start` for help.")
      else:
        fmt=discord.embed(title="⌘ Welcome", description="Welcome to Nayuta Kani, <@{}>. Type `nayu start` / `nayu help` to get Started.".format(ctx.message.author.id), color=0x000080)
        fmr = await ctx.send(account.register(ctx.message.author.id))
        await aiosleep(5)
        await fmr.edit(
          "Your Account Was Ready to Use."
        )
        await ctx.send(embed=fmt)
      return
    elif regi.startswith("<@!"):
      await ctx.send("That user is a bot and can't open balance.")
    elif regi.startswith("<@"):
        print(regi.strip("<@>"))
        if account.bal(regi.strip("<@>")) is None:
            await ctx.send(
                "That user does not exist or has not registered a bank account."
            )
            return
    else:
            user = await bot.fetch_user(int(regi.strip("<@>")))
            embed = discord.Embed(title="Bank Account info:",
                                  colour=discord.Colour(0xf5a623),
                                  description="{}'s balance is: `{}`".format(
                                      user.display_name,
                                      account.bal(regi.strip("<@>"))))
            await ctx.send(embed=embed)
            return


@bot.command(aliases=['bal', 'account', 'profile', 'me'])
async def balance(ctx, regi: str = None):
    if regi is None:
        if account.bal(ctx.message.author.id) is None:
            embed=discord.Embed(title="❌ Account is not registered!", description="It seems like your Account is not Registered or Unreadable!", color=0x008000)
            embed.add_field(name="Try this:", value="-Register your account by typing `nayu bank register`.\n-Try again later.\n-Report Bug if this problem still occurs.", inline=True)
            await ctx.send(embed=embed)
            return
        else:
            embed = discord.Embed(title="Account info:",
                                  colour=discord.Colour(0xf5a623),
                                  description="Your balance is: `{}`".format(
                                      account.bal(ctx.message.author.id)))
            await ctx.send(embed=embed)
            return
    elif regi.startswith("<@!"):
        await ctx.send("That user is a bot and cannot have an account")
        return
    elif regi.startswith("<@"):
        print(regi.strip("<@>"))
        if account.bal(regi.strip("<@>")) is None:
            await ctx.send(
                "That user does not exist or has not registered a bank account."
            )
            return
        else:
            user = await bot.fetch_user(int(regi.strip("<@>")))
            embed = discord.Embed(title="Bank Account info:",
                                  colour=discord.Colour(0xf5a623),
                                  description="{}'s balance is: `{}`".format(
                                      user.display_name,
                                      account.bal(regi.strip("<@>"))))
            await ctx.send(embed=embed)
            return

#Top
@bot.command()
async def top(ctx):
    leadboard = account.top()
    name1 = await bot.fetch_user(leadboard[0][0])
    name2 = await bot.fetch_user(leadboard[1][0])
    name3 = await bot.fetch_user(leadboard[2][0])
    name4 = await bot.fetch_user(leadboard[3][0])
    name5 = await bot.fetch_user(leadboard[4][0])

    fmt = '1.`{0.display_name}`: {1}2.`{2.display_name}`: {3}3.`{4.display_name}`: {5}4.`{6.display_name}`: {7}5.`{8.display_name}`: {9}'
    board = fmt.format(name1, leadboard[0][1] + '\n', name2,
                       leadboard[1][1] + '\n', name3, leadboard[2][1] + '\n',
                       name4, leadboard[3][1] + '\n', name5, leadboard[4][1])

    embed = discord.Embed(title="Leaderboard",
                          colour=discord.Colour(0x724ded),
                          description=board)
    await ctx.send(embed=embed)


#Pay
@bot.command()
async def pay(ctx, user: str = None, amount=None):
    if user is None:
        await ctx.send(
            "Please specify the target user using this format: `nayu pay @USERNAME AMOUNT`"
        )
        return
    if amount is None:
        await ctx.send(
            "Please specify the payment amount using this format: `nayu pay @USERNAME AMOUNT`"
        )
        return
    try:
        amount = int(amount)
    except ValueError:
        await ctx.send("Please only use whole numbers")
        return
    await ctx.send(
        account.pay(ctx.message.author.id, user.strip("<@>"), amount))


#Daily
@bot.command()
async def daily(ctx):
    await ctx.send(account.payday(ctx.message.author.id))


#Where
@bot.command()
async def where(ctx):
    await ctx.send("I'm Here!")


#Number Guessing Game
@bot.command()
async def numgame(ctx):
    if account.bal(ctx.message.author.id) is None:
        await ctx.send("Please register first using `nayu bank register`")
        return

    await ctx.send('Guess a number between 1 to 100')

    answer = random.randint(1, 100)
    guessnumber = 0

    def guess_check(m):
        return m.content.isdigit() and m.author == ctx.message.author

    while guessnumber < 10:
        guessnumber = guessnumber + 1

        try:
            guess = await bot.wait_for('message',
                                       check=guess_check,
                                       timeout=10.0)
        except asyncio.TimeoutError:
            fmt = 'Sorry, you took too long. It was {}.'
            await ctx.send(fmt.format(answer))
            break
        else:
            await ctx.send(
                account.numgame(ctx.message.author.id, int(guess.content),
                                guessnumber, answer))

        if int(guess.content) == answer:
            break


@bot.command()
async def rob(ctx, ramount=None):
    if ramount is None:
        await ctx.send(
            "Please supply the amount you are robbing with using this format: `nayu rob [AMOUNT]`"
        )
        return
    try:
        ramount = int(ramount)
    except ValueError:
        await ctx.send("Please only use whole numbers")
    await ctx.send(account.rob(ctx.message.author.id, ramount))


@bot.command()
async def buy(ctx, itemid: int = None):
  if itemid is None:
    await ctx.send("Please type the id of the item you want to buy `nayu buy 1-2`.")
    return
  try:
      itemid = int(itemid)
  except ValueError:
      await ctx.send("Please only use whole numbers")
      return
  await ctx.send(account.buy(ctx.message.author.id, itemid))

#Srob
@bot.command()
async def srob(ctx):
    await ctx.send(account.rob(ctx.message.author.id, 300))


#Roulette
@bot.command()
async def roulette(ctx):

    answer = None
    while answer not in ('y', 'n'):
        await ctx.send(
            'Are you sure you want to do this? If you lose, then all your money will be gone. (y or n)'
        )

        def check(m):
            return m.author == ctx.message.author

        try:
            answer = (await bot.wait_for('message', timeout=10.0, check=check))
        except asyncio.TimeoutError:
            await ctx.send('Hey, why are you not responding?! :rage:')
            return

        answer = answer.content.lower()

        if answer == 'y':
            await ctx.send(account.roulette(ctx.message.author.id))
        elif answer == 'n':
            await ctx.send('That\'s ok, WIMP! :grin:')
        else:
            await ctx.send('Type "y" or "n", pleaseeee.:upside_down:')
            await asyncio.sleep(0.5)


@bot.command()
async def work(ctx):
    await ctx.send(account.work(ctx.message.author.id))


#Definition
@bot.command()
async def definition(ctx, *, word: str = None):
    await ctx.send(account.definition(word))


#Count
@bot.command()
async def count(ctx):
    await ctx.send("There are {} users registered".format(account.count()))


#Who
@bot.command()
async def who(ctx):
    await ctx.send("You are **{}**!".format(ctx.message.author))


#Messages
@bot.command()
async def messages(ctx):
    tmp = await ctx.send('Calculating messages...')
    counter = 0
    counter2 = 0
    async for log in ctx.history(limit=1000):
        counter2 += 1
        if log.author == ctx.message.author:
            counter += 1

    await tmp.edit(
        content=
        'You have sent {} messages out of the last {}. This is roughly {}% of them'
        .format(counter, counter2, (counter * 100) // counter2))


@bot.command(aliases=['h', 'cmds', 'commands', 'command', 'start'])
async def help(ctx):
        embed=discord.Embed(title="⌘ Start", description="Welcome, <@{}>! Nayuta Kani current prefix is `nayu`.\n———————————————————".format (ctx.message.author.id), color=0x000080)
        embed.add_field(name="◈ Recommended:", value="-`bank register` Register your account to Nayuta Kani now! \n-`bank` Opens your Account Info.\n-`daily` Get your daily prize now!\n", inline=False)
        embed.add_field(name="◈ All Commands:", value="◇ **Game Commands:**\n- `rob [amount]` Bet an amount of Rp and try and steal some more\n- `srob` robs with 300 Rp\n- `daily` Receive Rp every 24 hours\n- `numgame` Starts a number guessing game\n- `roulette` If you win, you double your Rp\n- `work` Work for 1 hour and get some sweet amount of Rp !\n\n◇ **Currency Commands:**\n- `top` Displays the users with the most amount of Rp!\n- `bank` Displays curent balance of bank account\n- `bank register` Registers a bank account\n- `bank [@username]` Check the balance of anyone that you @mention\n- `pay [@username] [amount]` Allows you to give money to users that you @mention\n\n◇ **Utility Commands:**\n- `who` Says who you are\n- `count:` Lists the number of users registered\n- `messages` Lists the amount of messages you have sent\n- `definition [word]` Finds the meaning of the word supplied", inline=False)
        embed.set_footer(text="UTC Time: {}, Prefix: 'nayu', Running v2021.06.04.2.".format(utctime))
        await ctx.message.author.send(embed=embed)


#Moonlight Shop
@bot.command()
async def shop(ctx):
    shopembed=discord.Embed(title="NayuShop: Moonlight Bakery", description="Showing Moonlight Bakery Items on sale: 2 Total.", color=0x800000)
    shopembed.set_author(name="[Link] • Owned by Akira", url="https://discord.gg/mZWkufa6Bq", icon_url="https://media.discordapp.net/attachments/831740920939937796/844050735061532672/ba91aad2a9563eba28a36666b1549be0.png")
    shopembed.set_thumbnail(url="https://wallpaperaccess.com/full/5056828.jpg")
    shopembed.add_field(name="1.Custom Movies • 3000Rp", value="Sets your own cinema in this server for 1 movie!", inline=False)
    shopembed.add_field(name="2. Private Room Pass • 30000Rp • Limited Stock!", value="Your own House in this server? yes. Only you and person you invite will be able to see and chat in your channel", inline=True)
    shopembed.set_footer(text="NayuShop: Offline")
    await ctx.send(embed=shopembed)

#Help
@bot.event
async def on_ready():
    print('Bot logged in as')
    print('Username: ' + bot.user.name)
    print('Id: ' + str(bot.user.id))
    print('--------')
    print(
        f'| Connected to {str(len(bot.guilds))} servers | Connected to {str(len(set(bot.get_all_members())))} users |'
    )
    print(' Servers include:')
    for item in bot.guilds:
        print('  - {}'.format(item.name))
    print('--------')
    print(
        f'Current Discord.py Version: {discord.__version__} | Current Python Version: {platform.python_version()}'
    )
    print('--------')
    print(f'Use this link to invite {bot.user.name}:')
    print(
        f'https://discordapp.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8'
    )
    print('--------')
    print('Status:')
    print('Core: ONLINE')
    print('Shop: OFFLINE')
    print('TRPG: OFFLINE')
    print('CSV, Replit: ONLINE')
    print('--------')

    return await bot.change_presence(activity=discord.Game(
        name='⌘ Nayu Start'))
    
@bot.command()
async def donate(ctx):
  donateembed=discord.Embed(title="Donations!", url="https://www.patreon.com/yuanarib", description="Support Nayuta Kani by Donating via Patreon, or by Boosting this server!")
  donateembed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1283496547624210432/CaCsxhzc.jpg")
  donateembed.add_field(name="Get Server and Bot Special Perks by Donating or by Boosting this server!", value="Read this down to see Donate perks", inline=False)
  donateembed.add_field(name="Perks Included: ", value=" -Patreon/Booster Badge (based by donation type)\n -Cooldown Reduction\n -20% bonus $ at Daily\n -Shop discount every week. ", inline=False)
  donateembed.add_field(name="How to claim Donator perks:", value="DM <@714207165350543403>, or the server owner to claim.", inline=False)
  donateembed.set_footer(text="Nayuta Kani Bot")
  await ctx.send(embed=donateembed)

alive()
bot.run(os.getenv('TOKEN'))