import random
def roll(min, max, challenge):
    diceTotal=0 
    ch=("Rolling for c", challenge )
    print(ch)
    diceTotal=random.randint(min, max)
    print(diceTotal)
    return(diceTotal)
Totalscore=0
print("This is a challenge for Health!")           
chlth = roll(1, 12, "hlth")
print("This is a challenge for Strength!")           
cstr= roll(1, 12, "str")    
print("This is a challenge for Dexterity!")           
cdex= roll(1, 12, "dex")
cdic = {"Strength": cstr, "Health": chlth,  "Dexterity": cdex}
print("\n")
print(cdic, "\n")
Totalscore= cstr+cdex+chlth
if Totalscore > 20:
    print("Total score more than 20 you have won the game")
else:
    print("you have lost the game")

        