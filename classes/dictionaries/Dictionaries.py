import copy


class Dictionaries:
    @staticmethod
    def remove_stack_trace(message):
        return message.split("<br>")[0]

    @staticmethod
    def clear_spaces(curr_message):
        curr_message = curr_message.replace(" ", "")
        curr_message = curr_message.replace("\n ", "")
        return curr_message

    @staticmethod
    def dictionary_check(message, dictionary):
        results = {}
        for block in dictionary.messages:
            message = message.replace("'", "\'")
            target_copy = copy.deepcopy(block["target"])
            target_copy = target_copy.split("[[target]]")
            for string in target_copy:
                if string not in message:
                    target_copy = False
                    break
            if target_copy is not False:
                results = copy.deepcopy(block)
                results["target"] = target_copy
                break

        return results

    @staticmethod
    def service_search(msg, dictionary):
        msg = Dictionaries.clear_spaces(msg)
        target = ""
        for service in dictionary:
            if service["msg"] in msg:
                target = f"{msg} ({service['service']})"
                break
            else:
                target = msg

        return target
