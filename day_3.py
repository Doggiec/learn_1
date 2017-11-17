import random

fn = ['毛', '习', '李', '刘', '马']
ln1 = ['云', '超', '强', '峰']
ln2 = ['化腾', '近平', '家印', '冠希']

class FakeUser:
    def fake_name(self, one_word=False, two_words=False):
        if(one_word):
            full_name = random.choice(fn) + random.choice(ln1)
        elif two_words:
            full_name = random.choice(fn) + random.choice(ln2)
        else:
            full_name = random.choice(fn) + random.choice(ln1+ln2)
        print full_name

    def fake_genfer(self):
        gender = random.choice(['男', '女', '未知'])
        print gender


class SnsUser(FakeUser):
    def get_followers(self, few=True, a_lot=False):
        if few:
            followers = random.randrange(1, 50)
        elif a_lot:
            followers = random.randrange(20, 10000)
         print  followers

user_a = FakeUser()
user_b = SnsUser()
user_a.fake_name()
user_b.get_followers()
