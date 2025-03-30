import telebot

TOKEN = "7672809563:AAGFS-dru2noPxEpRQC3YjGo5L4FK-GXo28"
bot = telebot.TeleBot(TOKEN)

user_data = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	print(f"User {message.chat.id} started the bot.")
	bot.reply_to(message, "Hello! What's your name?")
	bot.register_next_step_handler(message, ask_age)

def ask_age(message):
	user_data[message.chat.id] = {'name': message.text}
	print(f"User {message.chat.id} provided name: {message.text}")
	bot.reply_to(message, f"Nice to meet you, {message.text}! How old are you?")
	bot.register_next_step_handler(message, final_response)

def final_response(message):
	try:
		age = int(message.text)
		name = user_data[message.chat.id]['name']
		print(f"User {message.chat.id} is {age} years old.")
		bot.reply_to(message, f"Great, {name}! You are {age} years old.")
	except ValueError:
		print(f"User {message.chat.id} entered an invalid age: {message.text}") 
		bot.reply_to(message, "Please enter a valid age (number).")
		bot.register_next_step_handler(message, final_response)

if __name__ == "__main__":
	print("Bot is running...")
	bot.infinity_polling()
