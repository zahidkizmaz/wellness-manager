from src.wellness_manager.domains.heartbeat import HeartBeat


class TestHeartBeat:
    def test_create_heartbeat(self):
        heartbeat = HeartBeat(name="test", location="test.com")

        assert heartbeat.name == "test"
        assert heartbeat.location == "test.com"
        assert heartbeat.finished_at is None
        assert heartbeat.created_at is not None
