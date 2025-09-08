from services.processor.pros_manager import ProcessorManager
from services.persister.per_manager import PersisterManager
if __name__=="__main__":
    m1 = ProcessorManager()
    m2 = PersisterManager()
    m2.manage_all_files()
    m1.manage_all_files()
