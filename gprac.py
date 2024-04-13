# import random
# list1 = ["apple", "banana", "orange"]
# v = random.randint(0,2)
# choice = list1[v]
# print(v)
# print(choice)

# import random
# def roll():
#     minimum_val=1
#     maximum_val=6
#     roll=random.randint(minimum_val,maximum_val)
#     return roll
# while True:
#     players=int(input("Enter players (2-4): "))
#     if 2<=players<=4:
#         break
#     else:
#         print("Range is (2-4)")
# max_score=10
# player_scores=[0]*players
# while max(player_scores)<max_score:
#     for i in range(players):
#         print(f"Player {i+1} turn has just started!")
#         print(f"Your score is: ",player_scores[i])
#         current_score=0
#         while True:
#             you_roll=input("You want to roll(yes/no): ")
#             if you_roll.lower()=='no':
#                 break
#             value=roll()
#             if value==1:
#                 print("You rolled 1! Turn done!")
#                 break
#             else:
#                 current_score+=value
#                 print("You rolled a ",value)
#             print("Your current score is: ",current_score)
#         player_scores[i]+=current_score
#         print("Your total score is: ",player_scores[i])

# max_score=max(player_scores)
# winner=player_scores.index(max_score)
# print(f"Player {winner+1} is the winner with a score of: {max_score}")
