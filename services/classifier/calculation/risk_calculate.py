from services.utils.elastic.queries import Queries

class RiskCalculation:

    """ Calculate all hostile terms divided by all words amount
    if the term is more then one word it multiplied by amount of
    words in term."""
    @staticmethod
    def bds_percent(text,terms):
        percent = 0
        text = text.lower()
        for term in terms:
            term = term.lower()
            if text:
                print(term)
                count_terms = text.count(term) * len(term.split(" "))
                text_length = len(text)
                print(count_terms)
                print(text_length)
                percent += (count_terms / text_length) * 100
        return percent

    # Classify percent if above one is hostile.
    @staticmethod
    def is_bds(percent):
        if percent < 1.0:
            return 0
        else:
            return 1

    # Classify percent by three levels.
    @staticmethod
    def bds_threat_level(percent):
        if percent <= 1.0:
            return "none"
        elif percent <= 5.0:
            return "medium"
        else:
            return "high"