from flask import Flask

try:
    from n0core.lib.n0mq import N0MQ
    from n0core.config import config
except:
    import sys
    sys.path.append('../../')
    from n0core.lib.n0mq import N0MQ
    from n0core.config import config

from n0core.lib.proto import CreateVolumeRequest


app = Flask("api")

n0mq = N0MQ(config['pulsar']['service_url'])
producer_scheduler = n0mq.create_producer(config['pulsar']['scheduler_topic'])


@app.route('/')
def test():
    req = CreateVolumeRequest(id="hoge", host="host")
    producer_scheduler.send(req)
    return '', 200


if __name__ == '__main__':
    app.run()
