import os
import sys
import datetime

project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)


TOKEN_TIME_LIMIT = datetime.timedelta(days=30)