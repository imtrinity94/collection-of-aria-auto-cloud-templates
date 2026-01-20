# Single Virtual Machines - Multiple Disks (OnDemand)

**Version:** `1.0.0`

## 🛠️ Technologies
- `Cloud.vSphere.Disk`
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| location | location | `string` | `cloud:vsphere` | - |
| size | size | `string` | `small` | - |
| image | image | `string` | `Ubuntu-18-SSC` | - |
| diskConfig | Add Additional Disks | `array` | `-` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| vm | `Cloud.vSphere.Machine` |
| extraDisk | `Cloud.vSphere.Disk` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Parent](../README.md)