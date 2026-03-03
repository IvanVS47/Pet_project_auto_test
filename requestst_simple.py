import requests
import data
import conf

def post_new_user():
    return requests.post(conf.base_url + conf.endpoint_post_new_user,
                         headers=data.headers_new_user,
                         json=data.body_post_new_user)


def post_new_kit():
    return requests.post(conf.base_url + conf.endpoint_post_new_kits,
                         headers=data.token,
                         json=data.body_post_new_kits)


def get_kit_with_token(id_kit, token):
    return requests.get(conf.base_url + conf.endpoint_get_kits + str(id_kit),
                        headers=token)

def get_kit_without_token(id_kit):
    return requests.get(conf.base_url + conf.endpoint_get_kits + str(id_kit))

def put_kit_with_token(id_kit, token, body):
    print(body)
    return requests.put(conf.base_url + conf.endpoint_put_kits + str(id_kit),
                        headers=token,
                        json=body)

