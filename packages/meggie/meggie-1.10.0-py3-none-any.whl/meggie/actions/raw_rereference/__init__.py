"""Contains implementation for raw rereference"""

from meggie.utilities.threading import threaded

from meggie.actions.raw_rereference.dialogs.rereferencingDialogMain import (
    RereferencingDialog,
)

from meggie.mainwindow.dynamic import Action
from meggie.mainwindow.dynamic import subject_action


class Rereference(Action):
    """Shows a dialog and then allows rereferencing eeg data."""

    def run(self, params={}):
        rereference_dialog = RereferencingDialog(
            self.window, self.experiment, self.handler
        )
        rereference_dialog.show()

    @subject_action
    def handler(self, subject, params):
        """ """

        @threaded
        def rereference_fun():
            raw = subject.get_raw()
            raw = raw.set_eeg_reference(
                ref_channels=params["selection"],
                projection=False,
            )

        rereference_fun(do_meanwhile=self.window.update_ui)
        subject.rereferenced = True
        subject.save()
        self.experiment.save_experiment_settings()
