
import re
import csv
from github import Github  #install: pip install PyGithub
import yaml #install: pip install PyYAML

with open("config.yaml", 'r') as yamlfile:
    config = yaml.load(yamlfile, Loader=yaml.FullLoader)

# import yaml  # install: pip install PyYAML


def convertlogtocsv():
    pattern = re.compile(r'(?P<ip>.*?)- - \[(?P<time>.*?)\] "(?P<request>.*?)" (?P<status>.*?) (?P<bytes>.*?)'
                         r' "(?P<referer>.*?)" "(?P<http_user_agent>.*?)" (?P<bytes_sent>\d+) (?P<upstream_response_time>\S+)'
                         r' (?P<name>.*?) (?P<unknown>\S+) (?P<server_port>\S+) (?P<upstream_bytes_received>\S+)'
                         r' (?P<time_request>\S+) (?P<https>\S+) (?P<http_cookie>.*)')  # pattern for parsing ngnix.conf
    file = open(config['full_path_to_nginx_log'])  # start parsing

    with open(config['full_path_to_export_csv_file'], 'w') as out:  # write a head of converted log
        csv_out = csv.writer(out)
        csv_out.writerow(['Host', 'Date:Time', 'Request', 'Status', 'Bytes', 'Refer_URL', 'Http_user_agent', 'Bytes_sent',
                          'Response_time', 'Service_name', 'Unknown', 'Server_with_port', 'Upstream_bytes_received',
                          'Time_request', 'Https_status', 'Http_cookie'])
        for line in file:  # compare with pattern and creating csv
            m = pattern.match(line)
            result = m.groups()
            csv_out.writerow(result)
    file.close()


def uploadtogithub():
    with open(config['full_path_to_export_csv_file'], 'r') as file:  # start uploading to GitHub
       content = file.read()
    g = Github(config['access_token'])  # access_token. You have to change it#
    repo = g.get_repo(config['repository_name'])  # GitNub repository. Paste own
    repo.create_file(config['full_path_to_export_csv_file'], "Uploading csv file", content,
                    branch=config['branch'])  # upload csv file


if __name__ == '__main__':
    convertlogtocsv()
    print ("Converting from log to csv DONE")
    uploadtogithub()
    print ("Uploading to GitHub DONE")
