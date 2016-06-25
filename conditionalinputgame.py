name = input("What is your name? ")
print("Hi, %s! Your mission for today will be to traverse the dungeon, find the hidden treasure, and make it out alive." % name)
command = input("You're at the entrance of the dungeon, what do you do? (Enter/Leave): ")
if command == "Leave":
	print("You're a coward!\n")
elif command == "Enter":
	print("The dungeon is dark and cold. The walls seem to be glistening with blood.\n")
	command = input("You approach a fork. You can hear screams of agony echoing from the left, and you can only see complete darkness on the right. \nWhich direction will you go? (Left/Right): ")
	if command == "Left":
		print("\nYou come across an ugly troll, gnawing on a carcass. It notices you, and closes the gap within the blink of an eye. \nAll you see before the blackness closes in is the troll's club swinging towards you.")
		print("\nYou have died by troll, failing at your mission, %s.\n" % name)
	elif command == "Right":
		print("\nYou feel your way through the darkness by hugging the wall.")
		command = input("As you approach a torch-lit room, a zombie appears! What do you do? (Fight/Flee): ")
		if command == "Flee":
			print("\nI can't believe you ran away. How would you ever expect to be a treasure hunter? FAILURE!\n")
		elif command == "Fight":
			print("\nYou swing your blade at the zombie, swiftly cutting it down in one blow.")
			print("As you step over the fallen body, you see a glistening treasure chest in the back of the room! Opening the treasure chest reveals a cache of gold.")
			print("\nCongratulations! You have succeeded. You're awesome, %s!\n" % name)
		else: print("You need to type the command exactly as is. Restart the program.")
	else: print("You need to type the command exactly as is. Restart the program.")
else: print("You need to type the command exactly as is. Restart the program.")