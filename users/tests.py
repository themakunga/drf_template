# MIT License
#
# Copyright (c) 2022 Nicolas Martinez
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from users.models import UserModel

import logging
logger = logging.getLogger(__name__)

class UsersTestCase(TestCase):
    def setUp(self):
        user = UserModel(
            email='testemail@test.ts',
            first_name='test',
            last_name='yes',
            username='testing'
            )
        user.set_password('**abc12345**')
        user.save()

    def test_signup_user(self):
        """
        Adds a test person into the database
        """
        client = APIClient()
        logger.debug('Adding a new person into database')

        response = client.post(
            '/user/', {
                'email': 'newtest@test.ts',
                'password': 'acab12345555',
                'password_confirmation': 'acab12345555',
                'first_name': 'Testing',
                'last_name': 'Testing',
                'username': 'testing1'
            },
            format='json'
        )

        logger.debug('Assert response 201')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
