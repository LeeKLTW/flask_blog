# encoding: utf-8
from datetime import datetime
import time
from flask_bcrypt import Bcrypt

crypt = Bcrypt()

for i in range(5):
    password = 'test'
    fake_password = 'testing'
    hash_ = crypt.generate_password_hash(password)
    print(f'{datetime.utcnow()}:  {hash_}')
    print(f'Real password:{password}      check: {crypt.check_password_hash(hash_, password)}')
    print(f'fake password:{fake_password} check:{crypt.check_password_hash(hash_, fake_password)}')
    print('\n')
    time.sleep(0.5)
