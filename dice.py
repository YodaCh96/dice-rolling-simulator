import random

ΜΑΧ = 6
ΜΙΝ = 1

roll_again = "yes"

while (roll_again.lower() == "yes") or (roll_again.lower() == "y"):
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(ΜΙΝ, ΜΑΧ))
    print(random.randint(ΜΙΝ, ΜΑΧ))
    roll_again = input("Roll the dices again? ").strip()
