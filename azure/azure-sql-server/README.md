# Single MS Azure SQL database

**Version:** `1.0.0`

## 🛠️ Technologies
- `Cloud.Azure.ResourceGroup`
- `Cloud.Service.Azure.SQL.Database`
- `Cloud.Service.Azure.SQL.Server`

## 📥 Inputs
| Name | Title | Type | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| resourceGroup | Azure Resource Group Name | `string` | `-` | - |
| sqlServerName | SQL Server Name | `string` | `-` | - |
| sqlDatabaseName | SQL Database Name | `string` | `-` | - |
| sqlAdminName | Admin User Name | `string` | `-` | - |
| sqlAdminPassword | Admin Password | `string` | `-` | - |

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| Azure_ResourceGroup | `Cloud.Azure.ResourceGroup` |
| Azure_SQL_Server | `Cloud.Service.Azure.SQL.Server` |
| Azure_SQL_Database | `Cloud.Service.Azure.SQL.Database` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Parent](../README.md)