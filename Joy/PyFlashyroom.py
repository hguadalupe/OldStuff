from sys import exit
import sys
import time

print ("""
Hi dear. I presume this is your first Python adventure. 
May I ask your name?""")
name = raw_input(">")

print ("""
I should know your age too. 
This is important stuff for the plot im creating for you. 
Dont be shy, your data will be safe with me.""")
age = int(raw_input(">"))

print ("""
It is also important for me to have your gender in my database. 
You know, it is not that im a sexist program. 
What is sexist is the reality i've been coded into.
#1 Male
#2 Female""")
gender = raw_input(">")

global flashyroom
	
def flashyroom ():

	print ("""%s look around you. 
	Now we are entering a a new reality... 
	WHOA! You are floating between millions of lights, colors and flashes! 
	Incredible world with an incredible narrator.""" % name)
	syms = ['\\', '|', '/', '-']
	bs = '\b'
	for _ in range(10):
	
		for sym in syms:
			sys.stdout.write("\b%s" % sym)
			sys.stdout.flush()
			time.sleep(.1)

			
	print ("""What do you do while you float in this strange flashy space?
		#1 Scream in horror, you think you are falling.
		#2 Laugh and dance in the air. You are flying!""")

	firstdec = raw_input (">")

	if firstdec == "1":
		print ("You land in the White House. Yeah %s! You are in that big presidential mansion in washington." % name)
		syms = ['\\', '|', '/', '-']
		bs = '\b'
		for _ in range(5):
	
			for sym in syms:
				sys.stdout.write("\b%s" % sym)
				sys.stdout.flush()
				time.sleep(.1) 
				
		whitehouse()
		
	elif firstdec == "2":
		print ("You land in a endless space with tons of moneypaper of euros and dollars. %s, stop walking and dancing over the money. You'll have to make a desicion." % name)
		syms = ['\\', '|', '/', '-']
		bs = '\b'
		for _ in range(5):
	
			for sym in syms:
				sys.stdout.write("\b%s" % sym)
				sys.stdout.flush()
				time.sleep(.1) 
	
		moneyroom()
		
	else: 
		wake("You find yourself in your bed doing stupid things.")

def whitehouse():
	print """
	Oh, you has found Obama, the President of UUEE, in the Oval Office! He is reading the newspaper peacefully. What do you do? 
	#1 You say \'hey Mr president, how are you doing\'
	#2 You try to shoot him.
	#3 Type your answer."""
	choice = raw_input("> ")
	print (choice)
	
	if choice == "1":
	
		if gender == "1":
			print ("""Mr. Obama glances at you with a contemptuous look... and keep reading HAWAII NEWS. 
			He sais: \'What the hell is this insignificant insect in this room\'. Now your selfsteem is extremely low. 
			You mean nothig to your president""")
			flasshyroom()
		
		elif gender == "2":
			print("""
			Mr. Obama glances at your breast and then at your face... 
			and keep reading HAWAII NEWS. He sais: 
			\"What the hell is this sillygirl in this room\". 
			Now your selfsteem is extremely low. 
			You mean nothig to your president """)
			flashyroom ()
		
		else:
			print ("""That seems dangerous for your president. 
			The bodyguards pick you from the neck 
			and throw your agitating body trough the back door.""") 
			wake("You are not a proper american cityzen.")
	
	elif choice == "2":
		print ("Mr. Obama look at your eyes and says the United States needs more people like you. People who risks their life for moral principles. He sends you to fight ISIS at Siria")
		wake("You are not a proper american cityzen.")
	
	else:
		print ("That seems dangerous for your president. The bodyguards pick you from the neck and throw your agitating body trough the back door.")
		wake("You are not a proper american cityzen.")
		

def moneyroom ():

	print """
	This room is full of gold.  
	How much do you take?"""

	money = int(raw_input("> "))

	if money < 50:
		print("""
		Nice %s, you're not greedy, you have became the richest person you know. 
		And you have no friends to spread your incredible story.""" % name)
		flashyroom ()

	elif money > 50:
		wake("You greedy bastard!")
		
	else:
		wake("Hey %s, learn to type a number." % name)
        


def ageroom():
	if age < 50:
		print("%s, your body has changed. Now your skin is full of ripples and you are in bed." % name)
		wake("You try to enjoy your last seconds of life before you die.")
	
	if age > 50:
		print ("""
		what happened? 
		Now your body has no more than fourty centimetres and your personalyty has disapeared. 
		It seems %s that you will have to start your life from the beginning 
		as you are now a crying child with almost no conscience of itself.""" % name)
		wake("You cannot help to poop while you cry." % name)

def wake(why):
	print (why, "Now you wake from that endless dream.")
	exit(0)
		
flashyroom()
