kubectl create namespace retail
minikube addons enable ingress
minikube ip

for redeploy images

# Restart a specific deployment
kubectl rollout restart deployment/product-deployment -n retail

# Or, restart all deployments in your namespace at once
kubectl rollout restart deployment -n retail

istio:

https://freedium.cfd/https://harsh05.medium.com/understanding-istio-security-peer-authentication-and-mtls-for-microservices-d1fd1ef60d55
https://minimaldevops.com/mastering-mtls-in-kubernetes-25a762b58d90

curl -L https://istio.io/downloadIstio | sh -
cd istio-*
export PATH=$PWD/bin:$PATH

istioctl install --set profile=demo -y

# enable istio injection in containers
minikube kubectl -- label namespace retail istio-injection=enabled

# add some test services
minikube kubectl -- apply -f https://raw.githubusercontent.com/istio/istio/release-1.26/samples/httpbin/httpbin.yaml -n retail
minikube kubectl -- apply -f https://raw.githubusercontent.com/istio/istio/release-1.26/samples/curl/curl.yaml -n retail

# test services could connect each other
for from in "retail"; do for to in "retail"; do minikube kubectl -- exec "$(minikube kubectl -- get pod -l app=curl -n ${from} -o jsonpath={.items..metadata.name})" -c curl -n ${from} -- curl http://httpbin.${to}:8000/ip -s -o /dev/null -w "curl.${from} to httpbin.${to}: %{http_code}\n"; done; done

minikube kubectl -- get peerauthentication --all-namespaces #check peer auth in cluster

# Create and apply a PeerAuthentication policy to enforce mTLS on retiail namespace
minikube kubectl -- apply -f k8s-manifests/istio-mtls-policy.yaml

istio dashboard kiali
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.26/samples/addons/kiali.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.26/samples/addons/prometheus.yaml
expose kiali
minikube kubectl -- port-forward svc/kiali 20001:20001 -n istio-system
to check mtls:

istioctl ps (all should be SYNCED)

find istio ingress IP
      
minikube service istio-ingressgateway -n istio-system --url

istioctl analyze -n retail