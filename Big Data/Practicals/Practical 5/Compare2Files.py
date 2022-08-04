def open_file(file_path, open_mode="r"):
    
    try:
        file_handler = open(file_path, mode=open_mode)

    except FileNotFoundError:
        print(f"Sorry the file {file_path} doesn't exist")
        exit()

    except ValueError:
        print(f"Sorry the file {file_path} can't be opened with mode {open_mode}")
        exit()

    return file_handler            


def get_file_words(file_path):
    file_words = set()
    read_file = open_file(file_path)
    for word in read_file.read().split():
        file_words.add(word.lower())
    return file_words

def merge(*filenames):
    list_of_file_words = []
    for filename in filenames:
        file_words = get_file_words(filename)
        list_of_file_words.append(file_words)
    common_words = set.intersection(*list_of_file_words)
    for word in common_words:
        print(word)
        # word = word + ", "



def main():

    file1 = "sample1.txt"

    file2 = "sample2.txt"

    merge(file1, file2)


if __name__ == "__main__":
    main()