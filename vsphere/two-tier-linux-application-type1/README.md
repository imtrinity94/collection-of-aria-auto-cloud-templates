# Distributed System

### 🚀 Overview
Provisions LoadBalancer, Machine, Network.

**Version:** `3`

## 🛠️ Technologies
- `Cloud.NSX.LoadBalancer`
- `Cloud.NSX.Network`
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| tier1_flavor | Server Size | `string` | `medium` | - |
| tier1_image | Tier-1 Operating System | `string` | `Ubuntu18` | - |
| tier1_ServerRole | Tier 1 Server Role | `string` | `web` | - |
| tier1_count | number of servers in Tier-1 | `number` | `1` | - |
| tier2_flavor | Server Size | `string` | `medium` | - |
| tier2_image | Tier-2 Operating System | `string` | `Ubuntu18` | - |
| tier2_ServerRole | Tier 2 Server Role | `string` | `sql` | - |
| tier2_count | number of servers in this Tier-2 | `number` | `1` | - |
| enviornment | Environment | `string` | `prd` | - |
| projectCode | Project Code | `string` | `-` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| Cloud_LoadBalancer_1 | `Cloud.NSX.LoadBalancer` |
| tier1_linux | `Cloud.vSphere.Machine` |
| tier2_linux | `Cloud.vSphere.Machine` |
| Cloud_Network_2 | `Cloud.NSX.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[🏠 Back to Root](../../README.md) | [⬅️ Back to Parent](../README.md)