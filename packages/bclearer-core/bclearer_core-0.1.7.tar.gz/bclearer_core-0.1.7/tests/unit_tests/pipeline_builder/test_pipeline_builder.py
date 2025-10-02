import json
import os
import shutil
from pathlib import Path

import pytest
from bclearer_core.pipeline_builder.generator import (
    generate_pipeline,
)
from bclearer_core.pipeline_builder.schema import (
    validate_pipeline_config,
)


class TestPipelineBuilder:
    """Test class for the pipeline builder functionality."""

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
            config_dict = json.load(f)

        # Get the domain name from the config
        domain_name = config_dict[
            "domain_name"
        ]

        # Clean up any existing test pipelines from previous runs
        self.domain_path = os.path.join(
            pipeline_output_folder_absolute_path,
            "bclearer_pipelines",
            domain_name,
        )

        if os.path.exists(
            self.domain_path
        ):
            shutil.rmtree(
                self.domain_path
            )

    def test_validate_pipeline_config_valid_config(
        self,
        pipeline_builder_configuration_file_path,
    ):
        """Test that a valid configuration file is correctly validated."""
        # Load the test configuration
        with open(
            pipeline_builder_configuration_file_path,
            "r",
        ) as f:
            config_dict = json.load(f)

        # Validate the configuration
        config = (
            validate_pipeline_config(
                config_dict
            )
        )

        # Assert basic structure is correct
        assert (
            config.domain_name
            == config_dict[
                "domain_name"
            ]
        )
        assert len(
            config.pipelines
        ) == len(
            config_dict["pipelines"]
        )
        assert (
            config.pipelines[0].name
            == config_dict["pipelines"][
                0
            ]["name"]
        )
        assert (
            len(
                config.pipelines[
                    0
                ].thin_slices
            )
            == 1
        )
        assert (
            len(
                config.pipelines[0]
                .thin_slices[0]
                .stages
            )
            == 5
        )

        # Check specific stages
        collect_stage = (
            config.pipelines[0]
            .thin_slices[0]
            .stages[0]
        )
        evolve_stage = (
            config.pipelines[0]
            .thin_slices[0]
            .stages[2]
        )

        assert (
            collect_stage.name
            == "1c_collect"
        )
        assert (
            len(collect_stage.b_units)
            == 2
        )
        assert (
            collect_stage.b_units[0]
            == "ca_b_unit"
        )

        assert (
            evolve_stage.name
            == "3e_evolve"
        )
        assert (
            len(evolve_stage.sub_stages)
            == 2
        )
        assert (
            evolve_stage.sub_stages[
                0
            ].name
            == "sub_stage_1"
        )
        assert (
            evolve_stage.sub_stages[
                1
            ].name
            == "sub_stage_2"
        )

    def test_validate_pipeline_config_missing_domain(
        self,
    ):
        """Test validation with missing domain_name."""
        invalid_config = {
            "pipelines": []
        }

        with pytest.raises(
            ValueError
        ) as exc_info:
            validate_pipeline_config(
                invalid_config
            )

        assert (
            "domain_name is required"
            in str(exc_info.value)
        )

    def test_validate_pipeline_config_missing_pipeline_name(
        self,
    ):
        """Test validation with missing pipeline name."""
        invalid_config = {
            "domain_name": "test_domain",
            "pipelines": [{}],
        }

        with pytest.raises(
            ValueError
        ) as exc_info:
            validate_pipeline_config(
                invalid_config
            )

        assert (
            "Pipeline name is required"
            in str(exc_info.value)
        )

    def test_generate_pipeline_from_config(
        self,
        pipeline_builder_configuration_file_path,
        pipeline_output_folder_absolute_path,
        template_pipeline_folder_absolute_path,
    ):
        """Test generating a pipeline from a configuration file."""
        # Load the test configuration
        with open(
            pipeline_builder_configuration_file_path,
            "r",
        ) as f:
            config_dict = json.load(f)

        # Extract configuration values for assertions
        domain_name = config_dict[
            "domain_name"
        ]
        first_pipeline_name = (
            config_dict["pipelines"][0][
                "name"
            ]
        )
        first_thin_slice = config_dict[
            "pipelines"
        ][0]["thin_slices"][0]["name"]

        # Generate the pipeline
        pipeline_path = generate_pipeline(
            config_dict,
            pipeline_output_folder_absolute_path,
        )

        # Check the pipeline directory was created
        domain_path = os.path.join(
            pipeline_output_folder_absolute_path,
            "bclearer_pipelines",
            domain_name,
        )
        assert os.path.exists(
            domain_path
        )

        # Check key directories
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

        # Check app runner file
        app_runner_path = os.path.join(
            domain_path,
            "b_source",
            "app_runners",
            f"{domain_name}_b_clearer_pipeline_b_application_runner.py",
        )
        assert os.path.exists(
            app_runner_path
        )

        # Check pipeline directories
        pipeline_path = os.path.join(
            domain_path,
            "b_source",
            first_pipeline_name,
        )
        assert os.path.exists(
            pipeline_path
        )
        assert os.path.exists(
            os.path.join(
                pipeline_path, "objects"
            )
        )
        assert os.path.exists(
            os.path.join(
                pipeline_path,
                "orchestrators",
            )
        )

        # Check pipeline orchestrator
        orchestrator_path = os.path.join(
            pipeline_path,
            "orchestrators",
            "pipeline",
            f"{first_pipeline_name}_orchestrator.py",
        )
        assert os.path.exists(
            orchestrator_path
        )

        # Check thin slice orchestrator
        thin_slice_path = os.path.join(
            pipeline_path,
            "orchestrators",
            "thin_slices",
            f"{first_thin_slice}_orchestrator.py",
        )
        assert os.path.exists(
            thin_slice_path
        )

        # Check stage orchestrator
        stages_path = os.path.join(
            pipeline_path,
            "orchestrators",
            "stages",
        )
        assert os.path.exists(
            os.path.join(
                stages_path,
                f"{first_pipeline_name}_1c_collect_orchestrator.py",
            )
        )
        assert os.path.exists(
            os.path.join(
                stages_path,
                f"{first_pipeline_name}_2l_load_orchestrator.py",
            )
        )
        assert os.path.exists(
            os.path.join(
                stages_path,
                f"{first_pipeline_name}_3e_evolve_orchestrator.py",
            )
        )

        # Check b_units
        b_units_path = os.path.join(
            pipeline_path,
            "objects",
            "b_units",
        )

        # Extract configuration values for b_units and sub-stages
        first_collect_stage_b_units = (
            config_dict["pipelines"][0][
                "thin_slices"
            ][0]["stages"][0]["b_units"]
        )
        evolve_stage_index = next(
            (
                i
                for i, stage in enumerate(
                    config_dict[
                        "pipelines"
                    ][0]["thin_slices"][
                        0
                    ][
                        "stages"
                    ]
                )
                if stage["name"]
                == "3e_evolve"
            ),
            None,
        )

        if (
            evolve_stage_index
            is not None
        ):
            evolve_stage = config_dict[
                "pipelines"
            ][0]["thin_slices"][0][
                "stages"
            ][
                evolve_stage_index
            ]
            if evolve_stage[
                "sub_stages"
            ]:
                first_sub_stage_name = (
                    evolve_stage[
                        "sub_stages"
                    ][0]["name"]
                )
                first_sub_stage_b_units = evolve_stage[
                    "sub_stages"
                ][
                    0
                ][
                    "b_units"
                ]

                # Check collect stage b_units
                collect_b_units_path = os.path.join(
                    b_units_path,
                    f"{first_pipeline_name}_1c_collect",
                )
                assert os.path.exists(
                    collect_b_units_path
                )
                for (
                    b_unit
                ) in first_collect_stage_b_units:
                    assert os.path.exists(
                        os.path.join(
                            collect_b_units_path,
                            f"{b_unit}_b_units.py",
                        )
                    )

                # Check evolve stage sub-stages
                evolve_sub_stages_path = os.path.join(
                    pipeline_path,
                    "orchestrators",
                    "sub_stages",
                    f"{first_pipeline_name}_3e_evolve_{first_sub_stage_name}",
                )
                assert os.path.exists(
                    evolve_sub_stages_path
                )
                assert os.path.exists(
                    os.path.join(
                        evolve_sub_stages_path,
                        f"{first_pipeline_name}_3e_evolve_{first_sub_stage_name}_orchestrator.py",
                    )
                )

                # Check sub-stage b_units
                evolve_sub_stage_b_units_path = os.path.join(
                    b_units_path,
                    f"{first_pipeline_name}_3e_evolve",
                    f"{first_pipeline_name}_3e_evolve_{first_sub_stage_name}",
                )
                assert os.path.exists(
                    evolve_sub_stage_b_units_path
                )
                for (
                    b_unit
                ) in first_sub_stage_b_units:
                    assert os.path.exists(
                        os.path.join(
                            evolve_sub_stage_b_units_path,
                            f"{b_unit}_b_units.py",
                        )
                    )

    def test_generate_pipeline_file_contents(
        self,
        pipeline_builder_configuration_file_path,
        pipeline_output_folder_absolute_path,
        template_pipeline_folder_absolute_path,
    ):
        """Test that generated files have the correct content."""
        # Load the test configuration
        with open(
            pipeline_builder_configuration_file_path,
            "r",
        ) as f:
            config_dict = json.load(f)

        # Extract configuration values for assertions
        domain_name = config_dict[
            "domain_name"
        ]
        first_pipeline_name = (
            config_dict["pipelines"][0][
                "name"
            ]
        )
        first_thin_slice = config_dict[
            "pipelines"
        ][0]["thin_slices"][0]["name"]
        first_b_unit = config_dict[
            "pipelines"
        ][0]["thin_slices"][0][
            "stages"
        ][
            0
        ][
            "b_units"
        ][
            0
        ]

        # Generate the pipeline
        generate_pipeline(
            config_dict,
            pipeline_output_folder_absolute_path,
        )

        # Check the application runner file content
        app_runner_path = os.path.join(
            pipeline_output_folder_absolute_path,
            "bclearer_pipelines",
            domain_name,
            "b_source",
            "app_runners",
            f"{domain_name}_b_clearer_pipeline_b_application_runner.py",
        )

        with open(
            app_runner_path, "r"
        ) as f:
            content = f.read()
            assert (
                "from bclearer_orchestration_services.b_app_runner_service.b_application_runner import"
                in content
            )
            assert (
                f"from bclearer_pipelines.{domain_name}.b_source.app_runners.runners.{domain_name}_b_clearer_pipelines_runner import"
                in content
            )
            assert (
                f"run_{domain_name}_b_clearer_pipelines"
                in content
            )
            assert (
                f"run_{domain_name}_b_clearer_pipeline_b_application"
                in content
            )

        # Check the pipelines runner file content
        pipelines_runner_path = os.path.join(
            pipeline_output_folder_absolute_path,
            "bclearer_pipelines",
            domain_name,
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
                "from bclearer_orchestration_services.reporting_service.wrappers.run_and_log_function_wrapper_latest import"
                in content
            )
            assert (
                f"from bclearer_pipelines.{domain_name}.b_source.app_runners.runners.{first_pipeline_name}_runner import"
                in content
            )
            assert (
                f"run_{first_pipeline_name}"
                in content
            )

        # Check b_unit file content
        b_unit_path = os.path.join(
            pipeline_output_folder_absolute_path,
            "bclearer_pipelines",
            domain_name,
            "b_source",
            first_pipeline_name,
            "objects",
            "b_units",
            f"{first_pipeline_name}_1c_collect",
            f"{first_b_unit}_b_units.py",
        )

        with open(
            b_unit_path, "r"
        ) as f:
            content = f.read()
            assert (
                "from bclearer_core.configurations.datastructure.logging_inspection_level_b_enums import"
                in content
            )

            # Create proper class name for assertion (CaBUnitBUnits)
            class_name_parts = (
                first_b_unit.split("_")
            )
            class_name = "".join(
                part.capitalize()
                for part in class_name_parts
            )
            assert (
                f"class {class_name}BUnits:"
                in content
            )
            assert (
                "def run(self) -> None:"
                in content
            )
            assert (
                "def b_unit_process_function("
                in content
            )

        # Check orchestrator file content
        orchestrator_path = os.path.join(
            pipeline_output_folder_absolute_path,
            "bclearer_pipelines",
            domain_name,
            "b_source",
            first_pipeline_name,
            "orchestrators",
            "pipeline",
            f"{first_pipeline_name}_orchestrator.py",
        )

        with open(
            orchestrator_path, "r"
        ) as f:
            content = f.read()
            assert (
                f"from bclearer_pipelines.{domain_name}.b_source.{first_pipeline_name}.orchestrators.thin_slices.{first_thin_slice}_orchestrator import"
                in content
            )
            assert (
                f"orchestrate_{first_thin_slice}"
                in content
            )
            assert (
                f"def orchestrate_{first_pipeline_name}():"
                in content
            )
