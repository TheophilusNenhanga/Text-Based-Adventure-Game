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
They are guarded by elemental bosses that are known as 'Mancers'
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

	"escape_die":f"""
The {Fore.LIGHTRED_EX}Exiled villager{Fore.RESET} makes a run for it.


Then suddendly, you hear a loud scream, then the groan of an undead, and the rattling of bones.
The {Fore.LIGHTRED_EX}Exiled villager{Fore.RESET} is dead."""


}


possibilities1 = [
	"save the village",
	"rescue the village",
	"save",
	"rescue",
	"escape",
	"fight",
	"village",
	"family",
]

possibilities2 = [
	"why",
	"explain",
	"talk",
	"okay",
	"fight",
]

the_end_abandon = [
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

storyteller4: dict = {
	"one": "Do you know who I am?", 
	"two": "Why is it that I know you? Do you remember me?",
	"remember": "If you do remember me, tell me what my name is.",
	"wrong_name": "Well that is not my name. So it seems that you were lying",
	"forget": """
I don't blame you for forgetting, the last time I saw you you were still young.
Do you want to know who I am?"""
}
