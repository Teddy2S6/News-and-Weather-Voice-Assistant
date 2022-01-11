from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from playsound import playsound
import speech_recognition as sr
from time import sleep
import pyttsx3
import pyglet

def hello():
	print("Hello I'm Tina, your basic assistant")

	hello = pyttsx3.init()
	voices = hello.getProperty('voices')
	rate = hello.getProperty('rate')
	hello.setProperty('rate', 150)
	hello.setProperty('voice', voices[1].id)
	hello.say("Hello I'm Tina, your basic assistant")
	hello.runAndWait()
	hello.stop()

	main()

def main():
	print("What would you like to know? (news/weather): ")

	know = pyttsx3.init()
	voices = know.getProperty('voices')
	rate = know.getProperty('rate')
	know.setProperty('rate', 150)
	know.setProperty('voice', voices[1].id)
	know.say("What would you like to know?")
	know.runAndWait()
	know.stop()

	c = sr.Recognizer()
	with sr.Microphone() as source:
		print("Speak now:")
		choice_audio = c.listen(source) 

		try:
			choice_text = c.recognize_google(choice_audio)
			choice = format(choice_text)

			if choice == "news":
				print("Here are the top headlines from the global news:")
				sleep(1)

				new = pyttsx3.init()
				voices = new.getProperty('voices')
				rate = new.getProperty('rate')
				new.setProperty('rate', 150)
				new.setProperty('voice', voices[1].id)
				new.say("Here are the top headlines from the global news")
				new.runAndWait()
				new.stop()

				print()
				news()

			elif choice == "weather":
				print("Here is the weather for the current week as well as the next week following it:")
				sleep(1)

				weathers = pyttsx3.init()
				voices = weathers.getProperty('voices')
				rate = weathers.getProperty('rate')
				weathers.setProperty('rate', 150)
				weathers.setProperty('voice', voices[1].id)
				weathers.say("Here is the weather for the current week as well as the next week following it")
				weathers.runAndWait()
				weathers.stop()

				print()
				weather()

			else:
				print("Invalid Input")

				invalid = pyttsx3.init()
				voices = invalid.getProperty('voices')
				rate = invalid.getProperty('rate')
				invalid.setProperty('rate', 150)
				invalid.setProperty('voice', voices[1].id)
				invalid.say("Invalid Input")
				invalid.runAndWait()
				invalid.stop()

				main()
		except:
			print("Could not understand")

			understand = pyttsx3.init()
			voices = understand.getProperty('voices')
			rate = understand.getProperty('rate')
			understand.setProperty('rate', 150)
			understand.setProperty('voice', voices[1].id)
			understand.say("Could not understand")
			understand.runAndWait()
			understand.stop()

			main()

def news():
	news_url = 'https://globalnews.ca/canada/'

	# Opening up connection, and grabbing the page
	uClient = uReq(news_url)
	page_html = uClient.read()
	uClient.close()

	# HTML parsing
	page_soup = soup(page_html, "html.parser")

	# Grabs each product
	posts = page_soup.findAll("li",{"class":"c-posts__item c-posts__loadmore"})

	print("The top 10 headlines are as follows:")

	tellingNews1 = pyttsx3.init()
	voices = tellingNews1.getProperty('voices')
	rate = tellingNews1.getProperty('rate')
	tellingNews1.setProperty('rate', 150)
	tellingNews1.setProperty('voice', voices[1].id)
	tellingNews1.say("The top 10 headlines are as follows")
	tellingNews1.runAndWait()
	tellingNews1.stop()

	for post in posts:
		title_post = post.findAll("span", {"class":"c-posts__headlineText"})
		title = title_post[0].text

		description_post = post.findAll("div", {"class":"u-lineClamp"})
		description = description_post[0].text.strip()

		link_post = post.findAll("a", {"class":"c-posts__inner"})
		link = link_post[0]["href"]

		print()
		print("Title: " + title)
		print("Description: " + description)
		print("Link: " + link)
		print()

		tellingNews2 = pyttsx3.init()
		voices = tellingNews2.getProperty('voices')
		rate = tellingNews2.getProperty('rate')
		tellingNews2.setProperty('rate', 150)
		tellingNews2.setProperty('voice', voices[1].id)
		tellingNews2.say(title)
		tellingNews2.runAndWait()
		tellingNews2.stop()

	anythingElse()

def weather():
	count = 0

	weather_url = 'https://globalnews.ca/ottawa/weather/CAXX0343'

	# Opening up connection, and grabbing the page
	uClient = uReq(weather_url)
	page_html = uClient.read()
	uClient.close()

	# HTML parsing
	page_soup = soup(page_html, "html.parser")

	# Grabs each product
	slides = page_soup.findAll("div",{"class":"weather-forecast-item clearfix"})

	for slide in slides:
		day_post = slide.findAll("span", {"class":None})
		day = day_post[0].text

		highWeather_post = slide.findAll("span", {"class":None})
		highWeather = highWeather_post[2].text

		lowWeather_post = slide.findAll("span", {"class":None})
		lowWeather = lowWeather_post[3].text

		description_post = slide.findAll("span", {"class":None})
		description = description_post[4].text

		print()
		print(day + ":")
		print(description)
		print("Average High of " + highWeather)
		print("Average Low of " + lowWeather)
		print()

		tellingWeather = pyttsx3.init()
		voices = tellingWeather.getProperty('voices')
		rate = tellingWeather.getProperty('rate')
		tellingWeather.setProperty('rate', 150)
		tellingWeather.setProperty('voice', voices[1].id)
		tellingWeather.say(day + " will be " + description)
		tellingWeather.runAndWait()
		tellingWeather.stop()

		count = count + 1
		if count == 5:
			print("Next Five Days:")

			nextDays = pyttsx3.init()
			voices = nextDays.getProperty('voices')
			rate = nextDays.getProperty('rate')
			nextDays.setProperty('rate', 150)
			nextDays.setProperty('voice', voices[1].id)
			nextDays.say("For the next five days")
			nextDays.runAndWait()
			nextDays.stop()

	anythingElse()

def anythingElse():
	print("Shall I assist you with anything else? (yes/no): ")

	assist = pyttsx3.init()
	voices = assist.getProperty('voices')
	rate = assist.getProperty('rate')
	assist.setProperty('rate', 150)
	assist.setProperty('voice', voices[1].id)
	assist.say("Shall I assist you with anything else?")
	assist.runAndWait()
	assist.stop()

	a = sr.Recognizer()
	with sr.Microphone() as source:
		print("Speak now:")
		cont_audio = a.listen(source) 

		try:
			cont_text = a.recognize_google(cont_audio)
			cont = format(cont_text)

			if cont == "yes":
					print("Sure thing, just a moment")

					yes = pyttsx3.init()
					voices = yes.getProperty('voices')
					rate = yes.getProperty('rate')
					yes.setProperty('rate', 150)
					yes.setProperty('voice', voices[1].id)
					yes.say("Sure thing, just a moment")
					yes.runAndWait()
					yes.stop()

					main()

			elif cont == "no":
				print("Very well, I was happy to assist")

				no = pyttsx3.init()
				voices = no.getProperty('voices')
				rate = no.getProperty('rate')
				no.setProperty('rate', 150)
				no.setProperty('voice', voices[1].id)
				no.say("Very well, I was happy to assist")
				no.runAndWait()
				no.stop()

			else:
				print("Invalid Input")

				invalid = pyttsx3.init()
				voices = invalid.getProperty('voices')
				rate = invalid.getProperty('rate')
				invalid.setProperty('rate', 150)
				invalid.setProperty('voice', voices[1].id)
				invalid.say("Invalid Input")
				invalid.runAndWait()
				invalid.stop()

				anythingElse()

		except:
			print("Could not understand")

			understand = pyttsx3.init()
			voices = understand.getProperty('voices')
			rate = understand.getProperty('rate')
			understand.setProperty('rate', 150)
			understand.setProperty('voice', voices[1].id)
			understand.say("Could not understand")
			understand.runAndWait()
			understand.stop()

			anythingElse()

def call():
	ca = sr.Recognizer()
	with sr.Microphone() as source:
		print("Speak now:")
		call_audio = ca.listen(source) 

		try:
			call_text = ca.recognize_google(call_audio)
			callVoice = format(call_text)

			if callVoice == "hey Tina":
				hello()

			else:
				print("Invalid Input")

				invalid = pyttsx3.init()
				voices = invalid.getProperty('voices')
				rate = invalid.getProperty('rate')
				invalid.setProperty('rate', 150)
				invalid.setProperty('voice', voices[1].id)
				invalid.say("Invalid Input")
				invalid.runAndWait()
				invalid.stop()

				call()
		except:
			print("Could not understand")

			understand = pyttsx3.init()
			voices = understand.getProperty('voices')
			rate = understand.getProperty('rate')
			understand.setProperty('rate', 150)
			understand.setProperty('voice', voices[1].id)
			understand.say("Could not understand")
			understand.runAndWait()
			understand.stop()

			call()

if __name__ == "__main__":
	call()