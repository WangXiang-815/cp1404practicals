"""
languages.py
client code
"""

#import class ProgrammingLanguage
from programming_language import ProgrammingLanguage

def main():
    #these 4 lines are copied from readme.md :)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python) #check if __str__ method working

    #create a list to store 3 existing objects
    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are: ")
    #loop to find and print which language is dynamic
    for language in languages:
        #use is_dynamic() method
        if language.is_dynamic():
            print(language.name)

#call main func
main()
