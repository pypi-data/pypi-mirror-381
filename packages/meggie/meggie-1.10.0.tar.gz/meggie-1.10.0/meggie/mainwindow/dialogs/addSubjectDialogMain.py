"""Contains a class for logic of add subject dialog."""

import os
import mne
import logging

from PyQt5 import QtWidgets
from PyQt5 import QtCore

from meggie.mainwindow.dialogs.addSubjectDialogUi import Ui_AddSubject

from meggie.utilities.messaging import exc_messagebox
from meggie.utilities.messaging import messagebox
from meggie.utilities.threading import threaded
from meggie.utilities.names import next_available_name
from meggie.utilities.filemanager import get_supported_formats
from meggie.utilities.filemanager import homepath


class AddSubjectDialog(QtWidgets.QDialog):
    """Contains the logic for add subject dialog."""

    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_AddSubject()
        self.ui.setupUi(self)

        self.parent = parent

    def accept(self):
        n_successful = 0
        for i in range(self.ui.listWidgetFileNames.count()):
            item = self.ui.listWidgetFileNames.item(i)
            raw_path = item.text()
            basename = os.path.basename(raw_path)
            subject_name = basename.split(".")[0]

            experiment = self.parent.experiment
            old_names = experiment.subjects.keys()

            try:
                subject_name = next_available_name(old_names, subject_name)

                @threaded
                def _create_subject():
                    experiment.create_subject(subject_name, raw_path)

                _create_subject(do_meanwhile=self.parent.update_ui)
                n_successful += 1

            except Exception:
                logging.getLogger("ui_logger").exception("")

        try:
            self.parent.experiment.save_experiment_settings()
        except Exception as exc:
            exc_messagebox(self, exc)
            return

        n_total = self.ui.listWidgetFileNames.count()

        if n_total != n_successful:
            message = (
                "Only {0} / {1} subjects added successfully. "
                "Please check console below for details."
            )
            messagebox(self.parent, message.format(n_successful, n_total))

        message = ("{0} / {1} subjects added successfully.").format(
            n_successful, n_total
        )
        logging.getLogger("ui_logger").info(message)

        self.parent.initialize_ui()
        self.close()

    def on_pushButtonSample_clicked(self, checked=None):
        if checked is None:
            return

        experiment = self.parent.experiment
        old_names = experiment.subjects.keys()
        subject_name = next_available_name(old_names, "sample_audvis_raw")

        @threaded
        def _create_subject():
            raw_path = os.path.join(
                str(mne.datasets.sample.data_path()),
                "MEG",
                "sample",
                "sample_audvis_raw.fif",
            )
            experiment.create_subject(subject_name, raw_path)

        try:
            _create_subject(do_meanwhile=self.parent.update_ui)
        except Exception:
            logging.getLogger("ui_logger").exception("")

        try:
            self.parent.experiment.save_experiment_settings()
        except Exception as exc:
            exc_messagebox(self, exc)
            return

        self.parent.initialize_ui()
        self.close()

    def on_pushButtonBrowse_clicked(self, checked=None):
        if checked is None:
            return

        mne_supported = get_supported_formats()

        all_ext = [val[0] for val in mne_supported]

        all_items = []
        for ext, names in mne_supported:
            for name in names:
                all_items.append(name + " files (*" + ext + ")")

        filter_string = "All supported (*" + " *".join(all_ext) + ");" ";"
        filter_string = filter_string + ";" ";".join(all_items)

        self.fnames = QtWidgets.QFileDialog.getOpenFileNames(
            self,
            "Select one or more files to open.",
            homepath(),
            filter_string,
        )[0]

        if len(self.fnames) > 0:
            for name in self.fnames:
                name = QtCore.QDir.toNativeSeparators(name)
                item = QtWidgets.QListWidgetItem()
                item.setText(name)
                if (
                    len(
                        self.ui.listWidgetFileNames.findItems(
                            name, QtCore.Qt.MatchExactly
                        )
                    )
                    > 0
                ):
                    continue
                self.ui.listWidgetFileNames.addItem(item)

    def on_pushButtonRemove_clicked(self, checked=None):
        if checked is None:
            return
        for item in self.ui.listWidgetFileNames.selectedItems():
            i = self.ui.listWidgetFileNames.indexFromItem(item)
            row = i.row()
            self.ui.listWidgetFileNames.takeItem(row)

    def on_listWidgetFileNames_itemSelectionChanged(self):
        items = self.ui.listWidgetFileNames.selectedItems()
        if len(items) > 0:
            self.ui.pushButtonRemove.setEnabled(True)
        else:
            self.ui.pushButtonRemove.setEnabled(False)
