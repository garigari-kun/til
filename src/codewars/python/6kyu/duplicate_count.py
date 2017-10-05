"""

Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters
and numeric digits that occur more than once in the input string.
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice



"""

from collections import Counter

def duplicate_count(text):
     word_count = Counter(text.lower())
     dup_count = 0
     for ch, count in word_count.items():
         if count > 1:
             dup_count += 1
     return dup_count


if __name__ == '__main__':
    print(duplicate_count("abcde"))
    print(duplicate_count("aabbcde"))
    print(duplicate_count("aabBcde"))
