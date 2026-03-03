import requestst_simple
import data
import copy


new_user = requestst_simple.post_new_user()
response = new_user.json()
data.token['Authorization'] ='Bearer ' +  response['authToken']
print(data.token)


new_kit = requestst_simple.post_new_kit()
response = new_kit.json()
data.id_kits_with_token = response['id']
print(data.id_kits_with_token)


def test_get_with_token():
    response = requestst_simple.get_kit_with_token(data.id_kits_with_token, data.token)
    assert response.status_code == 200

def test_get_without_200():
    response = requestst_simple.get_kit_without_token(data.id_kits_with_token)
    assert response.status_code == 401

def test_get_not_real_id():
    response = requestst_simple.get_kit_with_token(11223344, data.token)
    assert response.status_code == 404

def test_get_id_letter():
    response = requestst_simple.get_kit_with_token('two', data.token)
    assert response.status_code == 500

def test_get_another_token():
    token = data.token.copy()
    token['Authorization'] = 'Bearer fsadfhsakdc324284hsac'    
    response = requestst_simple.get_kit_with_token(data.id_kits_with_token, token)
    assert response.status_code == 401

def test_put_posistive():
    response = requestst_simple.put_kit_with_token(data.id_kits_with_token, data.token, data.body_put_kits)
    assert response.status_code == 200

def test_put_negative_without_empty_product_list():
    body = copy.deepcopy(data.body_put_kits)
    body['productsList'].pop()
    print(body)
    response = requestst_simple.put_kit_with_token(data.id_kits_with_token, data.token, body)
    assert response.status_code == 400

def test_put_without_letter_productList():
    body = copy.deepcopy(data.body_put_kits)
    body['productsList'].pop(0)
    response = requestst_simple.put_kit_with_token(data.id_kits_with_token, data.token, body)
    assert response.status_code == 400

def test_put_without_id_in_list():
    body = copy.deepcopy(data.body_put_kits)
    body['productsList'][0].pop('id')
    response = requestst_simple.put_kit_with_token(data.id_kits_with_token, data.token, body)
    assert response.status_code == 400

def test_put_without_quantity_in_list():
    body = copy.deepcopy(data.body_put_kits)
    body['productsList'][0].pop('quantity')
    response = requestst_simple.put_kit_with_token(data.id_kits_with_token, data.token, body)
    assert response.status_code == 400

def test_put_id_string():
    body = copy.deepcopy(data.body_put_kits)
    body['productsList'][0]['id'] = '10'
    response = requestst_simple.put_kit_with_token(data.id_kits_with_token, data.token, body)
    assert response.status_code == 400

def test_put_id_null():
    body = copy.deepcopy(data.body_put_kits)
    body['productsList'][0]['id'] = None
    response = requestst_simple.put_kit_with_token(data.id_kits_with_token, data.token, body)
    assert response.status_code == 400

def test_put_id_not_real():
    body = copy.deepcopy(data.body_put_kits)
    body['productsList'][0]['id'] = 20000000000000
    response = requestst_simple.put_kit_with_token(data.id_kits_with_token, data.token, body)
    assert response.status_code == 404

def test_put_id_zero():
    body = copy.deepcopy(data.body_put_kits)
    body['productsList'][0]['id'] = 0
    response = requestst_simple.put_kit_with_token(data.id_kits_with_token, data.token, body)
    assert response.status_code == 400

def test_put_quantity_null():
    body = copy.deepcopy(data.body_put_kits)
    body['productsList'][0]['quantity'] = None
    response = requestst_simple.put_kit_with_token(data.id_kits_with_token, data.token, body)
    assert response.status_code == 400

def test_put_quantity_string():
    body = copy.deepcopy(data.body_put_kits)
    body['productsList'][0]['quantity'] = '3'
    response = requestst_simple.put_kit_with_token(data.id_kits_with_token, data.token, body)
    assert response.status_code == 400

def test_put_quantity_zero():
    body = copy.deepcopy(data.body_put_kits)
    body['productsList'][0]['quantity'] = 0
    response = requestst_simple.put_kit_with_token(data.id_kits_with_token, data.token, body)
    assert response.status_code == 400

def test_put_not_real_id():
    response = requestst_simple.put_kit_with_token(1555555, data.token, data.body_put_kits)
    assert response.status_code == 404


def test_put_string_id():
    response = requestst_simple.put_kit_with_token("two", data.token, data.body_put_kits)
    assert response.status_code == 500

def test_put_quantity_not_real_for_warehouse():
    body = copy.deepcopy(data.body_put_kits)
    body['productsList'][0]['quantity'] = 5000
    response = requestst_simple.put_kit_with_token(data.id_kits_with_token, data.token, body)
    assert response.status_code == 409
