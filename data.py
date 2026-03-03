
headers_new_user = {
    "Content-Type": "application/json"
}

body_post_new_user = {
    "firstName": "Анатолий",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}

token = {"Authorization": ""} 

id_kits_with_token = -99

id_kits_without_token = -993

body_post_new_kits = {
    "productsList": [
        {
            "id": 1,
            "quantity": 2
        }
    ]
}

body_put_kits = {
 "productsList": [
    {
        "id": 10,
        "quantity": 3
    }
 ]
}
