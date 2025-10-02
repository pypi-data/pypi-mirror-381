import os

def analyze_dependencies(directory):
    print(f"Analyse des dépendances pour {directory} (Python uniquement)")
    for root, _, files in os.walk(directory):
        for f in files:
            if f.endswith(".py"):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    for line in file:
                        if line.startswith("import") or line.startswith("from"):
                            print(f"{f} : {line.strip()}")
