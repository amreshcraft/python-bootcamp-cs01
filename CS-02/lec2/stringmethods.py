word = "hello world, are You Polluted?"

print(word)
print(word.capitalize()) # capitalizes the first letter of the string and remainig is in lower case
print(word.upper()) # converts the string into upper case
print(word.lower()) # converts the string into lower case
print(word.title()) # capitalizes the first letter of each word in the string

c = word.count("o")
print(c ) # counts the number of occurences of the given character in the string

index = word.find("o")
print(index) # returns the index of the first occurence of the given character in the string

print(word.replace("o","z")) # replaces the given character with the new character in the string
print(word)

print(word.endswith("Polluted?")) # returns True if the string ends with the given character or substring, else returns False

print(word.startswith("hello")) # returns True if the string starts with the given character or substring, else returns False

print(word.split(" ")) # splits the string into a list of substrings based on the given delimiter

word
