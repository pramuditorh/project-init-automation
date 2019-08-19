import os 
import sys
from github import Github
from getpass import getpass

path = "/home/rh/projects/"

def nggawe():
    folderName = sys.argv[1]
    username = sys.argv[2]

    password = getpass("Github Password: ")

    g = Github(username, password)

    try:
        os.makedirs(path + folderName)
        print(f'Direktori {folderName} sukses dibuat.')
    except FileExistsError:
        print(f'Direktori {folderName} sudah ada.')

    user = g.get_user()
    user.create_repo(folderName)
    print("Repositoy di Github sukses dibuat.")

if __name__ == '__main__':
    nggawe()