from fastapi import FastAPI
from classifier_manager import ClassifierManager

app = FastAPI()
manager = ClassifierManager()

@app.get('/data')
def get_all_data():
    try:
        return manager.manage_all_files()
    except Exception as ex:
        print(ex)
        raise Exception(ex)
