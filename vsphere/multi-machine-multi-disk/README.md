# multi-machine-multi-disk

**Version:** `1.0.0`

## 🛠️ Technologies
- `Cloud.vSphere.Disk`
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| role | role | `string` | `-` | - |
| environment | environment | `string` | `prd` | - |
| location | location | `string` | `cloud:vmc` | - |
| size | size | `string` | `small` | - |
| image | image | `string` | `linux` | - |
| backup | backup | `boolean` | `False` | - |
| backupType | backupType | `string` | `full` | - |
| diskInfo | Add Additional Disks | `array` | `-` | - |
| vmCount | Number of VMs | `integer` | `1` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| vm | `Cloud.vSphere.Machine` |
| disk | `Cloud.vSphere.Disk` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Parent](../README.md)