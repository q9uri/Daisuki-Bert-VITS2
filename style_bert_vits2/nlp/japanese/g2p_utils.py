from kabosu_plus.sbv2.nlp.japanese import g2p_utils

def g2kata_tone(norm_text: str) -> list[tuple[str, int]]:
    """
    テキストからカタカナとアクセントのペアのリストを返す。
    推論時のみに使われる関数のため、常に `raise_yomi_error=False` を指定して g2p() を呼ぶ仕様になっている。

    Args:
        norm_text: 正規化されたテキスト。

    Returns:
        カタカナと音高のリスト。
    """
    out = g2p_utils.g2kata_tone(norm_text=norm_text)
    return out

def kata_tone2phone_tone(kata_tone: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """
    `phone_tone2kata_tone()` の逆の変換を行う。

    Args:
        kata_tone: カタカナと音高のリスト。

    Returns:
        音素と音高のリスト。
    """

    out = g2p_utils.kata_tone2phone_tone(kata_tone=kata_tone)
    return out

