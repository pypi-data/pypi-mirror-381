import json
import os
import shutil
from pathlib import Path

import pytest
from bclearer_core.pipeline_builder.generator import (
    generate_pipeline,
    update_pipeline,
)


class TestPipelineUpdate:
    """Test class for the pipeline update functionality."""

    @pytest.fixture(autouse=True)
    def setup_method(
        self,
        pipeline_output_folder_absolute_path,
        pipeline_builder_configuration_file_path,
    ):
        """Setup method that runs before each test."""
        # Load the configuration to get domain_name
        with open(
            pipeline_builder_configuration_file_path,
            "r",
        ) as f:
            self.config_dict = (
                json.load(f)
            )

        # Get the domain name from the config
        domain_name = self.config_dict[
            "domain_name"
        ]

        # Clean up any existing test pipelines from previous runs
        self.domain_path = os.path.join(
            pipeline_output_folder_absolute_path,
            f"{domain_name}_pipelines",
        )

        if os.path.exists(
            self.domain_path
        ):
            shutil.rmtree(
                self.domain_path
            )

        # Store paths for use in tests
        self.output_path = pipeline_output_folder_absolute_path
        self.pipeline_builder_config_path = pipeline_builder_configuration_file_path

    def test_update_pipeline_new_b_unit(
        self,
    ):
        """Test updating a pipeline by adding a new b_unit."""
        # First generate the initial pipeline
        generate_pipeline(
            self.config_dict,
            self.output_path,
        )

        # Make sure the initial pipeline exists
        domain_name = self.config_dict[
            "domain_name"
        ]
        first_pipeline = (
            self.config_dict[
                "pipelines"
            ][0]["name"]
        )
        first_stage = self.config_dict[
            "pipelines"
        ][0]["thin_slices"][0][
            "stages"
        ][
            0
        ][
            "name"
        ]

        # Create updated config with a new b_unit in the first stage
        updated_config = (
            self.config_dict.copy()
        )
        updated_config["pipelines"][0][
            "thin_slices"
        ][0]["stages"][0][
            "b_units"
        ].append(
            "new_b_unit"
        )

        # Update the pipeline
        updated_path = update_pipeline(
            updated_config,
            self.domain_path,
        )

        # Check that the new b_unit file was created
        new_b_unit_path = os.path.join(
            self.domain_path,
            "b_source",
            first_pipeline,
            "objects",
            "b_units",
            f"{first_pipeline}_{first_stage}",
            "new_b_unit_b_units.py",
        )

        assert os.path.exists(
            new_b_unit_path
        )

        # Check content of new b_unit file
        with open(
            new_b_unit_path, "r"
        ) as f:
            content = f.read()
            assert (
                "class NewBUnitBUnits:"
                in content
            )
            assert (
                "def run(self) -> None:"
                in content
            )

    def test_update_pipeline_new_stage(
        self,
    ):
        """Test updating a pipeline by adding a new stage."""
        # First generate the initial pipeline
        generate_pipeline(
            self.config_dict,
            self.output_path,
        )

        # Create updated config with a new stage
        updated_config = (
            self.config_dict.copy()
        )
        updated_config["pipelines"][0][
            "thin_slices"
        ][0]["stages"].append(
            {
                "name": "6x_extend",
                "sub_stages": [],
                "b_units": [
                    "new_extension_b_unit"
                ],
            }
        )

        # Update the pipeline
        updated_path = update_pipeline(
            updated_config,
            self.domain_path,
        )

        # Check that the new stage orchestrator was created
        domain_name = self.config_dict[
            "domain_name"
        ]
        first_pipeline = (
            self.config_dict[
                "pipelines"
            ][0]["name"]
        )

        new_stage_orchestrator_path = os.path.join(
            self.domain_path,
            "b_source",
            first_pipeline,
            "orchestrators",
            "stages",
            f"{first_pipeline}_6x_extend_orchestrator.py",
        )

        assert os.path.exists(
            new_stage_orchestrator_path
        )

        # Check that the new b_unit was created
        new_b_unit_path = os.path.join(
            self.domain_path,
            "b_source",
            first_pipeline,
            "objects",
            "b_units",
            f"{first_pipeline}_6x_extend",
            "new_extension_b_unit_b_units.py",
        )

        assert os.path.exists(
            new_b_unit_path
        )

        # Check that the thin slice orchestrator was updated to include the new stage
        thin_slice_name = (
            self.config_dict[
                "pipelines"
            ][0]["thin_slices"][0][
                "name"
            ]
        )
        thin_slice_orchestrator_path = os.path.join(
            self.domain_path,
            "b_source",
            first_pipeline,
            "orchestrators",
            "thin_slices",
            f"{thin_slice_name}_orchestrator.py",
        )

        with open(
            thin_slice_orchestrator_path,
            "r",
        ) as f:
            content = f.read()
            assert (
                f"orchestrate_{first_pipeline}_6x_extend()"
                in content
            )

    def test_update_pipeline_new_pipeline(
        self,
    ):
        """Test updating by adding a completely new pipeline."""
        # First generate the initial pipeline
        generate_pipeline(
            self.config_dict,
            self.output_path,
        )

        # Create updated config with a new pipeline
        updated_config = (
            self.config_dict.copy()
        )
        updated_config[
            "pipelines"
        ].append(
            {
                "name": "new_pipeline",
                "thin_slices": [
                    {
                        "name": "new_slice",
                        "stages": [
                            {
                                "name": "1c_collect",
                                "sub_stages": [],
                                "b_units": [
                                    "collector_b_unit"
                                ],
                            }
                        ],
                    }
                ],
            }
        )

        # Update the pipeline
        update_pipeline(
            updated_config,
            self.domain_path,
        )

        # Check that the new pipeline directory was created
        domain_name = self.config_dict[
            "domain_name"
        ]
        new_pipeline_path = (
            os.path.join(
                self.domain_path,
                "b_source",
                "new_pipeline",
            )
        )
        assert os.path.exists(
            new_pipeline_path
        )

        # Check that the new pipeline runner was created
        new_pipeline_runner_path = os.path.join(
            self.domain_path,
            "b_source",
            "app_runners",
            "runners",
            "new_pipeline_runner.py",
        )
        assert os.path.exists(
            new_pipeline_runner_path
        )

        # Check that the pipelines runner was updated to include the new pipeline
        pipelines_runner_path = os.path.join(
            self.domain_path,
            "b_source",
            "app_runners",
            "runners",
            f"{domain_name}_b_clearer_pipelines_runner.py",
        )

        with open(
            pipelines_runner_path, "r"
        ) as f:
            content = f.read()
            assert (
                f"from {domain_name}.b_source.app_runners.runners.new_pipeline_runner import"
                in content
            )
            assert (
                "run_new_pipeline()"
                in content
            )

    def test_update_pipeline_domain_name_mismatch(
        self,
    ):
        """Test that updating with a mismatched domain name raises an error."""
        # First generate the initial pipeline
        generate_pipeline(
            self.config_dict,
            self.output_path,
        )

        # Create updated config with a different domain name
        updated_config = (
            self.config_dict.copy()
        )
        updated_config[
            "domain_name"
        ] = "different_domain"

        # Updating the pipeline should raise a ValueError
        with pytest.raises(
            ValueError
        ) as excinfo:
            update_pipeline(
                updated_config,
                self.domain_path,
            )

        assert (
            "Domain name in configuration"
            in str(excinfo.value)
        )
        assert (
            "does not match existing domain name"
            in str(excinfo.value)
        )
