from src.word_order.util import count_words

def main():
    n = int(input("Enter number of words: "))  # User Input
    words = []


    for _ in range(n):
        word = input().strip()
        words.append(word)


    words_list, counts_list = count_words(words)

    print(len(words_list))
    print(' '.join(map(str, counts_list)))

if __name__ == "__main__":
    main()
