# LLM Service Configuration

Configuration files and deployment manifests for the LLM service.

## Local deployment

Use MiniKube to deploy a local development cluster and install the required addons:

```bash
minikube start

minikube addons enable ingress        # Enables routing of external traffic into the cluster
minikube addons enable ingress-dns    # Provides DNS resolution for ingress hostnames
minikube addons enable metrics-server # Supplies resource metrics for monitoring and autoscaling
```

Apply the manifest project manifest files.

```bash
kubectl apply -f manifest/**/*.yml 
```

Monitor the deployed resources from the kubernetes dashboard.

```bash
minikube dashboard
```
