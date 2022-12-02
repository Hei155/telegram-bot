from rutermextract import TermExtractor
term_extractor = TermExtractor()


def get_term(phrase):
    for term in term_extractor(phrase):
        return term.normalized
