# Agnostic Single Machine

**Version:** `0.0.4`

## 🛠️ Technologies
- `Cloud.Machine`
- `Cloud.Network`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| cloud | Cloud Endpoint | `string` | `env:vsphere` | - |
| image | Image | `string` | `-` | - |
| size | Size | `string` | `-` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| Cloud_Machine_1 | `Cloud.Machine` |
| Cloud_Network_1 | `Cloud.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Parent](../README.md)