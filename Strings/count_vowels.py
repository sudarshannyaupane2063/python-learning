#for counting total vowels contained in a string

string = "randomized"
vowels = 0

vowels+=string.count("a")
vowels+=string.count("e")
vowels+=string.count("i")
vowels+=string.count("o")
vowels+=string.count("u")

print("There are total",vowels,"vowels.")