# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.worker.services.s3_worker
~~~~~~~~~~~~~~~~~~~
Tag worker for s3

:license: MIT, see LICENSE for more details.
"""
from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("s3")
class S3Worker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("s3")

    @property
    def _bucket_name(self) -> str:
        return self.context.requestParameters.bucketName

    def execute(self, owner_name, create_date,code_name):
        self._client.put_bucket_tagging(
            Bucket=self._bucket_name,
            Tagging={
                'TagSet': [
                    {'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'code', 'Value': code_name}
                ]
            }
        )

        return {'s3bucket': self._bucket_name}
