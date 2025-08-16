from stats import count_words, count_characters, sort_on
import sys

def get_book_text(file):
	with open(file) as f:
		# f is a file object
		file_contents = f.read()
		return file_contents





def main():

	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
        # Your main program logic goes here
	result = get_book_text(sys.argv[1])
	count = count_words(result)

	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {count} total words")
	print("--------- Character Count -------")
	chars = count_characters(result)
	list_of_stats = []
	for key, value in chars.items():
		single_dict = {"char":	key, "num": value}
		list_of_stats.append(single_dict)
	list_of_stats.sort(reverse=True, key=sort_on)
	for item in list_of_stats:
		if item['char'].isalpha():
			print(f"{item['char']}: {item['num']}")
	print("============= END ===============")


if __name__ == "__main__":
	main()
