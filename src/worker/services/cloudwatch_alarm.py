# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.cloudwatch_alarm
~~~~~~~~~~~~~~~~~~~
description of cloudwatch_alarm

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("cloudwatchalarm")
class CloudWatchAlarmWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("cloudwatch")

    @property
    def _alarm_arn(self) -> str:
        arn = ['arn', self._aws_id, 'cloudwatch',
               self._aws_region,
               self._account_id,
               'alarm',
               self.context.requestParameters.alarmName]
        return ':'.join(arn)

    def execute(self, owner_name, create_date,code_name):
        self._client.tag_resource(
            ResourceARN=self._alarm_arn,
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'code', 'Value': code_name}]
        )

        return {'cloudwatch:alarm': self._alarm_arn}
