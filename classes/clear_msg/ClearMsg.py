import re


class ClearMsg:
    @staticmethod
    def clear_spaces(curr_message):
        curr_message = curr_message.replace(" ", "")
        curr_message = curr_message.replace("\n ", "")
        return curr_message

    @staticmethod
    def make_search_data(cleared_msg, dictionary):
        if cleared_msg != "" and cleared_msg is not None:
            search_data = cleared_msg.split("<br>")[0]
            search_data = ClearMsg.clear_spaces(search_data)

            for regex in dictionary.regex:
                search_data = re.sub(fr"{regex}", "", search_data)

            for split in dictionary.split:
                search_data = search_data.split(f"{split}")[0]

            return search_data
        else:
            return ""
