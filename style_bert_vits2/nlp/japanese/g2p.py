from kabosu_plus.sbv2.nlp.japanese import g2p as g2p_ja
from kabosu_plus.types import NjdObject
def g2p(
    norm_text: str,
    use_jp_extra: bool = True,
    raise_yomi_error: bool = False,
    keihan:bool = False,
    babytalk:bool = False,
    dakuten:bool = False,
) -> tuple[list[str], list[int], list[int], list[str], list[str], list[str]]:
    
    out = g2p_ja.g2p(norm_text=norm_text,
                     use_jp_extra=use_jp_extra,
                     raise_yomi_error=raise_yomi_error,
                     keihan=keihan,
                     babytalk=babytalk,
                     dakuten=dakuten,
                     )
    return out

def adjust_word2ph(
    word2ph: list[int],
    generated_phone: list[str],
    given_phone: list[str],
) -> list[int]:
    out = g2p_ja.adjust_word2ph(
        word2ph=word2ph,
        generated_phone=generated_phone,
        given_phone=given_phone
    )
    return out

def text_to_sep_kata(
    norm_text: str,
    njd_features: list[NjdObject] | None = None,
    raise_yomi_error: bool = False,
    keihan:bool = False,
    babytalk:bool = False,
    dakuten:bool = False,
) -> tuple[list[str], list[str], list[str]]:
    
    out = g2p_ja.text_to_sep_kata(norm_text=norm_text,
                                        njd_features=njd_features,
                                        raise_yomi_error=raise_yomi_error,
                                        keihan=keihan,
                                        babytalk=babytalk,
                                        dakuten=dakuten
    )
    return out