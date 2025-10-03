from meggie.utilities.testing import BaseTestAction
from meggie.actions.evoked_plot import PlotEvoked
from meggie.utilities.dialogs.outputOptionsMain import OutputOptions


class TestEvokedPlotAllChannels(BaseTestAction):
    def test_evoked_plot_all_channels(self):

        data = {"outputs": {"evoked": ["Evoked"]}}

        self.run_action(
            action_name="evoked_plot",
            handler=PlotEvoked,
            data=data,
        )
        dialog = self.find_dialog(OutputOptions)
        dialog.ui.radioButtonChannelAverages.setChecked(False)
        dialog.accept()
