
# 📘 Using ConfigMap in Kubernetes with Multiple Environment Variables

## 📖 Introduction: What is a ConfigMap?

A **ConfigMap** in Kubernetes is an object used to store **non-sensitive configuration data** in the form of key-value pairs. It is commonly used to **externalize app configuration** such as environment variables, file contents, command-line arguments, etc.

Instead of hardcoding variables into your container image, you can use a ConfigMap to inject them at runtime. This allows you to:
- Separate config from code
- Update configuration without rebuilding Docker images
- Use the same container in different environments (dev, staging, prod)

---

## ✅ This Guide Covers:
1. 🔁 Injecting **individual environment variables** using `valueFrom`
2. ✅ Injecting **all environment variables at once** using `envFrom`
3. 🧪 Testing via a simple Flask app

---

## 📁 Folder Structure

```

flask-multienv-app/
├── app.py
├── Dockerfile
├── requirements.txt
├── .env                 # optional
├── k8s-configmap.yaml   # ✅ defines the environment variables
└── k8s-deployment.yaml  # 🔁 multi or single reference to ConfigMap

````

---

## 🧾 ConfigMap Definition

### `k8s-configmap.yaml`

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: multi-env-config
data:
  FIRST_NAME: Ganesh
  LAST_NAME: Pandian
  DATABASE_URL: mysql://user:pass@mysql-service:3306/mydb
````

Apply it:

```bash
kubectl apply -f k8s-configmap.yaml
```

---

## 🔁 Method 1: Multi-Key Reference (`valueFrom`)

### `k8s-deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-multienv-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flask-multienv
  template:
    metadata:
      labels:
        app: flask-multienv
    spec:
      containers:
      - name: flask-container
        image: YOUR_USERNAME/flask-multienv-app
        ports:
        - containerPort: 80
        env:
        - name: FIRST_NAME
          valueFrom:
            configMapKeyRef:
              name: multi-env-config
              key: FIRST_NAME
        - name: LAST_NAME
          valueFrom:
            configMapKeyRef:
              name: multi-env-config
              key: LAST_NAME
        - name: DATABASE_URL
          valueFrom:
            configMapKeyRef:
              name: multi-env-config
              key: DATABASE_URL
```

---

## ✅ Method 2: Single ConfigMap Reference (`envFrom`)

### Simplified `k8s-deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-multienv-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flask-multienv
  template:
    metadata:
      labels:
        app: flask-multienv
    spec:
      containers:
      - name: flask-container
        image: YOUR_USERNAME/flask-multienv-app
        ports:
        - containerPort: 80
        envFrom:
        - configMapRef:
            name: multi-env-config
```

This will load all keys from the `multi-env-config` ConfigMap into the container environment.

---

## 🧪 Test in App (`app.py`)

```python
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    first = os.getenv("FIRST_NAME", "Unknown")
    last = os.getenv("LAST_NAME", "Unknown")
    db_url = os.getenv("DATABASE_URL", "Not Set")
    return (
        f"👋 Hello, {first} {last}!<br>"
        f"🔗 Connected to database: {db_url}"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

---

## 🧹 Cleanup

```bash
kubectl delete -f k8s-deployment.yaml
kubectl delete -f k8s-configmap.yaml
```

---

## ✅ Summary

| Method      | Description                                     |
| ----------- | ----------------------------------------------- |
| `valueFrom` | Reference each key separately (more control)    |
| `envFrom`   | Inject all ConfigMap keys at once (simpler)     |
| `ConfigMap` | Central store of non-sensitive environment data |

---

Happy Kubernetes Learning! 🚀

