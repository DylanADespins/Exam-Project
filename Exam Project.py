# Dylan Despins
# 3/7/19

print('A elfish man, in the medieval times where dragons and wizards still existed, was forced to join the Knights of the Blood Oath.')
print('The same elfish man, only a young child now, adventured the lands of Termina.')




try:
    who_will_you_follow = int(input("\n" "Who will you follow? The 17 year old Elfish Man(1) or the 12 year old Elfish Child(2)."))
    if who_will_you_follow == (1):
        print("Your Choice: " + str(who_will_you_follow) + " (Elfish Man)")
        print("The Young Elfish Man was sent out to fight off a dragon")

    if who_will_you_follow == (2):
        print("Your Choice: " + str(who_will_you_follow) + " (Elfish Child)")
        print("The Young Elfish Child was saving the village of Tarnace from hundreds of thieves and bandits attacking after walking the dangerous lands of Termina.")
except ValueError:
    print("Try (1) or (2)")

