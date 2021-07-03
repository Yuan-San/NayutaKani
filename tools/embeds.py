import discord

def accnotfound():
  embed=discord.Embed(title="❌ Account is not registered!", description="It seems like your Account is not Registered or Unreadable!", color=0x0000ff)
  embed.add_field(name="Try this:", value="-Register your account by typing `nayu bank register`.\n-Try again later.\n-Report Bug if this problem still occurs.", inline=False)
  
  return embed

def shop():
  shopembed=discord.Embed(title="NayuShop: Moonlight Bakery", description="Showing Moonlight Bakery Items on sale: 2 Total.", color=0x800000)
  shopembed.set_author(name="[Link] • Owned by Akira", url="https://discord.gg/mZWkufa6Bq", icon_url="https://media.discordapp.net/attachments/831740920939937796/844050735061532672/ba91aad2a9563eba28a36666b1549be0.png")
  shopembed.set_thumbnail(url="https://wallpaperaccess.com/full/5056828.jpg")
  shopembed.add_field(name="1.Custom Movies • 3000Rp", value="Sets your own cinema in this server for 1 movie!", inline=False)
  shopembed.add_field(name="2. Private Room Pass • 30000Rp • Limited Stock!", value="Your own House in this server? yes. Only you and person you invite will be able to see and chat in your channel", inline=True)
  shopembed.set_footer(text="NayuShop: Offline")
  return shopembed

def help(name, utctime):
  embed=discord.Embed(title="⌘ Start", description="Welcome, <@{}>! Nayuta Kani current prefix is `nayu`.\n———————————————————".format(name), color=0x000080)
  embed.add_field(name="◈ Recommended:", value="-`bank register` Register your account to Nayuta Kani now! \n-`bank` Opens your Account Info.\n-`daily` Get your daily prize now!\n", inline=False)
  embed.add_field(name="◈ All Commands:", value="◇ **Game Commands:**\n- `rob [amount]` Bet an amount of Rp and try and steal some more\n- `srob` robs with 300 Rp\n- `daily` Receive Rp every 24 hours\n- `numgame` Starts a number guessing game\n- `roulette` If you win, you double your Rp\n- `work` Work for 1 hour and get some sweet amount of Rp !\n\n◇ **Currency Commands:**\n- `top` Displays the users with the most amount of Rp!\n- `bank` Displays curent balance of bank account\n- `bank register` Registers a bank account\n- `bank [@username]` Check the balance of anyone that you @mention\n- `pay [@username] [amount]` Allows you to give money to users that you @mention\n\n◇ **Utility Commands:**\n- `who` Says who you are\n- `count:` Lists the number of users registered\n- `messages` Lists the amount of messages you have sent\n- `definition [word]` Finds the meaning of the word supplied", inline=False)
  embed.set_footer(text="UTC Time: {}, Prefix: 'nayu', Running v2021.06.04.2.".format(utctime))

  return embed

def successreg(name):
 fmt = discord.Embed(title="⌘ Welcome", description="Welcome to Nayuta Kani, <@{}>. Type `nayu start` / `nayu help` to get Started.".format(name), color=0x000080)
 return fmt