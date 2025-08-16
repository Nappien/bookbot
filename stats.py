def count_words(string):
	# Counting words
	word_count = len(string.split())
	return word_count

def count_characters(string):
    input_string = string.lower()
    char_counts = {}
    for char in input_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(items):
    return items["num"]
