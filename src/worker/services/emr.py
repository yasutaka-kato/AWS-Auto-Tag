# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.emr
~~~~~~~~~~~~~~~~~~~
description of emr

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("emr")
class EMRWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("emr")

    @property
    def _emr_id(self) -> str:
        return self.context.responseElements.jobFlowId

    def execute(self, owner_name, create_date):
        self._client.add_tags(
            ResourceId=self._emr_id,
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date}]
        )

        return {'emr': self._emr_id}
