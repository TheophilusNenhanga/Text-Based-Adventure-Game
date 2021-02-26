import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


storyteller1: dict = {
			1: f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
You are the first traveller that I have seen in a long time.
Tell me, what is your name?
			""",

			2: f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
What an interesting name you have.
I'll just call you 'little brat'\n
			""",

			3: f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
I assume that because you are here you seek to save the people of that sorry village.
Is that correct?
			""",

			3.1: f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
Your mission will place you in insurmountable danger. 
I almost pity you. 
I must at least tell you the secret of this forsaken cave.
			
The exit of this cave is guarded by four elemental deities.
Well five, if you chose to count the treacherous labyrinth as a deity on its owm. 

Before you can leave the cave there is something that you need to collect from the bosses.
What you really need to collect, I have no clue.

Well that's all I can tell you.
			""",

			3.2: f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
You ignorant little brat.
If you have no business in this cave then why are you here.
Are you here to get yourself killed?

You little brat, tell me the truth.
			
			""",

			3.3: f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
That's what I wanted to hear
However I must warn you.
			
			""",

			3.4: f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
			That's the wrong answer you brat
				""",

			4: f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
Now you must pay me.Ha Ha!
Yes information does not come cheap
			""",

			4.1: f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
Thank you for your kindness.
One day I will find a way to repay you.

Goodbye now, you little brat.
			""",

			4.2: f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
You can't even spare a couple gold coins for an old lady.
You heart may even be as empty as the hearts of the monsters in this cave. 

Well goodbye to you, you little brat.
			""",

			5: f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
I am surprised you made it this far, you little brat.
I honestly thought you would be dead by now.
Well I guess i can repay you for your kindness earlier.
			""",

			5.1: f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
I hope I don't see you again, you little brat
			""",

			6: f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
You're back again, you selfish little brat. 
I have no story for you today. 
Go annoy some other old lady.
			"""

}

storyteller2: dict = {
	"1":
		f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
What a fine young chap you are. 
You've made it this far I see.
Well, do you want to know the reason behind all of this?
	   		""",

	"1yes":
		f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
Ah, wise decision
I was just like you when I was younger.
A fine young chap. I had a heart just like yours.
I wanted to escape from this cave and save the people.
But sadly, I did not know what it would take.
 
But you young chap, you're a lucky one.
You have me to tell you all the secrets.
Do you want to know the secrets, young chap?
					""",

	"1no":
		f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
So you don't want know the reason for all this.
You young chaps of theses days, So boring.
				 
Are you sure you don't want to know?"
Come on, young chap, I am giving you one final chance
			""",
	"1else":
		f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
	Well I didn't understand what you said young chap.
	But it sounded like a yes to me.
	""",

	"2yes":
		f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
Hadn't you already said yes?
Forgive me young chap. Age has stolen my memory
But what I am about to tell you is something I can never forget.
				""",

	"2no":
		f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
Well young chap, I will tell you anyway.
Trust me young chap, you will thank me later.
		   	""",

	"3":
		f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
Okay let me tell you my story. 
Listen carefully young chap.
		
I was once strong and brave like you.
I also sought to save the people of the cave
I sought to save myself
 
But I care only about strength
I thought that defeating all the monsters and beasts in the cave I would accomplish something.
Young chap, I was wrong.
 
All I did was tire myself out.
It was only when old age hit me that I realised what had to be done.
 
Your mission is to gather the four elements.
These elements will unlock the door to the passage that leads to the outside world.
 
These elements: earth, water, fire, air
They are guarded by elemental deities that are known as 'Mancers'
I hope my words are not lost on you, young chap.
			""",

	"3.5":
		f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
Young chap, I couldn't hear a thing you just said.
These monsters and always making so much noise.
Well either way, not like I was going to repeat my story 
		""",

	"4":
		f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
All this talking puts me in a giving mood
Young chap
Would you want a gift?
It's the least i can do for you, I haven't told that story in a while
	 			
So, will you accept my gift?
	""",

	"4yes":
		f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
Thank you for accepting my kindness
If you do make it out of this forsaken cave,
Please do not forget me young chap.

Goodbye, Young chap.
Please, do not forget me!
			""",

	"4no":
		f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
So you won't accept my kindness.
Well young chap, I'll give it to you anyway
Ha ha ha! Whatever happens don't forget me young chap.

Goodbye young chap. Don't forget me!
	""",

	"before":
		f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
I think I have seen you before, but I don't remember.
In this state I won't be of any use to you.
Continue your adventure you young chap\n
	""",

	"forgotten":
		f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
What was I saying? It seems like I have forgotten
This is what old age does to you
I'm sorry young chap I cant help you.
		""",

	"understand":
		f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
Did you understand that young chap?
"""
}

challenger1: dict = {
	"1": """
I have not seen you here before.
Tell me what is your purpose in this forsaken cave?
""",

	"1long": """
Whatever you sound just sounded long and boring.
I stopped listening half way through. 
Just tell me.

Are you here to save the village?
Tell me, yes or no?
""",

	"destroy": """
So does that mean what I think it means?
Are you going to help me destroy the village?	
""",

	"1y": """
So that is your mission.
Sadly I can no longer let you live.

I hate that village and will do anything to destroy it.
Do you want to know why?
""",

	"1yw": """
Did you just ask me why?
Because those evil bastards in the village exiled me.
You look young so you probably don't remember when I was exiled.

I have been in this cave for years, fighting to survive.
I must get stronger to destroy that village with my own hands	
	""",

	"challenge": """
Are you going to stand in my way?
Answer carefully...

I do not mind staining my hands with your blood.
Will you fight me?
""",

	"accept": """
You have made a grave decision. 
I am not like any monster that you have encountered so far.
I will definitely take your life.	
""",

	"decline": """
Well I wasn't asking. 
Your mere existence is a sin in my eyes.
I WILL END YOU!	
""",

	"with": """
So you are with me.
Let's go and destroy that village right now.
""",

	"against": """
So you aren't on my side.
So you are siding  with those selfish villagers that exiled me?

Why am I not surprised.

So tell me:	
""",

	"victory": """
You may have defeated me today, but this is not the end.
I will make sure that one day. 
I will destroy that village...
No matter what it takes!	
""",

	"defeat": """
Do you now see what a foolish mistake you have made.
I will destroy that village, and there is nothing you can do about it.
I will leave you here, the monsters will finish you off.
Nothing will get in the way of my revenge!	
""",

	"fight_else": """
I didn't hear a thing you just said.
But I'll fight you anyway.
Nothing will get between me and my revenge.
""",

	"late": """
Well it's too late to change your mind now. 
Welcome to my side.
The side of revenge... 	
""",

	"revenge": """
I knew from the moment I saw you.
There is revenge in your eyes.
Let's destroy that village.	
""",

	"escape_die": f"""
The {Fore.LIGHTRED_EX}Exiled villager{Fore.RESET} makes a run for it.


Then suddenly, you hear a loud scream, then the groan of an undead, and the rattling of bones.
The {Fore.LIGHTRED_EX}Exiled villager{Fore.RESET} is dead."""


}


possibilities1: list = [
	"save the village",
	"rescue the village",
	"save",
	"rescue",
	"escape",
	"fight",
	"village",
	"family",
]

possibilities2: list = [
	"why",
	"explain",
	"talk",
	"okay",
	"fight",
]

the_end_abandon: list = [
	f"""{Fore.RED}
You, The player.\n
""",

	f"""{Fore.RED}
What have you done?\n""",

	f"""{Fore.RED}
You have forsaken the mission. 
You have forsaken the goal.\n""",

	f"""{Fore.RED}
You were here to save the village. 
But now you have chosen a path that leads to its destruction.\n""",

	f"""{Fore.RED}
---YOUR FATE---\n
""",

	f"""{Fore.RED}
You and the Exiled Villager form an alliance 
On your way to the village, a mob of undead attack you.
You easily over power them...but then 
	""",

	f"""{Fore.RED}
The Exiled Villager, stabs you in the back...
literally.
He leaves you, bleeding.
Might this be end for you?\n
"""

]

storyteller3: dict = {

	"who_i_am": """
Well, believe it or not, I am your uncle. 
I am Mr Corona.
Which means you are a Corona. 
The crown is your inheritance.
""",

	"nothing": """
Well since you have nothing to say I will just tell you a story.
Your story. 
I am only telling you this story because I like your smell.\n
""",

	"one": "Do you know who I am?\n",

	"two": """
I know your smell. 
I know who you are. 
Do you remember me?\n
	""",

	"remember": "If you do remember me, tell me what my name is.\n",

	"rude": """
	That's a bit rude don't you think?
	To think that my nephew would have the smell of disrespect.
	I shall tell you the story anyway""",


	"wrong_name": """Well that is not my name. So it seems that you were lying\nSo you have the smell of lies.\n""",

	"forget": """
I don't blame you for forgetting, the last time I saw you you were still young.
Do you want to know who I am?\n
	""",

	"correct": """
So you do remember me?
Do you remember why you are in this cave?\n
	""",

	"correct-story": """
Something about you smells like a lie. 
Let me just tell you the whole story, for good measure.\n
""",

	"here-i-go": """
Well this is the story...\n	
""",

	"tell": """
Very well, I like your smell so I will tell you. 
If it was not for your smell I would not be telling you anything.\n
	""",

	"STORY": [
		"""
It all started 20 years ago.
""",

		"""
The reason you are in this cave is to keep you safe from the outside world.
""",

		"""
Your brother, the king, wants your head on a plate.
From a young age, greatness was always your inheritance, but for your brother suffering and strife.
Knowledge of this angered him. He was driven into madness by his desire for power.
Now he is the king, but his kingdom is not pleasant by any means.
 """,

		"""
All who oppose him are sentenced to death.
Your mother and father the former royalty of the kingdom could not be spared.
Their very own son took their lives. 
Your very own brother
	""",

		"""
I was the one who saved you and brought you to this cave.
I have waited for the day that you would become strong enough to escape this cave and save the kingdom.
Will you be the fabled caver that will save the world?""",

		"""
But I must warn you the outside world is dangerous.
Here in the cave, all you know of are medieval tools and ways of life.
The outside world has technology and abundant power.
If you want to save the kingdom, avenge your parents and save that village.
There are many obstacles you have to overcome. \n""",

	],

	"nephew":
	"""
Getting to finally see my nephew, all grown up.

And your smell is of greatness. 
Your father would have been proud.
	""",
	
	"ready": """
	Are you ready for that?
	""",

	"give": """
You are, let me give you somethings to help as you continue your journey.
""",

	"not-ready":
	"""
Well you smell ready.
Let me give you something""",

		"given": """
This will not help you now, you will have to take on the boss with whatever it is you have now.
However, when you leave the cave these items might help you. 
""",

	"give-error": """
Oops, it seems like the smell of misfortune is on you. 
It turns out I have nothing to give you. 	
""",

	"what-to-say": """
Now what do you say?
""",

	"gratitude": f"""
At least you have the smell of gratitude	
""",

	"ungrateful": """
Well it seems you do not have the smell of gratitude	
""",

	"goodbye": f"""
Well now you have to go. 
Go out and smell the adventure. 

And when you become the the savior of the kingdom.
Say that Mr. Corona sent you	
"""
}


levels: dict = {
	"level1": f"""{Fore.BLUE}
	  LEVEL 1
	THE CAVERNS
	""", 

	"level2": f"""{Fore.BLUE}
	  LEVEL2
   WATERY GRAVES
	""", 

	"level3": f"""{Fore.BLUE}
	  LEVEL 3
	BURNING HELL
	""", 

	"level4": f"""{Fore.BLUE}
	  LEVEL 4
	  THIN AIR
	"""
}


random_texts: list = [
			"""You look a bit tired, maybe you should get some food""",
			"""Do you expect to exit this cave, with such weak weaponry?\nYou should get something stronger at the Weapon smith""",
			"""Your armour isn't strong enough, You won't survive.\nConsider upgrading?""",
			"""Hmm, have you considered completing a quest?""", 
			"""Are you sure you can do this? It isn't too late to turn back now""", 
			"""Will you be the one to save us?""",
			"""Please, help u...u...us!""", 
			"""You look weak, I don't think you will make it.""",
			"""We need you, we need you. WE NEED YOU!"""
		]


stone_texts: list = [
	"""
	The walls of the cave seem to be moving...
	Are the rocks alive?""", 
	"""
	You hear the sound of a crashing stalactite. 
	The cave could collapse at any moment.""", 
	"""You look over the edge...
	Falling would mean death by sharp stalagmites.""", 
	"""
	You hear the grumbling of rocks.
	It is as if the rocks have been angered.""", 
	"""
	You begin to see many rocky columns.
	Could enemies possibly be lurking?""" 
]

water_texts: list = [
	"""
	You hear crashing waves in the distance.
	will the waves overpower you?""", 
	"""
	A giant wave is approaching you.
	I hope you can swim?""", 
	"""
	The water level is increasing.
	You might need to start swimming.""", 
	"""
	The underground river begins to flood.
	What evils lie in the murky waters""", 
	"""
	Something grabs your leg...
	Will you sink to the bottom and die?"""
]

fire_texts: list = [
	"""
	All the water begins to evaporate
	Your sweat begins to evaporate,
	will your blood evaporate?""", 
	"""
	The ground below you is steaming
	How long can you survive here?""", 
	"""
	The heat is unbearable.
	What will melt next?""", 
	"""The rocks are beginning to melt.
	Soon everything will be magma""", 
	"""
	The deeper you go the hotter it becomes.
	You might just have entered the mantle.
	Does death surely await?"""
]

air_texts: list = [
	"""
	The air suddenly becomes thin.
	You might suffocate.""", 
	"""
	You have made it this far.
	Only to die from suffocation.""",
	"""
	No matter how strong you are.
	Without the gas of life, you will die.""", 
	"""
	Your air is being stolen.
	Soon you will be completely out of breath.""",
	"""Suffocation...Will you lose your life soon?"""
]

corridor_texts: dict = {
	"stone": """
	You have entered a narrow corridor.
	The stalactites above you seem to be getting closer""", 
	"water": """
	The corridor that you have entered is the only dry land.
	Relish this moment, before your watery grave""", 
	"fire": """
	The flames have made a corridor, just for you.
	Make sure, not to be burnt to a crisp""", 
	"air": """
	You are now on a corridor of clouds.
	The gusts of wind might send you flying to doom.
	"""
} 

complete: str = """

You take the four elemental stones that you have been collecting out of your inventory. 
They begin to glow very brightly. Suddenly, They begin to levitate and slowly move towards the wall of the cave. 
They are pulsating divine energy. The cave is filled with light. 
Then...
It all goes dark...

You hear a deep grumbling. 
The wall before you begins to move.
First you see a thin beam of light..As it begins to grow, you see it...

The outside world.
The world where dreams come true.
The world that you have to save...Your adventure
Is only beginning

You are a CAVER.


---ONE DAY YOU SHALL COMPLETE YOUR ADVENTURE---

"""