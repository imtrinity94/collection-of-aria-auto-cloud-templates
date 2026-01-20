# VMware Aria Automation Templates

![Banner](./aria_automation_banner.png)

Welcome to the collection of VMware Aria Automation (formerly Cloud Assembly) cloud templates. This repository serves as a centralized library for various infrastructure-as-code blueprints.

## 🚀 Overview

This collection provides a wide variety of templates ranging from simple single-machine deployments to complex multi-tier applications, including:
- **Cloud Agnostic**: Templates that work across AWS, Azure, and vSphere.
- **Application Stacks**: Web applications, SQL servers, and more.
- **Kubernetes**: On-demand cluster and namespace provisioning.
- **SE Labs**: Specialized lab environments and test beds.

## 🔧 Usage

1. **Browse** the categories below to find a template that fits your needs.
2. **Review** the `blueprint.yaml` and the corresponding documentation.
3. **Import** the YAML content into your Aria Automation environment.
4. **Configure** the required inputs as documented in each README.

## 📂 Repository Structure

## 🛠️ Maintenance

The documentation in this repository is automatically generated using the `generate_readmes.py` script. To update the README files after making changes to the blueprints:

```bash
python generate_readmes.py
```

## 📁 Blueprints & Categories

| Name | Description | Link |
| :--- | :--- | :--- |
| agnostic | Directory containing templates or sub-categories. | [View Details](./agnostic/) |
| apps | Directory containing templates or sub-categories. | [View Details](./apps/) |
| aws | Directory containing templates or sub-categories. | [View Details](./aws/) |
| azure | Directory containing templates or sub-categories. | [View Details](./azure/) |
| centos | Directory containing templates or sub-categories. | [View Details](./centos/) |
| docker | Directory containing templates or sub-categories. | [View Details](./docker/) |
| k8s | Directory containing templates or sub-categories. | [View Details](./k8s/) |
| se_labs | Directory containing templates or sub-categories. | [View Details](./se_labs/) |
| VMware vCenter Deployment (DO NOT USE) | Provisions Machine, Network. | [View Details](./vcenter/) |
| vsphere | Directory containing templates or sub-categories. | [View Details](./vsphere/) |

## 📄 Files
- [commands.txt](./commands.txt)

