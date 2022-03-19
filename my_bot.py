from telegram import Update
from telegram.ext import CallbackContext, Updater, Filters, MessageHandler


def message_handler(update: Update, context: CallbackContext):
    mesage_from_user = update.message.text
    mess_send="Проверка"
    if mesage_from_user == "Здравствуйте":
        mess_send = "Рады Вас видеть! Представьтесь!"
    elif mesage_from_user == "расскажи анектод":
        mess_send = "вот такой анекдот"
    elif mesage_from_user == "прогноз погоды":
        mess_send = "Сегодня ясно"
      

    update.message.reply_text(
        text=mess_send
    )


def main():
    print("Бот начал работать...")

    updater = Updater(
        token="",
        use_context=True
    )

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
