


# 🔐 Flask App with Kubernetes Secrets

This project demonstrates how to use **Kubernetes Secrets** to securely inject sensitive values like database credentials into a **Flask application** as environment variables.

---

## 📁 Project Structure

```

flask-secret-app/
├── app.py                # Flask app reading secrets
├── requirements.txt      # Python dependencies
├── Dockerfile            # Build the container
├── .env                  # (Optional) For local testing
├── k8s-secret.yaml       # Kubernetes Secret (base64 encoded)
└── k8s-deployment.yaml   # Deployment + Service using secrets

````

---

## 🔑 Secret Data

The following values are securely stored and injected into the container:

| Key       | Value       |
|-----------|-------------|
| `DB_USER` | `admin`     |
| `DB_PASS` | `s3cr3t123` |

They are encoded in base64 in the `k8s-secret.yaml`.

---

## 🚀 How to Deploy

### 1. Build and Push Docker Image

```bash
docker build -t YOUR_USERNAME/flask-secret-app .
docker push YOUR_USERNAME/flask-secret-app
````

> Replace `YOUR_USERNAME` with your DockerHub username.

---

### 2. Apply Kubernetes Resources

```bash
kubectl apply -f k8s-secret.yaml
kubectl apply -f k8s-deployment.yaml
```

---

### 3. Open in Browser (Minikube)

```bash
minikube service flask-secret-service
```

You will see:

```
🔐 Connected to DB as: admin
🔑 Password: s3cr3t123
```

---

## 🧹 Cleanup

```bash
kubectl delete -f k8s-deployment.yaml
kubectl delete -f k8s-secret.yaml
```

---

## 🧠 Concepts Covered

| Resource       | Purpose                             |
| -------------- | ----------------------------------- |
| `Secret`       | Secure key-value storage (base64)   |
| `secretKeyRef` | Injects secrets as env vars         |
| `Flask app`    | Reads vars via `os.getenv()`        |
| `Service`      | NodePort exposes the app externally |

---

## 🔒 Security Notes

* Secrets are base64-encoded (not encrypted by default).
* To encrypt secrets at rest, use Kubernetes EncryptionConfiguration or sealed-secrets.

---

## 📚 References

* [Kubernetes Secrets Documentation](https://kubernetes.io/docs/concepts/configuration/secret/)
* [Best Practices for Secrets](https://kubernetes.io/docs/concepts/configuration/secret/#best-practices)

---

Happy deploying! 🚀


