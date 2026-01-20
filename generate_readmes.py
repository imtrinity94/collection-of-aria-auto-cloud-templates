import os
import yaml

def parse_blueprint(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None

def generate_folder_readme(path, subdirs, files, relative_path):
    readme_path = os.path.join(path, "README.md")
    
    blueprint_data = None
    if "blueprint.yaml" in files:
        blueprint_data = parse_blueprint(os.path.join(path, "blueprint.yaml"))
    
    folder_name = os.path.basename(path)
    if not relative_path:
        folder_name = "VMware Aria Automation Templates"
    
    title = folder_name
    if blueprint_data and isinstance(blueprint_data, dict):
        title = blueprint_data.get('name', folder_name)

    content = f"# {title}\n\n"
    
    if not relative_path:
        content += "Welcome to the collection of VMware Aria Automation (formerly Cloud Assembly) cloud templates. This repository serves as a centralized library for various infrastructure-as-code blueprints.\n\n"
        content += "## 📂 Navigation\n\n"
        content += "| Category | Description |\n"
        content += "| :--- | :--- |\n"
        
        # We'll fill this in later or just use the list below
    
    if blueprint_data and isinstance(blueprint_data, dict):
        version = blueprint_data.get('version', '1.0.0')
        content += f"**Version:** `{version}`\n\n"
        
        description = blueprint_data.get('description', '')
        if description:
            content += f"## 📝 Description\n{description}\n\n"
        
        # Resources Summary
        resources = blueprint_data.get('resources', {})
        resource_types = set()
        if isinstance(resources, dict):
            for r in resources.values():
                if isinstance(r, dict):
                    resource_types.add(r.get('type', 'Unknown'))
        
        if resource_types:
            content += "## 🛠️ Technologies\n"
            for rt in sorted(resource_types):
                content += f"- `{rt}`\n"
            content += "\n"

        # Inputs Table
        inputs = blueprint_data.get('inputs', {})
        if isinstance(inputs, dict) and inputs:
            content += "## 📥 Inputs\n"
            content += "| Name | Title | Type | Default | Description |\n"
            content += "| :--- | :--- | :--- | :--- | :--- |\n"
            for key, val in inputs.items():
                if isinstance(val, dict):
                    ititle = val.get('title', key)
                    itype = val.get('type', 'string')
                    idefault = val.get('default', '-')
                    idesc = val.get('description', '-').replace('\n', ' ')
                    content += f"| {key} | {ititle} | `{itype}` | `{idefault}` | {idesc} |\n"
            content += "\n"
            
        # Resources Table
        if isinstance(resources, dict) and resources:
            content += "## 🏗️ Resources\n"
            content += "| Logical Name | Type |\n"
            content += "| :--- | :--- |\n"
            for key, val in resources.items():
                if isinstance(val, dict):
                    rtype = val.get('type', '-')
                    content += f"| {key} | `{rtype}` |\n"
            content += "\n"

    # Subdirectories
    valid_subdirs = sorted([sd for sd in subdirs if not sd.startswith('.') and sd not in ['icons']])
    if valid_subdirs:
        content += "## 📁 Sub-Categories & Blueprints\n\n"
        content += "| Name | Link |\n"
        content += "| :--- | :--- |\n"
        for sd in valid_subdirs:
            sd_path = os.path.join(path, sd)
            sd_bp = os.path.join(sd_path, "blueprint.yaml")
            display_name = sd
            if os.path.exists(sd_bp):
                sd_data = parse_blueprint(sd_bp)
                if sd_data and isinstance(sd_data, dict) and 'name' in sd_data:
                    display_name = sd_data['name']
            
            content += f"| {display_name} | [View Details](./{sd}/) |\n"
        content += "\n"
    
    # Files
    valid_files = sorted([f for f in files if f != "README.md" and not f.startswith('.') and f != "generate_readmes.py"])
    if valid_files:
        content += "## 📄 Files\n"
        for f in valid_files:
            content += f"- [{f}](./{f})\n"
        content += "\n"
        
    if relative_path:
        content += "---\n[⬅️ Back to Root](../README.md)" if os.path.dirname(relative_path) == "" else f"---\n[⬅️ Back to Parent](../README.md)"

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    root_dir = os.getcwd()
    print(f"Working in {root_dir}")
    for root, dirs, files in os.walk(root_dir):
        # Exclude hidden and specific directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['icons']]
        
        rel_path = os.path.relpath(root, root_dir)
        if rel_path == ".":
            rel_path = ""
            
        print(f"Generating README in {root}")
        generate_folder_readme(root, dirs, files, rel_path)

if __name__ == "__main__":
    main()
