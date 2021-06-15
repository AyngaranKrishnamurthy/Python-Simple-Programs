def max_occurence(str):
    freq = [0 for i in range (100)]
    max = -1
    len__ = len(str)
    for i in range (0,len__,1):             #Checks if string is a single character.
        freq[ord(str[i]) - ord('a')] +=1
    for i in range (26):                    #Checks max occurence of a string element.
        if (max<freq[i]):
            max = freq[i]
            result = chr(ord('a')+i) , max
    if (max == 1):                          #Checks if the max occurence is only 1.
      result = str[len__-1], 1
            
    return result

if __name__ =='__main__':
  string = input("Enter a string: ") 
  str = sorted(string)                  #Sorts the string obtained
  print('Ans: ', max_occurence(str))
  