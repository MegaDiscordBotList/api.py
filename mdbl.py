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
import time
import signal

__version__ = "7.5"

# Your id
owner = 'id'
# Admin IDS 
admins = ['id', 'id']

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def user_choice():
    return input("\n>>> ").lower().strip()

def keyboardInterruptHandler(signal, frame):
    if hiddenmdbl == True:
        exit(10)
    else:
        print("[MDBL] Exiting... {} (ID: {})".format(bot.user.name, signal))
        print("\n"
              "Would you like to give feedback? (y/n)")
        choice = user_choice()
        if choice == "y":
            print("Enter a message :D")
            try:
                ch = user_choice()
                channel = bot.get_channel("575258216137752577")
                localtime = time.asctime( time.localtime(time.time()) )
                data = {}
                data['Bot'] = []
                data['Bot'].append({
                    'Msg': "{}".format(ch),
                    'Time': "{}".format(localtime)
                    })
                with open('mdbl/msg.json'.format(bot.user.id), 'w') as outfile:
                    json.dump(data, outfile)
                print("Message will be sent on client startup!")
                exit(10)
            except:
                print("[MDBL] Error sending message exiting...")
                exit(10)
        else:
            exit(10)

if IS_WINDOWS:
    plat = "Win"
else:
    plat = "Linux"

async def delete():
    # Delete your bot from MDBL
    try:
        channel = apic
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

async def pull(opt="console", chan = discord.Channel.id == ""):
    # Pull previous bot data
    try:
        if os.path.isfile('mdbl/{}.json'.format(bot.user.id)):
            with open('mdbl/{}.json'.format(bot.user.id)) as json_file:  
                data = json.load(json_file)
                for p in data['Bot']:
                    try:
                        channel = apic
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
                        if opt == "send":
                            if chan == "":
                                print("[MDBL] Cant send because you have not entered an id")
                            else:
                                try:
                                    chaa = bot.get_channel(chan)
                                    em = discord.Embed(description="MDBL bot data for {}\n```ini\n! === Bot Data === !\nOS: {}\nServers: {}\nUsers: {}\nChannels: {}\nCommands: {}\n```".format(bot.user.name, plat, p['Servers'], p['Users'], p['Channels'], p['Commands']))
                                    em.set_footer(text="MDBL - https://mdbl.surge.sh/bot/{}".format(bot.user.id))
                                    await bot.send_message(chaa, embed=em)
                                except:
                                    print("[MDBL] Unable to send message to '{}'!".format(chan))
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
        if hiddenmdbl == True:
            pass
        else:
            print("[MDBL] Sending update command... If this doesn't change there must of been an error")
        try:
            await bot.send_message(apic, "@!update {} {} {} {}".format(servers, users, channels, commands))
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
            if hiddenmdbl == True:
                pass
            else:
                return print("[MDBL]: Updated bot status (Guilds: {} | Users: {} | Channels: {} | Commands: {})".format(servers, users, channels, commands))
        except:
            print("[MDBL] Error sending or awaiting message!")
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print("[MDBL] Unable to execute script!\n{}".format(exc))

async def start(bt, hidden=""):
    # Start MDBL client
    global bot
    global servers
    global users
    global channels
    global cmds
    global hiddenmdbl
    global apic
    if hidden == "":
        hiddenmdbl = False
    if hidden == "h":
        hiddenmdbl = True
    bot = bt
    apic = bot.get_channel("567208400891543552")
    cmds = len(bot.commands)
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    if os.path.isfile('mdbl/{}.json'.format(bot.user.id)):
        print("Starting Client... {}".format(bot.user.name))
        time.sleep(2)
        try:
            await bot.send_message(apic, "@!start")
            #msg = await bot.wait_for_message(content='True')
            if os.path.isfile('mdbl/msg.json'):
                cha = bot.get_channel("575258216137752577")
                with open('mdbl/msg.json') as json_file:  
                    data = json.load(json_file)
                    for p in data['Bot']:
                        # If this is spammed your bot will be instantly banned!
                        # its fine if you actually want help but otherwise dont be dumb :D
                        await bot.send_message(cha, "__**FEEDBACK**__\n"
                                                    "```\n"
                                                    "{}\n"
                                                    "```\n"
                                                    "**{}**".format(p['Msg'], p['Time']))
                        os.remove("mdbl/msg.json")
                        print("[MDBL] Message Sent!")
            else:
                pass
            print("[MDBL] Ready!")
            time.sleep(1)
            if hiddenmdbl == True:
                pass
            else:
                print("\n-----------MDBL-----------\n"
                      "Admins: {} | API: v{} | Discord.py: {} | Loaded Globals: {}\n"
                      "https://mdbl.surge.sh/bot/{}\n"
                      "----------------------------\n".format(len(admins), __version__, discord.__version__, len(globals()), bot.user.id))
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
            data = {}
            data['Config'] = []
            data['Config'].append({
                'Feedback_msg': "True"
                })
            with open('mdbl/config.json', 'w') as outfile:
                json.dump(data, outfile)
            print("[MDBL] Setup data file... Restarting!")
            asyncio.sleep(2)
            await start(bot)
        except:
            await start(bot)
        
        


# (C) MegaDiscordBotList 2019

# When MDBL is loaded it will say this
print("[MDBL] MDBL has been loaded!")
print("----------------------------\n")
time.sleep(2)
