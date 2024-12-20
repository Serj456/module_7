
def custom_write(file_name, strings):
    string_position = {}
    file = open(file_name, 'r+', encoding="utf-8")
    for i in strings:
        tell = file.tell()
        file.write(i + "\n" )
        file.seek(0)
        str_count = 0
        for str in enumerate(file.readlines()):
            str_count += 1
        string_position.update({(str_count, tell): i})
    return string_position
    file.close()





info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
