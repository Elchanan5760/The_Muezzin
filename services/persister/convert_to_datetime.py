from datetime import datetime

class DateTime:
    @staticmethod
    def convertor(date_time_str):
        try:
            format_with_float = "%Y-%m-%d %H:%M:%S.%f"
            datetime_object = datetime.strptime(date_time_str, format_with_float)
            return datetime_object
        except ValueError:
            try:
                format = "%Y-%m-%d %H:%M:%S"
                datetime_object = datetime.strptime(date_time_str, format)
                return datetime_object
            except ValueError as e:
                print(f"Error parsing string: {e}")