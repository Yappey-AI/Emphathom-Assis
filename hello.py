def greet(x="User"):
    print(f"Hello {x}!, I am Emphathom.")
greet()
def get_name():
    return input("What is your name? ").strip().capitalize()

name = get_name()
#What we doing?
def get_activity():
    return input(f"Aight {name}, what are we up to today? ").strip().capitalize()
a = get_activity()

if a == "Nothing":
    print("What's wrong bro, You tired or something?")
elif a == "Study" or a == "Studying":
    print("Aight, Leme know if you need help.")
elif a == "Work" or a == "Coding":
    print("Oh, So i don't have memory rn, Leme know if we have previosuly tlaked about it or if we are starting fresh.")
else:
    print(f"Aight, I'll find info on {a} for you.")









def greet():
    print("Hello! I am Emphathom.")
    print("Will you be able to understand me?")

def get_name():
    name = input("What is your name? ").strip().capitalize()
    return name

def get_activity(name):
    a = input(f"Aight {name}, what are we up to today? ").strip().lower()
    return a

def respond(a, name):
    if "nothing" in a:
        print(f"What's wrong {name}, you tired or something?")
    elif "study" in a:
        print(f"Aight {name}, leme know if you need help.")
    elif "coding" in a or "work" in a:
        print(f"Let's get it {name}, I'm right here with you.")
    elif "bye" in a or "quit" in a:
        print(f"Aight {name}, I'm here whenever you need me.")
    else:
        print(f"Aight {name}, I'll find info on {a} for you.")

def main():
    greet()
    name = get_name()
    a = get_activity(name)
    respond(a, name)

main()