# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.subnet
~~~~~~~~~~~~~~~~~~~
description of subnet

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("subnet")
class SubnetWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("ec2")

    @property
    def _subnet_id(self) -> str:
        return self.context.responseElements.subnet.subnetId

    def execute(self, owner_name, create_date,code_name):
        self._client.create_tags(
            Resources=[self._subnet_id],
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'code', 'Value': code_name}]
        )

        return {'subnet': self._subnet_id}
