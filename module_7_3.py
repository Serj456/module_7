import string


class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = file.read().split()

                words = [x.lower() for x in words]
                words = [y.translate(str.maketrans('', '', string.punctuation)) for y in words]
                all_words[file_name] = words
        return all_words
    def find(self, word):
        find_words = {}
        for name, words in self.get_all_words().items():
            word = word.lower()
            if word in words:
                find_words[name] = words.index(word)+1
        return find_words
    def count(self, word):
        count_words = {}
        for name, words in self.get_all_words().items():
            word = word.lower()
            if word in words:
                count_words[name] = words.count(word)
        return count_words



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
