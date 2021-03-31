import mock
import pytest

from openapi_core.templating.responses.finders import ResponseFinder


class TestResponses(object):

    @pytest.fixture(scope='class')
    def responses(self):
        return {
            '200': mock.sentinel.response_200,
            '299': mock.sentinel.response_299,
            '2XX': mock.sentinel.response_2XX,
            'default': mock.sentinel.response_default,
        }

    @pytest.fixture(scope='class')
    def finder(self, responses):
        return ResponseFinder(responses)

    def test_default(self, finder, responses):
        response = finder.find()

        assert response == responses['default']

    def test_range(self, finder, responses):
        response = finder.find('201')

        assert response == responses['2XX']

    def test_exact(self, finder, responses):
        response = finder.find('200')

        assert response == responses['200']
