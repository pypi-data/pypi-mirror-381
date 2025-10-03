from meggie.utilities.testing import BaseTestAction
from meggie.actions.tfr_plot import PlotTFR
from meggie.utilities.dialogs.TFROutputOptionsMain import TFROutputOptions


class TestTFRPlotChannelAverages(BaseTestAction):
    def test_tfr_plot_channel_averages(self):

        data = {"outputs": {"tfr": ["TFR"]}}

        self.run_action(
            action_name="tfr_plot",
            handler=PlotTFR,
            data=data,
        )
        dialog = self.find_dialog(TFROutputOptions)
        dialog.ui.radioButtonChannelAverages.setChecked(True)
        dialog.accept()
