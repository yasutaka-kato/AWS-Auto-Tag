# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.customer_gateway
~~~~~~~~~~~~~~~~~~~
description of customer_gateway

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("customergateway")
class CustomerGatewayWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("ec2")

    @property
    def _gateway_id(self) -> str:
        return self.context.responseElements.customerGateway.customerGatewayId

    def execute(self, owner_name, create_date,project_name):
        self._client.create_tags(
            Resources=[self._gateway_id],
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'project', 'Value': project_name}]
        )

        return {'customergateway': self._gateway_id}
