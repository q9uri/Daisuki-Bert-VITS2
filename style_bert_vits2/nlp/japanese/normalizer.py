import sys

from kabosu_plus.sbv2 import normalizer  

# tests\test_normalizer move to https://github.com/q9uri/kabosu-plus/blob/main/tests/test_normalizer.py
# other normlizer code move to https://github.com/q9uri/kabosu-plus/tree/main/src/kabosu_plus/sbv2

def normalize_text(text: str) -> str:
    """
    日本語のテキストを正規化する。
    結果は、ちょうど次の文字のみからなる：
    - ひらがな
    - カタカナ（全角長音記号「ー」が入る！）
    - 漢字
    - 半角数字
    - 半角アルファベット（大文字と小文字）
    - ギリシャ文字
    - `.` （句点`。`や`…`の一部や改行等）
    - `,` （読点`、`や`:`等）
    - `?` （疑問符`？`）
    - `!` （感嘆符`！`）
    - `'` （`「`や`」`等）
    - `-` （`―`（ダッシュ、長音記号ではない）や`-`等）
    - `/` （スラッシュは pyopenjtalk での形態素解析処理で重要なので、例外的に正規化後も残し、g2p 処理内で "." に変換される）
    - `—` （pyopenjtalk のバグ回避のために例外的に正規化後も残し、g2p 処理内で "-" に変換される）

    注意点:
    - 三点リーダー`…`は`...`に変換される（`なるほど…。` → `なるほど....`）
    - 読点や疑問符等の位置・個数等は保持される（`??あ、、！！！` → `??あ,,!!!`）

    Args:
        text (str): 正規化するテキスト

    Returns:
        str: 正規化されたテキスト
    """

    text = normalizer.normalize_text(text)
    return text


def replace_punctuation(text: str) -> str:
    """
    句読点等を「.」「,」「!」「?」「'」「-」に正規化し、OpenJTalk で読みが取得できるもののみ残す：
    漢字・平仮名・カタカナ、数字、アルファベット、ギリシャ文字

    Args:
        text (str): 正規化するテキスト

    Returns:
        str: 正規化されたテキスト
    """

    return normalizer.replace_punctuation(text)
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m style_bert_vits2.nlp.japanese.normalizer <text>")
        sys.exit(1)
    print(normalize_text(sys.argv[1]))
