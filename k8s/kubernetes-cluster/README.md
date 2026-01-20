# Kubernetes Cluster

**Version:** `1.0.0`

## 🛠️ Technologies
- `Cloud.Machine`
- `Cloud.Network`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| network | Network Capability tag | `string` | `-` | - |
| region | Region Capability Tag | `string` | `-` | Region |
| no_of_nodes | Number of kubernetes nodes | `integer` | `-` | Number of kubernetes nodes to be created for the Cluster setup |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| K8s_Node | `Cloud.Machine` |
| K8s_Master | `Cloud.Machine` |
| K8s_Network | `Cloud.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Parent](../README.md)