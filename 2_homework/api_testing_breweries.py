import pytest
import random


# @pytest.mark.parametrize('input_id, output_id',
#                          [(10000, '10000'),
#                              (-1, '-1'),
#                              (0, '0')])
# @pytest.mark.parametrize('input_title, output_title',
#                          [('title', 'title'),
#                              ('', ''),
#                              (100, '100'),
#                              ('&', '&')])
# def test_api_post_request(api_client, input_id, output_id, input_title, output_title):
#     res = api_client.post(
#         path="/posts",
#         data={'title': input_title, 'body': 'bar', 'userId': input_id})
#     res_json = res.json()
#     assert res_json['title'] == output_title
#     assert res_json['body'] == 'bar'
#     assert res_json['userId'] == output_id


# Параметр фильтрации постов по Id пользователя
# https://jsonplaceholder.typicode.com/posts?userId=1
#@pytest.mark.parametrize('userId', [-1, 0, 'a', 11])
def test_api_id_response(api_client_brew):
    res = api_client_brew.get_brew(
        path="/5745",
        #params={'userId': userId}
    )
    # Проверяем что на таких данных ответ пустой
    assert res.json() == {"id":5745,"name":"Brewery In Planning - Eugene","brewery_type":"planning","street":"","city":"Eugene","state":"Oregon","postal_code":"97401-7004","country":"United States","longitude":None,"latitude":None,"phone":"","website_url":"","updated_at":"2018-08-11T21:39:11.494Z"}


# Параметр фильтрации постов по Id пользователя
# https://jsonplaceholder.typicode.com/posts?userId=1
# @pytest.mark.parametrize('userId, userId_in_response', [(1, 1), (2, 2), (10, 10)])
# def test_api_filtering(api_client_brew, userId, userId_in_response):
#     response = api_client_brew.get_brew(
#         path="/posts",
#         params={'userId': userId}
#     )
#     # Проверка что случайный пост от пользователя с ожидаемым id
#     response_json = response.json()
#     random_post_number = random.randint(1, 9)
#     assert len(response_json) > 0
#     assert response.json()[random_post_number]['userId'] == userId_in_response

@pytest.mark.parametrize('by_som,by_item',[("by_city","san_diego"),("by_name","cooper")])
#@pytest.mark.parametrize('by_item', ["san_diego","cooper"])
def test_api_post_request(api_client_brew, by_som,by_item):
    res = api_client_brew.get_brew(
        query="?"+by_som,
        cond="="+by_item)


    print(res.json())