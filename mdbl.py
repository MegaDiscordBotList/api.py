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
import asyncio
import subprocess

import signal

def keyboardInterruptHandler(signal, frame):
    print("[MDBL] Exiting... {} (ID: {})".format(bot.user.name, signal))
    exit(10)

__version__ = "7.3"

# Your id
owner = 'id'
# Admin IDS 
admins = ['id', 'id']

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def user_choice():
    return input("\n>>> ").lower().strip()

if IS_WINDOWS:
    plat = "Win"
else:
    plat = "Linux"

async def delete():
    # Delete your bot from MDBL
    try:
        channel = bot.get_channel("567208400891543552")
        await bot.send_message(channel, "```\n[DEBUG] Delete Screen```")
        print("WARNING: Are you sure you want to delete your bot from MDBL?")
        print("(y/n)")
        choice = user_choice()
        if choice == "y":
            print("Sending Delete Command!")
            try:
                await bot.send_message(channel, "@!botdel")
                print("[MDBL] Deleted your bot from the servers!")
                try:
                    os.remove("{}.json".format(bot.user.id))
                    print("[MDBL] Removed data file ({}.json)".format(bot.user.id))
                except:
                    pass
                asyncio.sleep(3)
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

async def pull(opt="console"):
    # Pull previous bot data
    try:
        if os.path.isfile('mdbl/{}.json'.format(bot.user.id)):
            with open('mdbl/{}.json'.format(bot.user.id)) as json_file:  
                data = json.load(json_file)
                for p in data['Bot']:
                    try:
                        channel = bot.get_channel("567208400891543552")
                        em = discord.Embed(description="Pulled data\n```ini\n! === Bot Data === !\nOS: {}\nServers: {}\nUsers: {}\nChannels: {}\nCommands: {}\n```".format(plat, p['Servers'], p['Users'], p['Channels'], p['Commands']))
                        em.set_footer(text="MDBL - https://mdbl.surge.sh/bot/{}".format(bot.user.id))
                        await bot.send_message(channel, embed=em)
                        if opt == "console":
                            print("----MDBL DATA----\n"
                                  "OS: {}\n"
                                  "Servers: {}\n"
                                  "Users: {}\n"
                                  "Channels: {}\n"
                                  "Commands: {}".format(plat, p['Servers'], p['Users'], p['Channels'], p['Commands']))
                        if opt == "say":
                            try:
                                em = discord.Embed(description="Pulled data\n```ini\n! === Bot Data === !\nOS: {}\nServers: {}\nUsers: {}\nChannels: {}\nCommands: {}\n```".format(plat, p['Servers'], p['Users'], p['Channels'], p['Commands']))
                                em.set_footer(text="MDBL - https://mdbl.surge.sh/bot/{}".format(bot.user.id))
                                await bot.send_message(channel, embed=em)
                            except:
                                print("[MDBL] Unable to send this message (mdbl.pull(bt, {}, {}))".format(bot.user.id, opt))
                    except Exception as e:
                        exc = '{}: {}'.format(type(e).__name__, e)
                        print("[MDBL] Unable to execute script!\n{}".format(exc))
        else:
            print("Nothing to pull :(")
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print("[MDBL] Unable to execute script!\n{}".format(exc))
    
async def post(servers=0, users=0, channels=0, commands=0):
    # Posts status
    try:
        print("[MDBL] Sending update command... If this doesn't change there must of been an error")
        try:
            channel = bot.get_channel("567208400891543552")
            await bot.send_message(channel, "@!update {} {} {} {}".format(servers, users, channels, commands))
            msg = await bot.wait_for_message(content='API = True')
            data = {}
            data['Bot'] = []
            data['Bot'].append({
                'Servers': servers,
                'Users': users,
                'Channels': channels,
                'Commands': cmds
                })
            with open('mdbl/{}.json'.format(bot.user.id), 'w') as outfile:
                json.dump(data, outfile) 
            return print("[MDBL]: Updated bot status (Guilds: {} | Users: {} | Channels: {} | Commands: {})".format(servers, users, channels, commands))
        except:
            print("[MDBL] Error sending or awaiting message!")
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print("[MDBL] Unable to execute script!\n{}".format(exc))

async def start(bt):
    # Start MDBL client
    global bot
    global servers
    global users
    global channels
    global cmds
    bot = bt
    cmds = len(bot.commands)
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    if os.path.isfile('mdbl/{}.json'.format(bot.user.id)):
        print("Starting Client...")
        asyncio.sleep(2)
        try:
            channel = bot.get_channel("567208400891543552")
            await bot.send_message(channel, "@!start")
            #msg = await bot.wait_for_message(content='True')
            print("[MDBL] Ready!")
            print("\n-----------MDBL-----------\n"
                  "Admins: {} | API: v{}".format(len(admins), __version__))
            signal.signal(signal.SIGINT, keyboardInterruptHandler)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print("[MDBL] Unable to execute script!\n{}".format(exc))
    else:
        try:
            subprocess.call(("mkdir", "mdbl"))
            data = {}
            data['Bot'] = []
            data['Bot'].append({
                'Servers': servers,
                'Users': users,
                'Channels': channels,
                'Commands': commands
                })
            with open('mdbl/{}.json'.format(bot.user.id), 'w') as outfile:
                json.dump(data, outfile)
            print("[MDBL] Setup data file... Restarting!")
            asyncio.sleep(2)
            await start(bot)
        except:
            await start(bot)
        
        


# (C) MegaDiscordBotList 2019
