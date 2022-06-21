# write a class that takes .env file and parses it into a dictionary

from dotenv import dotenv_values

DEFAULTS = {
    "ALLOW_NSFW": "False",
    "POST_ID": "",
    "THEME": "DARK",
    "TIMES_TO_RUN": "",
    "MAX_COMMENT_LENGTH": "500",
    "OPACITY": "1",
    "STORYMODE": "False",
}


class Config:
        self.raw = dotenv_values("../.env")
        self.load_attrs()

    def __getattr__(self, attr):  # code completion for attributes fix.
        return getattr(self, attr)

    def load_attrs(self):
        for key, value in self.raw.items():
            self.add_attr(key, value)

    def add_attr(self, key, value):
        if value is None or value == "":
            setattr(self, key, DEFAULTS[key])
        else:
            setattr(self, key, str(value))


config = Config()

print(config.SUBREDDIT)
