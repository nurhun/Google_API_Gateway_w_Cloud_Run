from rest_framework.test import APITestCase, APIClient
from .test_setup import TestSetUp
from rest_framework import status
from movies.models import Movie
# from django.contrib.auth.models import User
from users.models import CustomUser

"""
test MovieViewSet all available methods:
- list - GET
- create - POST
- retrieve - GET a specific item
- update - PUT a specific item
- partial_update - PATCH a specific item
- destroy - DELETE
"""

# Inherenting from APITestCase as no need for pre-made setUp data.
class TestMovieViewsPOST(APITestCase):

    # @pytest.fixture
    def test_create_movie(self):
        '''
        test MovieViewSet create method
        '''

        # We need to create a user first, then send its credentials to the client, so that it can create the object.
        # This is because we have a project-level pemission IsAuthenticatedOrReadOnly.
        # OR
        # Inherent from TestSetUp() 
        self.user = CustomUser.objects.create_user(
            username='testuser1', 
            password='testuser1_secret_password',
            email='testuser1@test.com'
        )
        # self.user = User.objects.create_user(
        #     username='testuser1', 
        #     password='testuser1_secret_password',
        #     email='testuser1@test.com'
        # )
        self.client = APIClient()
        self.client.login(username=self.user.username, password="testuser1_secret_password")

        data = {
            "title": "Imagined for first post test case",
            "description": "Just in my mind",
            "year": 2022,
            "story_line": "hab'a a7kelak"
            }
            
        res = self.client.post('/api/v1/movie/', data)
        # self.assertEqual(res.status_code, 201)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)


# Inherenting from TestSetUp as we do need pre-made setUp data.
class TestMovieViewsGET(TestSetUp):

    def test_list_movies_response_status_code(self):
        '''
        test MovieViewSet list method
        '''
        res = self.client.get('/api/v1/movie/')
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_list_movies_response_list_count(self):
        res = self.client.get('/api/v1/movie/')
        self.assertEqual(Movie.objects.count(), 5)


    def test_retrieve_one_movie(self):
        '''
        test MovieViewSet retrieve method
        '''
        for movie in self.movies:
            res = self.client.get(f'/api/v1/movie/{movie.id}/')
            self.assertEqual(str(movie), movie.title)   # tests __str__ method in model that should return self.title

        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_delete_one_movie(self):
        '''
        test MovieViewSet delete method
        '''
        for movie in self.movies:
            res = self.client.delete(f'/api/v1/movie/{movie.id}/')
            
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)


    def test_update_one_movie(self):
        '''
        test MovieViewSet update method
        '''
        for movie in self.movies:
            # In update, you have to pass all data fields.
            data = {
                'id': movie.id,
                'title': movie.title,
                'description': movie.description,
                'year': movie.year,
                'story_line': "--------------"
                }
            res = self.client.put(f'/api/v1/movie/{movie.id}/', data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_patch_one_movie(self):
        '''
        test MovieViewSet patch method
        '''
        for movie in self.movies:
            # In patch, you don't have to pass all data fields, you need to pass only fields that will be modified.
            data = {'id': movie.id, 'year': 2000,'story_line': "--------------"}
            res = self.client.patch(f'/api/v1/movie/{movie.id}/', data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)