from typing import Any, Dict, Mapping

import pytest
from baby_steps import given, then, when
from d42 import validate
from d42.validation.errors import TypeValidationError
from th import PathHolder

from district42_exp_types.ci_multi_dict import schema_ci_multi_dict


@pytest.mark.parametrize("value", [
    {},
    {"id": 1},
    {"id": 1, "name": "Bob"},
])
def test_ci_multi_dict_type_validation(value: Dict[Any, Any]):
    with given:
        sch = schema_ci_multi_dict

    with when:
        result = validate(sch, value)

    with then:
        assert result.get_errors() == []


def test_ci_multi_dict_type_validation_error():
    with given:
        sch = schema_ci_multi_dict
        value = []

    with when:
        result = validate(sch, value)

    with then:
        assert result.get_errors() == [
            TypeValidationError(PathHolder(), value, Mapping)
        ]
