from trac.core import *
from trac.admin import IAdminCommandProvider
from trac.util.text import print_table, printout


class DigestReportSender(Component):
    implements(IAdminCommandProvider)

    # IAdminCommandProvider methods

    greetings = ['hi', 'hello', 'salut', 'hola', 'ciao']

    def get_admin_commands(self):
        yield ('digest info', '',
               'show digest status information',
               None, self._display_status)
        yield ('digest send', '',
               'Sends digest reports to configured emails',
               None, self._send_digest_reports)

    def _display_status(self):
        print "Env is " + self.env
        print_table([self.greetings])

    def _complete_greeting(self, args):
        return self.greetings

    def _send_digest_reports(self):
        printout(self.greetings)


class Report(object):
    def __init__(self):
        self._tickets = []

    @property
    def tickets(self):
        return self._tickets

    def add_ticket(self, ticket):
        self._tickets.append(ticket)


class ReportBuilder(object):
    def add(self, ticket):
        pass

    def get_report(self):
        last_run_time = self._data_source.get_last_run_time()
        ticket_changes = self._data_source.get_ticket_changes(last_run_time, self._start_time)
        tickets = set([ticket_change.ticket for ticket_change in ticket_changes])
        self._data_source.get_tickets(tickets)
        return Report()

    def set_data_source(self, data_source):
        self._data_source = data_source

    def set_start_time(self, start_time):
        self._start_time = start_time