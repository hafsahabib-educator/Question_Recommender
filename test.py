# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:48:24 2023

@author: DELL
"""

from app import app, get_similar_questions
import unittest
import json

class TestQuestionRecommender(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_similar_questions(self):
        # Test with a valid user input
        response = self.app.post('/get_similar_questions', json={'user_input': 'Romeo Juliet'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        

        # Test with an invalid user input
        response = self.app.post('/get_similar_questions', json={'user_input': 'Pakistan'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['similar_questions']), 0)

if __name__ == '__main__':
    unittest.main()
