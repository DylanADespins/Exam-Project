'''
Dylan Despins
3/7/19
Text Based Adventure
Juan and Alvaro helped with ValueError
'''
name = input("What is your name: ")

def greeting():
    print("Hi there " + name + "!")
    print("Welcome to my text based adventure project.")

greeting()

'''
The first part of the story starts here
If the person doesn't answer with 1 or 2 (Elfish Man or Elfish Child) it will end the program and say Enter (1) or (2) or Use one of the two numbers if they don't use an integer.
'''
print('\n''An elfish man, in the medieval times where dragons and wizards still existed, was forced to join the Knights of the Blood Oath.')
print('\n''The same elfish man, only a young child now, adventured the lands of Termina.')


'''
Below decides which story will be followed and tells bits and pieces in each part 
'''
try:
    who_will_you_follow = int(input("\n" "Who will you follow? The 17 year old Elfish Man(1) or the 12 year old Elfish Child(2)."))
# Elfish Man Story
    if who_will_you_follow > 2:
        print ("Use one of the two numbers")

    if who_will_you_follow < 1:
        print("Use one of the two numbers")

    if who_will_you_follow == (1):
        print("Your Choice: " + str(who_will_you_follow) + " (Elfish Man)")
        print("\n""The Young Elfish Man was sent out to fight off a dragon as a duty for the Kingdom")
# Elfish Child story


    if who_will_you_follow == (2):
        print("Your Choice: " + str(who_will_you_follow) + " (Elfish Child)")
        print("\n""The Young Elfish Child was saving the village of Tarnace from hundreds of thieves and bandits attacking after walking the dangerous lands of Termina.")

except ValueError:
    print("Use one of the two numbers")
#If in the beginning of the program the user types in the number 1 he will see this part of the story and then he will decide if he wants to fight or tame a dragon.
while who_will_you_follow == 1:
    print("\n" "The Elfish Man travels up the mountain to find the nest of the dragon and finds that it's just a baby fire dragon ")
    your_own_pet = (input("\n""While it is a baby it still burnt down an entire village. Will you take it in with you on your adventures? (yes/no)"))
    if your_own_pet == ("yes"):
        print ("\n""You move in to try and comfort and tame it, but it rejects your offer and bursts a firey flame towards you.")
        print("\n""You are now known as dead in the kingdom you once served as you never returned from the mission and live in the forest and are one with the animals.")
        print("\n""Later in life, the elfish man will start a family and make a community of his own where there are shops, blacksmithes, restaurants, bars, etc. in the area.")
        break
    else:
        the_right_choice = input("\n" "It seems to be harmful and could burn down another village, should you slay the dragon? (yes/no)")
        if the_right_choice == ("yes"):
            print("\n"" You move in to slash it with your sword and its mother appears deeper in the cave, and you now understand this is not a mission for you to complete.")
            print("\n""You are now known as dead in the kingdom you once served as you never returned from the mission and live in the forest and are one with the animals.")
            print("\n""Later in life, the elfish man will start a family and make a community of his own where there are shops, blacksmithes, restaurants, bars, etc. in the area.")
            break
# End of Elfish Man Story line
if who_will_you_follow == 1:
    print("\n""Thank you for reading the story of an Elfish Man that was forced into working for the kingdom and only wanted to live in harmony.")


# More to Elfish Child Story line
while who_will_you_follow == 2:
    print("\n""The Elfish Child had been defending the village from the bandits for a few hours and finally the action died down.")
    print("\n""The village offers you a gift for protecting them from the bandits, but they have you pick from two chests and you don't know what is in either one of them, all you know is that they both have a item of value in it.")
    the_reward = (input("Which chest will you choose? The chest to the left or the chest to the right, some reason the villagers are more directly pointing toward the one to the right.(r/l)"))
    if the_reward == ("r"):
          print ("\n""The villagers rewarded you with something of value from all of the villagers, a village of blacksmithes and shopkeepers gave you a mighty sword that they had spent days making before the raid of the bandits")
          print ("\n""This sword gave a very mysterious presence, you slash it around in a field of grass and started to speak to you.")
          break
    if the_reward == ("l"):
          print ("\n"" The villagers rewarded you with a lot of cash, a village of blacksmithes and shopkeepers, you assume the other chest had a sword of some sorts or something.")
          print ("\n"" You still feel like you did the right thing, but the other chest will always be on your mind from here on.")
          break

# End of part of Elfish Child Story line if user typed in left or l
if who_will_you_follow == 2:
    if the_reward == ("l"):
        print("\n""The child upgraded his equipment at the village with the money he achieved and grew up while saving other villages with more rewards.")


    if the_reward == ("r"):
        print("You run into a bandit that was abandoned by the others and he aggressively runs toward you with his sword.")
        dodging_slashes = int(input("The bandit slashes at you a total of 3 times. How many times do you want to dodge(2 or 3)?"))
        for i in range(dodging_slashes):
            if dodging_slashes == 2:
                print("\n""You successfully dodge 2 of the bandits foul swoops toward you but the other one went quite deep")
                print("\n""You slash back, but he notices that you are just a kid and he is pure of heart, stops you and requests that he helps you with your wound.")
                break
            if dodging_slashes == 3:
                print("\n""You successfully dodge the 3 slashes and pin him down and take his sword you get the villagers out to help you out and put him in jail.")
                print("\n""You are used to the new sword now and it speaks to you to help anyone you can, teaching you to spread peace to other villages and stop anyone that tries to violate peace.")
                break

if who_will_you_follow == 2:
    print("\n""Thank you for reading the story of an Elfish Child that was protecting the village from bandits and wanted peace across the land.")
# End of Elfish Child Story line if user typed in right or r