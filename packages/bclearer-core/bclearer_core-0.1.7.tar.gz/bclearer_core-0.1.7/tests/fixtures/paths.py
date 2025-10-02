import os

import pytest


@pytest.fixture(scope="session")
def data_folder_absolute_path():
    data_input_relative_path = "../data"
    base_path = os.path.dirname(
        os.path.abspath(__file__),
    )
    data_folder_absolute_path = os.path.normpath(
        os.path.join(
            base_path,
            data_input_relative_path,
        ),
    )
    return data_folder_absolute_path


@pytest.fixture(scope="session")
def data_input_folder_absolute_path(
    data_folder_absolute_path,
):
    data_input_relative_path = "input"

    data_input_folder_absolute_path = (
        os.path.join(
            data_folder_absolute_path,
            data_input_relative_path,
        )
    )

    return (
        data_input_folder_absolute_path
    )


@pytest.fixture(scope="session")
def data_output_folder_absolute_path(
    data_folder_absolute_path,
):
    data_output_relative_path = "output"

    data_output_folder_absolute_path = (
        os.path.join(
            data_folder_absolute_path,
            data_output_relative_path,
        )
    )

    return (
        data_output_folder_absolute_path
    )


@pytest.fixture(scope="session")
def configurations_folder_absolute_path():
    configurations_folder_relative_path = (
        "../configurations"
    )
    base_path = os.path.dirname(
        os.path.abspath(__file__),
    )
    configurations_folder_absolute_path = os.path.normpath(
        os.path.join(
            base_path,
            configurations_folder_relative_path,
        ),
    )
    return configurations_folder_absolute_path


@pytest.fixture(scope="session")
def log_folder_absolute_path(
    data_folder_absolute_path,
):
    log_folder_relative_path = "logs"
    log_folder_absolute_path = (
        os.path.join(
            data_folder_absolute_path,
            log_folder_relative_path,
        )
    )
    return log_folder_absolute_path


@pytest.fixture(scope="session")
def template_pipeline_folder_absolute_path():
    """
    Find the template_pipeline directory by searching up from the current directory.
    This approach is more robust to different directory structures.
    """
    # Start from the current directory
    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    # Try different possible paths to find the template_pipeline directory
    possible_relative_paths = [
        "../../../../pipelines/template_pipeline",  # If 4 levels up from fixtures
        "../../../pipelines/template_pipeline",  # If 3 levels up from fixtures
        "../../../../../pipelines/template_pipeline",  # If 5 levels up from fixtures
        "../../../../../../pipelines/template_pipeline",  # If 6 levels up from fixtures
    ]

    for (
        relative_path
    ) in possible_relative_paths:
        path = os.path.normpath(
            os.path.join(
                current_dir,
                relative_path,
            )
        )
        if os.path.exists(
            path
        ) and os.path.isdir(path):
            return path

    # If we're here, we need to search upwards through the directory tree
    root_dir = current_dir
    while True:
        # Move up one level
        parent_dir = os.path.dirname(
            root_dir
        )
        if (
            parent_dir == root_dir
        ):  # We've reached the filesystem root
            break
        root_dir = parent_dir

        # Check if pipelines/template_pipeline exists at this level
        template_path = os.path.join(
            root_dir,
            "pipelines",
            "template_pipeline",
        )
        if os.path.exists(
            template_path
        ) and os.path.isdir(
            template_path
        ):
            return template_path

    # If we couldn't find it, try using a direct path from D: drive (for Windows systems)
    if os.name == "nt":
        direct_path = r"D:\S\bclearer\ol_bclearer_pdk\pipelines\template_pipeline"
        if os.path.exists(
            direct_path
        ) and os.path.isdir(
            direct_path
        ):
            return direct_path

    # If we get here, we couldn't find the template pipeline directory
    raise FileNotFoundError(
        "Could not find template_pipeline directory. Please make sure it exists "
        "in your repository at 'pipelines/template_pipeline'."
    )


@pytest.fixture(scope="session")
def pipeline_builder_configuration_file_path(
    configurations_folder_absolute_path,
):
    config_path_relative = "pipeline_builder/sample_pipeline_config.json"
    config_file_path = os.path.join(
        configurations_folder_absolute_path,
        config_path_relative,
    )
    return config_file_path


@pytest.fixture(scope="session")
def pipeline_output_folder_absolute_path(
    data_output_folder_absolute_path,
):
    output_folder_relative = (
        "pipeline_builder"
    )
    output_folder_path = os.path.join(
        data_output_folder_absolute_path,
        output_folder_relative,
    )

    # Create the folder if it doesn't exist
    os.makedirs(
        output_folder_path,
        exist_ok=True,
    )

    return output_folder_path
