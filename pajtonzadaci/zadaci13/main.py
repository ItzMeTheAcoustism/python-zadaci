import random


player_ammo = 0
computer_ammo = 0
computers_options = ["shoot", "defend", "refill"]
players_options = ["shoot", "defend", "refill"]
playing = True


while playing == True:
    player = input("Choose what to do(shoot, defend, refill): ")
    computer = random.choice(computers_options)
    print(computer)
    if player == "shoot" and player_ammo == 0 and computer_ammo == 0 and computer == "shoot":
        print("What bullets are you using exactly?")
        continue
    if player == "shoot" and player_ammo > 0 and computer == "shoot" and computer_ammo == 0:
        player_ammo = player_ammo - 1
        print("I think its dead")
        break
    if player == "shoot" and player_ammo == 0 and computer == "shoot" and computer_ammo > 0:
        computer_ammo = computer_ammo - 1
        print("Welp, skill issue")
        break
    if player == "shoot" and player_ammo > 0 and computer == "shoot" and computer_ammo > 0:
        player_ammo = player_ammo - 1
        computer_ammo = computer_ammo - 1
        print("Now youre both dead, great job")
        break
    if player == "shoot" and player_ammo == 0 and computer == "refill":
        computer_ammo = computer_ammo + 1
        print("Oof, better defend yourself")
        continue
    if player == "shoot" and player_ammo > 0 and computer == "refill":
        computer_ammo = computer_ammo + 1
        player_ammo = player_ammo - 1
        print("Its dead")
        break
    if player == "shoot" and player_ammo == 0 and computer == "defend":
        print("What bullets are you shooting?")
        continue
    if player == "shoot" and player_ammo > 0 and computer == "defend":
        player_ammo = player_ammo - 1
        print("You just wasted a bullet, womp womp")
        continue
    if player == "refill" and computer == "refill":
        computer_ammo = computer_ammo + 1
        player_ammo = player_ammo + 1
        print("Gambling time")
        continue
    if player == "refill" and computer == "shoot" and computer_ammo == 0:
        player_ammo = player_ammo + 1
        print("Shoot, shoot, shoot, shoot")
        continue
    if player == "refill" and computer == "shoot" and computer_ammo > 0:
        player_ammo = player_ammo + 1
        print("Doesnt really matter now, youre dead")
        break
    if player == "refill" and computer == "defend":
        player_ammo = player_ammo + 1
        print("You winning depends on how many bullets the bot has")
        continue
    if player == "defend" and computer == "shoot" and computer_ammo == 0:
        print("How is that useful?")
        continue
    if player == "defend" and computer == "shoot" and computer_ammo > 0:
        computer_ammo = computer_ammo - 1
        print("Youve succsesfully defended yourself from a bullet, how")
        continue
    if player == "defend" and computer == "refill":
        computer_ammo = computer_ammo + 1
        print("Uh uh, its got bullets now")
        continue   