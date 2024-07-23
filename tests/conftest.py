from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from src.wellness_manager.domains.healthcheck import HealthCheck

if TYPE_CHECKING:
    from faker import Faker


@pytest.fixture()
def health_check_without_beat(faker: Faker) -> HealthCheck:
    return HealthCheck(name=faker.company(), title=faker.name())
