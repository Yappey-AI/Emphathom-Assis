
print("Hello, I am Emphathom")

#What we doing?
a = input("What are we up to today? ").strip().capitalize()
if a == "Nothing":
    print("What's wrong bro, You tired or something?")
elif a == "Study" or a == "Studying":
    print("Aight, Leme know if you need help.")
elif a == "Work" or a == "Coding":
    print("Oh, So i don't have memory rn, Leme know if we have previosuly tlaked about it or if we are starting fresh.")
else:
    print(f"Aight, I'll find info on {a}.")