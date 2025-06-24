 **Kubernetes Metrics Server with Resource Requests & Limits in Minikube**

---


# 📊 Kubernetes Metrics Server with Resource Requests & Limits (Minikube)

This guide explains how to install the **Metrics Server** on **Minikube** and configure pod-level **resource requests and limits**. It also demonstrates how to simulate CPU load to observe metrics using `kubectl top`.

---

## ✅ Prerequisites

- ✅ Minikube installed and running
- ✅ `kubectl` CLI configured

Start Minikube if it’s not running:

```bash
minikube start
````

---

## 🔧 Step 1: Enable Metrics Server

Enable Metrics Server addon in Minikube:

```bash
minikube addons enable metrics-server
```

Verify it's working:

```bash
kubectl get deployment metrics-server -n kube-system
kubectl top nodes
```

---

## ⚙️ Step 2: Create a Deployment with Resource Requests & Limits

Create a file named `resource-demo.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: resource-demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: resource-demo
  template:
    metadata:
      labels:
        app: resource-demo
    spec:
      containers:
      - name: demo-container
        image: nginx
        resources:
          requests:
            memory: "64Mi"
            cpu: "100m"
          limits:
            memory: "128Mi"
            cpu: "250m"
```

Apply the deployment:

```bash
kubectl apply -f resource-demo.yaml
```

---

## 📈 Step 3: View Resource Usage

After a few seconds, run:

```bash
kubectl top pods
kubectl describe pod -l app=resource-demo
```

You'll see current CPU and memory usage of the pod.

---

## 🔥 Step 4: Simulate CPU Load

Run a CPU stress pod using BusyBox:

```bash
kubectl run cpu-loader --image=busybox --restart=Never -it -- /bin/sh
```

Inside the pod shell, start infinite CPU loop:

```sh
while true; do :; done
```

Leave it running. Then in another terminal:

```bash
kubectl top pods
```

📊 **Example output:**

```
NAME           CPU(cores)   MEMORY(bytes)
cpu-loader     99m          0Mi
resource-demo  3m           5Mi
```

This confirms CPU stress is active and metrics are being collected.

---

## 🧹 Cleanup

```bash
kubectl delete -f resource-demo.yaml
kubectl delete pod cpu-loader
```

---

## 📌 Summary

| Concept       | Description                                      |
| ------------- | ------------------------------------------------ |
| `requests`    | Guaranteed resources Kubernetes reserves for pod |
| `limits`      | Maximum the pod is allowed to consume            |
| `kubectl top` | Shows real-time metrics (needs Metrics Server)   |
| `busybox`     | Used to simulate CPU load                        |

---

## 📚 Resources

* [Metrics Server Docs](https://github.com/kubernetes-sigs/metrics-server)
* [Resource Management in Kubernetes](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)

---

Happy Monitoring! 🚦📈


