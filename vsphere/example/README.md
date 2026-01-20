# Single VM

### 🚀 Overview
Single VM, No Networks

**Version:** `2`

## 📝 Detailed Description
Single VM, No Networks

## 🛠️ Technologies
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| role | role | `string` | `-` | - |
| environment | environment | `string` | `prd` | - |
| location | location | `string` | `cloud:vmc` | - |
| size | size | `string` | `small` | VM Size |
| image | image | `string` | `linux` | - |
| backup | backup | `boolean` | `False` | - |
| backupType | backupType | `string` | `full` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| vm | `Cloud.vSphere.Machine` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[🏠 Back to Root](../../README.md) | [⬅️ Back to Parent](../README.md)