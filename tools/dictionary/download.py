#Copyright 2025 q9uri
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#code from https://github.com/q9uri/merge-jtalkud

import requests
from pathlib import Path

_csv_dir = Path("./weight/dictionary")
csv_list = (
    ('https://github.com/q9uri/jtalkdic-ud-edict2/raw/refs/heads/main/build/jtalkdic-ud-edict2-noacc.csv', 
    _csv_dir / "jtalkdic-ud-edict2-noacc.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-sudachidict/raw/refs/heads/main/build/jtalkdic-ud-sudachidict-noacc-00.csv',
        _csv_dir / "jtalkdic-ud-sudachidict-noacc-00.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-sudachidict/raw/refs/heads/main/build/jtalkdic-ud-sudachidict-noacc-01.csv',
    _csv_dir / "jtalkdic-ud-sudachidict-noacc-01.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-sudachidict/raw/refs/heads/main/build/jtalkdic-ud-sudachidict-noacc-02.csv',
        _csv_dir / "jtalkdic-ud-sudachidict-noacc-02.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-sudachidict/raw/refs/heads/main/build/jtalkdic-ud-sudachidict-noacc-03.csv',
        _csv_dir / "jtalkdic-ud-sudachidict-noacc-03.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-jawiki/raw/refs/heads/main/build/jtalkdic-ud-jawiki-noacc-00.csv',
        _csv_dir / "jtalkdic-ud-jawiki-noacc-00.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-jawiki/raw/refs/heads/main/build/jtalkdic-ud-jawiki-noacc-01.csv',
    _csv_dir / "jtalkdic-ud-jawiki-noacc-01.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-jawiki/raw/refs/heads/main/build/jtalkdic-ud-jawiki-noacc-02.csv',
        _csv_dir / "jtalkdic-ud-jawiki-noacc-02.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-jawiki/raw/refs/heads/main/build/jtalkdic-ud-jawiki-noacc-03.csv',
        _csv_dir / "jtalkdic-ud-jawiki-noacc-03.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-alt-cannadic/raw/refs/heads/main/build/jtalkdic-ud-alt-cannadic-noacc.csv',
        _csv_dir / "jtalkdic-ud-alt-cannadic-noacc.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-skk-jisyo/raw/refs/heads/main/build/jtalkdic-ud-skk-jisyo-noacc.csv',
        _csv_dir / "jtalkdic-ud-skk-jisyo-noacc.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-personal-names/raw/refs/heads/main/build/jtalkdic-ud-personal-names-noacc.csv',
        _csv_dir / "jtalkdic-ud-personal-names-noacc.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-place-names/raw/refs/heads/main/build/jtalkdic-ud-place-names-noacc.csv',
        _csv_dir / "jtalkdic-ud-place-names-noacc.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-th-dic/raw/refs/heads/main/build/jtalkdic-ud-thdic-character-noacc.csv',
        _csv_dir / "jtalkdic-thdic-character-noacc.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-th-dic/raw/refs/heads/main/build/jtalkdic-ud-thdic-music-noacc.csv',
        _csv_dir / "jtalkdic-thdic-music-noacc.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-th-dic/raw/refs/heads/main/build/jtalkdic-ud-thdic-sakuhin-noacc.csv',
        _csv_dir / "jtalkdic-thdic-sakuhin-noacc.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-th-dic/raw/refs/heads/main/build/jtalkdic-ud-thdic-spelcard-noacc.csv',
        _csv_dir / "jtalkdic-thdic-spelcard-noacc.csv"),

    ('https://github.com/q9uri/jtalkdic-ud-th-dic/raw/refs/heads/main/build/jtalkdic-ud-thdic-word-noacc.csv',
        _csv_dir / "jtalkdic-thdic-word-noacc.csv"),
)
    
licence_list = (
    ( 'https://github.com/q9uri/jtalkdic-ud-edict2/raw/refs/heads/main/LICENSE',
        _csv_dir / "license_jtalkud-edict2.txt"),

    ('https://github.com/q9uri/jtalkdic-ud-sudachidict/raw/refs/heads/main/LICENSE',
        _csv_dir / "license_jtalkud-sudachidict.txt"),

    ('https://github.com/q9uri/jtalkdic-ud-jawiki/raw/refs/heads/main/LICENSE',
        _csv_dir / "license_jtalkud-jawiki.txt"),

    ('https://github.com/q9uri/jtalkdic-ud-alt-cannadic/raw/refs/heads/main/LICENSE',
        _csv_dir / "license_jtalkud-alt-cannadic.txt"),

    ('https://github.com/q9uri/jtalkdic-ud-skk-jisyo/raw/refs/heads/main/LICENSE',
        _csv_dir / "license_jtalkud-skk-jisyo.txt"),

    ('https://github.com/q9uri/jtalkdic-ud-personal-names/raw/refs/heads/main/LICENSE',
        _csv_dir / "license_jtalkud-personal-names.txt"),

    ('https://github.com/q9uri/jtalkdic-ud-place-names/raw/refs/heads/main/LICENSE',
        _csv_dir / "license_jtalkud-place-names.txt"),

    ('https://github.com/q9uri/jtalkdic-ud-th-dic/raw/refs/heads/main/build/LICENCE',
        _csv_dir / "license_jtalkud-thdic.txt"),

)

def download_dictionary():
    
    download_list = licence_list + csv_list

    for i in download_list:
        url = i[0]
        file_path = i[1]
        if not file_path.is_file():
            response = requests.get(url)
            with open(str(file_path), 'wb') as saveFile:
                saveFile.write(response.content)

if __name__ == "__main__":
    download_dictionary()