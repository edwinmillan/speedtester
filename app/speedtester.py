import speedtest
import json
import os
import time


def run_speed_test():
    service = speedtest.Speedtest(secure=True)
    servers = [4795]  # Set to Teklinks Speedtest ID
    service.get_servers(servers)
    service.get_best_server()
    service.download()
    service.upload()
    results = service.results.dict()
    results['download'] = results['download'] / 1000.0 / 1000.0
    results['upload'] = results['upload'] / 1000.0 / 1000.0
    print(json.dumps(results))


def main():
    env_interval = os.getenv('INTERVAL')
    if env_interval:
        interval = env_interval
    else:
        interval = 600
    while True:
        run_speed_test()
        time.sleep(interval)


if __name__ == '__main__':
    main()
