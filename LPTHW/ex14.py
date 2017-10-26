from sys import argv

script, user_name, game = argv
prompt = 'Please input here: '

print("Hi %s, I'm the %s script.") %(user_name, script)
print("I'd like to ask you a few questions.")
print("Do you like me %s?") %user_name
likes = str(input(prompt))

print("Where do you live %s?") %user_name
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. You like computer game %s most! Nice.
""" %(likes, lives, computer, game)) 
