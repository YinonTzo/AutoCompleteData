import os

if __name__ == '__main__':
    wordDict = {}
    for root, dirs, files in os.walk('resources'):
        for file in files:
            print(os.path.abspath(os.path.join(root, file)))

    """   f = open(file, "r")
            for line in f:
                for word in line:
                    if word not in wordDict.keys():
                        wordDict[word] = []
                    wordDict[word].append(line)
    print(wordDict)
    """


