import os

def change_permissions(directory, mode_str):
    print(f"Modification des permissions pour {directory} : {mode_str}")
    if mode_str.isdigit():
        mode = int(mode_str, 8)
        for root, _, files in os.walk(directory):
            for f in files:
                path = os.path.join(root, f)
                os.chmod(path, mode)
                print(f"{path} -> {mode_str}")
    else:
        print("⚠️ Mode symbolique non implémenté.")

def interactive_chmod(directory):
    print("Mode interactif chmod")
    for root, _, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            resp = input(f"Modifier permissions pour {path}? [y/N]: ")
            if resp.lower() == "y":
                mode = input("Nouveau mode (ex: 755) : ")
                os.chmod(path, int(mode, 8))
                print(f"{path} -> {mode}")
