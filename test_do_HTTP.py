#pip install pytest-mock
# from unittest.mock import patch
# from do_HTTP import do_GET, do_POST 

# @patch('requests.get')
# def test_do_GET(mock_get):
#     mock_get.return_value.status_code = 200
#     mock_get.return_value.json.return_value = {"title": "foo", "body": "bar", "userId": 1}
#     url = "https://jsonplaceholder.typicode.com/posts/1"
#     result = do_GET(url)

#     assert result["id"] == 1
#     assert result["title"] == "Test"
#     mock_get.assert_called_once_with(url)
    
# @patch("requests.post")
# def test_do_POST(mock_post):
#     mock_post.return_value.status_code = 201
#     mock_post.return_value.json.return_value = {"id": 101, "title": "foo"}

#     url = "https://jsonplaceholder.typicode.com/posts"
#     body = {"title": "foo", "body": "bar", "userId": 1}
#     result = do_POST(url)

#     assert result["id"] == 101
#     assert result["title"] == "foo"
#     mock_post.assert_called_once_with(url, json=body)