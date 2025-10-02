"""Tests for the template extractor."""

import os
import shutil
import tempfile
from pathlib import Path

import pytest
from bclearer_core.pipeline_builder.template_extractor import (
    TemplateExtractor,
    update_templates_from_pipeline,
)


class TestTemplateExtractor:
    """Test class for the template extractor functionality."""

    @pytest.fixture(scope="function")
    def temp_dir(self):
        """Create a temporary directory for testing."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    def test_template_extractor_initialization_errors(
        self, temp_dir
    ):
        """Test error handling during initialization."""
        # Test non-existent template path
        with pytest.raises(
            FileNotFoundError
        ) as excinfo:
            TemplateExtractor(
                "/path/does/not/exist"
            )
        assert (
            "Template path not found"
            in str(excinfo.value)
        )

        # Test file as template path (not a directory)
        test_file = os.path.join(
            temp_dir, "test.txt"
        )
        with open(test_file, "w") as f:
            f.write("test")

        with pytest.raises(
            NotADirectoryError
        ) as excinfo:
            TemplateExtractor(test_file)
        assert (
            "Template path is not a directory"
            in str(excinfo.value)
        )

    def test_create_minimal_template(
        self,
        temp_dir,
        template_pipeline_folder_absolute_path,
    ):
        """Test creating and using a minimal template structure."""
        # Create a minimal template structure for testing
        template_dir = os.path.join(
            temp_dir, "test_template"
        )
        os.makedirs(template_dir)

        # Create b_source directory
        b_source_dir = os.path.join(
            template_dir, "b_source"
        )
        os.makedirs(b_source_dir)

        # Create app_runners directory
        app_runners_dir = os.path.join(
            b_source_dir, "app_runners"
        )
        os.makedirs(app_runners_dir)

        # Create a simple application runner file
        app_runner_file = os.path.join(
            app_runners_dir,
            "aa_b_clearer_pipeline_b_application_runner.py",
        )
        with open(
            app_runner_file, "w"
        ) as f:
            f.write(
                """from bclearer_orchestration_services.b_app_runner_service.b_application_runner import (
    run_b_application,
)
from aa.b_source.app_runners.runners.aa_b_clearer_pipelines_runner import (
    run_aa_b_clearer_pipelines,
)


def run_aa_b_clearer_pipeline_b_application() -> (
    None
):
    run_b_application(
        app_startup_method=run_aa_b_clearer_pipelines
    )
"""
            )

        # Create output directory for extracted templates
        output_dir = os.path.join(
            temp_dir, "templates"
        )

        # Extract templates
        extractor = TemplateExtractor(
            template_dir
        )
        extractor.extract_templates(
            output_dir
        )

        # Check that the application runner template was extracted
        app_runner_template_file = (
            os.path.join(
                output_dir,
                "application_runner.py",
            )
        )
        assert os.path.exists(
            app_runner_template_file
        )

        # Check template content was properly formatted
        with open(
            app_runner_template_file,
            "r",
        ) as f:
            content = f.read()
            assert (
                "APPLICATION_RUNNER_TEMPLATE"
                in content
            )
            assert (
                "{domain_name}"
                in content
            )  # Should have replaced "aa" with "{domain_name}"
            assert (
                "aa" not in content
            )  # Should not contain the original domain name

    def test_update_templates_from_pipeline(
        self,
        temp_dir,
        template_pipeline_folder_absolute_path,
    ):
        """Test the update_templates_from_pipeline function."""
        # Create output directory
        output_dir = os.path.join(
            temp_dir, "templates"
        )

        # Call the function
        update_templates_from_pipeline(
            template_pipeline_folder_absolute_path,
            output_dir,
        )

        # Check that key template files were created
        expected_files = [
            "application_runner.py",
            "b_unit.py",
            "b_unit_creator_and_runner.py",
            "conftest.py",
            "e2e_test.py",
            "pipeline_orchestrator.py",
            "pipeline_runner.py",
            "pipelines_runner.py",
            "stage_orchestrator.py",
            "sub_stage_orchestrator.py",
            "thin_slice_orchestrator.py",
            "__init__.py",
        ]

        for file in expected_files:
            assert os.path.exists(
                os.path.join(
                    output_dir, file
                )
            ), f"File {file} was not created"
