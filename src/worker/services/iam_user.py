# -*- coding: utf-8 -*-

"""
AWS-Auto-Tag.iam_user
~~~~~~~~~~~~~~~~~~~
description of iam_user

:license: MIT, see LICENSE for more details.
"""

from __future__ import annotations

import boto3
from worker.worker import Worker


@Worker.register("iamuser")
class IAMUserWorker(Worker):
    @property
    def _client(self) -> any:
        return boto3.client("iam")

    @property
    def _user_name(self) -> str:
        return self.context.responseElements.user.userName

    def execute(self, owner_name, create_date,project_name):
        self._client.tag_user(
            RoleName=self._user_name,
            Tags=[{'Key': 'owner', 'Value': owner_name},{'Key': 'create', 'Value': create_date},{'Key': 'project', 'Value': project_name}]
        )

        return {'iamuser': self._user_name}
