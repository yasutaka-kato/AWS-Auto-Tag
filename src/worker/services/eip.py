# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.eip
~~~~~~~~~~~~~~~~~~~
description of eip

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("eip")
class EIPWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("ec2")

    @property
    def _allocation_id(self) -> str:
        return self.context.responseElements.allocationId

    def execute(self, owner_name, create_date):
        self._client.create_tags(
            Resources=[self._allocation_id],
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date}]
        )

        return {'eip': self._allocation_id}
