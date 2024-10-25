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


@Worker.register("cloudwatchrule")
class CloudWatchRuleWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("events")

    @property
    def _rule_arn(self) -> str:
        return self.context.responseElements.ruleArn

    def execute(self, owner_name, create_date,project_name):
        self._client.tag_resource(
            ResourceARN=self._rule_arn,
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'project', 'Value': project_name}]
        )

        return {'cloudwatch:rule': self._rule_arn}
