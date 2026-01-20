# Single Linux Virtual Machine (Complex)

**Version:** `1.0.0`

## 🛠️ Technologies
- `Cloud.NSX.Network`
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| hostname | Hostname | `string` | `-` | The hostname of the virtual machine |
| image | Linux Version | `string` | `linux-ubuntu-server-25.04` | Choose what version of windows |
| size | VM Size | `string` | `medium` | <b> Select the size of deployment </b></br> Small: 1 vCPU - 2GB ram - 40GB disk </br> Medium: 2 vCPU - 4GB ram - 40GB disk </br> Large: 4 vCPU - 16GB ram - 40GB disk </br> |
| costcenter | Cost Center | `integer` | `-` | - |
| backup | Backup | `string` | `24h31d` | - |
| ad_group | AD Groups | `string` | `` | Provide the Group of people to be permitted login to server in format group@domain.com |
| superuser_ad_group | Superuser AD Groups | `string` | `` | Provide the Group of people to have superuser priviliges in format group@domain.com |
| naming | Server Information | `object` | `-` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| machine | `Cloud.vSphere.Machine` |
| network | `Cloud.NSX.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Parent](../README.md)