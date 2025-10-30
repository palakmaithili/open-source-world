# Defining function to reverse words

def rev(s):

# Split the string into words and reverse the word order

words = s.split()

rev = " ".join(reversed(words))

return rev

 

# Printing the reverse words of a string

my_string = "Hello HeroVide!"

print(f"The reversed words of the string {my_string} is: {rev(my_string)}")

