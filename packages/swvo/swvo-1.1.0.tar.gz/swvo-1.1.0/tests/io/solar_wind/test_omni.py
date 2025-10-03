# SPDX-FileCopyrightText: 2025 GFZ Helmholtz Centre for Geosciences
#
# SPDX-License-Identifier: Apache-2.0

import os
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import pandas as pd
import pytest

from swvo.io.solar_wind import SWOMNI

TEST_DIR = os.path.dirname(__file__)
DATA_DIR = Path(os.path.join(TEST_DIR, "data/"))


class TestSWOMNI:
    @pytest.fixture
    def swomni(self):
        os.environ["OMNI_HIGH_RES_STREAM_DIR"] = str(DATA_DIR)
        yield SWOMNI()

    def test_initialization_with_env_var(self, swomni):
        assert swomni.data_dir.exists()

    def test_initialization_with_data_dir(self):
        swomni = SWOMNI(data_dir=DATA_DIR)
        assert swomni.data_dir == DATA_DIR

    def test_initialization_without_env_var(self):
        if "OMNI_HIGH_RES_STREAM_DIR" in os.environ:
            del os.environ["OMNI_HIGH_RES_STREAM_DIR"]
        with pytest.raises(ValueError):
            SWOMNI()

    def test_download_and_process(self, swomni):
        start_time = datetime(2020, 1, 1, tzinfo=timezone.utc)
        end_time = datetime(2020, 12, 31, tzinfo=timezone.utc)
        # download this file without mocking
        swomni.download_and_process(start_time, end_time)

        assert (TEST_DIR / Path("data/OMNI_HIGH_RES_1min_2020.csv")).exists()

    def test_read_without_download(self, swomni, mocker):
        start_time = datetime(2021, 1, 1, tzinfo=timezone.utc)
        end_time = datetime(2021, 12, 31, tzinfo=timezone.utc)
        with pytest.raises(
            ValueError
        ):  # value error is raised when no files are found hence no concatenation is possible
            swomni.read(start_time, end_time, download=False)

    def test_read_with_download(self, swomni, mocker):
        mocker.patch.object(swomni, "download_and_process")
        mocker.patch.object(
            swomni,
            "_read_single_file",
            return_value=pd.DataFrame(
                index=pd.date_range(
                    start=datetime(2022, 1, 1, tzinfo=timezone.utc),
                    end=datetime(2022, 12, 31, tzinfo=timezone.utc),
                )
            ),
        )
        start_time = datetime(2022, 1, 1)
        end_time = datetime(2022, 12, 31)
        swomni.read(start_time, end_time, download=True)
        swomni.download_and_process.assert_called_once()

    def test_invalid_cadence(self, swomni):
        start_time = datetime(2022, 1, 1, tzinfo=timezone.utc)
        end_time = datetime(2022, 12, 31, tzinfo=timezone.utc)

        with pytest.raises(AssertionError):
            swomni.read(start_time, end_time, cadence_min=2)

        with pytest.raises(AssertionError):
            swomni.download_and_process(start_time, end_time, cadence_min=10)

    def test_start_year_behind(self, swomni, mocker):
        start_time = datetime(1920, 1, 1)
        end_time = datetime(2020, 12, 31)

        mocked_df = pd.DataFrame(index=pd.date_range(start_time, end_time))

        mocker.patch.object(swomni, "_get_processed_file_list", return_value=([], []))
        mocker.patch.object(swomni, "_read_single_file", return_value=mocked_df)

        mocker.patch("pandas.concat", return_value=pd.DataFrame())

        mocker.patch.object(pd.DataFrame, "truncate", return_value=pd.DataFrame())

        with patch("logging.Logger.warning") as mock_warning:
            dfs = swomni.read(start_time, end_time)
            mock_warning.assert_any_call(
                "Start date chosen falls behind the existing data. Moving start date to first available mission files..."
            )

            assert len(dfs) == 0, "Expected dfs list to be empty since no files are found."

    def test_remove_processed_file(self):
        os.remove(Path(TEST_DIR) / "data/OMNI_HIGH_RES_1min_2020.csv")
