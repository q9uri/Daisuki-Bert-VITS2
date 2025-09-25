from kabosu_plus.sbv2.nlp.chinese import normalizer  

def normalize_text(text: str) -> str:
    text = normalizer.normalize_text(text)
    return text
