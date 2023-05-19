from time import sleep
from os import system
import random, re

try:
    from colorama import Fore, Style, init # For colored text
    
    init(True)
except ModuleNotFoundError:
    print('''
--------------------------
          Warning!
You do not have the module
colorama installed. Please
open your command prompt
and install the colorama 
module.

To install, type:
  pip install colorama
--------------------------''')
    exit()

tile_choices = random.choice([list(emojis) for emojis in # Convert to list
    [
        '🟧🟥🟨🟩🟦🟪🟫⬛',
        '😀🤣😅😎😍🤔😏😭',
        '🎉🎈👖👑💎🍕🎣🎮',
        '🌭🍿🍟🍔🍕🥞🍣🍜'
    ] # Emojis to use
])

tiles = [ # Set to -1 because its just a placeholder value for now :D
    -1, -1, -1, -1,
    -1, -1, -1, -1,
    -1, -1, -1, -1,
    -1, -1, -1, -1
]

found_tiles = []

for tile_choice in range(8): # Initializes tiles
    empty_tiles = []
    
    for index, tile in enumerate(tiles):
        if tile == -1:
            empty_tiles.append(index)
            
    first_choice = empty_tiles.pop(random.randint(0, len(empty_tiles) - 1))
    second_choice = empty_tiles.pop(random.randint(0, len(empty_tiles) - 1))
    
    tiles[first_choice] = tile_choice
    tiles[second_choice] = tile_choice


def display_tiles(show: list=[]) -> None:
    rendered_tiles = [tile_choices[tile_id] if index in show else '🔳' for index, tile_id in enumerate(tiles)] # Uhh idk it works tho
    
    print(f'    [{Fore.YELLOW}A{Fore.RESET}][{Fore.YELLOW}B{Fore.RESET}][{Fore.YELLOW}C{Fore.RESET}][{Fore.YELLOW}D{Fore.RESET}]')
    print(f'[{Fore.YELLOW}1{Fore.RESET}]', ' '.join(rendered_tiles[:4])) # First row
    print(f'[{Fore.YELLOW}2{Fore.RESET}]', ' '.join(rendered_tiles[4:8])) # Second row
    print(f'[{Fore.YELLOW}3{Fore.RESET}]', ' '.join(rendered_tiles[8:12])) # Third row
    print(f'[{Fore.YELLOW}4{Fore.RESET}]', ' '.join(rendered_tiles[12:])) # Fourth row
    print('') # Empty line for padding

def coords_to_index(coords: str) -> int:
    coords = coords.strip() # Removes spaces at the end and stuff
    
    x = (ord(coords[0]) - 65) # Gets ASCII code (A = 65, B = 66), so if we subtract 65, we get A = 0, B = 1, C = 2, D = 3
    y = int(coords[1]) - 1
    
    return y * 4 + x

clear = lambda: system('cls') # Clears console

while len(found_tiles) < 16:
    clear() # Clear tiles cuz no peeking!!!
    display_tiles(found_tiles)
    
    print(f'Select {Fore.GREEN}2{Fore.RESET} tiles, or type {Fore.YELLOW}q{Fore.RESET} to give up.')
    print(f'    {Fore.BLUE}Example:')
    print(f'        First tile: {Fore.YELLOW}A1')
    print(f'        Second tile: {Fore.YELLOW}D2')
    print('') # Empty line for padding
    
    valid_first_tile = False
    first_choice = ''
    first_choice_index = 0
    
    while not valid_first_tile:
        first_choice = input(f'{Fore.BLUE}First tile{Style.RESET_ALL}: ').capitalize()
        
        if re.match('^[A-D][0-4]$', first_choice): # Basically, the if statement only runs if the coords are correct
            valid_first_tile = True
            first_choice_index = coords_to_index(first_choice)
        elif first_choice == 'Q': # If quit
            clear()
            display_tiles(range(16))
            break
        else:
            print(f'{Fore.RED}Invalid!')
    
    valid_second_tile = False
    second_choice = ''
    second_choice_index = 0
    
    while not valid_second_tile:
        second_choice = input(f'{Fore.BLUE}Second tile{Style.RESET_ALL}: ').capitalize()
        
        if re.match('^[A-D][0-4]$', second_choice): # Basically, the if statement only runs if the coords are correct
            valid_second_tile = True
            second_choice_index = coords_to_index(second_choice)
        elif second_choice == 'Q': # If quit
            clear()
            display_tiles(range(16))
            exit()
        else:
            print(f'{Fore.RED}Invalid!')
    
    clear()
    
    display_tiles([first_choice_index, second_choice_index] + found_tiles)
    
    if tiles[first_choice_index] == tiles[second_choice_index]:
        print(f'{Style.BRIGHT}{Fore.RED}M{Fore.YELLOW}A{Fore.GREEN}T{Fore.CYAN}C{Fore.BLUE}H{Fore.MAGENTA}!{Style.RESET_ALL} You found the {tile_choices[tiles[first_choice_index]]} pair!')
        found_tiles += [first_choice_index, second_choice_index] # Adds the pair to the show index
    
    if len(found_tiles) >= 16:
        print(f'{Style.BRIGHT}{Fore.GREEN}YOU WIN!')
    else:
        sleep(3)
        
input('Press Enter to quit.')
