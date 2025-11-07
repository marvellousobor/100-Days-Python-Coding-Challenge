from game_data import data
from art import logo
from art import vs
import random


A = random.choice(data)
B = random.choice(data)

def list(A, B):
    list = [A, B]
    return list

celeb_list = list(A, B) 

def game(celeb_list):
    text = f"Compare A: {celeb_list[0]['name']}, a {celeb_list[0]['description']}, from {celeb_list[0]['country']}.\n {vs}v\n Compare B: {celeb_list[1]['name']}, a {celeb_list[1]['description']}, from {celeb_list[1]['country']}."
    count_A = celeb_list[0]['follower_count']
    count_B = celeb_list[1]['follower_count']
    user_choice = input("Input your choice 'A' or 'B': ").lower()
   
    def compare():
        if user_choice == 'a':
            if count_A > count_B:
                new_item = celeb_list[0]
                list(A = new_item, B = random.choice(data))
                celeb_list = list(A, B)
                game(celeb_list)
            elif count_A < count_B:
                print("You were wrong.")
    compare()
game(celeb_list) 
# def compare(list):
    
#     count_A = list[0]['follower_count']
#     count_B = list[1]['follower_count']
#     user_choice = input("Input your choice 'A' or 'B': ")
    
#     if user_choice == 'a': #place this in another function
#         if count_A > count_B:
#             new_A = A
#             list(A = new_A, B = random.choice(data))
#         elif count_A < count_B:
#             print("You were wrong")
#             play_again = input("Would you like to play again 'y' or 'n'")
#             compare(A, B)
#         print(list)
# compare(list)
    
    
#     # def compare():
#     #     
            
    
# # def compare(A, B):
# #     
            

        
    
