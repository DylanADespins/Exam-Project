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
    if who_will_you_follow == int(1):
        print("Your Choice: " + str(who_will_you_follow) + " (Elfish Man)")
        print("The Young Elfish Man was sent out to fight off a dragon")
# Elfish Child story
    if who_will_you_follow == (2):
        print("Your Choice: " + str(who_will_you_follow) + " (Elfish Child)")
        print("The Young Elfish Child was saving the village of Tarnace from hundreds of thieves and bandits attacking after walking the dangerous lands of Termina.")
    else:
        print ("Enter (1) or (2)")
except ValueError:
    print("Use one of the two numbers")


