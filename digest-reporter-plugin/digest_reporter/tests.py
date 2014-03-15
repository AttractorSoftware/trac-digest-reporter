# coding: utf-8

import unittest
from datetime import datetime
from trac.test import Mock
from trac.ticket import Ticket
from digest_reporter.main import Report, ReportBuilder


class Environment(object):
    pass


class TestReportBuilder(unittest.TestCase):
    def test_me(self):
        data_source = Mock()
        report_builder = ReportBuilder()
        report_builder.set_data_source(data_source)
        report = report_builder.get_report()
        assert report != None


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
