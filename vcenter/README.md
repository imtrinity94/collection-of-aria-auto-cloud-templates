# VMware vCenter Deployment (DO NOT USE)

**Version:** `1.0`

## 🛠️ Technologies
- `Cloud.vSphere.Machine`
- `Cloud.vSphere.Network`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| vcFqdn | vcFqdn | `string` | `vcs02` | - |
| vcPassword | vcPassword | `string` | `VMware1!` | - |
| vcIpAddress | vcIpAddress | `string` | `172.16.10.22` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| vcsa | `Cloud.vSphere.Machine` |
| vmw_mgmt | `Cloud.vSphere.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Root](../README.md)