def reverser(word):
    reversed_word = ""
    for index in range(len(word)-1, -1, -1):
        reversed_word += word[index]
    return reversed_word

def capitalize(string):
    list = string.split()
    new_string = ""
    for word in list:
        new_string = new_string + word.capitalize() + " "
    return new_string

def compress_string(string):
   count = 1
   new_string = ""
   for char in range(1, len(string)):
      if string[char - 1] == string[char]:
         count += 1
      else:
         if count > 1:
            new_string += str(count)
         new_string = new_string + string[char - 1]
         count = 1

   if count > 1:
      new_string += str(count)
   new_string = new_string + string[-1]

   return new_string

def palindrome(string):
    lower_case_string = string.lower()
    pdrome = reverser(lower_case_string)
    if lower_case_string == pdrome:
        print(f"{string} is a palidrome")
    else:
        print(f"{string} is not a palidrome")
