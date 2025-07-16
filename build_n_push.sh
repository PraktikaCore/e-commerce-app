#!/bin/bash
alias kubectl="minikube kubectl --"

# docker build -t drjabber/swagger-ui-service:latest ./swagger-ui-service
# docker build -t drjabber/recommendation-service:latest ./recommendation-service
# docker build -t drjabber/user-service:latest ./user-service
# docker build -t drjabber/inventory-service:latest ./inventory-service
# docker build -t drjabber/order-service:latest ./order-service
# docker build -t drjabber/product-service:latest ./product-service

# docker push drjabber/recommendation-service:latest
# docker push drjabber/user-service:latest
# docker push drjabber/product-service:latest
# docker push drjabber/order-service:latest
# docker push drjabber/inventory-service:latest
# docker push drjabber/swagger-ui-service:latest

# minikube kubectl -- apply -f k8s-manifests/ingress.yaml
# minikube kubectl -- apply -f k8s-manifests/swagger-ingress.yaml

echo "--- Cleaning up old Ingress resources ---"
minikube kubectl -- delete ingress retail-ingress -n retail --ignore-not-found
minikube kubectl -- delete ingress swagger-retail-ingress -n retail --ignore-not-found

echo "--- Applying Kubernetes & Istio Manifests ---"
minikube kubectl -- apply -f k8s-manifests/istio-gateway.yaml
minikube kubectl -- apply -f k8s-manifests/istio-virtualservice.yaml

# Apply the mTLS policy
minikube kubectl -- apply -f k8s-manifests/istio-mtls-policy.yaml

minikube kubectl -- apply -f k8s-manifests/swagger-ui-service.yaml
minikube kubectl -- apply -f k8s-manifests/recommendation-service.yaml
minikube kubectl -- apply -f k8s-manifests/order-service.yaml
minikube kubectl -- apply -f k8s-manifests/user-service.yaml
minikube kubectl -- apply -f k8s-manifests/inventory-service.yaml
minikube kubectl -- apply -f k8s-manifests/product-service.yaml

minikube kubectl -- rollout restart deployment -n retail

minikube kubectl -- get pods -n retail