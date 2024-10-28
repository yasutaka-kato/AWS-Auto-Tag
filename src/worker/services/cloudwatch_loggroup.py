# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.cloudwatch_rule
~~~~~~~~~~~~~~~~~~~
description of cloudwatch_rule

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("cloudwatchloggroup")
class CloudWatchLogGroupWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("logs")

    @property
    def _log_group_name(self) -> str:
        return self.context.requestParameters.logGroupName

    def execute(self, owner_name, create_date,code_name):
        self._client.tag_log_group(
            logGroupName=self._log_group_name,
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'code', 'Value': code_name}]
        )

        return {'cloudwatch:loggroup': self._log_group_name}
