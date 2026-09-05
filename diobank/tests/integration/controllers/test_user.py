from http import HTTPStatus

def test_get_user_success(client):
    response = client.get("/users/4")
    assert response.status_code == HTTPStatus.OK