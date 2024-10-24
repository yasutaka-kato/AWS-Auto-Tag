# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.vpc
~~~~~~~~~~~~~~~~~~~
description of vpc

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("vpc")
class VPCWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("ec2")

    @property
    def _vpc_id(self) -> str:
        return self.context.responseElements.vpc.vpcId

    def execute(self, owner_name, create_date):
        self._client.create_tags(
            Resources=[self._vpc_id],
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date}]
        )

        return {'vpc': self._vpc_id}
