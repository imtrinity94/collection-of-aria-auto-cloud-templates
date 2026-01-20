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

def summarize_blueprint(data):
    if not data or not isinstance(data, dict):
        return "No description available."
    
    # Use description if it exists
    desc = data.get('description', '')
    if desc:
        # Take the first one or two lines and sanitize
        lines = desc.strip().split('\n')
        summary = " ".join(lines[:2])
        if len(summary) > 150:
            summary = summary[:147] + "..."
        return summary

    # Otherwise, summarize based on resources
    resources = data.get('resources', {})
    if isinstance(resources, dict) and resources:
        res_types = []
        for r in resources.values():
            if isinstance(r, dict):
                rtype = r.get('type', '').split('.')[-1]
                if rtype and rtype not in res_types:
                    res_types.append(rtype)
        
        if res_types:
            return f"Provisions {', '.join(res_types[:3])}{' and more' if len(res_types) > 3 else ''}."
    
    return "VMware Aria Automation template."

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
        content += "![Banner](./aria_automation_banner.png)\n\n"
        content += "Welcome to the collection of VMware Aria Automation (formerly Cloud Assembly) cloud templates. This repository serves as a centralized library for various infrastructure-as-code blueprints.\n\n"
        content += "## 🚀 Overview\n\n"
        content += "This collection provides a wide variety of templates ranging from simple single-machine deployments to complex multi-tier applications, including:\n"
        content += "- **Cloud Agnostic**: Templates that work across AWS, Azure, and vSphere.\n"
        content += "- **Application Stacks**: Web applications, SQL servers, and more.\n"
        content += "- **Kubernetes**: On-demand cluster and namespace provisioning.\n"
        content += "- **SE Labs**: Specialized lab environments and test beds.\n\n"
        content += "## 🔧 Usage\n\n"
        content += "1. **Browse** the categories below to find a template that fits your needs.\n"
        content += "2. **Review** the `blueprint.yaml` and the corresponding documentation.\n"
        content += "3. **Import** the YAML content into your Aria Automation environment.\n"
        content += "4. **Configure** the required inputs as documented in each README.\n\n"
        content += "## 📂 Repository Structure\n\n"
        
    # Maintenance Note for Root
    if not relative_path:
        content += "## 🛠️ Maintenance\n\n"
        content += "The documentation in this repository is automatically generated using the `generate_readmes.py` script. To update the README files after making changes to the blueprints:\n\n"
        content += "```bash\npython generate_readmes.py\n```\n\n"
    
    if blueprint_data and isinstance(blueprint_data, dict):
        content += f"### 🚀 Overview\n"
        content += f"{summarize_blueprint(blueprint_data)}\n\n"
        
        version = blueprint_data.get('version', '1.0.0')
        content += f"**Version:** `{version}`\n\n"
        
        description = blueprint_data.get('description', '')
        if description:
            content += f"## 📝 Detailed Description\n{description}\n\n"
        
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
        content += "## 📁 Blueprints & Categories\n\n"
        content += "| Name | Description | Link |\n"
        content += "| :--- | :--- | :--- |\n"
        for sd in valid_subdirs:
            sd_path = os.path.join(path, sd)
            sd_bp = os.path.join(sd_path, "blueprint.yaml")
            display_name = sd
            summary = "Directory containing templates or sub-categories."
            
            if os.path.exists(sd_bp):
                sd_data = parse_blueprint(sd_bp)
                if sd_data and isinstance(sd_data, dict):
                    display_name = sd_data.get('name', sd)
                    summary = summarize_blueprint(sd_data)
            
            content += f"| {display_name} | {summary} | [View Details](./{sd}/) |\n"
        content += "\n"
    
    # Files
    valid_files = sorted([f for f in files if f != "README.md" and not f.startswith('.') and f != "generate_readmes.py" and not f.endswith('.png')])
    if valid_files:
        content += "## 📄 Files\n"
        for f in valid_files:
            content += f"- [{f}](./{f})\n"
        content += "\n"
        
    if relative_path:
        # Determine how many levels up to go for the root link
        levels = len(relative_path.split(os.sep))
        root_link = "../" * levels + "README.md"
        parent_link = "../README.md"
        
        content += f"---\n[🏠 Back to Root]({root_link}) | [⬅️ Back to Parent]({parent_link})"

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
