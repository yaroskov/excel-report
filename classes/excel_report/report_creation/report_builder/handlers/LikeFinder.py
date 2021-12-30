from classes.data.Data import Data


class LikeFinder(Data):
    def __init__(self, config):
        super(LikeFinder, self).__init__(config)
        self.likes = config.likes

    def run(self, prev_msg):
        if prev_msg is None:
            prev_msg = ""

        curr_like = None
        for like in self.likes:

            if like in prev_msg:
                curr_like = like
                break

        return curr_like
