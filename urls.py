from Handlers.BaseHandlers import *
import os

urls = [
    (r"/(.*)", BaseStaticFileHandler,
     dict(path=os.path.join(os.path.dirname(__file__), "Templates")))
]
