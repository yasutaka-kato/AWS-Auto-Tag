# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.autoscaling
~~~~~~~~~~~~~~~~~~~
description of autoscaling

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("autoscaling")
class AutoScalingWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("autoscaling")

    @property
    def _autoscaling_group_name(self) -> str:
        return self.context.requestParameters.autoScalingGroupName

    def execute(self, owner_name, create_date):
        self._client.create_or_update_tags(
            Tags=[
                {
                    'Key': 'owner',
                    'Value': owner_name,
                    'ResourceId': self._autoscaling_group_name,
                    'ResourceType': 'auto-scaling-group',
                    'PropagateAtLaunch': False,
                },
                {
                    'Key': 'create',
                    'Value': create_date,
                    'ResourceId': self._autoscaling_group_name,
                    'ResourceType': 'auto-scaling-group',
                    'PropagateAtLaunch': False,
                }
            ]
        )

        return {'autoscaling': self._autoscaling_group_name}
