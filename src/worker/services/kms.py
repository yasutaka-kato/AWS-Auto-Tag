# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.kms
~~~~~~~~~~~~~~~~~~~
description of kms

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("kms")
class KMSWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("kms")

    @property
    def _key_id(self) -> str:
        return self.context.requestParameters.keyId

    def execute(self, owner_name, create_date,project_name):
        self._client.tag_resource(
            KeyId=self._key_id,
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'project', 'Value': project_name}]
        )

        return {'kms': self._key_id}
