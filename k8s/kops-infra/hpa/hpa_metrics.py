import subprocess
import datetime
import json
import boto3

current_time = datetime.datetime.now()
metric_data = []


class PostMetricError(Exception):
    pass


def shell(command):
    p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    return p.communicate()[0]


def calc_hpa_percentage(max_pods=None, current=None):
    utilization = 100 * (float(current) / float(max_pods))
    return round(utilization, 2)


def add_metric_data(desired_pods=None, max_pods=None, min_pods=None, current_pods=None, hpa_name=None):
    utilization = calc_hpa_percentage(max_pods=max_pods, current=current_pods)
    metric_data.extend([
        {
            'MetricName': 'hpa_utilization',
            'Dimensions': [
                {
                    'Name': 'hpa_name',
                    'Value': hpa_name
                },
            ],
            'Unit': 'Percent',
            'Value': utilization
        },
        {
            'MetricName': 'hpa_desired_state',
            'Dimensions': [
                {
                    'Name': 'hpa_name',
                    'Value': hpa_name
                },
            ],
            'Unit': 'Count',
            'Value': float(desired_pods)
        },
        {
            'MetricName': 'hpa_min_pods',
            'Dimensions': [
                {
                    'Name': 'hpa_name',
                    'Value': hpa_name
                },
            ],
            'Unit': 'Count',
            'Value': float(min_pods)
        },
        {
            'MetricName': 'hpa_max_pods',
            'Dimensions': [
                {
                    'Name': 'hpa_name',
                    'Value': hpa_name
                },
            ],
            'Unit': 'Count',
            'Value': float(max_pods)
        },
        {
            'MetricName': 'hpa_current_pods',
            'Dimensions': [
                {
                    'Name': 'hpa_name',
                    'Value': hpa_name
                },
            ],
            'Unit': 'Count',
            'Value': float(current_pods)
        },
    ])


def add_hpa_metric(metric_namespace=None, metric_list=None):
    metric_namespace = metric_namespace
    response = client.put_metric_data(
        MetricData=metric_list,
        Namespace=metric_namespace
    )
    if not response:
        raise PostMetricError("Cannot communicate CloudWatch service")
    else:
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print "Custom metrics uploaded successfully"
        else:
            raise PostMetricError("An error occurred while posting metrics data")


def get_hpa_data(k8s_namespace='production'):
    hpa_cmd = "kubectl get hpa -n {0} --output=json".format(k8s_namespace)
    results = json.loads(shell(hpa_cmd))
    hpa_items = results["items"]
    for hpa in hpa_items:
        name = hpa["metadata"]["name"]
        current_replica = hpa["status"]["currentReplicas"]
        desired_replicas = hpa["status"]["desiredReplicas"]
        max_replicas = hpa["spec"]["maxReplicas"]
        min_replicas = hpa["spec"]["minReplicas"]

        add_metric_data(hpa_name=name, current_pods=current_replica, desired_pods=desired_replicas,
                        max_pods=max_replicas, min_pods=min_replicas)
    add_hpa_metric(metric_namespace="EKS/HPA", metric_list=metric_data)


if __name__ == "__main__":
    client = boto3.client("cloudwatch")
    get_hpa_data()
    # count = 1
    # while count < 20:
    #     import random
    #
    # add_hpa_metric(desired_pods='6', min_pods='1', max_pods=str(random.randint(6, 10)),
    #                current_pods=str(random.randint(1, 6)), hpa_name="test123")
#     count += 1
#     time.sleep(60)

