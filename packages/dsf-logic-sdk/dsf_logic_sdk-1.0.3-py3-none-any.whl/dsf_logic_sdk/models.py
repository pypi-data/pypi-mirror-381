# ============================================
# dsf_logic_sdk/models.py
# ============================================
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class Field:
    name: str
    default: Any
    weight: float = 1.0
    criticality: float = 1.5
    
    def to_dict(self) -> Dict:
        return {'default': self.default, 'weight': self.weight, 'criticality': self.criticality}

class Config:
    def __init__(self):
        self.fields: Dict[str, Field] = {}
    
    def add_field(self, name: str, default: Any, weight: float = 1.0, criticality: float = 1.5) -> 'Config':
        self.fields[name] = Field(name, default, weight, criticality)
        return self
    
    def to_dict(self) -> Dict:
        return {name: field.to_dict() for name, field in self.fields.items()}

@dataclass
class EvaluationResult:
    score: float
    tier: str = 'community'
    confidence_level: float = 0.65
    metrics: Optional[Dict] = None
    # Campos opcionales que tu API puede devolver:
    valid: Optional[bool] = None
    access: Optional[str] = None

    @classmethod
    def from_response(cls, response: Dict) -> 'EvaluationResult':
        return cls(
            score=response.get('score', 0.0),
            tier=response.get('tier', 'community'),
            # usa 'confidence_level' y cae a 'threshold' si el backend lo usa
            confidence_level=response.get('confidence_level', response.get('threshold', 0.65)),
            metrics=response.get('metrics'),
            valid=response.get('valid'),
            access=response.get('access')
        )

    @property
    def is_above_threshold(self) -> bool:
        # compatibilidad con código existente
        return self.score >= self.confidence_level

    @property
    def is_valid(self) -> bool:
        # si el backend manda 'valid', úsalo; si no, calcula por umbral
        return self.valid if self.valid is not None else self.score >= self.confidence_level
