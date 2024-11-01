# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.rds
~~~~~~~~~~~~~~~~~~~
description of rds

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("rds")
class RDSWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("rds")

    @property
    def _db_arn(self) -> str:
        if self.context.responseElements.dBInstanceArn is not None:
            return self.context.responseElements.dBInstanceArn

        arn = ['arn', self._aws_id, 'rds',
               self._aws_region,
               self._account_id,
               'db',
               self.context.responseElements.dBInstanceIdentifier]
        return ':'.join(arn)

    def execute(self, owner_name, create_date,code_name):
        self._client.add_tags_to_resource(
            ResourceName=self._db_arn,
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'code', 'Value': code_name}]
        )

        return {'rds': self._db_arn}
