"""This script will handle all the game's files. The creation of directories and files will be done in this script"""
import os
import pickle


def dump(file_path):
	"""This function creates the save file that will be used throughout the game
	However if the file already exists this function does not perform any action."""

	exists = os.path.isfile(file_path + "\\leaders.dat")
	if exists:
		pass
	else:
		list_for_dump = ["---LEADERBOARD---"]
		pickle.dump(list_for_dump, open(file_path + "\\leaders.dat", "wb"))


def create_files(file_path):
	"""This function creates the directory that will contain all the file that the game will use"""

	try:
		os.mkdir(file_path)
	except FileExistsError:
		pass

	player_story = """
	...CAVER...
	
	The Story
	
	The player has lived in a cave their whole life. The player lives in a small village in the cave.
	The player may live in the cave, but it is clear that the player does not come from the cave.
	Compared to the other people that live in the cave the player has more muscle and a more well-defined bone structure.
	The player has been in the cave for as long as they can remember, but the people of the cave could remember more.
	The player knows that they are different from the people of the cave but still treats them as their own.
	
	Tales have been told. Tales of a bright yellow ball that floats far above.
	Tales of a bright white ball that floats with many small white dots to accompany it.
	Tales of a vast expanse of land that is not confined by the dark walls of a cave.
	These are the tales that the character has grown up to. However, the player has never left the cave.
	No one dares to try and leave the cave. There is only one way to leave the cave. It is treacherous and unforgiving.
	It holds many vicious beasts. No one can make it through.
	
	No one, except one man. An old man, who many in the village called senile. In the days of his prime, he left the cave 
	and witnessed the outside world. He saw first hand what the outside world was like. He now can only tell the tales of 
	technology that surpassed his comprehension and people who, to him looked like muscular giants. He is the only one 
	who has seen the legendary yellow ball, the one called ‘sun’. The tales of the outside world where he was known as a 
	Caver. 
	
	Alas, the people of the cave are slowly dying. Their resources are dwindling. The old risk their lives every time 
	they awake from their slumber. The old man is at the greatest risk. He is the oldest of all the people of the cave. 
	He was the one to find the player and rescue him from death's door. Once upon a time. The player sees the old man as 
	a father figure. The love he had for the old man was great 
	
	The player has to save the people of the cave. The player has to save their friends. The player has to save the old man. 
	Save his father. The player will now have to journey out of the cave. The player will encounter many dangers, 
	but the player must survive or else. 
	
	You are the player. You are a Caver.
	Will you survive?
	
	"""

	help_text = """
	GAME HELP:
	
	1. Enemy Tiles: You cannot leave an enemy tile unless you have defeated the enemy.
	2. Input: If a non player character asks you a question, enter the most obvious answer.
	3. As you play along, draw a map so you don't get lost
	4. The leaderboard can only store the last 6 scores.
	5. If and only if you are completly lost. You can use the 'map.txt' file to help you navigate through the cave.
	   However the 'map.txt' file does not give you a key to read the map with, so there are still somethings that
	   need to be figured out. 

	The objective of the game is to make your way through the cave.
	Making it all the way to the end without dying will mean completion of the game. 

	
	"""

	crd = """
              ---GAME CREDITS---
    Game Developer          Theophilus Nenhanga
    Main Game Tester        Colbert Jansen
    Icon                    Icon made by Freepik from www.flaticon.com

    © Theophilus Nyasha Nenhanga
	"""

	story = open(file_path + "\\story.txt", "w")
	story.writelines(player_story)
	story.close()

	leaderboard = open(file_path + "\\leaderboard.txt", "a")
	leaderboard.writelines("---LEADERBOARD---")
	leaderboard.close()

	credit = open(file_path + "\\credits.txt", "w")
	credit.writelines(crd)
	credit.close()

	info = open(file_path + "\\help.txt", "w")
	info.writelines(help_text)
	info.close()
