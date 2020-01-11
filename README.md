# Generative-Algorithm-Password-Guesser


genetic algorithm
this programm works by giving a password and then letting a generative algorythm figure it out by first 80 generating random strings and then grading them on how close they are to the password and then by working the algorithm

# In more detail

First it randomly generates 80 strings with varing lenght this is only done at the beginning the following parts are done indefinetly until the password is found.

Then gives them points on how close they are to the password and then the top 10 are kept and 10 are randomly chosen from the 70 remaining strings the rest are deleted.

Then the strings are doubled by crossbreeding them.

# A detailed explaination of crossbreeding
For example you have the strings "food" and "milk" now we randomly take the first and last letter from "food" and replace them in milk: "filk".Now since we took "f" and "d" from "food" we can also take the letters that were replaced by "f" and "d" in our "milk" string so "m" and "k" and modify the "food" srting with them so it becomes:"mook".In the programm we keep both these strings.

And like this we have 40 string now we need 80 again since we originaly had 80 and to do that we double the strings by just cloning the first 40 again and mutate the 40 clones

# More on Mutating
Mutating means randomly changing the strings a bit.
Mutating happens randomly so there is always a chance that something doesnt mutate.

Mutating works like this for every letter in the string there is a chance it chance that it changes the letter and there is a chance for the word to get shorter or longer.

Then we go back to grading the 80 and keeping the top 10 and randomly choosing another 10.

We do that until the password is found or the programm is stopped.


And this is how the genertive algorithm works to guess a password this is more a plaything and only the concept has real world application


you can play araound with it by changing the password at the begginning of the code
