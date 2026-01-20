# Azure Virtual Machine - Outbound Network

**Version:** `1.0.0`

## 🛠️ Technologies
- `Cloud.Azure.Machine`
- `Cloud.Azure.ResourceGroup`
- `Cloud.Network`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| hostname | Servername | `string` | `-` | - |
| size | Size | `string` | `Small` | - |
| image | Image | `string` | `Windows Server 2019` | - |
| service | Service Tier | `string` | `service:bronze` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| Cloud_Azure_ResourceGroup_1 | `Cloud.Azure.ResourceGroup` |
| Cloud_Azure_Machine_1 | `Cloud.Azure.Machine` |
| Cloud_Network_1 | `Cloud.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Parent](../README.md)