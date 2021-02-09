import os, string


def remove_symbols(sentence):
    """
    Remove numbers and symbols from ASCII
    """
    del_estr = string.punctuation.replace('\'', '') + string.digits  # ASCII 标点符号，数字
    replace = " " * len(del_estr)
    tran_tab = str.maketrans(del_estr, replace)
    sentence = sentence.translate(tran_tab)
    return sentence


def wordsFrequency(tmp_filename):
    file = open(tmp_filename)
    content = file.read()
    content = remove_symbols(content)
    words = content.split()
    wordsDict = {}
    for word in words:
        if word in wordsDict.keys():
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1
    maxValue = max(wordsDict.values())
    items = wordsDict.items()
    importantWordsSet = set()
    for key, value in items:
        if value == maxValue:
            importantWordsSet.add(key)
    return importantWordsSet


if __name__ == '__main__':
    path = 'txtFiles'
    files = os.walk(path)
    for dirpath, dirnames, filenames in files:
        for filename in filenames:
            if not filename.lower().endswith('.txt'):
                continue
            print('The most important word of {}: {}'.
                  format(filename, wordsFrequency(dirpath + os.path.sep + filename)))
