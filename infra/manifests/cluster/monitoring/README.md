## Installation

NOTE: Not currently working.

```bash
kubectl apply -f namespace.yaml
helm install elasticsearch elastic/elasticsearch --values elasticsearch-values.yaml -n logging
helm install kibana elastic/kibana -n logging
kubectl apply -f fluentd-daemonset-elasticsearch.yml
```