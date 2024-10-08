from lib.cat_facts import CatFacts
from unittest.mock import Mock

def test_cat_facts_returns_a_fact():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"fact":"The cat has 500 skeletal muscles (humans have 650)."}
    cat_fact = CatFacts(requester_mock)
    assert cat_fact.provide() == "Cat fact: The cat has 500 skeletal muscles (humans have 650)."