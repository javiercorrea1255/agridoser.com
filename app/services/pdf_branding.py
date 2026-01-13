"""Minimal branding helpers for local report generation tests."""
from dataclasses import dataclass
from typing import Optional

BRAND_GREEN = "#16a34a"


@dataclass
class PDFBrandingContext:
    company_name: str = "Agridoser"
    company_tagline: Optional[str] = None
    company_address: Optional[str] = None
    company_email: Optional[str] = None
    company_phone: Optional[str] = None


def draw_professional_letterhead(*_args, **_kwargs) -> None:
    """No-op placeholder for environments without branding assets."""


def draw_professional_footer(*_args, **_kwargs) -> None:
    """No-op placeholder for environments without branding assets."""
