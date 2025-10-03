from typing import Any

from d42.validation import ValidationResult, Validator
from d42.validation.errors import (
    MaxValueValidationError,
    MinValueValidationError,
    TypeValidationError,
)
from niltype import Nil, Nilable
from th import PathHolder

from ._numeric_schema import NumericSchema

__all__ = ("NumericValidator",)


class NumericValidator(Validator, extend=True):
    def visit_numeric(self, schema: NumericSchema, *,
                      value: Any = Nil, path: Nilable[PathHolder] = Nil,
                      **kwargs: Any) -> ValidationResult:
        result = self._validation_result_factory()
        if path is Nil:
            path = self._path_holder_factory()

        if error := self._validate_type(path, value, str):
            return result.add_error(error)

        try:
            int(value)
        except ValueError:
            error = TypeValidationError(path, value, "numeric str")  # type: ignore
            return result.add_error(error)

        if schema.props.value is not Nil:
            if error := self._validate_value(path, value, schema.props.value):
                return result.add_error(error)

        if schema.props.min is not Nil:
            if int(value) < int(schema.props.min):
                result.add_error(MinValueValidationError(path, value, schema.props.min))

        if schema.props.max is not Nil:
            if int(value) > int(schema.props.max):
                result.add_error(MaxValueValidationError(path, value, schema.props.max))

        return result
