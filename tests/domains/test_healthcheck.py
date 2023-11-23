from src.wellness_manager.domains.healthcheck import HealthCheck


class TestHealtCheck:
    def test_create_healthcheck(self):
        health_check = HealthCheck(name="test", title="Test HC")

        assert health_check.name == "test"
        assert health_check.title == "Test HC"
        assert health_check.description == ""
        assert health_check.beats == []
        assert health_check.created_at is not None
