# MDBL - Discord Bot Listing
# Last Updated: 6/5/2019

# https://mdbl.surge.sh
# https://github.com/MegaDiscordBotList

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import config
import json
import sys
import os

__version__ = "7.2"

owner = 'id'
admins = ['id', 'id']

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def user_choice():
    return input("\n>>> ").lower().strip()

if IS_WINDOWS:
    plat = "Win"
else:
    plat = "Linux"

async def delete(bt):
    # Delete your bot from MDBL
    bot = bt
    try:
        channel = bot.get_channel("567208400891543552")
        await bot.send_message(channel, "[DEBUG] Delete Screen")
        print("WARNING: Are you sure you want to delete your bot from MDBL?")
        print("(y/n)")
        choice = user_choice()
        if choice == "y":
            print("Sending Delete Command!")
            try:
                await bot.send_message(channel, "@!botdel")
                print("[MDBL] Deleted your bot from the servers!")
                print("\n"
                      "Current server count: {}".format(len(bot.servers)))
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print("[MDBL] Unable to execute script!\n{}".format(exc))
        else:
            print("Canceled!")
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print("[MDBL] Unable to execute script!\n{}".format(exc))

async def pull(bt, opt="console"):
    # Pull previous bot data
    bot = bt
    if os.path.isfile('{}.json'.format(bot.user.id)):
        with open('{}.json'.format(bot.user.id)) as json_file:  
            data = json.load(json_file)
            for p in data['Bot']:
                try:
                    channel = bot.get_channel("567208400891543552")
                    await bot.send_message(channel, "Pulled data\n```ini\n! === Bot Data === !\nOS: {}\nServers: {}\nUsers: {}\nChannels: {}\nCommands: {}\n```".format(plat, p['Servers'], p['Users'], p['Channels'], p['Commands']))
                    if opt == "console":
                        print("----MDBL DATA----\n"
                              "Servers: {}\n"
                              "Users: {}\n"
                              "Channels: {}\n"
                              "Commands: {}".format(p['Servers'], p['Users'], p['Channels'], p['Commands']))
                    if opt == "say":
                        try:
                            await bot.say("```ini\n! === Bot Data === !\nOS: {}\nServers: {}\nUsers: {}\nChannels: {}\nCommands: {}\n```".format(plat, p['Servers'], p['Users'], p['Channels'], p['Commands']))
                        except:
                            print("[MDBL] Unable to send this message (mdbl.pull(bt, {}, {}))".format(bot.user.id, opt))
                except Exception as e:
                    exc = '{}: {}'.format(type(e).__name__, e)
                    print("[MDBL] Unable to execute script!\n{}".format(exc))
    else:
        print("Nothing to pull :(")
    
async def post(bt, servers=0, users=0, channels=0, commands=0):
    # Posts status
    bot = bt
    try:
        print("\n-----------MDBL-----------\n"
              "Admins: {} | API: v{}".format(len(admins), __version__))
        print("\nSending update command... If this doesn't change there must of been an error")
        channel = bot.get_channel("567208400891543552")
        try:
            await bot.send_message(channel, "@!update {} {} {} {}".format(servers, users, channels, commands))
            msg = await bot.wait_for_message(content='API = True')
            data = {}
            data['Bot'] = []
            data['Bot'].append({
                'Servers': servers,
                'Users': users,
                'Channels': channels,
                'Commands': commands
                })
            with open('{}.json'.format(bot.user.id), 'w') as outfile:
                json.dump(data, outfile) 
            return print("[MDBL]: Updated bot status (Guilds: {} | Users: {} | Channels: {} | Commands: {})".format(servers, users, channels, commands))
        except:
            print("[MDBL] Error sending or awaiting message!")
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print("[MDBL] Unable to execute script!\n{}".format(exc))

# (C) MegaDiscordBotList 2019
