
---


# 🚀 Flask + Kubernetes Project with Environment Variables

This project demonstrates how to:

- ✅ Build a simple Flask app that uses environment variables
- ✅ Load `.env` variables in Python using `python-dotenv`
- ✅ Override environment variables using Kubernetes `env` field

---

## 📁 Project Structure

```

flask-env-app/
├── app.py
├── Dockerfile
├── requirements.txt
├── .env
└── k8s-deployment.yaml

````

---

## 🧠 Step 1: Python Flask App

### `app.py`

```python
import os
from flask import Flask
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    env = os.getenv("ENVIRONMENT", "development")
    return f"✅ Running in {env} mode!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
````

---

### `requirements.txt`

```
flask
python-dotenv
```

---

### `.env`

```env
ENVIRONMENT=staging
```

---

## 🐳 Step 2: Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

---

## 🏗️ Step 3: Build and Push Docker Image

```bash
# Build and push
docker build -t YOUR_USERNAME/flask-env-app .
docker push YOUR_USERNAME/flask-env-app
```

🔁 Replace `YOUR_USERNAME` with your DockerHub username.

---

## ☸️ Step 4: Kubernetes Deployment

### `k8s-deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-env-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flask-env
  template:
    metadata:
      labels:
        app: flask-env
    spec:
      containers:
      - name: flask-container
        image: YOUR_USERNAME/flask-env-app
        ports:
        - containerPort: 80
        env:
        - name: ENVIRONMENT
          value: "production"

---
apiVersion: v1
kind: Service
metadata:
  name: flask-env-service
spec:
  type: NodePort
  selector:
    app: flask-env
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30080
```

---

## 🚀 Step 5: Deploy to Kubernetes

If using Minikube:

```bash
minikube start
kubectl apply -f k8s-deployment.yaml
minikube service flask-env-service
```

---

## ✅ Expected Output

Visit the browser and you should see:

```
✅ Running in production mode!
```

---

## 🔁 To Change Environment

Update the `env` section in your YAML:

```yaml
        - name: ENVIRONMENT
          value: "staging"
```

Then reapply:

```bash
kubectl apply -f k8s-deployment.yaml
```

---

## 🧹 Clean Up

```bash
kubectl delete -f k8s-deployment.yaml
```

---

## 🎓 Summary Table

| Component       | Purpose                       |
| --------------- | ----------------------------- |
| `.env`          | Local testing only            |
| `load_dotenv()` | Loads `.env` into app runtime |
| `env:` in K8s   | Injects variable in container |
| Flask app       | Reads via `os.getenv()`       |
| Minikube        | Run Kubernetes locally        |

---


