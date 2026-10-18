from unittest.mock import patch
import pytest
from requests.exceptions import HTTPError
from src.main_client import MainClient


@pytest.fixture
def client():
  return MainClient()


@patch("src.main_client.requests.get")
def test_fetch_data_success(mock_get, client):
  # মক রেসপন্স সেটআপ
  mock_get.return_value.status_code = 200
  mock_get.return_value.json.return_value = {"status": "success", "id": 1}

  # ফাংশন কল
  result = client.fetch_data("test-endpoint")

  # অ্যাসার্ট বা যাচাই
  assert result["status"] == "success"
  assert result["id"] == 1
  mock_get.assert_called_once_with(
      "https://jsonplaceholder.typicode.com/test-endpoint", timeout=5
  )


@patch("src.main_client.requests.get")
def test_fetch_data_error(mock_get, client):
  # এরর হ্যান্ডলিং টেস্ট
  mock_get.return_value.raise_for_status.side_effect = HTTPError(
      "500 Server Error"
  )

  with pytest.raises(HTTPError):
    client.fetch_data("error-endpoint")
    
