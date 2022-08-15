print("Welcome to XO Borad Game!\n")
print("The rules of this game are:")
print("Enter where you want to place your character as example 1,a without spaces or capitalisation")

print("Choose which character you want to play: ")
user_chr = input()

while True:
    if user_chr == 'X' or user_chr == 'x' or user_chr == 'O' or user_chr == 'o':
        break
    else:
        print("Please choose betwwen X or O.")
        user_chr = input()

def print_board():
    print("  a   b   c")
    print("1   |   |   ")
    print(" -----------")
    print("2   |   |   ")
    print(" -----------")
    print("3   |   |   ")

def p1_plc_chr():
    print("Enter location of your character")
    p1_pl = input()

print_board()

if user_chr == 'X' or user_chr == 'x':
    p1_plc_chr()
    