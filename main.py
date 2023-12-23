from prometheus_client import start_http_server, Gauge
import socket
import time
import random
from CPU_metrics import CPUMETRICSE


class Metrics(CPUMETRICSE):
    def __init__(self):
        host = socket.gethostname()
        self.cpu_metrics = Gauge("linux_exporter_cpu_usage_percent", "CPU usage percent.")

    def man(self):
        self.load_cpu()
        #self.cpu_metrics.set(value=random.random())


if __name__ == '__main__':
    start_http_server(8000)
    metrics = Metrics()

    while True:
        time.sleep(1)
        metrics.man()