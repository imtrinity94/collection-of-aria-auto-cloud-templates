# K8s On-Demand Namespace

### 🚀 Overview
Provisions Namespace.

**Version:** `1.0`

## 🛠️ Technologies
- `Cloud.K8S.Namespace`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| namespace | Name | `string` | `-` | - |
| maxPods | Max Pods | `string` | `-` | The maximum number of pods in a non-terminal state in the namespace. |
| sumCPU | CPU | `string` | `-` | The sum of CPU requests in the namespace. |
| sumMemory | Memory | `string` | `-` | The sum of memory requests in the namespace. |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| TKGi_Namespace | `Cloud.K8S.Namespace` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[🏠 Back to Root](../../README.md) | [⬅️ Back to Parent](../README.md)