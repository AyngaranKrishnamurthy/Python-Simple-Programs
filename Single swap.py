def swapstr(str1, str2):
  len1 = len(str1)
  len2 = len(str2)
  if (len1 != len2):          #Checks for if both the strings are of same length
    return False
  prev = -1
  curr = -1
  count = 0
  i = 0
  while i<len1:                 #Compares string for resemblence of elements
    if (str1[i] != str2[i]):    #Counts number of swaps needed
      count = count + 1
      if (count > 2):
        return False
      prev = curr
      curr = i
    i = i+1
  return(count==2 and str1[prev] == str2[curr] and str1[curr] == str2[prev])

str1 = input("Enter string 1: ") 
str2 = input("Enter string 2: ") 
if (swapstr(str1,str2)):
  print ('True')
else:
  print ('False')