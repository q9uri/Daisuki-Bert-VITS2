from kabosu_plus.sbv2.nlp.english import g2p as g2p_en 

def g2p(text: str) -> tuple[list[str], list[int], list[int]]:
    out = g2p_en.g2p(text=text)
    return out