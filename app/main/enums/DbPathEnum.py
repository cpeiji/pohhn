from enum import Enum
import os

class DbPathEnum(Enum):
    curPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    rootPath = os.path.split(curPath)[0]
    db_path = rootPath+"/rss.sqlite"