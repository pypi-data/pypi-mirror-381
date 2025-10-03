from unittest.mock import sentinel

import pytest
from baby_steps import given, then, when
from d42 import schema, substitute
from d42.substitution.errors import SubstitutionError
from pytest import raises

from district42_exp_types.ci_multi_dict import schema_ci_multi_dict


def test_ci_multi_dict_empty_dict_substitution():
    with given:
        sch = schema_ci_multi_dict

    with when:
        res = substitute(sch, {})

    with then:
        assert res == schema_ci_multi_dict({})
        assert res != sch


def test_ci_multi_dict_dict_keys_substitution():
    with given:
        sch = schema_ci_multi_dict
        value = {
            "id": 1,
            "name": "Bob"
        }

    with when:
        res = substitute(sch, value)

    with then:
        assert res == schema_ci_multi_dict([
            ("id", schema.int(1)),
            ("name", schema.str("Bob")),
        ])
        assert res != sch


def test_ci_multi_dict_dict_value_substitution_error():
    with given:
        sch = schema_ci_multi_dict

    with when, raises(Exception) as exception:
        substitute(sch, {"val": sentinel})

    with then:
        assert exception.type is SubstitutionError


def test_ci_multi_dict_dict_incorrect_value_substitution_error():
    with given:
        sch = schema_ci_multi_dict({
            "id": schema.int,
        })

    with when, raises(Exception) as exception:
        substitute(sch, {"id": "1"})

    with then:
        assert exception.type is SubstitutionError


def test_ci_multi_dict_dict_substitution():
    with given:
        sch = schema_ci_multi_dict({
            "id": schema.int,
        })

    with when:
        res = substitute(sch, {
            "ID": 1,
        })

    with then:
        assert res == schema_ci_multi_dict([
            ("id", schema.int(1)),
        ])
        assert res != sch


def test_ci_multi_dict_dict_more_keys_substitution_error():
    with given:
        sch = schema_ci_multi_dict({
            "id": schema.int,
        })

    with when, raises(Exception) as exception:
        substitute(sch, {
            "id": 1,
            "name": "Bob",
        })

    with then:
        assert exception.type is SubstitutionError


def test_ci_multi_dict_dict_less_keys_substitution():
    with given:
        sch = schema_ci_multi_dict({
            "id": schema.int,
            "name": schema.str,
        })

    with when:
        res = substitute(sch, {
            "id": 1,
        })

    with then:
        assert res == schema_ci_multi_dict([
            ("id", schema.int(1)),
            ("name", schema.str),
        ])
        assert res != sch


@pytest.mark.parametrize("key", ["id", "ID"])
def test_ci_multi_dict_dict_multi_key_substitution(key: str):
    with given:
        sch = schema_ci_multi_dict([
            ("id", schema.int),
            ("id", schema.int),
            ("name", schema.str),
        ])

    with when:
        res = substitute(sch, {
            key: 1,
        })

    with then:
        assert res == schema_ci_multi_dict([
            ("id", schema.int(1)),
            ("id", schema.int(1)),
            ("name", schema.str),
        ])
        assert res != sch


@pytest.mark.parametrize("key", ["id", "ID"])
def test_ci_multi_dict_dict_multi_key_lower_upper_substitution(key: str):
    with given:
        sch = schema_ci_multi_dict([
            ("id", schema.int),
            ("ID", schema.int),
            ("name", schema.str),
        ])

    with when:
        res = substitute(sch, {
            key: 1,
        })

    with then:
        assert res == schema_ci_multi_dict([
            ("id", schema.int(1)),
            ("id", schema.int(1)),
            ("name", schema.str),
        ])
        assert res != sch


@pytest.mark.parametrize("key", ["id", "ID"])
def test_ci_multi_dict_dict_multi_key_substitution_error(key: str):
    with given:
        sch = schema_ci_multi_dict([
            ("id", schema.int),
            ("id", schema.str),
            ("name", schema.str),
        ])

    with when, raises(Exception) as exception:
        substitute(sch, {
            key: 1,
        })

    with then:
        assert exception.type is SubstitutionError


@pytest.mark.parametrize("key", ["id", "ID"])
def test_ci_multi_dict_dict_multi_key_lower_upper_substitution_error(key: str):
    with given:
        sch = schema_ci_multi_dict([
            ("id", schema.int),
            ("ID", schema.str),
            ("name", schema.str),
        ])

    with when, raises(Exception) as exception:
        substitute(sch, {
            key: 1,
        })

    with then:
        assert exception.type is SubstitutionError
