# Dylan Despins
# 3/7/19


'''
The first part of the story starts here
'''
print('A elfish man, in the medieval times where dragons and wizards still existed, was forced to join the Knights of the Blood Oath.')
print('The same elfish man, only a young child now, adventured the lands of Termina.')


'''
If the person doesn't answer with 1 or 2 (Elfish Man or Elfish Child) it will end the program and say Enter (1) or (2) or Use one of the two numbers if they don't use an integer.
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
        print("The Young Elfish Man was sent out to fight off a dragon as a duty for the Kingdom")
# Elfish Child story
    if who_will_you_follow == (2):
        print("Your Choice: " + str(who_will_you_follow) + " (Elfish Child)")
        print("The Young Elfish Child was saving the village of Tarnace from hundreds of thieves and bandits attacking after walking the dangerous lands of Termina.")

except ValueError:
    print("Use one of the two numbers")

while who_will_you_follow == 1:
    print("\n" "The Elfish Man travels up the mountain to find the nest of the dragon and finds that it's just a baby fire dragon ")
    your_own_pet = (input("\n""While it is a baby it still burnt down an entire village. Will you take it in with you on your adventures? (yes/no)"))
    if your_own_pet == ("yes"):
        print ("\n""You move in to try and comfort and tame it, but it rejects your offer and bursts a firey flame towards you.")
        break
    else:
        the_right_choice = input("\n" "It seems to be harmful and could burn down another village, should you slay the dragon? (yes/no)")
        if the_right_choice == ("yes"):
            print("\n"" You move in to slash it with your sword and its mother appears deeper in the cave, and you now understand this is not a mission for you to complete")
            print("\n""You are now known as dead in the kingdom you once served as you never returned from the mission and live in the forest and are one with the animals")

while who_will_you_follow == 2:
    print("\n""The Elfish Child had been defending the village from the bandits for a few hours and finally the action died down.")
    print("\n""The village offers you a gift for protecting them from the bandits, but they have you pick from two chests and you don't know what is in either one of them, all you know is that they both have a item of value in it.))
    the_reward = input("Which chest will you choose? The chest to the left or the chest to the right, some reason the villagers are more directly pointing toward the one to the right.(r/l)")
    if the_reward == r:
          print ("\n""The villagers rewarded you with something of value from all of the villagers, a village of blacksmithes and shopkeepers gave you a mighty sword that they had spent days making before the raid of the bandits")
          print ("\n""This sword gave a very mysterious presence, you slash it around in a field of grass and started to speak to you.")
          break
    if the_reward == l:
          print ("\n"" The villagers rewarded you with a lot of cash, a village of blacksmithes and shopkeepers, you assume the other chest had a sword of some sorts or something.")
          print ("\n"" You still feel like you did the right thing, but the other chest will always be on your mind from here on")
          break
     
