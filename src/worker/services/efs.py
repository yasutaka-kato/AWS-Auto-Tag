# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.efs
~~~~~~~~~~~~~~~~~~~
description of efs

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("efs")
class EFSWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("efs")

    @property
    def _filesystem_id(self) -> str:
        return self.context.responseElements.fileSystemId

    def execute(self, owner_name, create_date,code_name):
        self._client.tag_resource(
            ResourceId=self._filesystem_id,
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'code', 'Value': code_name}]
        )

        return {'efs': self._filesystem_id}
