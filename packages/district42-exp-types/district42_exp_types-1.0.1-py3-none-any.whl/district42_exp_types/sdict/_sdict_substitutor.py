from typing import Any, cast

from d42.substitution import Substitutor
from niltype import Nil

from ._rollout import rollout
from ._sdict_schema import SDictSchema

__all__ = ("SDictSubstitutor",)


class SDictSubstitutor(Substitutor, extend=True):
    def visit_sdict(self, schema: SDictSchema, *, value: Any = Nil, **kwargs: Any) -> SDictSchema:
        assert isinstance(value, dict)
        return cast(SDictSchema, self.visit_dict(schema, value=rollout(value), **kwargs))
