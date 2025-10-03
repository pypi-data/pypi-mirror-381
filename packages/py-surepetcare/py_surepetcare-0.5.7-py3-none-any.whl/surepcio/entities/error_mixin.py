from typing import get_type_hints
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import model_validator

from surepcio.security.exceptions import ValidationMissingFieldsError


class ImprovedErrorMixin(BaseModel):
    """A mixin class that improves error handling and serialization for Pydantic models."""

    @model_validator(mode="after")
    def check_required_fields(cls, values):
        missing = []
        hints = get_type_hints(cls)
        for field, hint in hints.items():
            is_optional = getattr(hint, "__origin__", None) is Optional or (
                hasattr(hint, "__args__") and type(None) in getattr(hint, "__args__", [])
            )
            has_default = getattr(cls, field, None) is not None
            if not is_optional and not has_default and getattr(values, field, None) is None:
                missing.append(field)
        if missing:
            raise ValidationMissingFieldsError(
                "Missing required fields for {}: {}. Input was: {}".format(
                    cls.__name__, missing, values.dict() if hasattr(values, "dict") else values
                )
            )
        return values

    model_config = ConfigDict(extra="ignore")

    def model_dump(self, *args, **kwargs):
        kwargs.setdefault("exclude_none", True)
        kwargs.setdefault("by_alias", True)
        return super().model_dump(*args, **kwargs)
