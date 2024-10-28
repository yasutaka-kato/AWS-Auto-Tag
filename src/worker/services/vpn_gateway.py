# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.vpn_gateway
~~~~~~~~~~~~~~~~~~~
description of vpn_gateway

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("vpngateway")
class VPNGatewayWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("ec2")

    @property
    def _gateway_id(self) -> str:
        return self.context.responseElements.vpnGateway.vpnGatewayId

    def execute(self, owner_name, create_date,code_name):
        self._client.create_tags(
            Resources=[self._gateway_id],
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'code', 'Value': code_name}]
        )

        return {'vpngateway': self._gateway_id}
