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
    def setUp(self):
        self._start_time = _minutes_ago(0)
        self.get_last_run_time = _minutes_ago(10)
        self.data_source = Mock(
            get_last_run_time=lambda: self.get_last_run_time,
        )
        self.data_source.get_ticket_changes = MagicMock(return_value=[])
        self.data_source.get_tickets = MagicMock(return_value=[])
        self.report_builder = ReportBuilder()
        self.report_builder.set_data_source(self.data_source)
        self.report_builder.set_start_time(self._start_time)

    def test_requests_changes_from_data_source(self):
        self.data_source.get_ticket_changes = MagicMock(return_value=[])
        report = self.report_builder.get_report()
        self.data_source.get_ticket_changes.assert_called_once_with(self.get_last_run_time, self._start_time)

    def test_requests_ticket_that_were_changed(self):
        change23 = Mock(ticket=23)
        change34 = Mock(ticket=34)
        self.data_source.get_ticket_changes = MagicMock(return_value=[change23, change34])
        ticket23 = Mock()
        ticket34 = Mock()
        self.data_source.get_tickets = MagicMock(return_value=[ticket23, ticket34])
        report = self.report_builder.get_report()
        self.data_source.get_ticket_changes.assert_called_once_with(self.get_last_run_time, self._start_time)
        self.data_source.get_tickets.assert_called_once_with({23, 34})


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
