# CentOS Machine

### 🚀 Overview
Provisions Machine, Network.

**Version:** `0.0.1`

## 🛠️ Technologies
- `Cloud.Network`
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| image | Image | `string` | `CentOS 8` | - |
| size | Size | `string` | `Small` | - |
| hostname | hostname | `string` | `centos` | - |
| username | username | `string` | `demo` | - |
| password | password | `string` | `VMware1!` | - |
| domain | domain | `string` | `thecloudxpert.local` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| Cloud_Machine_1 | `Cloud.vSphere.Machine` |
| Cloud_Network_1 | `Cloud.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[🏠 Back to Root](../../README.md) | [⬅️ Back to Parent](../README.md)