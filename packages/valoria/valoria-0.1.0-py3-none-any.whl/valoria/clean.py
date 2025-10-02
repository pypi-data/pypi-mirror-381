import os
import hashlib
import time

def remove_empty_files(directory):
    """Supprime les fichiers vides"""
    print("🗑️  Suppression des fichiers vides...")
    empty_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            if os.path.getsize(filepath) == 0:
                try:
                    os.remove(filepath)
                    empty_count += 1
                    print(f"  Supprimé: {filepath}")
                except Exception as e:
                    print(f"  ❌ Erreur avec {filepath}: {e}")
    print(f"✅ {empty_count} fichiers vides supprimés")
    return empty_count

def remove_empty_dirs(directory):
    """Supprime les répertoires vides"""
    print("🗑️  Suppression des répertoires vides...")
    empty_dirs = 0
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir in dirs:
            dirpath = os.path.join(root, dir)
            try:
                if not os.listdir(dirpath):
                    os.rmdir(dirpath)
                    empty_dirs += 1
                    print(f"  Supprimé: {dirpath}")
            except Exception as e:
                print(f"  ❌ Erreur avec {dirpath}: {e}")
    print(f"✅ {empty_dirs} répertoires vides supprimés")
    return empty_dirs

def find_duplicates(directory):
    """Trouve les fichiers dupliqués"""
    print("🔍 Recherche des fichiers dupliqués...")
    hashes = {}
    duplicates = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                if os.path.getsize(filepath) == 0:
                    continue
                with open(filepath, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                if file_hash in hashes:
                    existing_file = hashes[file_hash]
                    existing_mtime = os.path.getmtime(existing_file)
                    current_mtime = os.path.getmtime(filepath)
                    if current_mtime < existing_mtime:
                        duplicates.append({
                            'file1': filepath,
                            'file2': existing_file,
                            'original': filepath,
                            'duplicate': existing_file
                        })
                        hashes[file_hash] = filepath
                    else:
                        duplicates.append({
                            'file1': existing_file,
                            'file2': filepath,
                            'original': existing_file,
                            'duplicate': filepath
                        })
                else:
                    hashes[file_hash] = filepath
            except Exception as e:
                print(f"  ❌ Erreur avec {filepath}: {e}")
    return duplicates

def format_file_time(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

def format_file_size(size):
    for unit in ['o', 'Ko', 'Mo', 'Go']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} To"

def confirm_delete_duplicates(duplicates):
    """Demande confirmation pour chaque doublon"""
    deleted_count = 0
    for i, dup_info in enumerate(duplicates, 1):
        file1 = dup_info['file1']
        file2 = dup_info['file2']
        original = dup_info['original']
        duplicate = dup_info['duplicate']

        print(f"\n{'='*60}")
        print(f"📋 DOUBLON {i}/{len(duplicates)}")
        print(f"{'='*60}")

        file1_size = os.path.getsize(file1)
        file1_mtime = os.path.getmtime(file1)
        file2_size = os.path.getsize(file2)
        file2_mtime = os.path.getmtime(file2)

        print(f"📄 FICHIER 1:\n  📁 {file1}\n  📊 Taille: {format_file_size(file1_size)}\n  📅 Modifié: {format_file_time(file1_mtime)}")
        if file1 == original:
            print("  🏷️  CONSIDÉRÉ COMME ORIGINAL")
        print(f"\n📄 FICHIER 2:\n  📁 {file2}\n  📊 Taille: {format_file_size(file2_size)}\n  📅 Modifié: {format_file_time(file2_mtime)}")
        if file2 == duplicate:
            print("  🏷️  CONSIDÉRÉ COMME DOUBLON")

        # Options de suppression
        print("\n🔧 OPTIONS DE SUPPRESSION:\n  1. Supprimer le FICHIER 1\n  2. Supprimer le FICHIER 2\n  3. Conserver les DEUX fichiers\n  4. Arrêter")
        while True:
            choice = input("Votre choix (1-4): ").strip()
            if choice == '1':
                file_to_delete = file1
                break
            elif choice == '2':
                file_to_delete = file2
                break
            elif choice == '3':
                file_to_delete = None
                break
            elif choice == '4':
                return deleted_count
            else:
                print("❌ Choix invalide.")

        if file_to_delete:
            confirm = input(f"Confirmer suppression '{os.path.basename(file_to_delete)}'? (o/n): ").lower()
            if confirm == 'o':
                try:
                    os.remove(file_to_delete)
                    deleted_count += 1
                    print(f"✅ SUPPRIMÉ: {file_to_delete}")
                except Exception as e:
                    print(f"❌ Erreur lors de la suppression: {e}")
    return deleted_count

def clean_directory(directory):
    """Nettoie le répertoire des fichiers vides et doublons"""
    print(f"🧹 NETTOYAGE DU RÉPERTOIRE: {directory}")
    empty_files = remove_empty_files(directory)
    empty_dirs = remove_empty_dirs(directory)
    duplicates = find_duplicates(directory)
    deleted_duplicates = 0
    if duplicates:
        global_confirm = input(f"\n{len(duplicates)} paires de doublons trouvées. Examiner chaque paire? (o/n): ").lower()
        if global_confirm == 'o':
            deleted_duplicates = confirm_delete_duplicates(duplicates)
    print(f"\n📊 Fichiers vides supprimés: {empty_files}\n📊 Répertoires vides supprimés: {empty_dirs}\n📊 Doublons supprimés: {deleted_duplicates}\n📊 Paires de doublons: {len(duplicates)}")
