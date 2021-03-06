from unittest import mock

import pytest
from patrol.patrol import Patrol


@pytest.fixture
def patrol():
    patrol = Patrol('TOKEN')
    patrol.api = mock.Mock()
    return patrol


def test_events(patrol):
    events_mock = mock.Mock()
    patrol.events = events_mock
    patrol.events('organization', 'project')
    assert events_mock.called
