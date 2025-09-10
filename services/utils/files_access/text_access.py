from services.utils.elastic.logger import Logger

class Text:
    def __init__(self,file_path):
        self.logger = Logger.get_logger()
        self.file_path = file_path

    def read_txt(self):
        try:
            with open(self.file_path, "r") as t:
                all_lines = t.read()
                list_all_lines = all_lines.split("\n")
                self.logger.info("Text read successfully.")
                return list_all_lines
        except FileNotFoundError:
            self.logger.error(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")

    def organized_txt(self):
        dict_words = {}
        key = ""
        for line in self.read_txt():
            if line:
                if key:
                   dict_words[key] = line
                if not key in dict_words.values():
                    key = line
            else:
                key = ""
        return dict_words

o1 = Text(r"C:\Users\HOME\PycharmProjects\The_Muezzin\data\hostile.txt")
print(o1.read_txt())
print(o1.organized_txt())