from services.utils.elastic.search_query import Queries

class RiskCalculation:
    def __init__(self):
        self.search_query = Queries()

    def bds_percent(self,doc_id,field,words):
        tv = self.search_query.count_words(doc_id, field)
        print("tv", tv)
        terms = tv['term_vectors'][field]['terms']
        print(terms)
        total_terms = sum(term_info['term_freq'] for term_info in terms.values())
        print(total_terms)
        percentages = {}
        for word in words:
            word = word.lower()
            word_count = terms.get(word, {}).get('term_freq', 0)
            print(word_count)
            if percentages:
                percentages['words_persent'] += (word_count / total_terms * 100) if total_terms > 0 else 0
            else:
                percentages['words_persent'] = (word_count / total_terms * 100) if total_terms > 0 else 0
            print(percentages['words_persent'], "%")
        return percentages