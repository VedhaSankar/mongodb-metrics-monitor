# mongodb-metrics-monitor
Use prometheus and k8s to monitor the metrics in K8s.


```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install mongodb-exporter prometheus-community/prometheus-mongodb-exporter
```

prom-aggregation-gateway

https://github.com/prometheus/client_python
https://www.youtube.com/watch?v=HzEiRwJP6ag