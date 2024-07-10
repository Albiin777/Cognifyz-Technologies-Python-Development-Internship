'''LEVEL 2 TASK 5
FILE MANIPULATION'''

def occurrences(filename):
    with open(filename, 'r') as f:
        print(f"Reading from the file '{filename}'...\n")
        text=f.read()
        words=text.split()
        word_counts={}
        maxlen = max(len(word.strip('.,!?')) for word in words)
        for word in words:
            cleanword=word.strip('.,!?').lower()
            if cleanword:
                if cleanword in word_counts:
                    word_counts[cleanword]+=1
                else:
                    word_counts[cleanword]=1
        sorted_word_counts=sorted(word_counts.items())
        for word, count in sorted_word_counts:
            print(f"Word: {word.ljust(maxlen)}\tOccurrence count: {count}")

filename="test.txt"
occurrences(filename)
