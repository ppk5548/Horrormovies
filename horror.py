import random
adjective = ['beautiful', 'scary', 'disgusting', 'ackward', 'delecious', 'gross', 'stinky', 'juicy', 'random', 'careless','big', 'adorable', 'angry', 'broad', 'evil', 'grumpy', 'lazy', 'dizzy', 'flat', 'deep', 'cloudy', 'tired', 'terrible']
pn = ['cars', 'movies', 'schools', 'pants', 'shoe', 'cows', 'balls', 'blocks', 'spunges', 'grapes', 'cherries', 'strawberries']
pobp = ['hands', 'eyes', 'mouths', 'legs', 'fingers', 'toes', 'noses', 'ears', 'knees', 'chins', 'cheeks', 'elbows', 'palms', 'heads']
pob = ['hand', 'eye', 'mouth', 'leg', 'finger', 'toe', 'nose', 'knee', 'chin', 'cheek', 'elbow', 'palm', 'head', 'hair']
noun = ['apple', 'couch', 'cave','composer', 'clock', 'cane', 'coffee', 'baby', 'bridge', 'children', 'church', 'bakery', 'cat', 'ambulance', 'boxers', 'canoe', 'cabinet', 'cinema', 'blender', 'candy', 'chest', 'brother', 'arrow', 'airport', 'ankle', 'boy']


while True:
	print("Would you like to make a story?")
	print("Type 1 for yes, 2 for no")
	ask = raw_input(">>>")
	if ask == '2':
		break
	elif ask == '1':
		print("\n")
		adj1 = random.choice(adjective)
		pn1 = random.choice(pn)
		adj2 = random.choice(adjective)
		pobp1 = random.choice(pobp)
		print("Here is the list of the most " + adj1 + " horror " + pn1 + "ever made in Hollywood! Each of these " + adj2 + "films received a rating of two" + pobp1 + "up from Siskel and Elbert.") 
		pob1 = random.choice(pob)
		n1 = random.choice(noun)
		print("The Hunch " + pob1 + " of Notre" + n1 )
		n2 = random.choice(noun)
		n3 = random.choice(noun)	
		print("The " + n2 + " of the living" + n3)
		n4 = random.choice(noun)
		print(n4 + " of Frankenstein" )
		n5 = random.choice(noun)
		print("Invasion of the " + n5 + " Snatchers")
		n6 = random.choice(noun)
		adj3 = random.choice(adjective)
		print(n6 + " from the " + adj3 + " Lagoon")
		n7 = random.choice(noun)
		("Last " + n7 + " on the left")
		n8 = random.choice(noun)
		("The " + n8 + " of the Opera")
