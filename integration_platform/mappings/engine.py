from typing import Dict, Any, List, Optional
from pydantic import BaseModel

class FieldMappingRule(BaseModel):
    source_field: str      # e.g., "job.rate" or "person.legalName.givenName"
    target_field: str      # e.g., "base_salary" or "first_name"
    default_value: Optional[Any] = None
    transform_type: Optional[str] = None  # "FLOAT", "STRING", "LOWERCASE", "UPPERCASE", "DATE"

class MappingDefinition(BaseModel):
    provider_name: str
    tenant_id: str
    rules: List[FieldMappingRule]

class DataMappingEngine:
    """Transforms raw provider JSON into PayBridge Canonical fields using configurable mapping rules."""

    @staticmethod
    def _extract_nested_value(data: Dict[str, Any], path: str) -> Any:
        keys = path.split(".")
        current = data
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        return current

    @classmethod
    def transform(cls, raw_data: Dict[str, Any], mapping_def: MappingDefinition) -> Dict[str, Any]:
        transformed = {}
        for rule in mapping_def.rules:
            val = cls._extract_nested_value(raw_data, rule.source_field)
            if val is None:
                val = rule.default_value

            if val is not None and rule.transform_type:
                try:
                    if rule.transform_type == "FLOAT":
                        val = float(val)
                    elif rule.transform_type == "STRING":
                        val = str(val)
                    elif rule.transform_type == "LOWERCASE":
                        val = str(val).lower()
                    elif rule.transform_type == "UPPERCASE":
                        val = str(val).upper()
                except (ValueError, TypeError):
                    val = rule.default_value

            transformed[rule.target_field] = val

        return transformed
