# put your code here.
def word_count_dict(file_name):

    word_counts = {}
    file = open(file_name)
    
    for line in file:
        line = line.replace("\n", "")
        words = line.split(" ")
   
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        
    return word_counts

poem_dict = (word_count_dict("test.txt"))

for word, count in poem_dict.items():
    print(f"{word} {count}")

