# Web Application v1

### 🚀 Overview
Provisions LoadBalancer, Machine, Network.

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
| web1Hostname | web1Hostname | `string` | `web` | - |
| web2Hostname | web2Hostname | `string` | `web` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| webLB | `Cloud.NSX.LoadBalancer` |
| webServer1 | `Cloud.vSphere.Machine` |
| webServer2 | `Cloud.vSphere.Machine` |
| webNetwork | `Cloud.NSX.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[🏠 Back to Root](../../README.md) | [⬅️ Back to Parent](../README.md)