Absolutely! Here's the **complete Horizontal Pod Autoscaler (HPA) demo**, including:

* YAML files for Deployment and HPA
* Simulation commands
* Full README.md documentation

---

## 📁 Folder Structure

```
k8s-hpa-demo/
├── hpa-deployment.yaml
├── hpa.yaml
└── README.md
```

---

## ✅ `hpa-deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: php-apache
spec:
  replicas: 1
  selector:
    matchLabels:
      app: php-apache
  template:
    metadata:
      labels:
        app: php-apache
    spec:
      containers:
      - name: php-apache
        image: k8s.gcr.io/hpa-example
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: 200m
          limits:
            cpu: 500m
```

---

## ✅ `hpa.yaml`

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: php-apache-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: php-apache
  minReplicas: 1
  maxReplicas: 5
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
```

---

## 📖 `README.md`


# ⚖️ Horizontal Pod Autoscaler (HPA) in Minikube

This project demonstrates how to use **Horizontal Pod Autoscaler (HPA)** in Kubernetes to scale pods based on CPU usage.

---

## ✅ Prerequisites

- Minikube running
- Metrics Server enabled

```bash
minikube start
minikube addons enable metrics-server
````

---

## 📁 Files

* `hpa-deployment.yaml`: Deploys a php-apache pod with CPU resource requests
* `hpa.yaml`: Creates an HPA that scales pods from 1 to 5 based on CPU

---

## 🚀 Step-by-Step Instructions

### 1. Apply the Deployment

```bash
kubectl apply -f hpa-deployment.yaml
```

### 2. Apply the HPA

```bash
kubectl apply -f hpa.yaml
```

### 3. Watch the HPA Behavior

```bash
kubectl get hpa
watch kubectl get hpa
```

Initially, it will stay at 1 pod.

---

## 🔥 Simulate Load (Trigger Autoscaling)

```bash
kubectl run -i --tty load-generator --rm --image=busybox --restart=Never -- /bin/sh
```

Inside the terminal:

```sh
while true; do wget -q -O- http://php-apache; done
```

Watch the pod count scale:

```bash
watch kubectl get hpa
watch kubectl get pods
```

---

## 📉 Expected Output

You’ll see the number of pods scale up (e.g., 3–5) if CPU crosses 50%.

```bash
NAME               REFERENCE              TARGETS    MINPODS   MAXPODS   REPLICAS
php-apache-hpa     Deployment/php-apache  70%/50%     1         5         4
```

---

## 🧹 Cleanup

```bash
kubectl delete -f hpa.yaml
kubectl delete -f hpa-deployment.yaml
```

---

## 📌 Summary

| Feature        | Description                      |
| -------------- | -------------------------------- |
| Deployment     | php-apache with CPU requests     |
| HPA            | Scales from 1–5 based on 50% CPU |
| Load test      | `wget` loop in busybox           |
| Metrics Server | Required for HPA to function     |

---

Happy Autoscaling! ⚙️📈


