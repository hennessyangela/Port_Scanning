import random
from censys.search import CensysHosts
API_ID='5b3a045d-903b-4d29-99b3-a7af51be9ac7'
api_secret='ied0oG1T2SdPkN6Q4mw0QHoRe5oIhLHX'
c = CensysHosts(API_ID, api_secret)
#c = censys.ipv4.CensysIPv4(api_id="5b3a045d-903b-4d29-99b3-a7af51be9ac7", api_secret="ied0oG1T2SdPkN6Q4mw0QHoRe5oIhLHX")
def get_random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

for i in range(2):

    ip=get_random_ip()
    print(ip+'\n')
    output=c.search("ip:"+ip)
    print(output)
