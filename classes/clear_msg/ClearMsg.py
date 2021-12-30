import re


class ClearMsg:
    @staticmethod
    def clear_spaces(curr_message):
        curr_message = curr_message.replace(" ", "")
        curr_message = curr_message.replace("\n ", "")
        return curr_message

    @staticmethod
    def make_search_data(cleared_msg):
        if cleared_msg != "" and cleared_msg is not None:
            search_data = cleared_msg.split("<br>")[0]
            search_data = ClearMsg.clear_spaces(search_data)
            search_data = re.sub(r'[0-9]', '', search_data)
            search_data = search_data.split("MessageId =")[0]
            search_data = search_data.split("message id =")[0]
            search_data = search_data.split("Message processing error")[0]
            search_data = search_data.split("messageId=ID")[0]
            search_data = search_data.split("xsd-схеме (Обработка документа")[0]

            return search_data
        else:
            return ""
