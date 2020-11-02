from run import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'PHC_test'
    assert response.status_code == 200