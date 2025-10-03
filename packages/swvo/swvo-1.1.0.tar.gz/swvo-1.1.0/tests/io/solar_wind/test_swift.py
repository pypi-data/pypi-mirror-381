# SPDX-FileCopyrightText: 2025 GFZ Helmholtz Centre for Geosciences
#
# SPDX-License-Identifier: Apache-2.0

import json
import os
import shutil
import warnings
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import numpy as np
import pandas as pd
import pytest

from swvo.io.solar_wind import SWSWIFTEnsemble

TEST_DATA_DIR = Path("test_data")
MOCK_DATA_PATH = TEST_DATA_DIR / "mock_swift"


class TestSWIFT:
    @pytest.fixture(autouse=True)
    def setup_and_cleanup(self):
        TEST_DATA_DIR.mkdir(exist_ok=True)
        MOCK_DATA_PATH.mkdir(exist_ok=True)

        yield

        if TEST_DATA_DIR.exists():
            shutil.rmtree(TEST_DATA_DIR, ignore_errors=True)

    @pytest.fixture
    def swift_instance(self):
        with patch.dict("os.environ", {SWSWIFTEnsemble.ENV_VAR_NAME: str(MOCK_DATA_PATH)}):
            instance = SWSWIFTEnsemble()
            return instance

    @pytest.fixture
    def sample_swift_data(self):
        current_time = int(datetime.now(timezone.utc).replace(microsecond=0, minute=0, second=0).timestamp())
        return {
            "arrays": {
                "Unix time": {"data": [current_time, current_time + 3 * 24 * 3600]},
                "Vx": {"data": [-400000, -450000]},
                "Vy": {"data": [50000, 55000]},
                "Vz": {"data": [10000, 12000]},
                "Bx": {"data": [5e-9, 5.2e-9]},
                "By": {"data": [3e-9, 3.1e-9]},
                "Bz": {"data": [-2e-9, -2.1e-9]},
                "Temperature_ion": {"data": [200000, 210000]},
                "Rho": {"data": [1e-20, 1.1e-20]},
            }
        }

    @pytest.fixture
    def create_mock_swift_files(self, sample_swift_data):
        def _create_files(base_date: datetime, num_tasks: int = 2):
            date_str = base_date.strftime("%Y%m%dt0000")
            base_dir = MOCK_DATA_PATH / date_str

            for task_num in range(num_tasks):
                task_dir = base_dir / f"task{task_num}"
                swift_dir = task_dir / "SWIFT"
                swift_dir.mkdir(parents=True, exist_ok=True)

                gsm_file = swift_dir / f"gsm_{task_num}.json"
                with open(gsm_file, "w") as f:
                    json.dump(sample_swift_data, f)

            return base_dir

        return _create_files

    def test_initialization_with_env_var(self):
        with patch.dict("os.environ", {SWSWIFTEnsemble.ENV_VAR_NAME: str(MOCK_DATA_PATH)}):
            swift = SWSWIFTEnsemble()
            assert swift.data_dir == MOCK_DATA_PATH

    def test_initialization_with_explicit_path(self):
        explicit_path = MOCK_DATA_PATH / "explicit"
        explicit_path.mkdir(parents=True)
        swift = SWSWIFTEnsemble(data_dir=explicit_path)
        assert swift.data_dir == explicit_path

    def test_initialization_without_env_var(self):
        if SWSWIFTEnsemble.ENV_VAR_NAME in os.environ:
            del os.environ[SWSWIFTEnsemble.ENV_VAR_NAME]
        with pytest.raises(
            ValueError,
            match=f"Necessary environment variable {SWSWIFTEnsemble.ENV_VAR_NAME} not set!",
        ):
            SWSWIFTEnsemble()

    def test_initialization_with_nonexistent_directory(self):
        non_existent_dir = MOCK_DATA_PATH / "does_not_exist"
        with pytest.raises(
            FileNotFoundError,
            match=f"Data directory {non_existent_dir} does not exist!",
        ):
            SWSWIFTEnsemble(data_dir=non_existent_dir)

    def test_read_single_file(self, swift_instance, sample_swift_data, tmp_path):
        test_file = tmp_path / "test_gsm.json"
        with open(test_file, "w") as f:
            json.dump(sample_swift_data, f)

        data = swift_instance._read_single_file(test_file)

        assert isinstance(data, pd.DataFrame)
        expected_columns = [
            "proton_density",
            "speed",
            "bavg",
            "temperature",
            "bx_gsm",
            "by_gsm",
            "bz_gsm",
            "file_name",
        ]
        assert all(col in data.columns for col in expected_columns)

        assert data["speed"].iloc[0] == pytest.approx(np.sqrt((-400) ** 2 + 50**2 + 10**2))
        assert data["bx_gsm"].iloc[0] == pytest.approx(5.0)
        assert data["proton_density"].iloc[0] > 0
        assert data["temperature"].iloc[0] == 200000

    def test_read_single_file_with_old_columns(self, swift_instance, sample_swift_data, tmp_path):
        test_file = tmp_path / "test_gsm.json"
        with open(test_file, "w") as f:
            json.dump(sample_swift_data, f)

        data = swift_instance._read_single_file(test_file, use_old_column_names=True)

        assert isinstance(data, pd.DataFrame)
        expected_columns = [
            "proton_density",
            "speed",
            "b",
            "temperature",
            "bx",
            "by",
            "bz",
            "ux",
            "uy",
            "uz",
            "file_name",
        ]
        assert all(col in data.columns for col in expected_columns)

    def test_read_ensemble(self, swift_instance, create_mock_swift_files):
        base_date = datetime.now(timezone.utc).replace(microsecond=0, minute=0, second=0)
        create_mock_swift_files(base_date, num_tasks=3)

        start_time = base_date
        end_time = base_date + timedelta(days=1)

        result = swift_instance.read(start_time, end_time)

        assert isinstance(result, list)
        assert len(result) == 3
        assert all(isinstance(df, pd.DataFrame) for df in result)

        expected_columns = [
            "proton_density",
            "speed",
            "bavg",
            "temperature",
            "bx_gsm",
            "by_gsm",
            "bz_gsm",
            "file_name",
        ]
        for df in result:
            assert all(col in df.columns for col in expected_columns)

    def test_read_with_missing_gsm_files(
        self,
        swift_instance,
        create_mock_swift_files,
    ):
        base_date = datetime.now().replace(microsecond=0, minute=0, second=0)
        task_dir = create_mock_swift_files(base_date, num_tasks=1)

        gsm_file = next(task_dir.rglob("gsm_*.json"))
        gsm_file.unlink()

        with warnings.catch_warnings(record=True) as w:
            result = swift_instance.read(base_date, base_date + timedelta(days=1))
            print(result)
            assert "GSM SWIFT output file for date" in str(w[-1].message)
            assert len(result) == 0

    def test_read_with_default_times(self, swift_instance, create_mock_swift_files):
        base_date = datetime.now(timezone.utc).replace(microsecond=0, minute=0, second=0)
        create_mock_swift_files(base_date, num_tasks=2)

        result = swift_instance.read(None, None)

        assert isinstance(result, list)
        assert len(result) == 2

        for df in result:
            assert df.index.min() <= base_date
            assert df.index.max() >= base_date + timedelta(days=3)

    def test_with_propagation(self):
        start_time = datetime(2024, 11, 23, tzinfo=timezone.utc)
        end_time = datetime(2024, 11, 25, tzinfo=timezone.utc)

        swace_instance = SWSWIFTEnsemble(Path(__file__).parent / "data" / "ensemble")
        data = swace_instance.read(start_time, end_time, propagation=True)
        assert isinstance(data, list)
        for df in data:
            assert any(df["file_name"] == "propagated from previous SWIFT FORECAST file")
            assert df.index.is_monotonic_increasing
