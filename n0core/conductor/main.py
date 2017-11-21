from n0core.lib.n0mq import N0MQ
from n0core.config import config


n0mq = N0MQ(config['pulsar']['service_url'])
consumer = n0mq.subscribe(config['pulsar']['conductor_topic'])


@consumer.on('SomeRequest')
def on_request(message):
    pass


def main():
    n0mq.listen()


if __name__ == '__main__':
    main()
