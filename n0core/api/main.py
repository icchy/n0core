from flask import Flask
from uuid import uuid4 as uuid

from n0core.lib.n0mq import N0MQ
from n0core.config import config
from n0core.lib.proto import Request, VM, Volume


app = Flask("api")

n0mq = N0MQ(config['pulsar']['service_url'])
producer_scheduler = n0mq.create_producer(config['pulsar']['scheduler_topic'])


@app.route('/')
def test():
    req = Request()

    vm = req.object.VM
    vm.state = VM.STARTED
    vm.arch = 'amd64'
    vm.vcpus = 1
    vm.memory_mb = 512
    vm.vnc_password = 'test'

    vol = req.object.relations.add().object.Volume
    vol.state = Volume.CLAIMED
    vol.volume_type = 'file'
    vol.size_mb = 1024
    vol.url = ''

    producer_scheduler.send(req)

    return '', 200


def main():
    app.run()

if __name__ == '__main__':
    main()
