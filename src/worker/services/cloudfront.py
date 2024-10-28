# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.cloudfront
~~~~~~~~~~~~~~~~~~~
description of cloudfront

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("cloudfront")
class CloudFrontWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("cloudfront")

    @property
    def _arn(self) -> str:
        return self.context.responseElements.distribution.aRN

    def execute(self, owner_name, create_date,code_name):
        self._client.tag_resource(
            Resource=self._arn,
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'code', 'Value': code_name}]
        )

        return {'cloudfront': self._arn}
