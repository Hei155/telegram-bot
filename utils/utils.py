from rutermextract import TermExtractor
term_extractor = TermExtractor()


#   Извлечение ключевых слов


def get_term(phrase):
    key_array = []
    for term in term_extractor(phrase):
        key_array.append(term.normalized)
    return ' '.join(key_array)
