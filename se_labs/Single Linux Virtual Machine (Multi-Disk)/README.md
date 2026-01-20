# Single Virtual Machines - Multiple Disks (OnDemand)

### 🚀 Overview
Provisions Machine, Disk, Network.

**Version:** `1.0.0`

## 🛠️ Technologies
- `Cloud.NSX.Network`
- `Cloud.vSphere.Disk`
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| size | Virtual Machine Size | `string` | `small` | <strong>VM Size Information:</strong> <ul>   <li> small = 1vCPU, 1GB </li>   <li> medium = 2vCPU, 4GB </li>   <li> large = 4vCPU, 8GB </li> </ul>  |
| image | Operating System | `string` | `linux-ubuntu-server-22.04` | - |
| diskConfig | Add Additional Disks | `array` | `-` | - |
| username | username | `string` | `admin` | - |
| password | password | `string` | `VMw@re1!` | - |
| naming | Server Information | `object` | `-` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| machine | `Cloud.vSphere.Machine` |
| disk | `Cloud.vSphere.Disk` |
| network | `Cloud.NSX.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[🏠 Back to Root](../../README.md) | [⬅️ Back to Parent](../README.md)