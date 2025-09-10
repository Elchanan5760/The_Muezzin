from processing_metadata_manager import ProcessorManager
from services.utils.elastic.queries import Queries

manager = ProcessorManager()
if __name__=="__main__":
    manager.manage_all_files()