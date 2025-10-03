from baby_steps import given, then, when
from d42 import substitute
from d42.substitution.errors import SubstitutionError
from pytest import raises

from district42_exp_types.multi_dict import schema_multi_dict


def test_multi_dict_invalid_value_substitution_error():
    with given:
        sch = schema_multi_dict

    with when, raises(Exception) as exception:
        substitute(sch, None)

    with then:
        assert exception.type is SubstitutionError
