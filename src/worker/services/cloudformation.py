# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.cloudformation
~~~~~~~~~~~~~~~~~~~
description of cloudformation

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("cloudformation")
class CloudFormationWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("cloudformation")

    @property
    def _stack_name(self) -> str:
        return self.context.requestParameters.stackName

    def execute(self, owner_name, create_date,code_name):
        self._client.update_stack(
            StackName=self._stack_name,
            UsePreviousTemplate=True,
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'code', 'Value': code_name}]
        )

        return {'cloudformation': self._stack_name}
