# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.route_table
~~~~~~~~~~~~~~~~~~~
description of route_table

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("routetable")
class RouteTableWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("ec2")

    @property
    def _route_table_id(self) -> str:
        return self.context.responseElements.routeTable.routeTableId

    def execute(self, owner_name, create_date,project_name):
        self._client.create_tags(
            Resources=[self._route_table_id],
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'project', 'Value': project_name}]
        )

        return {'routetable': self._route_table_id}
