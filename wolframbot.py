import wolframalpha
import telebot

id = '9KYKKJ-75RVTV8779'
bot = telebot.TeleBot('1653586848:AAG32NGn83Q0Gti4s7Mjcs36flQimirMOyU')
client = wolframalpha.Client(id)


def get_answer(question):
    try:
        response = client.query(question)
    except :
        pass
    global answer
    try:
        answer = next(response.results).text
    except:
        pass
    

@bot.message_handler(content_types=["text"])
def main(message):
    get_answer(message.text)
    bot.send_message(message.chat.id, answer)
    print(answer)


if __name__ == '__main__':
    bot.polling(none_stop=True)