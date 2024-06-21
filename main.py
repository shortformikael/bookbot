def main():
	path = input("Enter path to book: \n")
	if(path == "1"):
		path = "books/frankenstein.txt"
	print(f"--- Begin report of {path} ---")

	with open(path) as f:
		file_contents = f.read()
		# print(file_contents)
		words = file_contents.split()

		# print(f"Words: {len(words)}")
		# print(str(count_characters(file_contents)))
		dictionary = count_characters(file_contents)
		print(f"{len(words)} words found in the document")
		for char in dictionary:
			print(f"The '{char}' character was found {dictionary[char]} times")
	print("--- End report ---")

def count_characters(string):
	dictionary = {}
	s = string.lower()
	for char in s:
		dictionary[char] = dictionary.get(f'{char}', 0) + 1
	return dictionary

main()