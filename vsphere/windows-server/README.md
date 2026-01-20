# Windows Server (Spec)

**Version:** `1`

## 🛠️ Technologies
- `Cloud.NSX.Network`
- `Cloud.SecurityGroup`
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| environment | environment | `string` | `env:prod` | - |
| network | network | `string` | `tier:infra` | - |
| size | size | `string` | `Medium` | - |
| image | image | `string` | `Windows 2016` | - |
| hostname | hostname | `string` | `-` | - |
| username | username | `string` | `-` | - |
| password | password | `string` | `-` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| Windows_SG | `Cloud.SecurityGroup` |
| windowsServer | `Cloud.vSphere.Machine` |
| nsx | `Cloud.NSX.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Parent](../README.md)