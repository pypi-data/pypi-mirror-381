import json
import os
import shutil
import tempfile
from pathlib import Path

import pytest
from bclearer_core.pipeline_builder.generator import (
    generate_pipeline,
)
from bclearer_core.pipeline_builder.schema import (
    get_sample_config,
)


class TestPipelineGenerationFlow:
    """Test class for end-to-end pipeline generation flow."""

    @pytest.fixture(autouse=True)
    def setup_method(
        self,
        pipeline_output_folder_absolute_path,
    ):
        """Setup method that runs before each test."""
        # Create a temporary directory for output
        self.temp_output_dir = os.path.join(
            pipeline_output_folder_absolute_path,
            "temp_flow_test",
        )
        os.makedirs(
            self.temp_output_dir,
            exist_ok=True,
        )

        # Clean up any existing test pipelines from previous runs
        self.test_domain_path = os.path.join(
            self.temp_output_dir,
            "example_domain_pipelines",
        )

        if os.path.exists(
            self.test_domain_path
        ):
            shutil.rmtree(
                self.test_domain_path
            )

        # Also clean up custom_domain directory for the custom test
        self.custom_domain_path = os.path.join(
            self.temp_output_dir,
            "custom_domain_pipelines",
        )

        if os.path.exists(
            self.custom_domain_path
        ):
            shutil.rmtree(
                self.custom_domain_path
            )

    def teardown_method(self):
        """Cleanup after tests."""
        if os.path.exists(
            self.temp_output_dir
        ):
            shutil.rmtree(
                self.temp_output_dir
            )

    def test_full_pipeline_generation_flow(
        self,
        template_pipeline_folder_absolute_path,
    ):
        """
        Test the complete flow from sample config to pipeline generation,
        verifying the structure and runability of the generated pipeline.
        """
        # Get sample config
        sample_config = (
            get_sample_config()
        )

        # Generate the pipeline
        pipeline_path = (
            generate_pipeline(
                sample_config,
                self.temp_output_dir,
            )
        )

        # Verify pipeline structure
        domain_path = os.path.join(
            self.temp_output_dir,
            "example_domain_pipelines",
        )
        assert os.path.exists(
            domain_path
        )

        # Check key top-level directories
        assert os.path.exists(
            os.path.join(
                domain_path, "b_source"
            )
        )
        assert os.path.exists(
            os.path.join(
                domain_path, "resources"
            )
        )
        assert os.path.exists(
            os.path.join(
                domain_path, "tests"
            )
        )

        # Check app_runners directory structure
        app_runners_path = os.path.join(
            domain_path,
            "b_source",
            "app_runners",
        )
        assert os.path.exists(
            app_runners_path
        )
        assert os.path.exists(
            os.path.join(
                app_runners_path,
                "runners",
            )
        )
        assert os.path.exists(
            os.path.join(
                app_runners_path,
                f"{sample_config['domain_name']}_b_clearer_pipeline_b_application_runner.py",
            )
        )

        # Check common directory structure
        common_path = os.path.join(
            domain_path,
            "b_source",
            "common",
        )
        assert os.path.exists(
            common_path
        )
        assert os.path.exists(
            os.path.join(
                common_path,
                "operations",
                "b_units",
            )
        )

        # Verify the pipeline directory structure
        pipeline_name = sample_config[
            "pipelines"
        ][0]["name"]
        pipeline_path = os.path.join(
            domain_path,
            "b_source",
            pipeline_name,
        )
        assert os.path.exists(
            pipeline_path
        )

        # Check pipeline subdirectories
        assert os.path.exists(
            os.path.join(
                pipeline_path, "objects"
            )
        )
        assert os.path.exists(
            os.path.join(
                pipeline_path,
                "operations",
            )
        )
        assert os.path.exists(
            os.path.join(
                pipeline_path,
                "orchestrators",
            )
        )

        # Check orchestrator subdirectories
        orchestrators_path = (
            os.path.join(
                pipeline_path,
                "orchestrators",
            )
        )
        assert os.path.exists(
            os.path.join(
                orchestrators_path,
                "pipeline",
            )
        )
        assert os.path.exists(
            os.path.join(
                orchestrators_path,
                "stages",
            )
        )
        assert os.path.exists(
            os.path.join(
                orchestrators_path,
                "thin_slices",
            )
        )
        assert os.path.exists(
            os.path.join(
                orchestrators_path,
                "sub_stages",
            )
        )

        # Check the specific orchestrator files exist
        assert os.path.exists(
            os.path.join(
                orchestrators_path,
                "pipeline",
                f"{pipeline_name}_orchestrator.py",
            )
        )

        # Verify thin slice generation
        thin_slice_name = sample_config[
            "pipelines"
        ][0]["thin_slices"][0]["name"]
        assert os.path.exists(
            os.path.join(
                orchestrators_path,
                "thin_slices",
                f"{thin_slice_name}_orchestrator.py",
            )
        )

        # Verify stage generation
        for stage in sample_config[
            "pipelines"
        ][0]["thin_slices"][0][
            "stages"
        ]:
            stage_name = stage["name"]
            stage_orchestrator_name = f"{pipeline_name}_{stage_name}_orchestrator.py"
            assert os.path.exists(
                os.path.join(
                    orchestrators_path,
                    "stages",
                    stage_orchestrator_name,
                )
            )

            # If the stage has b_units, verify their generation
            if stage["b_units"]:
                stage_b_units_path = os.path.join(
                    pipeline_path,
                    "objects",
                    "b_units",
                    f"{pipeline_name}_{stage_name}",
                )
                assert os.path.exists(
                    stage_b_units_path
                )

                for b_unit in stage[
                    "b_units"
                ]:
                    b_unit_file_name = f"{b_unit.lower()}_b_units.py"
                    assert os.path.exists(
                        os.path.join(
                            stage_b_units_path,
                            b_unit_file_name,
                        )
                    )

            # If the stage has sub_stages, verify their generation
            for sub_stage in stage.get(
                "sub_stages", []
            ):
                sub_stage_name = (
                    sub_stage["name"]
                )
                sub_stage_path = os.path.join(
                    orchestrators_path,
                    "sub_stages",
                    f"{pipeline_name}_{stage_name}_{sub_stage_name}",
                )
                assert os.path.exists(
                    sub_stage_path
                )

                # Check sub_stage orchestrator
                sub_stage_orchestrator_name = f"{pipeline_name}_{stage_name}_{sub_stage_name}_orchestrator.py"
                assert os.path.exists(
                    os.path.join(
                        sub_stage_path,
                        sub_stage_orchestrator_name,
                    )
                )

                # Check sub_stage b_units
                if sub_stage["b_units"]:
                    sub_stage_b_units_path = os.path.join(
                        pipeline_path,
                        "objects",
                        "b_units",
                        f"{pipeline_name}_{stage_name}",
                        f"{pipeline_name}_{stage_name}_{sub_stage_name}",
                    )
                    assert os.path.exists(
                        sub_stage_b_units_path
                    )

                    for (
                        b_unit
                    ) in sub_stage[
                        "b_units"
                    ]:
                        b_unit_file_name = f"{b_unit.lower()}_b_units.py"
                        assert os.path.exists(
                            os.path.join(
                                sub_stage_b_units_path,
                                b_unit_file_name,
                            )
                        )

        # Verify test directory structure
        tests_path = os.path.join(
            domain_path, "tests"
        )
        assert os.path.exists(
            os.path.join(
                tests_path, "common"
            )
        )
        assert os.path.exists(
            os.path.join(
                tests_path, "universal"
            )
        )

        # Check E2E test setup
        e2e_path = os.path.join(
            tests_path,
            "universal",
            "e2e",
        )
        assert os.path.exists(
            os.path.join(
                e2e_path, "conftest.py"
            )
        )
        assert os.path.exists(
            os.path.join(
                e2e_path,
                f"test_{sample_config['domain_name']}_b_clearer_pipeline_b_application_runner.py",
            )
        )

    def test_custom_pipeline_generation(
        self,
        template_pipeline_folder_absolute_path,
    ):
        """Test generating a pipeline with a custom configuration."""
        # Create a custom pipeline config
        custom_config = {
            "domain_name": "custom_domain",
            "pipelines": [
                {
                    "name": "data_processing",
                    "thin_slices": [
                        {
                            "name": "data_extraction",
                            "stages": [
                                {
                                    "name": "1c_collect",
                                    "sub_stages": [
                                        {
                                            "name": "api_extraction",
                                            "b_units": [
                                                "api_reader",
                                                "api_parser",
                                            ],
                                        },
                                        {
                                            "name": "file_extraction",
                                            "b_units": [
                                                "csv_reader",
                                                "json_reader",
                                            ],
                                        },
                                    ],
                                    "b_units": [
                                        "extraction_coordinator"
                                    ],
                                },
                                {
                                    "name": "2l_load",
                                    "sub_stages": [],
                                    "b_units": [
                                        "data_loader",
                                        "data_validator",
                                    ],
                                },
                            ],
                        }
                    ],
                }
            ],
        }

        # Generate the pipeline
        pipeline_path = (
            generate_pipeline(
                custom_config,
                self.temp_output_dir,
            )
        )

        # Verify pipeline structure
        domain_path = os.path.join(
            self.temp_output_dir,
            "custom_domain_pipelines",
        )
        assert os.path.exists(
            domain_path
        )

        # Check data_processing pipeline exists
        data_processing_path = (
            os.path.join(
                domain_path,
                "b_source",
                "data_processing",
            )
        )
        assert os.path.exists(
            data_processing_path
        )

        # Check thin slice exists
        thin_slice_path = os.path.join(
            data_processing_path,
            "orchestrators",
            "thin_slices",
            "data_extraction_orchestrator.py",
        )
        assert os.path.exists(
            thin_slice_path
        )

        # Check collect stage with sub-stages
        collect_path = os.path.join(
            data_processing_path,
            "orchestrators",
            "stages",
            "data_processing_1c_collect_orchestrator.py",
        )
        assert os.path.exists(
            collect_path
        )

        # Check api_extraction sub-stage
        api_extraction_path = os.path.join(
            data_processing_path,
            "orchestrators",
            "sub_stages",
            "data_processing_1c_collect_api_extraction",
            "data_processing_1c_collect_api_extraction_orchestrator.py",
        )
        assert os.path.exists(
            api_extraction_path
        )

        # Check file_extraction sub-stage
        file_extraction_path = os.path.join(
            data_processing_path,
            "orchestrators",
            "sub_stages",
            "data_processing_1c_collect_file_extraction",
            "data_processing_1c_collect_file_extraction_orchestrator.py",
        )
        assert os.path.exists(
            file_extraction_path
        )

        # Check b_units for collect stage
        collect_b_units_path = os.path.join(
            data_processing_path,
            "objects",
            "b_units",
            "data_processing_1c_collect",
        )
        assert os.path.exists(
            collect_b_units_path
        )
        assert os.path.exists(
            os.path.join(
                collect_b_units_path,
                "extraction_coordinator_b_units.py",
            )
        )

        # Check b_units for api_extraction sub-stage
        api_extraction_b_units_path = os.path.join(
            data_processing_path,
            "objects",
            "b_units",
            "data_processing_1c_collect",
            "data_processing_1c_collect_api_extraction",
        )
        assert os.path.exists(
            api_extraction_b_units_path
        )
        assert os.path.exists(
            os.path.join(
                api_extraction_b_units_path,
                "api_reader_b_units.py",
            )
        )
        assert os.path.exists(
            os.path.join(
                api_extraction_b_units_path,
                "api_parser_b_units.py",
            )
        )

        # Check file contents for a b_unit
        with open(
            os.path.join(
                api_extraction_b_units_path,
                "api_reader_b_units.py",
            ),
            "r",
        ) as f:
            content = f.read()
            assert (
                "class ApiReaderBUnits:"
                in content
            )
            assert (
                "def run(self) -> None:"
                in content
            )
            assert (
                "def b_unit_process_function"
                in content
            )
