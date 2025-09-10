import os

from services.utils.elastic.search_query import Queries
from risk_calculate import RiskCalculation
from services.utils.files_access.text_access import Text
from services.utils.encryption.encryption import Encryption

class ClassifierManager:
    def __init__(self):
        self.search_query = Queries()
        self.risk_calc = RiskCalculation()
        self.FILE_PATH = os.getenv("FILE_PATH",r"C:\Users\HOME\PycharmProjects\The_Muezzin\data\hostile.txt")
        self.text = Text(self.FILE_PATH)
        self.encription = Encryption()

    def manage_all_files(self):
        list_id = self.search_query.get_all_id()
        for doc_id in list_id:
            encrypt_words = self.text.organized_txt()
            decrypt_hostile = str(self.encription.decrypt(encrypt_words["hostile"]))[2:].split(',')
            hostile_percentage = self.risk_calc.bds_percent(doc_id,"transcribed", decrypt_hostile)
            print(hostile_percentage)
            decrypt_less_hostile = str(self.encription.decrypt(encrypt_words["less hostile"]))[2:].split(',')
            less_hostile_percentage = self.risk_calc.bds_percent(doc_id,"transcribed", decrypt_less_hostile)
            print(less_hostile_percentage['words_persent'] / 2)
            final_result = less_hostile_percentage['words_persent'] / 2 + hostile_percentage['words_persent']
