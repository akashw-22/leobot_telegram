from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import datetime

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN = 'TOKEN'                                         #add your bots token
launch_date = datetime.datetime(2021, 9, 25)


def start(update, context):
    context.bot.sendMessage(chat_id = update.effective_chat.id, text = "hey")


def welcome(update, context, new_member):                      #welcome message
    reply = f'''Welcome @{new_member.username} to Windmill, the next generation decentralized eco-friendly utility token. You can also reach us at:

Website: http://windmilltoken.com

Twitter: https://mobile.twitter.com/WindMillOffici1

Reddit: https://www.reddit.com/user/Official_Windmill/

Facebook: https://www.facebook.com/Windmill-Token-106614645101945

Discord: https://discord.gg/eUq6uJQsKh

YouTube Channel: https://www.youtube.com/channel/UCxpbYiBzUvDgYP8wGN-YZCg'''
    context.bot.sendMessage(chat_id = update.effective_chat.id, text = reply)




def message(update, context):                                       #all the message replies

    #print(update.message.text)
    #print(update.message.new_chat_members)

    text = update.message.text.lower()
    reply = ''
    user = update.message.from_user.username

    if text[:3] == 'hi ' or text == 'hi':
        reply = f"Hello @{user}, How are you Windmill Warrior"

    if text == 'when bmw?':
        reply = 'Bro you lack taste. Get your lambo'

    if text == 'who are you leo?':
        reply = "I'm Leonidas. Windmill rescued me on July 15th! First of many charitable initiatives on the horizon."

    if f" {'launch'} " in f" {text} ":
        if datetime.datetime.now() > launch_date:
            reply = "We started our service on 25th September"
        reply = "We'll be launching on 25th September in Pancakeswap"

    if f" {'presale'} " in f" {text} ":
        reply = "It's a Fairlaunch, We want to be fair to the whole community."

    if f" {'love'} " in f" {text} " or f" {'❤️'} " in f" {text} ":
        reply = 'Leo gives you the love back ❤️\n'

    if reply != '':
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = reply)


def greeting(update, context):                              #the greeting message for each new user

    #print(update.message.new_chat_members)
    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            #print(new_member)
            if new_member.is_bot == False:
                return welcome(update, context, new_member)


def contract(update, context):                              #for /contract command
    'dispalys the contract'

    reply = '0x7cc620917fb2c96a2aaf412aad664fb210fc3068'
    context.bot.sendMessage(chat_id = update.effective_chat.id, text = reply)


def social(update, context):                                #for /social command
    'displays our social media platforms'

    reply = """Website: http://windmilltoken.com

Twitter: https://mobile.twitter.com/WindMillOffici1

Reddit: https://www.reddit.com/user/Official_Windmill/

Facebook: https://www.facebook.com/Windmill-Token-106614645101945

Discord: https://discord.gg/eUq6uJQsKh

YouTube Channel: https://www.youtube.com/channel/UCxpbYiBzUvDgYP8wGN-YZCg"""

    context.bot.sendMessage(chat_id = update.effective_chat.id, text = reply)


def main():
    updater = Updater(token = TOKEN, use_context = True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))                                  #handler for start command
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), message))      #handler for all the message driven replies
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, greeting))    #handler for greeting new memebers
    dispatcher.add_handler(CommandHandler('contract', contract))                            #handler for contract CommandHandler
    dispatcher.add_handler(CommandHandler('social', social))                                #handler for social command


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main();
