import tempfile
import os
import numpy as np
import mne

from meggie.utilities.filemanager import save_csv
from meggie.utilities.filemanager import load_csv
from meggie.utilities.filemanager import open_raw
from meggie.utilities.filemanager import save_raw
from meggie.utilities.filemanager import get_supported_formats


def test_save_and_load_csv():
    with tempfile.TemporaryDirectory() as dirpath:

        filepath = os.path.join(dirpath, "data.csv")

        data = np.array([[1, 2, 3], [4, 5, 6]])
        column_names = ["A", "B", "C"]
        row_descs = [("X", "Kissa"), ("Y", "Koira")]

        save_csv(filepath, data, column_names, row_descs)

        loaded_column_names, loaded_row_descs, loaded_data = load_csv(filepath)

        assert loaded_column_names == column_names
        assert loaded_row_descs[0] == row_descs[0]
        assert loaded_row_descs[1] == row_descs[1]
        assert np.array_equal(loaded_data, data)


def test_save_and_load_raw():
    sample_folder = mne.datasets.sample.data_path()
    sample_fname = os.path.join(sample_folder, "MEG", "sample", "sample_audvis_raw.fif")
    sample_raw = mne.io.read_raw_fif(sample_fname, preload=True)
    raw_copy = sample_raw.copy()

    # make long enough raw to test split files
    raw = mne.concatenate_raws([sample_raw] + 8 * [raw_copy])

    with tempfile.TemporaryDirectory() as dirpath:
        path = os.path.join(dirpath, "raw.fif")
        save_raw(raw, path)

        # release memory before opening again
        sample_raw = None
        raw_copy = None
        raw = None

        open_raw(path)


def test_supported_formats():
    supported_formats = get_supported_formats()
    assert isinstance(supported_formats, list)
    assert isinstance(supported_formats[0], tuple)
    assert isinstance(supported_formats[0][0], str)
    assert isinstance(supported_formats[0][1], list)
