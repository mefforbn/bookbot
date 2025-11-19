def get_book_text(file_path):

	with open(file_path) as f:
		file_innards = f.read()

	return file_innards

def count_words(content):

	book_list = content.split()
	count = 0

	for i in range(0, len(book_list)):
		count += 1

	return count


def main():
	count = count_words(get_book_text("books/frankenstein.txt"))
	print("Found " + str(count) + " total words")


main()
