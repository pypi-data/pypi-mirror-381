import os

def check_permissions(directory):
    print(f"Permissions des fichiers dans {directory}")
    for root, _, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            perms = oct(os.stat(path).st_mode)[-3:]
            print(f"{path} : {perms}")

def analyze_permission_issues(directory):
    print("Analyse des problèmes de permissions :")
    for root, _, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            if not os.access(path, os.R_OK):
                print(f"Lecture impossible : {path}")
            if not os.access(path, os.W_OK):
                print(f"Ecriture impossible : {path}")
