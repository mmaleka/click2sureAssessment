from enum import unique
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "accountApi.settings")

import django 
django.setup() 

from faker import factory,Faker 
from account.models import * 
from transaction.models import * 
from django.contrib.auth.models import User
# from user.models import * 
from model_bakery.recipe import Recipe,foreign_key 

fake = Faker() 

for k in range(20):
    user=Recipe(
        User,
        username= fake.user_name()+str(fake.random_int(0, 9999)),
        password='password',
        first_name= fake.name(),
        last_name= fake.name(),
        email= fake.email(),)

    account=Recipe(
        Account,
        user=foreign_key(user),
        type=fake.sentence(nb_words=1, variable_nb_words=True),
        amount=fake.random_int(0, 1000),)

    transaction=Recipe(
        Transaction,
        Account=foreign_key(account),
        user=foreign_key(user),
        action=fake.sentence(nb_words=1, variable_nb_words=True),
        amount=fake.random_int(0, 1000),
        created_at=fake.future_datetime(end_date="+30d", tzinfo=None),)

    transaction.make()

# for k in range(100):
#     author=Recipe(Author,
#                 name=fake.name(),
#                 createdDate=fake.future_datetime(end_date="+30d", tzinfo=None),
#                 updatedDate=fake.future_datetime(end_date="+30d", tzinfo=None),)
  
#     question=Recipe(Question, 
#                 question_text=fake.sentence(nb_words=6,variable_nb_words=True),
#                 pub_date=fake.future_datetime(end_date="+30d",tzinfo=None),
#                 refAuthor=foreign_key(author),
#                 createdDate=fake.future_datetime(end_date="+30d",tzinfo=None),
#                 updatedDate=fake.future_datetime(end_date="+30d",tzinfo=None),)
    
#     choice = Recipe(Choice, 
#                 question=foreign_key(question), 
#                 choice_text = fake.sentence(nb_words=1, variable_nb_words=True), 
#                 createdDate=fake.future_datetime(end_date="+30d", tzinfo=None),  
#                 updatedDate=fake.future_datetime(end_date="+30d", tzinfo=None), ) 
    # choice.make()