from flask import Flask

from os.path import join, dirname, abspath
import configparser

try:
    from n0core.lib.n0mq import N0MQ
except:
    import sys
    sys.path.append('../../')
    from n0core.lib.n0mq import N0MQ

from n0core.lib.proto import CreateVolumeRequest


app = Flask("api")

# read config.ini
config = configparser.ConfigParser()
config.read(join(dirname(abspath(__file__)), '..', 'config.ini'))

n0mq = N0MQ(config['pulsar']['service_url'])
producer_scheduler = n0mq.create_producer(config['pulsar']['scheduler_topic'])


@app.route('/')
def test():
    req = CreateVolumeRequest(id="hoge", host="host")
    producer_scheduler.send(req)
    return '', 200


if __name__ == '__main__':
    app.run()
