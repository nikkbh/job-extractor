from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class ExperienceLevel(str, Enum):
    junior = "junior"
    mid = "mid"
    senior = "senior"
    lead = "lead"
    unknown = "unknown"

class JobListing(BaseModel):
    job_title: str = Field(description="Exact job title from the job listing or description")
    company_name: Optional[str] = Field(None, description="Company name if mentioned")
    location: Optional[str] = Field(None, description="City, State or Remote")
    is_remote: bool = Field(description="True if remote is offered")
    experience_level: ExperienceLevel
    years_experienced_required: Optional[int] = None
    required_skills: list[str] = Field(description="Hard requirements only")
    nice_to_have_skills: list[str] = Field(default_factory=list)
    tech_stack: list[str] = Field(description="Technologies, frameworks, languages mentioned")
    benefits: list[str] = Field(default_factory=list)
    summary: str = Field(description="One sentence summary of the role")
    