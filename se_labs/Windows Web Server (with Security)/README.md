# Windows Web Server (with Security)

**Version:** `1.0`

## 🛠️ Technologies
- `Cloud.NSX.Network`
- `Cloud.SaltStack`
- `Cloud.SecurityGroup`
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| size | Virtual Machine Size | `string` | `small` | <strong>VM Size Information:</strong> <ul>   <li> small = 1vCPU, 1GB </li>   <li> medium = 2vCPU, 4GB </li>   <li> large = 4vCPU, 8GB </li> </ul>  |
| image | Operating System | `string` | `windows-server-2019` | - |
| naming | Server Information | `object` | `-` | - |
| securityZone | Security Zone | `string` | `security:internal` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| webRules | `Cloud.SecurityGroup` |
| zoneRules | `Cloud.SecurityGroup` |
| config | `Cloud.SaltStack` |
| machine | `Cloud.vSphere.Machine` |
| network | `Cloud.NSX.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Parent](../README.md)