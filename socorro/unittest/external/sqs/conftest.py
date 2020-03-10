# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from socorro.unittest.external.sqs import get_sqs_config, SQSHelper


@pytest.yield_fixture
def sqs_helper():
    config = get_sqs_config()
    with SQSHelper(config) as sqs:
        yield sqs
