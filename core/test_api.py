import pytest
from django.urls import reverse
from rest_framework.test import APIClient


def test_api_health_check():
    client = APIClient()
    response = client.get(reverse("health_check"))
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


@pytest.mark.parametrize(
    "a,b,operator,expected",
    [
        (1, 2, "+", 3),
        (6, 1, "-", 5),
        (4, 9, "*", 36),
        (17, 8, "/", 2),
    ],
)
def test_calculate_parametrized(a, b, operator, expected):
    client = APIClient()
    response = client.post(
        reverse("calculate"),
        {"operand_one": a, "operand_two": b, "operator": operator},
        format="json",
    )

    assert response.status_code == 200
    assert response.json()["result"] == expected


@pytest.mark.parametrize(
    "a,b,operator,expected",
    [
        (1, 2, "plus", "Unsupported operator"),
        (4, 0, "/", "Division by zero is not allowed"),
    ],
)
def test_calculate_invalid_operation(a, b, operator, expected):
    client = APIClient()
    response = client.post(
        reverse("calculate"), {"operand_one": a, "operand_two": b, "operator": operator}
    )
    assert response.status_code == 400
    assert list(response.json().values())[0][0] == expected
