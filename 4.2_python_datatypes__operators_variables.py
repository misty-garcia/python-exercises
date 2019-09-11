# exercise 1
little_mermaid_days = 3
brother_bear_days = 5
hercules_days = 1
price_per_movie_per_day = 3

total = price_per_movie_per_day * little_mermaid_days + price_per_movie_per_day * brother_bear_days + price_per_movie_per_day * hercules_days

print(total)

# exercise 2
google_pay_per_hour = 400
amazon_pay_per_hour = 380
facebook_pay_per_hour = 350
google_hours = 6
amazon_hours = 4
facebook_hours = 10

total_pay = 
print(total_pay)

# exercise 3
class_has_space = True
schedule_works = True
student_can_enroll = class_has_space and schedule_works
print(student_can_enroll)

# exercise 4
is_premium_member = True
person_bought_more_than_two_items = False
offer_not_expired = True

offer_can_be_applied = offer_not_expired and (person_bought_more_than_two_items or is_premium_member)
print(offer_can_be_applied)

# exercise 5
username = 'codeup'
password = 'notastrongpassword' 

password_length =len(password) >= 5
print("password length is appropriate: ", password_length )

username_length = len(username) <= 20
print("username length is appropriate: ", username_length )

same_username_password = username != password 
print("the username and password are not the same: ", same_username_password)

doesnt_contain_whitespace = password.strip() + username.strip() == password + username
print("the username and password doesnt start or end with whitespace: ", doesnt_contain_whitespace)

