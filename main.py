def get_book_text(file_path):

	with open(file_path) as f:
		file_innards = f.read()

	return file_innards

import sys

from stats import count_words, count_characters, sorted_characters


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    count = count_words(text)
    print("----------- Word Count ----------")
    print("Found " + str(count) + " total words")

    dict_chars = count_characters(text)
    sorted_list = sorted_characters(dict_chars)

    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

    


main()
