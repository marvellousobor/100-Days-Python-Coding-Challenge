# # Scope
# Modifying Global Scope
enemies = 1
# Avoid modifying global scope. This can cause errors
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}") 

increase_enemies()
print(f"enemies outside function: {enemies}")

enemies = 1

# INSTEAD DO THIS THEN JUST CALL IT
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")

# #Local scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
# drink_potion()
# print(drink_potion)     #unaccessible outside function

#Global Scope
# player_health = 10 #global variable because it is outside any function

# def drink_potion():
#     position_strength = 2 #local variable
#     print(player_health)

# drink_potion()

# game_level = 3

# enemies = ["Skeleton", "Zombies", "Alien"]
# def create_enemy():
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)



#Global scopes are useful for constants e.g
PI = 3.14159            #you can write your code in capital letters to keep note of not changing the value in the variable
TWITTER_HANDLE = "@marvellousobor"
