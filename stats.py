def count_words(content):

	book_list = content.split()
	count = 0

	for i in range(0, len(book_list)):
		count += 1

	return count


def count_characters(content):
    dict_chars = {}
    content_low = content.lower()

    for char in content_low:
        if char not in dict_chars:
            dict_chars[char] = 0
        dict_chars[char] += 1

    return dict_chars

def sort_on(item):
    return item["num"]

def sorted_characters(dict_chars):
    my_list =[]
    for char, key in dict_chars.items():
        if char.isalpha():
            my_list.append({"char": char, "num": key})
    my_list.sort(key=sort_on,  reverse=True)
    return my_list


