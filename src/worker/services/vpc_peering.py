# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.vpc_peering
~~~~~~~~~~~~~~~~~~~
description of vpc_peering

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("vpcpeering")
class VPCPeeringWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("ec2")

    @property
    def _peering_id(self) -> str:
        return self.context.responseElements.vpcPeeringConnection.vpcPeeringConnectionId

    def execute(self, owner_name, create_date,code_name):
        self._client.create_tags(
            Resources=[self._peering_id],
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'code', 'Value': code_name}]
        )

        return {'vpcpeering': self._peering_id}
