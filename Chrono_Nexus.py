name = input("Type your name: ")
print("Welcome", name, "to Chrono Nexus: The Key of Destiny!")
print("In the sprawling metropolis of Evershade, a quiet museum holds an artifact of unimaginable power, known as the Chrono Nexus. Legend has it that this mysterious device can manipulate time itself, granting its possessor the ability to shape their destiny. You, as the protagonist, find yourself drawn into a web of intrigue as you stumble upon the existence of this artifact. Your adventure begins with a simple visit to the Evershade Museum, but your choices will determine the fate of the world.")
answer=input("You are on a dirt road which has come to an end. You see a museum infront of you, Do you wish to enter or walk away?.(enter/walk)?" ).lower()
if answer=="enter":
    answer = input("You enter the huge museum. In the midst of if it is kept a diary, Do you want to read or explore?(read/explore)").lower()
    if answer == 'read':
        print("You proceed to read the diary which consists of secrets and unravellings of the past. As you read further and further, you begin to lose consciousness and drift away into the century when the diary was engraved upon")
    elif answer == "explore":
        answer =input("You continue to walk across the museum, You proceed to see a room full of gold but its locked. Do you want to find they key or walk away?(find/walk)").lower()
        if answer=='find':
            answer=input("You can either go left or right. Which way would you tread upon?(left/right)").lower()
            if answer=='left':
                print("You walk into a room full of mines. Unfortunately you step on one and die.")
            elif answer=='right':
                print("You find the key. You open the door to the room which contains the gold which can set you free for life. You Win!")
    else:
        print('Not a valid option. You lose.')
elif answer == 'walk':
    answer= input("You proceed to walk away. You see a wobbly bridge which takes you across a river, would you like to cross it or swim across?(cross/swim)").lower()
    if answer=='cross':
        print("The bridge stars wobbling, it snaps from one side, you fall into the river and get eaten by alligators.")
    elif answer=='swim':
        print("You start swimming, as soon as you're halfway, an alligator eats you and you die.")
    else:
        print('Not a valid option. You lose')
else: 
    print('Not a Valid option. You lose') 