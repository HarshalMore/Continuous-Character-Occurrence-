# Continuous-Character-Occurrence-
Getting index positions of the repeated characters in a given string.

This program returns the starting index and ending index of the 
consecutive repeated characters if the character is repeated more than n times.
Here, n is called 'repeat_threshold' and it is provided by the user.

For e.g. input 'Heeeello' for repeat_threshold 2 would return {'e':[(1,4)]} 
as the letter 'e' is repeated more than twice consecutively. Here 1 is 
the start index of the repeated character(i.e. 'e' in this case) and 
4 is the end index. 
similarly, input 'Hiiii, what uppp?' for repeat_threshold 2 would 
return {'i':[(1,4)], 'p':[(13,15)]}.

This program also provides an option to select your own text file as an
input. Just make sure that you keep both .py file and .txt file in the same 
folder.
