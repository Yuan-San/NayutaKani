import csv
import time
import random
import pandas as pd
import discord
try:
    import wikipedia
except ImportError:
    WikiWork = False
else:
    WikiWork = True


def count():
    df = pd.read_csv('accounts.csv')
    return len(df.index)


def bump(name):
  df = pd.read_csv('accounts.csv')
  df.loc[df["UserId"] == int(name), "Balance"] += 2000
  return "Thanks for Bumping this server! <3.\nPS: I put 1000Rp on your wallet for a reward! Please bump again another time!"


def register(name):
    df = pd.read_csv('accounts.csv')

    if (df["UserId"] == int(name)).any():
        return "You already registered :P"
    else:
        with open('accounts.csv', 'a', newline='') as fd:
            fdw = csv.writer(fd)
            fdw.writerow([name, 0, 0, 0, 0, 0, 0, 0, 0])
        return "Bank registered! Thanks for Registering! You got 1000Rp"


def bal(name):
    df = pd.read_csv('accounts.csv')

    if (df["UserId"] == int(name)).any():
        return int(df.loc[df["UserId"] == int(name), "Balance"])
    else:
        return None


def top():
    global top, top2, top3, top4, top5
    df = pd.read_csv('accounts.csv')
    df = df.sort_values(by=["Balance"], ascending=[0])
    df.to_csv('accounts.csv', index=False)

    with open('accounts.csv', 'r') as readin:
        counter = 0
        leaderboard = []

        next(readin)
        for row in readin:
            counter += 1
            if counter <= 5:
                leaderboard.append(row.split(','))

        if len(leaderboard) < 5:
            while len(leaderboard) < 5:
                leaderboard.append(['838945094676512778', '0'])

        return leaderboard


def pay(startuser, enduser, amount):
    if amount < 1:
        return 'The minimum amount of <:bean_silver:840499858771148820> is 1'
    balnum = bal(startuser)
    if balnum is None:
        return "Please register first using `nayu bank register`"
    if amount > int(balnum):
        return 'You do not have enough rp. Use `nayu bank` to see your current balance'

    df = pd.read_csv('accounts.csv')

    if (df["UserId"] == int(enduser)).any():
        df = pd.read_csv('accounts.csv')
        df.loc[df["UserId"] == int(enduser), "Balance"] += amount
        df.to_csv('accounts.csv', index=False)

        df = pd.read_csv('accounts.csv')
        df.loc[df["UserId"] == int(startuser), "Balance"] -= amount
        df.to_csv('accounts.csv', index=False)

        return 'Payment successful!'
        print(f'Payment by {startuser} to {enduser} with amount of {amount} is successful.')
    else:
        return "That user does not exist or has not registered a bank account."


def payday(name):
    df = pd.read_csv('accounts.csv')

    if (df["UserId"] == int(name)).any():
        timer = int(df.loc[df["UserId"] == int(name), "Payday"])

    if (df["UserId"] == int(name)).any():
        donor = int(df.loc[df["UserId"] == int(name), "Donator"])

    if donor == 1:
      timeleft = int(time.time() - timer)
      timeleft = 64.800 - timeleft
      if timeleft > 0:
            typeT = 'seconds'
            if timeleft > 60:
                timeleft = timeleft // 60
                typeT = 'minutes'
                if timeleft > 60:
                   timeleft = timeleft // 60
                   typeT = 'hours'

            fmt = 'You still have to wait {} {}!'
            return fmt.format(timeleft, typeT)


      df.loc[df["UserId"] == int(name), "Balance"] += 5000
      df.loc[df["UserId"] == int(name), "Payday"] = time.time()
      df.to_csv('accounts.csv', index=False)

    return 'You just got 5000 Rp from opening your daily mailbox!'
     

    if donor == 0:
        timeleft = int(time.time() - timer)
        timeleft = 86.400 - timeleft
        if timeleft > 0:
            typeT = 'seconds'
            if timeleft > 60:
                timeleft = timeleft // 60
                typeT = 'minutes'
                if timeleft > 60:
                   timeleft = timeleft // 60
                   typeT = 'hours'

            fmt = 'You still have to wait {} {}!'
            return fmt.format(timeleft, typeT)


        df.loc[df["UserId"] == int(name), "Balance"] += 2000
        df.loc[df["UserId"] == int(name), "Payday"] = time.time()
        df.to_csv('accounts.csv', index=False)
    else:
        return "Please register first using `nayu bank register`"

    return 'You just got 2000 Rp from opening your daily mailbox!'


def numgame(name, guess, guessnum, answer):
    if guess == answer:
        reward = {1: 1000, 2: 900, 3: 750, 4: 600, 5: 450, 6: 300}

        fmt = "You are right! You guessed it in {} guesses. As a reward, you get {} <:bean_silver:840499858771148820>"

        df = pd.read_csv('accounts.csv')
        df.loc[df["UserId"] == int(name), "Balance"] += reward[guessnum]
        df.to_csv('accounts.csv', index=False)

        return fmt.format(guessnum, reward[guessnum])

    elif guessnum != 6:
        if guess < answer:
            return 'The number is higher'
        if guess > answer:
            return 'The number is lower'

    if guessnum == 10 and guess != answer:
            fmt = 'You did not guess the number in time. It was {}'
            return fmt.format(answer)

def shop(server):
  if server == "moonlight":
    embed=discord.Embed(title="Moonlight's Bakery Official Shop", description="Buy some in-server items from this server! :)", color=0x800000)
    embed.set_author(name="Click here to get the invite link • Owned by Akira", url="https://discord.gg/mZWkufa6Bq", icon_url="https://media.discordapp.net/attachments/831740920939937796/844050735061532672/ba91aad2a9563eba28a36666b1549be0.png")
    embed.set_thumbnail(url="https://wallpaperaccess.com/full/5056828.jpg")
    embed.add_field(name="1. <:cinema~1:840533281069858827> Custom Movies • 3000Rp", value="Sets your own cinema in this server for 1 movie!", inline=False)
    embed.add_field(name="2. <:privateroom:840533258475405320> Private Room Pass • 30000Rp • Limited Stock!", value="Your own House in this server? yes. Only you and person you invite will be able to see and chat in your channel", inline=True)
    embed.set_footer(text="Nayuta Kani Bot • Type nayu buy [item number] to buy an item. Example: nayu buy 1")
    return embed


def buy(name, item):
  df = pd.read_csv('accounts.csv')

  if (df["UserId"] == int(name)).any():
    balbuy = int(df.loc[df["UserId"] == int(name), "Balance"])
    if item == 1:
     if balbuy < 3000:
      return 'You don\'t have enough money to buy this. Earn money by claiming daily rewards and working! ^^'
     else:
        df = pd.read_csv('accounts.csv')
        df.loc[df["UserId"] == int(name), "Balance"] -= 3000
        df.loc[df["UserId"] == int(name), "CC"] += 1
        df.to_csv('accounts.csv', index=False)
        return 'Thanks for Purchasing! You\'re given 1 Custom Cinema Pass in your inventory'
    if item == 2:
     if balbuy < 30000:
      return 'You don\'t have enough money to buy this. Earn money by claiming daily rewards and working! ^^'
     else:
        df = pd.read_csv('accounts.csv')
        df.loc[df["UserId"] == int(name), "Balance"] -= 30000
        df.loc[df["UserId"] == int(name), "PR"] += 1
        df.to_csv('accounts.csv', index=False)
        return 'Thanks for Purchasing! You\'re given 1 Private Room Pass in your inventory'
    


def rob(name, ramount):

    df = pd.read_csv('accounts.csv')

    if (df["UserId"] == int(name)).any():
        timer = int(df.loc[df["UserId"] == int(name), "Rob"])
        balrob = int(df.loc[df["UserId"] == int(name), "Balance"])
    else:
        return "Please register first using `nayu bank register`"

    timeleft = int(time.time()-timer)
    timeleft = 60 - timeleft
    if timeleft > 0:
        fmt = 'You still have to wait {} seconds!'
        return fmt.format(timeleft)

    if ramount > 300:
        return 'The maximum amount of <:bean_silver:840499858771148820> is 300'
    elif ramount < 1:
        return 'The minimum amount of <:bean_silver:840499858771148820> is 1'
    elif balrob < ramount:
        return 'You do not have enough <:bean_silver:840499858771148820>. Use nayu bank to see your current balance'
    else:
        if ramount > 249:
            chance = 65
        elif ramount > 200:
            chance = 60
        elif ramount > 149:
            chance = 55
        elif ramount > 100:
            chance = 50
        elif ramount > 0:
            chance = 45

    chancenum = random.randint(0, 100)
    if chancenum <= chance:
        df = pd.read_csv('accounts.csv')
        df.loc[df["UserId"] == int(name), "Balance"] += ramount
        df.loc[df["UserId"] == int(name), "Rob"] = time.time()
        df.to_csv('accounts.csv', index=False)
        return 'Congrats!, you doubled your {} <:bean_silver:840499858771148820>'.format(ramount)
    else:
        df = pd.read_csv('accounts.csv')
        df.loc[df["UserId"] == int(name), "Balance"] -= ramount
        df.loc[df["UserId"] == int(name), "Rob"] = time.time()
        df.to_csv('accounts.csv', index=False)
        return 'Sorry, you got caught. You lost {} <:bean_silver:840499858771148820>'.format(ramount)


def definition(word):
    if WikiWork:
        if word is None:
            return "Please supply the word you are defining using this format: `nayu definition WORD`"
        try:
            wp = wikipedia.summary(word, sentences=2)
            return wp
        except wikipedia.DisambiguationError:
            return "Please be more specific. That word is too ambiguous"
    else:
        return 'The bot owner has not installed the Wikipedia package.'


def roulette(name):
    df = pd.read_csv('accounts.csv')

    if (df["UserId"] == int(name)).any():
        timer = int(df.loc[df["UserId"] == int(name), "Roulette"])
    else:
        return "Please register first using `nayu bank register`"

    timeleft = int(time.time() - timer)
    timeleft = 3600 - timeleft

    if timeleft > 0:
        typeT = 'seconds'
        if timeleft > 60:
            timeleft = timeleft // 60 + 1
            typeT = 'minutes'
            if timeleft > 60:
                timeleft = timeleft // 60
                typeT = 'hours'

        fmt = 'You still have to wait {} {}!'
        return fmt.format(timeleft, typeT)

    num = random.randint(1, 6)
    if num == 1:
        df.loc[df["UserId"] == int(name), "Balance"] = (bal(name) * 2)
        df.loc[df["UserId"] == int(name), "Roulette"] = time.time()
        df.to_csv('accounts.csv', index=False)
        return 'You are safe! Your balance has doubled!'
    else:
        df.loc[df["UserId"] == int(name), "Balance"] = 0
        df.loc[df["UserId"] == int(name), "Roulette"] = time.time()
        df.to_csv('accounts.csv', index=False)
        return 'BOOM! You are dead. :('

def work(name):
   df = pd.read_csv('accounts.csv')

   if (df["UserId"] == int(name)).any():
        timer = int(df.loc[df["UserId"] == int(name), "Work"])
   else:
        return "Please register first using `nayu bank register`"

   timeleft = int(time.time() - timer)
   timeleft = 1800 - timeleft

   if timeleft > 0:
        typeT = 'seconds'
        if timeleft > 60:
            timeleft = timeleft // 60 + 1
            typeT = 'minutes'
            if timeleft > 60:
                timeleft = timeleft // 60
                typeT = 'hours'

        fmt = 'You still have to wait {} {}!'
        return fmt.format(timeleft, typeT)

   cash = random.randint(300, 600)
   df.loc[df["UserId"] == int(name), "Balance"] = (bal(name) + cash)
   df.loc[df["UserId"] == int(name), "Work"] = time.time()
   df.to_csv('accounts.csv', index=False)
   wtl = 'You got {} <:bean_silver:840499858771148820> for an hour of work! Do this again in the next 30 minutes!'
   return wtl.format(cash)