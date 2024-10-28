# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.dynamodb
~~~~~~~~~~~~~~~~~~~
description of dynamodb

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("dynamodb")
class DynamoDBWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("dynamodb")

    @property
    def _table_arn(self) -> str:
        return self.context.responseElements.tableDescription.tableArn

    def execute(self, owner_name, create_date,code_name):
        self._client.tag_resource(
            ResourceArn=self._table_arn,
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'code', 'Value': code_name}]
        )

        return {'dynamodb': self._table_arn}
