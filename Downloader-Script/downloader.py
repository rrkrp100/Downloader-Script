#! Python 3

def uDown(ulink):
	"""Youtube downloader function"""

	try:
		import os, bs4, webbrowser, requests

	except:
		print("You are missing one or all of the following libraries\n# bs4(BeautifulSoup)\n# webbrowser\n# requests\n ")
		exit()


	try:
		print("The link given is: " + ulink + "\n")

		dlink=ulink
		ulink = "https://www.gen" + ulink[12:]


		print("Searching for the requested file\n")

		res = requests.get(ulink);
		soup= bs4.BeautifulSoup(res.text,features='html5lib')

		elems= soup.select('a[data-itag="22"]')

		if len(elems)!=0:
			webbrowser.open(elems[0].get('href'))

	except:
		print("Something went wrong with the GEN server, trying the \"Save from net\" Server")



		#####  GOING FOR THE SAVE FROM NET ######

	if len(elems)==0:
		print("The 720p downloadable file is missing from the Gen repository\n Opening the \"Save from net\" website\n")
		try:
			from selenium import webdriver

		except:
			print("The Selenium module is missing\n Please install the selenium module\n")

		dlink= "https://www.ss"+ dlink[12:]
		browser= webdriver.Firefox()
		browser.get(dlink)

		link = browser.find_elements_by_link_text('Download')

		if len(link)==0:
			print("Downloadable file NOT FOUND, \nExiting... \n")
			exit()

		link[0].click()

		print("Commencing the download via Browser\n PLEASE SELECT SAVE AS \n\n THANK YOU")

		#exit()



######################################################################


def fb():
	"""Open's facebook and log's into it)"""

	try:
		from selenium import webdriver
	except:
		print("\nSelenium module is missing.\nPlease install the Selenium Module/library\n")
		exit()


	import getpass
	import time

	usr=raw_input("\nFaceBook User name: ").strip()
	pas=getpass.getpass()

	browser = webdriver.Firefox()
	browser.get("https://www.facebook.com")

	email = browser.find_elements_by_id("email")
	email[0].send_keys(usr)

	paswrd = browser.find_elements_by_id("pass")
	paswrd[0].send_keys(pas)
	paswrd[0].submit()

	print("\nLoging you in...\n")

	label = browser.find_elements_by_id("userNavigationLabel")
	while len(label)==0:
		label = browser.find_elements_by_id("userNavigationLabel")

	a = raw_input("Logged in. \nPress Enter to logout... ")

	label[0].click()

	print("\nLogging Out, waiting for network")

	log=browser.find_elements_by_link_text("Log Out")

	while len(log)==0:
		log=browser.find_elements_by_link_text("Log Out")


	log[0].click()

	print("Thank you for using this service")

	#exit()


###############################################################################


def youtube():

	try:
		from selenium import webdriver
		from selenium.webdriver.common.keys import Keys
	except:
		printf("\nSelenium module is missing.\nPlease install the Selenium Module/library\n")
		exit()

	item = raw_input("\nEnter the video to search on youtube:  ").strip()

	browser = webdriver.Firefox()
	""" The following code section directly opens the search page for the iten on youtube """

	browser.get("https://www.youtube.com/results?search_query="+item)
	vid= browser.find_elements_by_id("video-title")
	ulink= vid[0].get_attribute("href")

	vid[0].send_keys(Keys.CONTROL+Keys.ENTER)

	while len(browser.window_handles)==1:
		pass

	browser.switch_to_window(browser.window_handles[1])

	#######

	""" This code section is to open youtube main page and then enter the values in the search box

	browser.get("https://www.youtube.com")
	search = browser.find_elements_by_id("search")

	search[3].send_keys[item]
	search[3].submit()

	vid= browser.find_elements_by_id("title-wrapper")

	##Now all the search results are in the vid[] list starting from index 0

	vid[0].send_keys(Keys.CONTROL + Keys.ENTER)"""

	#######



	answer = raw_input("\nDo you want to download this Video?\n(YES/NO): ")
	answer= answer.lower().strip()[0]

	if answer=='y':
		uDown(ulink)
	else:
		print("Thank you fo using it. ^_^ \n\nExiting Now.\n")
		exit()


##################################################################################


def anime():

	try:
		from selenium import webdriver
	except:
		print("The selenium module is not installed!!!\nPlease install selenium and try again\n")
		exit()

	#anime=pyperclip.paste()

	anime=raw_input('Enter the anime name \n')

	if len(anime)==0:
		print('Please Input a valid name and relaunch')
		exit()

	link ="http://animeheaven.eu/i.php?a="+anime

	browser= webdriver.Firefox()
	browser.get(link)

	ep=browser.find_elements_by_class_name('infovanr')
	if len(ep)==0:
		ep=browser.find_elements_by_class_name('infovan')

	if len(ep)==0:
		print("Could not Find "+anime+"'s latest episode")
		exit()

	eplink= ep[0].get_attribute('href')

	browser.get(eplink)

	FDlink=browser.find_elements_by_link_text('Force Download')

	if len(FDlink)!=0:
		ulink=FDlink[0].get_attribute('href')

	elif len(FDlink)==0:
		FDlink=browser.find_elements_by_class_name('an')
		if len(FDlink)==0:
			print("Could not Find "+anime+"'s latest episode")
			exit()
		ulink=FDlink[1].get_attribute('href')

	browser.get(ulink)
	#exit()

#######################################


def ask():
	""" Asks what to do next"""

	print("Choose the task to perform:\n")
	print("TO:\t\t\t Enter:\n")
	print("To Browse facebook:-\t facebook\nTo Browse Youtube:-\t youtube\nTo Download Anime:-\t anime")

	choice= raw_input("\nYour Choice: ")
	choice=choice.lower().strip()

	if choice[0] == 'f':
		fb()

	elif choice[0]=='e':
		print("\nExiting the Downloader,\n Thank you for using it. ^_^ ")
		exit()

	elif choice[0] =='y' or choice[0] == 'u':
		youtube()

	elif choice[0] == 'a':
		anime()

	else:
		print("\nOops! Maybe a Spelling Mistake, try again.")
		ask()


########################################## -> MAIN FOLLOWS

import pyperclip, time
ulink  = pyperclip.paste();


if ulink.startswith('https://www.youtube.com'):
	answer= raw_input('\n\n Download the youtube link you\'ve copied '.upper()+' (i.e. ' +ulink+ ') ? \n Answer:(Yes/No)  :')
	answer=answer.lower().lstrip()[0]

	if answer=='y':
		print("\nDownloading the youtube video\n")
		try:
			uDown(ulink)
		except:
			print("  NO INTERNET ACCESS OR CONTENT COULD NOT BE FOUND \n PLEASE CHECK THE CONNECTION AND RE-TRY \n ")
			a= raw_input("")
			exit()

	else:
		print("\nWhat would you like to do? ^_^\n")
		try:
			ask()
		except:
			print("***** NO INTERNET ACCESS OR CONTENT COULD NOT BE FOUND \n PLEASE CHECK THE CONNECTION AND RE-TRY \n")
			a= raw_input("")
			exit()
else:
	print("\nDid not find any links in the ClipBoard, let's do somthing.  ^_^\n")
	try:
		ask()
	except:
		print("***** NO INTERNET ACCESS OR CONTENT COULD NOT BE FOUND \n PLEASE CHECK THE CONNECTION AND RE-TRY \n")
		a= raw_input("")
		exit()


time.sleep(100000)
a = raw_input("")
