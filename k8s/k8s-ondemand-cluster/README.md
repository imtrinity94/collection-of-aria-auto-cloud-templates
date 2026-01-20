# K8S On-Demand Cluster

### 🚀 Overview
Provisions Cluster.

**Version:** `1.0`

## 🛠️ Technologies
- `Cloud.K8S.Cluster`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| clusterName | Cluster Name | `string` | `CHANGE-ME-NO-SPACES` | This is the cluster name. It should NOT contain spaces, only dashes (ex. pks-dev-cluster) |
| clusterHostname | Master Node Hostname | `string` | `-` | This is the DNS name for the Master Node in the cluster (ex. test.pks.domain.local). |
| clusterPort | clusterPort | `integer` | `8443` | - |
| numWorkers | numWorkers | `integer` | `3` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| Cloud_K8S_Cluster_1 | `Cloud.K8S.Cluster` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[🏠 Back to Root](../../README.md) | [⬅️ Back to Parent](../README.md)