# Single Windows Virtual Machine (complex)

**Version:** `1.0.0`

## 🛠️ Technologies
- `Cloud.NSX.Network`
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| size | Virtual Machine Size | `string` | `small` | <strong>VM Size Information:</strong> <ul>   <li> small = 1vCPU, 1GB </li>   <li> medium = 2vCPU, 4GB </li>   <li> large = 4vCPU, 8GB </li> </ul>  |
| image | Operating System | `string` | `windows-server-2019` | - |
| username | username | `string` | `vmware` | - |
| password | password | `string` | `VMw@re1!` | - |
| passwordExpiry | Allow Password Expiry? | `boolean` | `False` | - |
| passwordChange | Change Password On Logon? | `boolean` | `False` | - |
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