'''
to check the number of vowels
'''
string_input=input("enter a string")
vowels_count=0
consonant_count=0
vowels="aeiouAEIOU"
for char in string_input:
    if char in vowels:
        vowels_count+=1
    else: consonant_count+=1
print(f"number of vowels in the string {vowels_count}")
print(f"number of consonant in the string {consonant_count}")


