import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    user = Github(email, password).get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()
