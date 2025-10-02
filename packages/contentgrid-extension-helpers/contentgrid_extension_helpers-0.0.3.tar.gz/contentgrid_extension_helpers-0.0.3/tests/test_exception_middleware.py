import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from contentgrid_hal_client.exceptions import (
    NotFound,
    Unauthorized,
    BadRequest,
    IncorrectAttributeType,
    NonExistantAttribute,
    MissingRequiredAttribute,
    MissingHALTemplate,
)
from requests.exceptions import HTTPError
from contentgrid_extension_helpers.exceptions import LLMDenyException
from contentgrid_extension_helpers.problem_response import ProblemResponse
from fixtures import *


@pytest.fixture(params=["client", "client_no_db"])
def test_client(request):
    """Parametrized fixture that provides both client and client_no_db"""
    if request.param == "client":
        return request.getfixturevalue("client")
    else:
        return request.getfixturevalue("client_no_db")


def test_no_exception(test_client: TestClient):
    """Tests the middleware when no exception is raised."""

    @test_client.app.get("/no-error")
    async def no_error():
        return {"message": "OK"}

    response = test_client.get("/no-error")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}


def test_no_exception_with_origin(test_client: TestClient):
    """Tests the middleware when no exception is raised and origin is present."""

    @test_client.app.get("/no-error")
    async def no_error():
        return {"message": "OK"}

    response = test_client.get("/no-error", headers={"Origin": "https://example.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}


def test_not_found_exception(test_client: TestClient):
    """Tests the NotFound exception handling."""

    @test_client.app.get("/not-found")
    async def not_found():
        raise NotFound()

    response = test_client.get("/not-found")
    assert response.status_code == 404
    problem = response.json()
    assert problem["title"] == "Not found"
    assert problem["type"] == "https://problems.contentgrid.test/not-found"


def test_unauthorized_exception(test_client: TestClient):
    """Tests the Unauthorized exception handling."""

    @test_client.app.get("/unauthorized")
    async def unauthorized():
        raise Unauthorized()

    response = test_client.get("/unauthorized", headers={"Origin": "https://example.com"})
    assert response.status_code == 401
    problem = response.json()
    assert problem["title"] == "Unauthorized"
    assert problem["type"] == "https://problems.contentgrid.test/unauthorized"


def test_bad_request_exception(test_client: TestClient):
    """Tests the BadRequest exception handling."""

    @test_client.app.get("/bad-request")
    async def bad_request():
        raise BadRequest()

    response = test_client.get("/bad-request")
    assert response.status_code == 400
    problem = response.json()
    assert problem["title"] == "Bad Request"
    assert problem["type"] == "https://problems.contentgrid.test/bad-request"


def test_incorrect_attribute_type_exception(test_client: TestClient):
    """Tests the IncorrectAttributeType exception handling."""

    @test_client.app.get("/incorrect-attribute")
    async def incorrect_attribute():
        raise IncorrectAttributeType("Incorrect type")

    response = test_client.get("/incorrect-attribute", headers={"Origin": "https://different.com"})
    assert response.status_code == 400
    problem = response.json()
    assert problem["title"] == "Incorrect Attribute Type"
    assert problem["type"] == "https://problems.contentgrid.test/incorrect-attribute-type"
    assert problem["detail"] == "Incorrect type"


def test_non_existent_attribute_exception(test_client: TestClient):
    """Tests the NonExistantAttribute exception handling."""

    @test_client.app.get("/non-existent-attribute")
    async def non_existent_attribute():
        raise NonExistantAttribute("Attribute does not exist")

    response = test_client.get("/non-existent-attribute")
    assert response.status_code == 404
    problem = response.json()
    assert problem["title"] == "Non-Existent Attribute"
    assert problem["type"] == "https://problems.contentgrid.test/non-existent-attribute"
    assert problem["detail"] == "Attribute does not exist"


def test_missing_required_attribute_exception(test_client: TestClient):
    """Tests the MissingRequiredAttribute exception handling."""

    @test_client.app.get("/missing-required-attribute")
    async def missing_required_attribute():
        raise MissingRequiredAttribute("Missing attribute")

    response = test_client.get("/missing-required-attribute")
    assert response.status_code == 400
    problem = response.json()
    assert problem["title"] == "Missing Required Attribute"
    assert problem["type"] == "https://problems.contentgrid.test/missing-required-attribute"
    assert problem["detail"] == "Missing attribute"


def test_missing_hal_template_exception(test_client: TestClient):
    """Tests the MissingHALTemplate exception handling."""

    @test_client.app.get("/missing-hal-template")
    async def missing_hal_template():
        raise MissingHALTemplate("HAL template missing")

    response = test_client.get("/missing-hal-template")
    assert response.status_code == 404
    problem = response.json()
    assert problem["title"] == "Missing HAL Template"
    assert problem["type"] == "https://problems.contentgrid.test/missing-hal-template"
    assert problem["detail"] == "HAL template missing"


def test_http_error_exception(test_client: TestClient):
    """Tests the HTTPError exception handling."""

    @test_client.app.get("/http-error")
    async def http_error():
        response = MagicMock()
        response.status_code = 418  # I'm a teapot!
        raise HTTPError("Teapot error", response=response)

    response = test_client.get("/http-error")
    assert response.status_code == 418
    problem = response.json()
    assert problem["title"] == "HTTP Error"
    assert problem["type"] == "https://problems.contentgrid.test/http-error"
    assert problem["detail"] == "An HTTP error occurred: Teapot error"


def test_llm_deny_exception(test_client: TestClient):
    """Tests the LLMDenyException exception handling."""

    @test_client.app.get("/llm-deny")
    async def llm_deny():
        raise LLMDenyException("LLM denied")

    response = test_client.get("/llm-deny")
    assert response.status_code == 400
    problem = response.json()
    assert problem["title"] == "Request Denied"
    assert problem["type"] == "https://problems.contentgrid.test/request-denied"
    assert problem["detail"] == "LLM denied"


def test_generic_exception(test_client: TestClient):
    """Tests the generic Exception handling."""

    @test_client.app.get("/generic-exception")
    async def generic_exception():
        raise Exception("Something went wrong")

    response = test_client.get("/generic-exception")
    assert response.status_code == 500
    problem = response.json()
    assert problem["title"] == "Internal server error"
    assert problem["type"] == "https://problems.contentgrid.test/unknown"
    assert problem["detail"] == "An unexpected error occurred: Something went wrong"


def test_http_error_no_response(test_client: TestClient):
    """Tests HTTPError when e.response is None"""
    @test_client.app.get("/http-error-no-response")
    async def http_error_no_response():
        raise HTTPError("Generic HTTP Error")

    response = test_client.get("/http-error-no-response")
    assert response.status_code == 500
    problem = response.json()
    assert problem["title"] == "HTTP Error"
    assert problem["type"] == "https://problems.contentgrid.test/http-error"