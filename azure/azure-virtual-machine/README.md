# Azure Virtual Machine

### 🚀 Overview
Provisions ResourceGroup, Machine, Network.

**Version:** `1.0.0`

## 🛠️ Technologies
- `Cloud.Azure.Machine`
- `Cloud.Azure.ResourceGroup`
- `Cloud.Network`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| size | Size | `string` | `-` | - |
| image | Image | `string` | `Windows Server 2019` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| Cloud_Azure_ResourceGroup_1 | `Cloud.Azure.ResourceGroup` |
| Cloud_Azure_Machine_1 | `Cloud.Azure.Machine` |
| Cloud_Network_1 | `Cloud.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[🏠 Back to Root](../../README.md) | [⬅️ Back to Parent](../README.md)