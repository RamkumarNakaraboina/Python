# Reverse a String
# name="hello"
# rev=""
# for ch in name:
#     rev=ch+rev
# print(rev)

# Check Palindrome
# name=input("Enter: ")
# rev=""
# for ch in name:
#     rev=ch+rev
# if name==rev:
#     print(True)
# else:
#     print(False)

# Count Vowels and Consonants
# Input="Python "
# vowels="aeiou"
# Vowels=0
# Consonants=0
# for ch in Input.lower():
#     if ch in vowels:
#         Vowels+=1
#     else:
#         Consonants+=1         
# print(f"Vowels = {Vowels}, Consonants = {Consonants}")

# Find the First Non-Repeated Character
# Input="aabbcdeff"
# for ch in Input:
#     if Input.count(ch)==1:
#         print(f"{ch}")
#         break
# else:
#     print("No non-repeating characters")

# Remove All Duplicates
# Input="programming"
# result=""
# for ch in Input:
#     if ch not in result:
#         result+=ch
# print(result)

# Count Word Frequency
# Input="hello world hello"
# dis={}
# for ch in Input.split():
#     if ch in dis:
#         dis[ch]+=1
#     else:
#         dis[ch]=1
# print(dis)

#Anagram Checker
# s1="listen"
# s2="silent"
# if len(s1)!=len(s2):
#     print("Not Anagrams")
# else:
#     if sorted(s1)==sorted(s2):
#         print("Anagrams!")
#     else:
#         print("Not Anagrams")

# Longest Word in a Sentence
# sentence = "Python makes coding enjoyable"
# current = ""
# longest = ""

# for ch in sentence:
#     if ch != " ":
#         current += ch
#     else:
#         if len(current) > len(longest):
#             longest = current
#         current = ""

# # check the last word
# if len(current) > len(longest):
#     longest = current

# print(longest)

# Remove Duplicate Words
# Input="This is is  a test test"
# Output=""
# for i in Input.split():
#     if i not in Output:
#         Output+=i+' '
# print(Output)

# Capitalize First Letter of Each Word
# Input="python is fun"
# Output=""
# for i in Input.split():
#     Output+=i.capitalize()+' '
# print(Output)

# check Pangram
# Input="The quick brown fox jumps over the lazy dog"
# alphabets="abcdefghijklmnopqrstuvwxyz"
# for ch in alphabets:
#     if ch not in Input.lower():
#         print(False)
#         break
# else:
#     print(True)

# Covert to Title Case Without .title()
# Input="welcome to python"
# Output=""
# for i in Input.split():
#     Output+=i[0].upper()+i[1:].lower()+' '
# print(Output)

# Remove Special characters
# Input="Hello@2025!!"
# Output=""
# special_characters="!@#$%^&*()_+"
# for ch in Input:
#     if ch not in special_characters:
#         Output+=ch
# print(Output)

# Find Common Characters Between Two Strings
# s1="python"
# s2="typhoon"
# Output=""
# for ch in s1:
#     if ch in s2 and ch not in Output:
#         Output+=ch
# print(Output)

# Count Digits, Alphabets, and Symbols
# Input="Python3.9!"
# alphabets='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digits='123456789'
# symbols="!@#$%^&*()_+."
# Alphabets=0
# Digits=0
# Symbols=0
# for ch in Input:
#     if ch in alphabets:
#         Alphabets+=1
#     elif ch in digits:
#         Digits+=1
#     elif ch in symbols:
#         Symbols+=1
# Output=f"Alphabets={Alphabets}, Digits={Digits}, Symbols={Symbols}"
# print(Output)

# Replace All Spaces with Hyphens
Input="Python is great"
Output=""
for ch in Input:
    if ch == " ":
        Output+="-"
    else:
        Output+=ch
print(Output)
# Input="Python is great"
# Output=Input.replace(" ","-")
# print(Output)