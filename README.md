# Generative-Algorithm-Password-Guesser


genetic algorithm
this programm works by giving a password and then letting a generative algorythm figure it out by grading its trys on how close they are to the password
first it randomly generates 80 strings and then gives them points on how close they are to the password and then the top 10 are kept and 10 are randomly chosen from the 70 remaining strings.

then the strings are doubled by crossbreeding them that means that with 2 strings and then replace characters from the first with the other one.

for example you have the strings "food" and "milk" now we randomly take the first and last char from "food" and replace them in milk "filk" now since we took "f" and "d" from "food" we can also take the chars that were replaced by "f" and "d" in our "milk" string so "m" and "k" and modify the "food" srting with them so it becomes "mook"

and like this we have 40 string now we need 80 again and to do that we double the strings by just cloning the first 40 again and mutate the 40 clones

here mutating here can happens randomly so there is always a chance that something doesnt mutate

mutating works like this for every letter in the string there is a chance it chance that it changes the letter and there is a chance for the letter to get shorter or longer


and this is how the genertive algorithm works to guess a password this is more a plaything and only the concept has real world application


you can play araound with it by changing the password at the begginning of the code
