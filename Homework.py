s = input("Please enter a string: ")
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
position = s[0]
longest = ""
sReverse = s[::-1]
longestReverse = longest[::-1]

for i in range(len(s)-1):
   if s[i] <= s[i+1]:
       longest = longest + s[i]
if sReverse[0] >= longest[::-1]:
    longest = longest + sReverse[0]
else:
    print("Lets see if this works")

print("Your String is: ", s)
print("Longest Alphabetical Sub String: ", longest)