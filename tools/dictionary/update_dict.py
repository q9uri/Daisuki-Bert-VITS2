#Copyright 2025 q9uri
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#code from https://github.com/q9uri/merge-jtalkud

from pathlib import Path
from tools.dictionary.download import csv_list

def update():
    out = []

    text = Path("./weight/dictionary/default_bak.csv").read_text(encoding="utf-8")
    split_text = text.split("\n")
    out += split_text

    for i in csv_list:
        file_path = i[1]
        text = file_path.read_text(encoding="utf-8")
        split_text = text.split("\n")
        out += split_text

    while "" in out:
        out.remove("")
    
    new_out = []
    for line in out:
        split_line = line.split(",")
        
        if line == "土、日,1345,1345,8000,名詞,一般,*,*,*,*,土、日,ド、ニチ,ド、ニチ,*/*,*":
            new_out.append("土、日,1345,1345,8000,名詞,一般,*,*,*,*,土、日,ドニチ,ドニチ,*/*,*")
        
        else:
            if len(split_line) == 15:
                new_out.append(line)
            else:
                continue

    out_text = "\n".join(new_out)
    Path("./dict_data/default.csv").write_text(out_text, encoding = "utf-8")

if __name__ == "__main__":
    update()