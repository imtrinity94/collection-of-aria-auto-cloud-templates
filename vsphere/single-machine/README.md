# Single Machine

**Version:** `1.0.0`

## 🛠️ Technologies
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| role | role | `string` | `-` | - |
| environment | environment | `string` | `prd` | - |
| location | location | `string` | `cloud:vmc` | - |
| size | size | `string` | `small` | - |
| image | image | `string` | `linux` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| vm | `Cloud.vSphere.Machine` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Parent](../README.md)