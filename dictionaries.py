from collections import Counter

input_filename = "input.txt"

with open(input_filename, "w") as file:
    file.write()

word_count = Counter()

with open(input_filename, "r") as file:
    for line in file:
         words = line.lower().replace(".", "").replace(",", "").split()
         word_count.update(words)

most_common_words = word_count.most_common(5)

print("Top 5 most common words:")
for word, count in most_common_words:
    print(f"{word}: {count}")