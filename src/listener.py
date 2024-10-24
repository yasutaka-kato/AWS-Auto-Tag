# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.listener
~~~~~~~~~~~~~~~~~~~
The lambda listener of AutoTag

:license: MIT, see LICENSE for more details.
"""

import logging
import json
import os

from config import load_config
from evals import eval_exp, eval_condition
from worker import *

if os.getenv("EnableLog", "True").lower() == "true":
    logging.getLogger().setLevel(logging.INFO)

logger = logging.getLogger(__name__)


def lambda_handler(evt, _):
    logger.info('Event received: %s' % json.dumps(evt))

    evt_dict = DictX(evt)
    detail = evt.get('detail', dict())
    event_name = detail.get('eventName', None)  # get the event name
    owner_name = detail.get('userIdentity',{}).get('arn', None)
    create_date = detail.get('eventTime', None)
    config = load_config()

    for t in config.triggers:
        if event_name in t.events:

            if not Worker.is_registered(t.service):
                logger.info('Trigger worker not register: %s', t.service)
                continue

            logger.info('Trigger matched: %s-%s Owner: %s Date: %s' % (t.service, event_name,owner_name,create_date))

            worker = Worker.by_name(t.service)(detail)
            targets = worker.execute(owner_name,create_date)

            if len(targets) == 0:
                logger.warning('Execute canceled: no target(s) to tag')
                return

            logger.info('Execute finished: target - %s, tags - %s' % (json.dumps(targets), json.dumps(tags)))
            return

    logger.info('Execute exited: no matched/actived trigger')
