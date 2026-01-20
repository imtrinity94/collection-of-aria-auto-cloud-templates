# Web Application v2

**Version:** `0.0.1`

## 🛠️ Technologies
- `Cloud.NSX.LoadBalancer`
- `Cloud.NSX.Network`
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| size | size | `string` | `small` | - |
| image | image | `string` | `Ubuntu-18` | - |
| username | username | `string` | `demo` | - |
| password | password | `string` | `-` | - |
| web1Hostname | web1Hostname | `string` | `-` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| Cloud_NSX_LoadBalancer_1 | `Cloud.NSX.LoadBalancer` |
| webServer1 | `Cloud.vSphere.Machine` |
| Cloud_NSX_Network_1 | `Cloud.NSX.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Parent](../README.md)