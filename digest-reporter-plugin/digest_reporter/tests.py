# coding: utf-8

import unittest
from datetime import datetime, timedelta
from trac.test import Mock
from trac.ticket import Ticket
from digest_reporter.main import Report, ReportBuilder
from mock import MagicMock

class Environment(object):
    pass


class TestReportBuilder(unittest.TestCase):
    def test_me(self):
        last_run_time = _minutes_ago(10)
        ticket_change_time = _minutes_ago(1)
        now = _minutes_ago(0)
        data_source = Mock(
            get_last_run_time = lambda : last_run_time,
        )
        data_source.get_ticket_changes = MagicMock(return_value = [])
        report_builder = ReportBuilder()
        report_builder.set_data_source(data_source)
        report_builder.set_start_time(now)
        report = report_builder.get_report()
        assert report != None
        data_source.get_ticket_changes.assert_called_once_with(last_run_time, now)


def _minutes_ago(minutes):
    return datetime.now() - timedelta(minutes=minutes)


class TestReport(unittest.TestCase):

    def test_can_add_ticket_change(self):
        ticket = Mock(summary="asdf")
        report = Report()
        report.add_ticket(ticket)
        assert report.tickets[0].summary == 'asdf'


class TestTracMocks(unittest.TestCase):
    def test_setting_property(self):
        ticket = Mock(type="defect")
        assert ticket.type == "defect"

    def test_mock_can_use_local_values(self):
        name = "the name"
        ticket = Mock(get_name=lambda: name)
        assert ticket.get_name() == "the name"
