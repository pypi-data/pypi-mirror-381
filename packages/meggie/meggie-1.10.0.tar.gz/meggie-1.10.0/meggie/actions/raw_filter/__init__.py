"""Contains implementation for raw filter"""

from meggie.utilities.threading import threaded

from meggie.actions.raw_filter.dialogs.filterDialogMain import FilterDialog
from meggie.actions.raw_filter.controller.filter import filter_data

from meggie.mainwindow.dynamic import Action
from meggie.mainwindow.dynamic import subject_action


class Filter(Action):
    """Shows a dialog for getting parameters and allows
    filtering the raw data.
    """

    def run(self, params={}):
        filter_dialog = FilterDialog(self.window, self.experiment, self.handler)
        filter_dialog.show()

    @subject_action
    def handler(self, subject, params):
        """ """

        @threaded
        def filter_fun():
            filter_data(subject, params)

        filter_fun(do_meanwhile=self.window.update_ui)
