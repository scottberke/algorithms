# Brutish approach with built in sort on strings
def group_anagram(strings):
    # Create a dict to hold our anagrams
    strings_reference = {}
    # Iterate through each word of our strings
    for word in strings:
        # Key is lowercase alpha sorted word with no spaces
        key = ''.join(sorted(word.replace(" ", "").lower()))
        try:
            # Try to append our word
            strings_reference[key].append(word)
        except:
            # Rescue if key doesnt exist and add it
            strings_reference[key] = [word]

    # Return grouped flattened word values
    return [ word for words in strings_reference.values() for word in words ]


# Simple approach with sort key
def simple_group_anagram(strings):
    # Sort our strings array using custom key to sort on
    strings.sort(key=lambda x: lower_and_sort(x))
    return strings

def lower_and_sort(string):
    # Lowercase our string, sort the chars and return
    string = string.replace(" ", "").lower()
    return ''.join(sorted(list(string)))
