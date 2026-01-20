# Web Application

**Version:** `0.0.1`

## 🛠️ Technologies
- `Cloud.NSX.LoadBalancer`
- `Cloud.NSX.Network`
- `Cloud.SecurityGroup`
- `Cloud.vSphere.Machine`

## 🏗️ Resources
| Logical Name | Type |
| :--- | :--- |
| backend | `Cloud.NSX.Network` |
| webLb | `Cloud.NSX.LoadBalancer` |
| webServer | `Cloud.vSphere.Machine` |
| dbServer | `Cloud.vSphere.Machine` |
| allowHTTPS | `Cloud.SecurityGroup` |
| allowSSH | `Cloud.SecurityGroup` |
| frontend | `Cloud.NSX.Network` |

## 📄 Files
- [blueprint.yaml](./blueprint.yaml)

---
[⬅️ Back to Parent](../README.md)