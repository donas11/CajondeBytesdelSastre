If you were to create your own function in Python for example, then it may look like this:
```
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    return req
```

# Triggering a Function via MQTT
[MINIO](https://min.io/)
git clone https://github.com/lftraining/mqtt-to-s3.git


# Monitoring Rate Error and Duration for Functions
kubectl port-forward -n openfaas svc/prometheus 9090:9090 & http://127.0.0.1:9090

```rate(gateway_function_invocation_total[15s])```

```
rate(gateway_function_invocation_total{
  function_name="mqtt-s3.openfaas-fn",
  code="200"
}[1m])


gateway_functions_seconds_sum / gateway_functions_seconds_count

rate(gateway_functions_seconds_sum[1m]) /
rate(gateway_functions_seconds_count[1m])
```

These PromQL queries can be pasted into a Grafana dashboard so that you and your team can monitor the status of functions and other K3s endpoints without having to interact with Prometheus directly. The OpenFaaS project offers a dashboard that can be downloaded and comes pre-populated with useful queries.