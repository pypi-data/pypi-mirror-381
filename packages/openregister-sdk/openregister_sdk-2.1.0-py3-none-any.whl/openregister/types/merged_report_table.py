# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel

__all__ = ["MergedReportTable"]


class MergedReportTable(BaseModel):
    rows: List["MergedReportRow"]


from .merged_report_row import MergedReportRow
