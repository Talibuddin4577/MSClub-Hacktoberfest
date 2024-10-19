def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = sum(1 for char in s if char in consonants)
    return count

def count_specific_vowels(s, specific_vowels):
    count = sum(1 for char in s if char in specific_vowels)
    return count

if __name__ == "__main__":
    string = input("Enter a string: ")
    
    total_vowels = count_vowels(string)
    total_consonants = count_consonants(string)
    
    print(f"Number of vowels in '{string}': {total_vowels}")
    print(f"Number of consonants in '{string}': {total_consonants}")
    
    specific = input("Enter specific vowels to count (e.g., 'ae' for 'a' and 'e'): ")
    specific_count = count_specific_vowels(string, specific)
    print(f"Number of specified vowels '{specific}' in '{string}': {specific_count}")

    print(f"Summary: {total_vowels} vowels and {total_consonants} consonants in the input.")
