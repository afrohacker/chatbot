from telegram.ext import Updater, CommandHandler
import config


def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text('Hello Madam')
    #update.message.reply_text(
     #   'Hello {}'.format(update.message.from_user.first_name))

updater = Updater(config.token)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()