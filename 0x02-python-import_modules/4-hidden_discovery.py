#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for words in dir(hidden_4):
        if not (words.startswith('__')):
            print(words)
