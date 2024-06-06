import datetime
from unittest import mock
import pytest
from app.main import outdated_products


@pytest.fixture()
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "expected_result, today_changed_date",
    [
        (
            ["salmon", "chicken", "duck"],
            datetime.date(2022, 2, 11)
        ),
        (
            ["chicken", "duck"],
            datetime.date(2022, 2, 8)
        ),
        (
            ["duck"],
            datetime.date(2022, 2, 3)
        ),
        (
            [],
            datetime.date(2022, 1, 15)
        ),
        (
            [],
            datetime.date(2022, 2, 1)
        )
    ]
)
def test_outdated_products(
        products: list,
        expected_result: str,
        today_changed_date: callable
) -> None:
    with mock.patch("app.main.datetime.date") as mock_time:
        mock_time.today.return_value = today_changed_date
        assert outdated_products(products) == expected_result
