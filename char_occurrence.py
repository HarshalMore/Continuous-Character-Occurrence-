'''
Author : Harshal More
Code created on: 16th Oct, 2019 (Google coding interview question - Phone screen round)

This program returns the starting index and ending index of the consecutive repeated characters if the character is repeated more than n times. Here, n is called 'repeat_threshold' and it is provided by the user.

For e.g. input 'Heeeello' for repeat_threshold 2 would return {'e':[(1,4)]} as the letter 'e' is repeated more than twice consecutively. Here 1 is the start index of the repeated character(i.e. 'e' in this case) and 4 is the end index. similarly, input 'Hiiii, what uppp?' for repeat_threshold 2 would return {'i':[(1,4)], 'p':[(13,15)]}.

This program also provides an option to select your own text file as an input. Just make sure that you keep both .py file and .txt file in the same folder.
'''
#a = "wowww!fff"
#a = "Helloooo!eee,oooo ffff"
#a = "aassddff rrr-eeeerrr!"

print("""\nFor an input string, you can find the start and end index of all the
consecutive repeated characters based on the repeating threshold you provide.""")

#global variables
global input_string 
global repeat_threshold 

#give user a choice to either type out the string on the
#user prompt or upload a txt file 
print("\nChoose one of the following options:(type 1 or 2)")


#mechanism to check user entered choice
while True:
  user_choice = input("""\n1: Enter the string on the prompt\n2: Use your own file (Use the text file and keep it in the same directory as this one)\n""")
  if(user_choice == '1'):
    input_string = input("\nEnter the input string:\n")
    break

  elif(user_choice == '2'):
    userfile = open("test.txt","r") 
    content = userfile.read()
    break
  else:
    print("\nPlease type 1 or 2 to select one of the below choices!")
    continue

#mechanism to accept values greater than 0 for repeat threshold
while True:
  try:
    repeat_threshold = int(input("\nEnter the repeat threshold value:\n"))
  except ValueError:
    print("\nPlease enter a number greater than 0.")
    continue
  if(repeat_threshold <= 0):
    print("\nPlease enter a number greater than 0.")
    continue
  else:
    break
#function that takes a string and repeat threshold as parameters
def char_occ(a,repeat_threshold):
  
  if(a != ''):
    visited = a[0] #keeps track of the visited character in a given string
    index = [] #keeps track of the index postion of starting and ending index 
    char = [] #keeps track of the repeating character
    combine = [] #this is to combine the starting index and the ending index from a list of indices
    count_count = [] #to keep the track of the count variable. if count of any chracter goes beyond the threshold value,we append that count value to count_count list. This means that there IS a character which has repeated more than the threshold value otherwise there is no such character
    new_dic = {} #to store the characters with thier index positions
    blank = [] 
    count = 0 
    last_char = 0 #to keep the track of the last character

    for i in range(1,len(a)):
      last_char += 1 
      if(a[i] == visited[-1]):
        count += 1
        visited = visited + a[i]
        if(count == repeat_threshold):#wowww
          if(last_char == len(a)-1): #last char w

            index.append(i-repeat_threshold)
            index.append(i)
            if(a[i] != " "):
              char.append(a[i])
            else:
              char.append("<Space>")
            count_count.append(count)
            count = 0
          else: # if it's not the last character
            index.append(i-repeat_threshold) 
            if(a[i] != " "):
              char.append(a[i])
            else:
              char.append("<Space>")
            count_count.append(count)

        elif(count >= repeat_threshold and last_char == len(a)-1): #wowww
          index.append(i)
          #count_count.append(count)
          #count = 0
    
      elif(a[i] != visited[-1] and count >= repeat_threshold): #wowwww!
        index.append(i-1)
        count_count.append(count)
        count = 0
        visited = visited + a[i]

      else: #if nothing, just add the char in the visited list
        count_count.append(count)
        count = 0
        visited = visited + a[i]
    #print(count_count)
    #if none character is repeated more than the threshold
    if(all(x <= repeat_threshold-1 for x in count_count)): 
        print("\nNo character has been repeated more than",repeat_threshold,"times consecutively!")
        
    #combine the elements of the 'index' list pair wise
    for j in range(0,len(index),2):
      combine.append(index[j: j + 2]) #a = [[0, 3], [5, 7], [9, 11]]
    
    #add all the index positions of the same character
    #under the same key using a dictionary 
    # for e.g. new_dic = {'a': [[0, 3], [9, 11]], 't': [[5, 7]]}
    for i in range(len(char)):
      if char[i] not in new_dic:
        blank.append(combine[i])
        new_dic[char[i]] = blank.copy() 
        del blank[:] #make blank empty
       
      else:
        new_dic[char[i]].append(combine[i])

    #print the output dictionary if you find 
    #atleast one character that is repeated more than n times   
    if(len(new_dic) != 0):
      #converting collection of lists into collection of tuples
      for i in new_dic.keys():
        for x in new_dic[i]:
          new_dic[i] = [tuple(x) for x in new_dic[i]]
      #print(new_dic)
      #for e.g. a = 'aaaatrrraaa' the new_dic will be b = {
      #                                                     'a': [(0, 3), (8, 10)],

      #                                                     'r': [(5, 7)],
      #                                                    }

      #printing every character and it's index position on the new line
      print("\n{" + "\n".join("\n{!r}: {!r},".format(k, v) for k, v in new_dic.items()) + "\n}")
        
    #for key,value in zip(char, combine):
    #  print(key,":",value)

  #if nothing was entered for input string
  else:
    print("\nNothing was entered for input string!")

if(user_choice == '2'):
  #call the function with the content of the file and the repeat threshold value
  char_occ(content, repeat_threshold) 
  userfile.close()
else:
  #call the function with the input string and the repeat threshold value
  char_occ(input_string,repeat_threshold)   
