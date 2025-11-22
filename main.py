def get_book_text(file_path):

	with open(file_path) as f:
		file_innards = f.read()

	return file_innards

from stats import count_words, count_characters, sorted_characters


def main():
    text = get_book_text("books/frankenstein.txt")

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

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
