from instapy import InstaPy
from instapy import smart_run

my_username="trendyground"
my_passowrd="socool666"

session = InstaPy(username=my_username,password=my_passowrd,headless_browser=False)

with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=5000,
                                    min_followers=20,
                                    min_following = 30)

    session.follow_user_followers(['vintage_perfume_shop'],amount=10,randomize=False)
    session.end()