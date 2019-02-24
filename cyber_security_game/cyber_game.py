import pygame

import sys

from settings import Settings
from player import Player
from terminal import Terminal
from room import Room

def check_events(player,terminal,state,room):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True 
                player.orientation = 'right'
            elif event.key == pygame.K_LEFT:
                player.moving_left = True 
                player.orientation = 'left'
            elif event.key == pygame.K_DOWN:
                player.moving_down = True 
            elif event.key == pygame.K_UP:
                player.moving_up = True
            elif event.key == pygame.K_RETURN:
                user_input = terminal.get_input()
                if state == -1:
                    terminal.next_line(["No terminal to recieve command."])
                else:
                    output = room.terminals[state].get_response(user_input)
                    terminal.next_line(output)
            elif event.key == pygame.K_BACKSPACE:
                terminal.delete()
            else:
                terminal.add_char(event.unicode)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            elif event.key == pygame.K_LEFT:
                player.moving_left = False
            elif event.key == pygame.K_DOWN:
                player.moving_down = False
            elif event.key == pygame.K_UP:
                player.moving_up = False


        
        
def get_terminal_collision(player,room):
    i = 0
    for computer in room.terminals:
        if pygame.sprite.collide_rect(computer,player):
            return i
        i = i + 1
    return -1
    
def run_game():

    # Initialize game and create a screen object.
    
    state = 'none'
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Cyber Game")
    
    player = Player(settings,screen)
    
    terminal = Terminal(settings,screen,'')
    room1 = Room(settings,screen)
    room1.add_terminal(75,639,130,105,'','You are at the Computer. Try to get the safe code from it.',False)
    room1.terminals[0].add_response('help',['Commands:','help','echo','safe code','','Type in unfamiliar words or phrase to search them (ex. brute force)','Come back here whenever you are stuck'])
    room1.terminals[0].add_response('echo',['echo'])
    room1.terminals[0].add_response('safe code',['5902'])
    room1.terminals[0].add_response('brute force',['Brute force can be helpful for finding simple password.',
                                                    'Computers can be helpful to speed this up',
                                                    'Common Bad Passwords: 123456, Password, qwerty, abc123'])
    room1.terminals[0].add_response('the answer to the life the universe and everything',['Password from part 3: 42'])
    room1.terminals[0].add_response('what is the answer to the life the universe and everything',['Password from part 3: 42'])
    room1.terminals[0].add_response("Hichicker's guide to the Galaxy",['Password from part 3: 42'])
    room1.terminals[0].add_response('cat',['Linux command to read the given file'])
    room1.terminals[0].add_response('ls',['Linux command to list everything in the current folder'])
    room1.terminals[0].add_response('cd',['Linux command to chnage directory (you move into a new folder)'])
    room1.terminals[0].add_response('caesar shift',['A cipher where every letter is moved down n letters in the alphabet',"For Example: 'abc' rot 3 would become 'def'",
                                                    'Your command line has a caesar shift decoder','just type "shift <text> <n>"'])
    room1.terminals[0].add_response('shift',['A cipher where every letter is moved down n letters in the alphabet',"For Example: 'abc' rot 3 would become 'def'",
                                                    'Your command line has a caesar shift decoder','just type "shift <text> <n>"'])
    room1.terminals[0].add_response('hexadecimal',['Hexidecimal is base 16, meaning that in addition to the','digits 0-9, it also has "digits" A-F, where A = 10,',
                                        'B=11, etc. As in base ten, each digit to the left has a greater',
                                         'power of the base. In hexadecimal, 26 would be represented as 1A',
                                         'where the 1 represents 16 and A represents 1',
                                         "Type 'hex to dec <hex num>' in your terminal to convert a",
                                         'hexadecimal number to a base ten number'])
    room1.terminals[0].add_response("Three Cups of Tea",['Password from part 4: is the number in the title']) 
    
    room1.add_terminal(640,624,102,120,'5902','Open the Safe.',True)
    room1.terminals[1].add_response('help',['Commands:','ls -> examines safe','cat <text name> -> reads the chosen text','','(Hint) people often choose password numbers from their interests'])
    room1.terminals[1].add_response('ls',['You see two books, book1.txt and book2.txt'])
    room1.terminals[1].add_response('cat book1.txt',["Hichicker's guide to the Galaxy","...the answer to the Life, the Universe, and Everything is..."])
    room1.terminals[1].add_response('cat book2.txt',["Three Cups of Tea"])
     
     
    room1.add_terminal(440,35,300,70,'Password','Get more info about Brute force and search the desk.',True)
    room1.terminals[2].add_response('help',['You can use the ls command to see where you are','and cd <filename> to move through files','cd .. will move you up a folder'])
    
    room1.add_terminal(623,510, 138,106,'','Phone. Dial the secret number.',False)
    room1.terminals[3].add_response('help','Phone. Dial the secret number.')
    room1.terminals[3].add_response('9',['mvezmzuzmztyz'])
    room1.terminals[3].add_response('2078037452',['A trapdoor opens from beneath the rug'])
    
    
    room1.add_terminal(8,165,124,338,'','You are at the Sofa. What do you want to do?',False)
    room1.terminals[4].add_response('help',["You are at the Sofa. What do you want to do?"])
    room1.terminals[4].add_response('search',["You find a slip of paper with the following text: '7E3'"])
    room1.terminals[4].add_response('search sofa',["You find a slip of paper with the following text: '7E3'"])
    room1.terminals[4].add_response('look',["You find a slip of paper with the following text: '7E3'"])
    room1.terminals[4].add_response('ls',["You find a slip of paper with the following text: '7E3'"])
    room1.terminals[4].add_response('sleep',["You sleep for some time"])
    room1.terminals[4].add_response('sit',["You sit for some time"])
    
    
    room1.add_terminal(465,639,161,125,'','Get the right station in the Radio.',False)
    room1.terminals[5].add_response('2019',['Password from part 1: HackCU'])
    
    
    room1.add_terminal(140,215,136,240,'','Just a carpet. Or is it?',False)
    room1.terminals[6].add_response('help',['Just a carpet. Or is it?'])
    room1.terminals[6].add_response('roll',['A trapdoor is revealed underneath'])
    room1.terminals[6].add_response('enter',['Good job!','You found the back entrance, the one that is often','forgotten about. Remember, no matter how strong your',"encryption is, you're still suceptible to a personal password attack"])
    room1.terminals[6].add_response('enter trapdoor',['Good job!','You found the back entrance, the one that is often','forgotten about. Remember, no matter how strong your',"encryption is, you're still suceptible to a personal password attack"])
    room1.terminals[6].add_response('enter door',['Good job!','You found the back entrance, the one that is often','forgotten about. Remember, no matter how strong your',"encryption is, you're still suceptible to a personal password attack"])
    room1.terminals[6].add_response('open trapdoor',['Good job!','You found the back entrance, the one that is often','forgotten about. Remember, no matter how strong your',"encryption is, you're still suceptible to a personal password attack"])

    room1.add_terminal(243,1,72,104,'HackCUvenividivichi423','Combine the 4 passwords to open the lock',True)
    room1.terminals[7].add_response('help',['Open the lock with the password you have obtained.'])
    room1.terminals[7].add_response('open door',['Good job','You escaped'])
    room1.terminals[7].add_response('open',['Good job','You escaped'])
    room1.terminals[7].add_response('enter door',['Good job','You escaped'])
    room1.terminals[7].add_response('enter',['Good job','You escaped'])
    
    
    # Start the main loop for the game.
    while True:
        check_events(player,terminal,state,room1)
        
        # Redraw the screen during each pass through the loop.
        screen.fill(settings.bg_color)
        
        player.update()
         
        terminal.draw()
        room1.draw()
        
        player.blitme()
        
        state = get_terminal_collision(player,room1)
        if state == -1:
            terminal.update_header("No Signal.  Type help in any terminal to get more info.")
        else:
            terminal.update_header(room1.terminals[state].terminal_name)


        pygame.display.flip()

run_game()

