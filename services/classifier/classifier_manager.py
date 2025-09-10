import os
from services.utils.elastic.dal import DAL
from services.utils.elastic.queries import Queries
from services.classifier.calculation.risk_calculate import RiskCalculation
from services.utils.files_access.text_access import Text
from services.utils.encryption.encryption import Encryption
from services.utils.elastic.logger import Logger

class ClassifierManager:
    def __init__(self):
        self.logger = Logger.get_logger()
        self.es_dal = DAL()
        self.queries = Queries()
        self.risk_calc = RiskCalculation()
        self.FILE_PATH = os.getenv("FILE_PATH",r"C:\Users\HOME\PycharmProjects\The_Muezzin\data\hostile.txt")
        self.text = Text(self.FILE_PATH)
        self.encription = Encryption()

    def manage_all_files(self):
        self.logger.info("Classifier started.")
        doc_list = self.queries.get_all_data()
        encrypt_words = self.text.organized_txt()
        decrypt_hostile = str(self.encription.decrypt(encrypt_words["hostile"]))[2:].split(',')
        decrypt_less_hostile = str(self.encription.decrypt(encrypt_words["less hostile"]))[2:].split(',')
        for doc in doc_list:
            hostile_percentage = self.risk_calc.bds_percent(doc['_source']["transcribed"], decrypt_hostile)
            less_hostile_percentage = self.risk_calc.bds_percent(doc['_source']["transcribed"], decrypt_less_hostile)/2
            percent = hostile_percentage + less_hostile_percentage
            self.es_dal.update_doc(doc['_id'],"bds_percent",percent)
            is_bds = self.risk_calc.is_bds(percent)
            self.es_dal.update_doc(doc['_id'], "is_bds", is_bds)
            bds_treat_level = self.risk_calc.bds_threat_level(percent)
            self.es_dal.update_doc(doc['_id'], "bds_treat_level", bds_treat_level)
            print(self.queries.get_all_data())