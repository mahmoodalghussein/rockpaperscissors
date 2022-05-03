from random import randint

shapes = ["Rock", "Paper", "Scissors"]


def cpu_won():
    print("HA noob, I won ")


def player_won():
    print("oh fuck, I lost ")


def tie():
    print("Tie")


while True:
    cpu_hand = shapes[randint(0, 2)]
    player_hand = input("Rock, Paper or Scissors? ")
    if player_hand in shapes:
        print(f"I picked {cpu_hand}")
        if player_hand == cpu_hand:
            tie()
        elif player_hand == "Paper":
            if cpu_hand == "Scissors":
                cpu_won()
            else:
                player_won()
        elif player_hand == "Rock":
            if cpu_hand == "Paper":
                cpu_won()
            else:
                player_won()
        elif player_hand == "Scissors":
            if cpu_hand == "Rock":
                cpu_won()
            else:
                player_won()
    else:
        print("wtf? learn english!")

