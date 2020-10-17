msg = "Hello fellow detectives and welcome to Ulitimate Crime Solvers "
print(msg)
msg = "Are you a good cop or a bad cop? There has been a recent crime at a university and which ever detective solves the crime he or she recieves a bonus. "
print(msg)
choice = None
choice = input("Choice: ")
print(choice)
  # create new char
if choice == "good":
        name = input("What name do you want your character to have?: ")
        while name == "":
            name = input("What name do you want your character to have?: ")
        cname = name.capitalize() 
        import Goodcop
else :       
        name = input("What name do you want your character to have?: ")
        while name == "":
            name = input("What name do you want your character to have?: ")
        cname = name.capitalize()
        import Badcop
       
