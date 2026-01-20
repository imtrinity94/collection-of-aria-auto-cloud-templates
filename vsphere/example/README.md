# Single VM

**Version:** `2`

## 📝 Description
Single VM, No Networks

## 🛠️ Technologies
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| role | role | `string` | `-` | - |
| environment | environment | `string` | `prd` | - |
| location | location | `string` | `cloud:vmc` | - |
| size | size | `string` | `small` | VM Size |
| image | image | `string` | `linux` | - |
| backup | backup | `boolean` | `False` | - |
| backupType | backupType | `string` | `full` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| vm | `Cloud.vSphere.Machine` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Parent](../README.md)