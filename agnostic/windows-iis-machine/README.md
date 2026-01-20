# Windows-IIS-Machine

### 🚀 Overview
Provisions Machine, Network.

**Version:** `0.0.1`

## 🛠️ Technologies
- `Cloud.Machine`
- `Cloud.Network`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| user | Username for SSH | `string` | `Administrator` | The username you would like to usee for admin. |
| password | Admin Account Password | `string` | `VMware1!` | The password you would like to use for the user account. |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| windowsserver | `Cloud.Machine` |
| Cloud_Network_1 | `Cloud.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[🏠 Back to Root](../../README.md) | [⬅️ Back to Parent](../README.md)