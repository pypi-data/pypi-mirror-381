import json
import os
import shutil
import subprocess
import sys
from io import StringIO
from pathlib import Path
from unittest import mock

import pytest
from bclearer_core.pipeline_builder.cli import (
    create_parser,
    interactive_config,
    run_cli,
    save_sample_config,
)


class TestPipelineBuilderCLI:
    """Test class for the pipeline builder CLI functionality."""

    @pytest.fixture(autouse=True)
    def setup_method(
        self,
        pipeline_output_folder_absolute_path,
    ):
        """Setup method that runs before each test."""
        # Clean up any existing test pipelines from previous runs
        self.test_domain_path = os.path.join(
            pipeline_output_folder_absolute_path,
            "pipelines",
            "test_domain",
        )

        if os.path.exists(
            self.test_domain_path
        ):
            shutil.rmtree(
                self.test_domain_path
            )

        # Create a temporary config file for CLI tests
        self.temp_config_path = os.path.join(
            pipeline_output_folder_absolute_path,
            "temp_config.json",
        )
        self.temp_sample_path = os.path.join(
            pipeline_output_folder_absolute_path,
            "sample_config.json",
        )

    def teardown_method(self):
        """Cleanup after tests."""
        if os.path.exists(
            self.temp_config_path
        ):
            os.remove(
                self.temp_config_path
            )

        if os.path.exists(
            self.temp_sample_path
        ):
            os.remove(
                self.temp_sample_path
            )

    def test_parser_create_command(
        self,
    ):
        """Test the CLI argument parser with create command."""
        parser = create_parser()
        args = parser.parse_args(
            [
                "create",
                "--config",
                "test.json",
                "--output",
                "/test/path",
            ]
        )

        assert args.command == "create"
        assert (
            args.config == "test.json"
        )
        assert (
            args.output == "/test/path"
        )
        assert args.interactive == False

    def test_parser_sample_command(
        self,
    ):
        """Test the CLI argument parser with sample command."""
        parser = create_parser()
        args = parser.parse_args(
            [
                "sample",
                "--output",
                "test_sample.json",
            ]
        )

        assert args.command == "sample"
        assert (
            args.output
            == "test_sample.json"
        )

    def test_save_sample_config(self):
        """Test saving a sample configuration file."""
        save_sample_config(
            self.temp_sample_path
        )

        # Check the file exists
        assert os.path.exists(
            self.temp_sample_path
        )

        # Check the content is valid JSON
        with open(
            self.temp_sample_path, "r"
        ) as f:
            config = json.load(f)

        # Verify basic structure
        assert "domain_name" in config
        assert "pipelines" in config
        assert (
            len(config["pipelines"]) > 0
        )

    @mock.patch("builtins.input")
    def test_interactive_config(
        self, mock_input
    ):
        """Test the interactive configuration process."""
        # Setup mock inputs
        mock_inputs = [
            "test_interactive_domain",  # Domain name
            "1",  # Number of pipelines
            "test_interactive_pipeline",  # Pipeline name
            "1",  # Number of thin slices
            "test_thin_slice",  # Thin slice name
            "y",  # Include Collect stage
            "y",  # Has direct b_units
            "ca,cb",  # B-unit names for collect
            "n",  # No sub-stages for collect
            "y",  # Include Load stage
            "y",  # Has direct b_units
            "la,lb",  # B-unit names for load
            "n",  # No sub-stages for load
            "y",  # Include Evolve stage
            "n",  # No direct b_units
            "y",  # Has sub-stages
            "2",  # Number of sub-stages
            "sub_stage_1",  # Sub-stage 1 name
            "ea1,ea2",  # B-unit names for sub-stage 1
            "sub_stage_2",  # Sub-stage 2 name
            "eb1,eb2",  # B-unit names for sub-stage 2
            "n",  # Don't include Assimilate stage
            "n",  # Don't include Reuse stage
        ]

        mock_input.side_effect = (
            mock_inputs
        )

        # Call the interactive config function
        config = interactive_config()

        # Check the configuration structure
        assert (
            config["domain_name"]
            == "test_interactive_domain"
        )
        assert (
            len(config["pipelines"])
            == 1
        )
        assert (
            config["pipelines"][0][
                "name"
            ]
            == "test_interactive_pipeline"
        )
        assert (
            len(
                config["pipelines"][0][
                    "thin_slices"
                ]
            )
            == 1
        )

        # Check stages
        stages = config["pipelines"][0][
            "thin_slices"
        ][0]["stages"]
        assert (
            len(stages) == 3
        )  # Only included Collect, Load, and Evolve

        # Check Collect stage
        collect_stage = next(
            s
            for s in stages
            if s["name"] == "1c_collect"
        )
        assert (
            len(
                collect_stage["b_units"]
            )
            == 2
        )
        assert collect_stage[
            "b_units"
        ] == ["ca", "cb"]

        # Check Evolve stage
        evolve_stage = next(
            s
            for s in stages
            if s["name"] == "3e_evolve"
        )
        assert (
            len(
                evolve_stage[
                    "sub_stages"
                ]
            )
            == 2
        )
        assert (
            evolve_stage["sub_stages"][
                0
            ]["name"]
            == "sub_stage_1"
        )
        assert evolve_stage[
            "sub_stages"
        ][0]["b_units"] == [
            "ea1",
            "ea2",
        ]

    @mock.patch("sys.argv")
    def test_cli_sample_command(
        self,
        mock_argv,
        pipeline_output_folder_absolute_path,
    ):
        """Test the CLI sample command."""
        # Setup mock command line args
        output_path = os.path.join(
            pipeline_output_folder_absolute_path,
            "cli_sample.json",
        )
        mock_argv.__getitem__.side_effect = lambda i: [
            "bclearer-pipeline-builder",
            "sample",
            "--output",
            output_path,
        ][
            i
        ]

        # Call the CLI function with mocked arguments
        with mock.patch(
            "sys.argv",
            [
                "bclearer-pipeline-builder",
                "sample",
                "--output",
                output_path,
            ],
        ):
            run_cli()

        # Check the sample file was created
        assert os.path.exists(
            output_path
        )

        # Check it contains valid JSON
        with open(
            output_path, "r"
        ) as f:
            config = json.load(f)

        # Verify basic structure
        assert "domain_name" in config
        assert "pipelines" in config
        assert (
            len(config["pipelines"]) > 0
        )
