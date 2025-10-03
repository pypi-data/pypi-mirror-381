"""Contains implementation for raw montage"""

import mne

from meggie.utilities.threading import threaded

from meggie.actions.raw_montage.dialogs.montageDialogMain import MontageDialog

from meggie.mainwindow.dynamic import Action
from meggie.mainwindow.dynamic import subject_action


class Montage(Action):
    """Shows a dialog for gathering parameters and then
    allows setting montage for EEG.
    """

    def run(self, params={}):
        montage_dialog = MontageDialog(self.window, self.experiment, self.handler)
        montage_dialog.show()

    @subject_action
    def handler(self, subject, params):
        """ """

        @threaded
        def montage_fun():
            """ """
            head_size = params["head_size"]

            if params["custom"] is True:
                montage_fname = params["selection"]
                montage = mne.channels.read_custom_montage(
                    montage_fname, head_size=head_size
                )
            else:
                montage_name = params["selection"]
                montage = mne.channels.make_standard_montage(
                    montage_name, head_size=head_size
                )

            if subject.has_raw:
                raw = subject.get_raw()
                raw.set_montage(montage)

            subject.save_montage(montage)
            subject.save()

        montage_fun(do_meanwhile=self.window.update_ui)
