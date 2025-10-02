import pytest
from bclearer_interop_services.file_system_service.objects.folders import (
    Folders,
)
from bclearer_orchestration_services.b_app_runner_service.b_app_runner import (
    run_b_application,
)
from bclearer_orchestration_services.log_environment_utility_service.common_knowledge.environment_log_level_types import (
    EnvironmentLogLevelTypes,
)


def app_runner_method(message):
    print(message)


class TestBAppRunner:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        pass

    def test_app_runner(
        self,
        test_message,
    ):
        run_b_application(
            app_startup_method=app_runner_method,
            environment_log_level_type=EnvironmentLogLevelTypes.FULL,
            output_folder_prefix="prefix",
            output_folder_suffix="suffix",
            output_root_folder=Folders(
                r"/bclearer_orchestration_services\tests\data",
            ),
            message=test_message,
        )

    def teardown_method(self):
        pass
