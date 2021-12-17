import os
import logging

logger = logging.getLogger("PYFolders")
logger.setLevel(logging.INFO)
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')


class Foldroot:
    def __init__(self, name, description, author, path, mainfunc):
        self.name = name
        self.description = description
        self.author = author
        self.path = path
        self.mainfunc = mainfunc

    @staticmethod
    def get_root(path):
        description = ""
        author = ""
        mainfunc = "main"
        rootdir = os.listdir(os.path.join(path, "PF:META"))
        name = os.path.split(path)[1]
        for subdir in rootdir:
            if subdir.startswith("PF:A:"):
                author = subdir.split("PF:A:")[1]
            elif subdir.startswith("PF:D:"):
                description = subdir.split("PF:D:")[1]
            elif subdir.startswith("PF:M:"):
                mainfunc = subdir.split("PF:M:")[1]

        logger.info(f"PYFolders project name is: {':'.join(name.split(':')[1:])}")
        logger.info(f"PYFolders project author name is: {author}")
        logger.info(f"PYFolders project description is: {description}")
        logger.info(f"PYFolders main function is: {mainfunc}")

        return Foldroot(name, description, author, path, mainfunc)

