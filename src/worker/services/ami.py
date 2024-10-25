# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.ami
~~~~~~~~~~~~~~~~~~~
description of ami

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("ami")
class AMIWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("ec2")

    @property
    def _image_id(self) -> str:
        return self.context.responseElements.imageId

    def execute(self, owner_name, create_date,project_name):
        self._client.create_tags(
            Resources=[self._image_id],
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'project', 'Value': project_name}]
        )

        return {'ami': self._image_id}
