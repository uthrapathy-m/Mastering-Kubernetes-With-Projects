Here's the complete installation and setup guide for **Minikube**, **Docker**, and **kubectl**, suitable for both **Windows**, **Linux**, and **macOS** 🛠️

---

# 🚀 Full Setup Guide for Minikube + Docker + kubectl

This guide walks you through:

1. ✅ Installing `kubectl`
2. 🐳 Installing Docker (for Minikube driver)
3. 🏗️ Installing Minikube
4. 🚦 Starting your first Minikube cluster
5. 🧪 Verifying setup

---

## ✅ 1. Install `kubectl` (Kubernetes CLI)

### 📦 On Linux

```bash
curl -LO "https://dl.k8s.io/release/$(curl -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client
```

### 🪟 On Windows (PowerShell)

```powershell
choco install kubernetes-cli
kubectl version --client
```

### 🍎 On macOS (Homebrew)

```bash
brew install kubectl
kubectl version --client
```

---

## 🐳 2. Install Docker

### 📦 On Linux (Ubuntu)

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) \
  signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" |
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
sudo usermod -aG docker $USER
newgrp docker
```

### 🪟 On Windows or 🍎 macOS

* Download **Docker Desktop** from: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
* Enable WSL 2 on Windows if needed
* Verify:

```bash
docker version
```

---

## 🏗️ 3. Install Minikube

### 📦 On Linux

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

### 🪟 On Windows

```powershell
choco install minikube
```

### 🍎 On macOS

```bash
brew install minikube
```

---

## 🚦 4. Start Minikube with Docker Driver

```bash
minikube start --driver=docker
```

If you're on Windows using VirtualBox or Hyper-V:

```bash
minikube start --driver=virtualbox
```

---

## 📋 5. Basic Minikube Commands

| Command                       | Purpose                 |
| ----------------------------- | ----------------------- |
| `minikube start`              | Start cluster           |
| `minikube status`             | Check status            |
| `minikube dashboard`          | Launch GUI dashboard    |
| `kubectl get nodes`           | Show running nodes      |
| `kubectl get pods -A`         | Show all pods           |
| `minikube service <svc-name>` | Open service in browser |
| `minikube stop`               | Stop cluster            |
| `minikube delete`             | Delete cluster          |

---

## ✅ Verify Installation

Run:

```bash
kubectl get nodes
```

Expected output:

```
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   Xs    vX.Y.Z
```

---

## 📎 Optional Addons

```bash
minikube addons enable metrics-server
minikube addons enable dashboard
```

Then open dashboard:

```bash
minikube dashboard
```

---

## 🎉 You're Ready!

Your Kubernetes lab is now live locally with:

* 📦 Docker
* 🧠 Minikube
* 💻 kubectl CLI


