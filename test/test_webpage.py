from bs4 import BeautifulSoup
import pytest
import pickle
import requests

class TestWebpage:
    @pytest.fixture(autouse=True)
    def get_soup(self):
        index_page = requests.get("http://localhost:8000/index.html")
        soup_index = BeautifulSoup(index_page.content, 'html.parser')
        self._index = soup_index
       
    # testing index.html
    def test_navbar(self):
        assert self._index.find('h1')
        assert self._index.find('h2')
        assert self._index.find('h3')
        assert self._index.find('h4')
        assert self._index.find('h5')
        assert self._index.find('h6')
        
