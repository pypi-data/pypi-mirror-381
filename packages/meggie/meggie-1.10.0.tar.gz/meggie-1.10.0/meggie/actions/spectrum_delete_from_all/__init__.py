"""Contains implementation for delete spectrum from all"""

import logging

from meggie.mainwindow.dynamic import Action
from meggie.mainwindow.dynamic import subject_action


class DeleteSpectrumFromAll(Action):
    """Deletes spectrum of selected name from all subjects"""

    def run(self, params={}):

        try:
            selected_name = self.data["outputs"]["spectrum"][0]
        except IndexError:
            return

        for subject in self.experiment.subjects.values():
            if selected_name in subject.spectrum:
                try:
                    self.handler(subject, {"name": selected_name})
                except Exception:
                    logging.getLogger("ui_logger").exception("")
                    logging.getLogger("ui_logger").warning(
                        "Could not remove spectrum for " + subject.name
                    )

        self.window.initialize_ui()

    @subject_action
    def handler(self, subject, params):
        subject.remove(params["name"], "spectrum")
        self.experiment.save_experiment_settings()
