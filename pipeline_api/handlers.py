import logging
import redis
import json


class RedisHandler(logging.Handler):
    def __init__(self, host='redis', port=6379, db=0, key='logging_queue'):
        super().__init__()
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db)
        self.key = key

    def format(self, record):
        return json.dumps(record.__dict__)

    def emit(self, record):
        try:
            log_entry = self.format(record)
            json_data = json.loads(log_entry)
            save_data = json_data['msg']
            self.redis_client.rpush(self.key, json.dumps(save_data))
        except Exception as e:
            self.handleError(record)
