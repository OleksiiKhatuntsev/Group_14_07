import requests

class UserSignUpModel:
    def __init__(self, name, last_name, email, password, repeat_password):
        self.name = name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.repeatPassword = repeat_password



# test_dict = {
#   "name": "John",
#   "lasstName": "Dou",
#   "email": "sadasdaasdsaasdasdsddas@test.com",
#   "password": "Qwerty12345",
#   "repeatPassword": "Qwerty12345"
# }


# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# headers = {'content-type': 'application/json'}
#
# r = requests.post(url=url, json=payload, headers=headers)

user_to_sign_up = UserSignUpModel("John", "Dou", "sadasdaasdasdasdasdsaasdasdsddas@test.com", "Qwerty12345", "Qwerty12345")

session = requests.session()
# session.headers.
get_current_user = session.get("https://qauto2.forstudy.space/api/users/current")
post_new_user = session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=user_to_sign_up.__dict__, headers=)
get_current_user_after_post = session.get("https://qauto2.forstudy.space/api/users/current")
print(get_current_user.text)
print(post_new_user.text)
print(get_current_user_after_post.text)


# session = requests.session()

#
# post_new_user = session.post("https://qauto2.forstudy.space/api/auth/signup", json=test_dict)
# get_current_user_after_post = session.get("https://qauto2.forstudy.space/api/users/current")
# print(get_current_user.text)
# print(post_new_user.text)
# print(get_current_user_after_post.text)