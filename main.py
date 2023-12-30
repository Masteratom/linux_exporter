from prometheus_client import start_http_server, Gauge, Counter
import socket
import time
import random
from CPU_metrics import CPUMETRICSE
from System import System


class Metrics(CPUMETRICSE, System):
    def __init__(self):
        host = socket.gethostname()
        self.cpu_metrics = Gauge("linux_exporter_cpu_usage_percent", "CPU usage percent.")
        self.uptime = Gauge("linux_exporter_uptime", "Uptime system")

    def man(self):
        #self.load_cpu()
        self.uptime.set(value=self.uptime_system())


if __name__ == '__main__':
    start_http_server(8000)
    metrics = Metrics()

    while True:
        time.sleep(1)
        metrics.man()