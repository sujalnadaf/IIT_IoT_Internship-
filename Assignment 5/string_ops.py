def reverse_string(s):
 return s[::-1]
def count_vowels(s):
 vowels = 'aeiouAEIOU'
 return sum(1 for ch in s if ch in vowels)
