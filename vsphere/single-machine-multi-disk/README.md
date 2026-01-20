# Multiple Virtual Machines - Multiple Disks (OnDemand)

**Version:** `1.0.0`

## 🛠️ Technologies
- `Cloud.vSphere.Disk`
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| location | location | `string` | `cloud:vmc` | - |
| size | size | `string` | `small` | - |
| image | image | `string` | `linux` | - |
| numVms | Number of VMs | `integer` | `2` | - |
| diskConfig | Add Additional Disks | `array` | `-` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| vm | `Cloud.vSphere.Machine` |
| disk | `Cloud.vSphere.Disk` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Parent](../README.md)