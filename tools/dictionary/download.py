#Copyright 2025 q9uri
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#code from https://github.com/q9uri/merge-jtalkud

import requests

def download_edict2():
    url = 'https://github.com/q9uri/jtalkdic-ud-edict2/raw/refs/heads/main/build/jtalkdic-ud-edict2-noacc.csv'
    response = requests.get(url)
    with open("./weight/dictionary/jtalkdic-ud-edict2-noacc.csv", 'wb') as saveFile:
        saveFile.write(response.content)
    url = 'https://github.com/q9uri/jtalkdic-ud-edict2/raw/refs/heads/main/LICENSE'
    response = requests.get(url)
    with open("./weight/dictionary/license_jtalkud-edict2.txt", 'wb') as saveFile:
        saveFile.write(response.content)

def download_sudachidict():
    url = 'https://github.com/q9uri/jtalkdic-ud-sudachidict/raw/refs/heads/main/build/jtalkdic-ud-sudachidict-noacc-00.csv'
    response = requests.get(url)
    with open("./weight/dictionary/jtalkdic-ud-sudachidict-noacc-00.csv", 'wb') as saveFile:
        saveFile.write(response.content)

    url = 'https://github.com/q9uri/jtalkdic-ud-sudachidict/raw/refs/heads/main/build/jtalkdic-ud-sudachidict-noacc-01.csv'
    response = requests.get(url)
    with open("./weight/dictionary/jtalkdic-ud-sudachidict-noacc-01.csv", 'wb') as saveFile:
        saveFile.write(response.content)

    url = 'https://github.com/q9uri/jtalkdic-ud-sudachidict/raw/refs/heads/main/build/jtalkdic-ud-sudachidict-noacc-02.csv'
    response = requests.get(url)
    with open("./weight/dictionary/jtalkdic-ud-sudachidict-noacc-02.csv", 'wb') as saveFile:
        saveFile.write(response.content)

    url = 'https://github.com/q9uri/jtalkdic-ud-sudachidict/raw/refs/heads/main/build/jtalkdic-ud-sudachidict-noacc-03.csv'
    response = requests.get(url)
    with open("./weight/dictionary/jtalkdic-ud-sudachidict-noacc-03.csv", 'wb') as saveFile:
        saveFile.write(response.content)

    url = 'https://github.com/q9uri/jtalkdic-ud-sudachidict/raw/refs/heads/main/LICENSE'
    response = requests.get(url)
    with open("./weight/dictionary/license_jtalkud-sudachidict.txt", 'wb') as saveFile:
        saveFile.write(response.content)

def download_dictionary():
    download_edict2()
    download_sudachidict()

if __name__ == "__main__":
    download_dictionary()