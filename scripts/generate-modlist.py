import os
import toml

def generate_modlist():
    mod_names = []
    # Adjust this path if your mods are in a different folder
    mods_dir = 'mods'
    
    for root, dirs, files in os.walk(mods_dir):
        for file in files:
            if file.endswith('.pw.toml'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    data = toml.load(f)
                    mod_names.append(data.get('name', file))
    
    mod_names.sort()
    
    with open('MODLIST.md', 'w', encoding='utf-8') as f:
        f.write("# Server Modpack\n\n## Mod List\n\n")
        for name in mod_names:
            f.write(f"- [ ] {name}\n")

if __name__ == "__main__":
    generate_modlist()