import pygame
from pygame.sprite import Sprite

class Computer(Sprite):
    
    def __init__(self, rect, password, terminal_name,is_locked):
        super().__init__()
        self.rect = rect
        self.is_locked = is_locked
        self.password = password
        self.responses = {}
        self.is_door = False
        if terminal_name == 'Get more info about Brute force and search the desk.':
            self.dir = 0
        self.terminal_name = terminal_name
        
    def add_response(self,user_input,response):
        self.responses[user_input.lower()] = response
        
    def get_response(self,user_input):
        if self.is_locked and user_input == self.password and self.is_door:
            self.is_locked = False
            return ["Door Unlocked!"]
        elif self.is_locked and user_input == self.password and not self.is_door:
            self.is_locked = False
            return ["Terminal Unlocked!"]
        elif self.is_locked and user_input != self.password:
            return ["Wrong Password,","try again"]
        elif user_input[0:5] == 'shift':
            try:
                rot = int(user_input[-2:])
                a = self.caesar_shift(rot,user_input[6:-2])
                return [a]
            except:
                return ["Command not understood"]
        elif user_input == 'ls' and self.terminal_name == 'Get more info about Brute force and search the desk.':
            if self.dir == 0:
                return['office passwords','python files','door password']
            elif self.dir == 1:
                return["july_pass.txt","october_pass.txt","january_pass.txt","april_pass.txt"]
            elif self.dir == 2:
                return ["trapdoor.py"]
            elif self.dir == 3:
                return ["part1.txt","part2.txt","part3.txt","part4.txt"]
        elif user_input[0:2] == 'cd' and self.terminal_name == 'Get more info about Brute force and search the desk.':
            if user_input[3:] == 'office passwords':
                self.dir = 1
                return ["Done","Secure agencies must change their passwords every three month..."]
            elif user_input[3:] == 'python files':
                self.dir = 2
                return ["Done"]
            elif user_input[3:] == 'door password':
                self.dir = 3
                return ["Done"]
            elif user_input[3:] == '..':
                self.dir = 0
                return ["Done"]
            else:
                return ["Command not understood"]
        elif user_input[0:3] == 'cat' and self.terminal_name == 'Get more info about Brute force and search the desk.':
            if user_input[4:] == "july_pass.txt":
                return ["summer 2018"]
            elif user_input[4:] == "october_pass.txt":
                return ["fall 2018"]
            elif user_input[4:] == "january_pass.txt":
                return ["winter 2018"]
            elif user_input[4:] == "april_pass.txt":
                return ["spring 2018"]
            elif user_input[4:] == "trapdoor.py":
                return ["if phone dial == 2078037452:","    open trapdoor"]
            elif user_input[4:] == "part1.txt":
                return ["Well hidden in the sofa, convert back from hexadecimal, tune in"]
            elif user_input[4:] == "part2.txt":
                return ["Dial 9, apply caesar shift"]
            elif user_input[4:] == "part3.txt":
                return ["The answer is in the best book in the galaxy"]
            elif user_input[4:] == "part4.txt":
                return ["Warm up to a few hot drinks while reading this book"]
            else:
                return ["Command not understood"]
        elif user_input[0:10] == 'hex to dec':
            return[str(int(user_input[11:],16))]
        else:
            try:
                return self.responses[user_input.lower()]
            except KeyError:
                if self.terminal_name == 'Get the right station in the Radio.':
                    return "Sshhhh"
                else:
                    return ["Command not understood"]
                
        
    
    def caesar_shift(self, rot, alpha):
         new_string = ''
         rot = rot % 26
         for char in alpha:
            if char.isalpha():
                if ord(char) + rot > ord('z'):
                    new_string = new_string + (chr(ord(char) + rot - 26))
                else:
                    new_string = new_string + (chr(ord(char) + rot))
            elif char == ' ':
                pass
            else:
                return "Caesar shift takes letters only"
         if new_string == "venividivichi":
             new_string = "Password from part 2: " + new_string
         return new_string
     
        
