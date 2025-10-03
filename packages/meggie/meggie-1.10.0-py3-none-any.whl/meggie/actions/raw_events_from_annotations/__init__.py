"""Contains implementation for events from annotations"""

from meggie.utilities.threading import threaded

from meggie.actions.raw_events_from_annotations.dialogs.eventsFromAnnotationsDialogMain import (
    EventsFromAnnotationsDialog,
)

from meggie.utilities.events import events_from_annotations

from meggie.mainwindow.dynamic import Action
from meggie.mainwindow.dynamic import subject_action


class EventsFromAnnotations(Action):
    """Shows a dialog for parameter selection and then
    applies a conversion from annotations to events.
    """

    def run(self, params={}):
        evs_from_annots_dialog = EventsFromAnnotationsDialog(
            self.window, self.experiment, self.handler
        )
        evs_from_annots_dialog.show()

    @subject_action
    def handler(self, subject, params):
        """ """

        @threaded
        def conv_fun():
            """ """
            events_from_annotations(subject, params["items"])
            subject.save()

        conv_fun(do_meanwhile=self.window.update_ui)
