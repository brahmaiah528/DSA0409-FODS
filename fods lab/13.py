from collections import Counter
import re

with open(r"D:\fods lab\sample_text.txt", "r") as file:
    text = file.read().lower()

words = re.findall(r"\b\w+\b", text)

frequency = Counter(words)

for word, count in frequency.most_common():
    print(word, ":", count)
