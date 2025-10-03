from meggie.utilities.testing import BaseTestAction
from meggie.actions.epochs_plot import PlotEpochs


class TestEpochsPlot(BaseTestAction):
    def test_epochs_plot(self):

        data = {"outputs": {"epochs": ["Epochs"]}}

        self.run_action(action_name="epochs_plot", handler=PlotEpochs, data=data)
