from kabosu_plus.sbv2.nlp.chinese import g2p as g2p_zh

def g2p(text: str) -> tuple[list[str], list[int], list[int]]:
    out = g2p_zh.g2p(text=text)
    return out