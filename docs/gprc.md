To get into the pod container:
```bash
POD_NAME=$(kubectl get pods | grep -i "api-locations-producer*" | awk '{print $1}')
kubectl exec -it "$POD_NAME" -- bash
```

To run the gRPC client test command:
```bash
python app/send_test_msg.py
```