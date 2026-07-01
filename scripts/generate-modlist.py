import os
import toml

def generate_modlist():
    mod_names = []
    mods_dir = 'mods'
    
    # Walk through the directory to find all .pw.toml files
    for root, dirs, files in os.walk(mods_dir):
        for file in files:
            if file.endswith('.pw.toml'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = toml.load(f)
                        # Try to get the name, fallback to filename if missing
                        name = data.get('name') or file.replace('.pw.toml', '')
                        mod_names.append(name)
                except Exception as e:
                    print(f"Skipping {file}: {e}")
    
    # Sort and write to MODLIST.md
    mod_names.sort()
    
    with open('MODLIST.md', 'w', encoding='utf-8') as f:
        f.write("# Server Modpack\n\n## Mod List\n\n")
        for name in mod_names:
            f.write(f"- [ ] {name}\n")
    
    print(f"Successfully generated MODLIST.md with {len(mod_names)} mods.")

if __name__ == "__main__":
    generate_modlist()