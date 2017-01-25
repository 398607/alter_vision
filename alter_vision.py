import requests

class AlterVision(object):

    host_url = 'http://nagizero.me:8000/alter_vision/'
    api_start = host_url + 'start'
    api_send = host_url + 'send'

    def __init__(self):
        r = requests.post(AlterVision.api_start)
        print r.status_code

    def vision(self, msg):
        values = {
            'msg': msg
        }
        r = requests.post(AlterVision.api_send, data=values)
        print r.status_code

if __name__ == '__main__':
    alter = AlterVision()
    alter.vision('remote test 1')
    alter.vision('remote test 2')
    alter.vision('remote test 3')
