# Speedtester

This is a tool to constantly poll and output the speedtest results.

This will be used in conjunction with splunk to provide historical data on internet speeds.

# Setup

1. You'll need to install [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/)
2. You'll need a working a splunk environment.
3. From the splunk environment, generate an HTTP Event Token and replace the `splunk-token: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX` with your token in `docker-compose.yml`


# Usage

1. Clone the repository
2. Use `docker-compose up -d --build` to build and deploy the script. Adjust the interval the speedtest is run at in the docker-compose file.