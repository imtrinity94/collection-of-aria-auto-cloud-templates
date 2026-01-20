# Two Tier Linux Application - Type 3

### 🚀 Overview
Two tier Linux application on routed NSX networks with Load Balancer. Automated naming based on role.

**Version:** `1`

## 📝 Detailed Description
Two tier Linux application on routed NSX networks with Load Balancer. Automated naming based on role.

## 🛠️ Technologies
- `Cloud.NSX.LoadBalancer`
- `Cloud.NSX.Network`
- `Cloud.vSphere.Machine`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| tier1_ServerRole | Server Role | `string` | `-` | - |
| tier1_flavor | Server Size | `string` | `-` | - |
| tier1_image | Operating System | `string` | `-` | - |
| tier1_count | number of servers in this tier | `number` | `1` | - |
| tier2_ServerRole | Server Role | `string` | `-` | - |
| tier2_flavor | Server Size | `string` | `-` | - |
| tier2_image | Operating System | `string` | `-` | - |
| tier2_count | number of servers in this tier | `number` | `1` | - |
| projectCode | Project Code | `string` | `-` | - |
| installAgent | Install Telegraf Monitoring | `boolean` | `False` | - |
| agentRunAsUsername | Telegraf Run User Account | `string` | `holuser` | - |
| agentRunAsPassword | Telegraf Run User Password | `string` | `${secret.password}` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| tier1_loadbalancer | `Cloud.NSX.LoadBalancer` |
| tier1_linux | `Cloud.vSphere.Machine` |
| tier2_linux | `Cloud.vSphere.Machine` |
| network | `Cloud.NSX.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[🏠 Back to Root](../../README.md) | [⬅️ Back to Parent](../README.md)