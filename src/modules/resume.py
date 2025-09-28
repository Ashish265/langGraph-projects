from typing import List, Optional
from pydantic import BaseModel, Field, field_validator

class WorkExperience(BaseModel):
    job_title:str  = Field(description="job title or position")
    company :str = Field(description="company name")
    experience:int = Field(description="number of years of experience")
    responsibilities: List[str] = Field(description="list of responsibilities")

class Education(BaseModel):
    degree: str = Field(description="degree obtained")
    school: str = Field(description="school name")
    major: str = Field(description="major or field of study")
    year : Optional[int] = Field(default=None, description="graduation year")

    @field_validator('year')
    def set_year(cls,v):
        if v is None:
            return 0
        return v


class Resume(BaseModel):
    """ Structured resume data"""

    name : str = Field(description="full name of the individual")
    professional_summary: str = Field(description="brief professional summary or objective")
    skills: List[str] = Field(description="list of key skills")
    work_experience: List[WorkExperience] = Field(description="list of work experiences")
    education: List[Education] = Field(description="list of educational qualifications")

    @classmethod
    def mock(cls):
        return cls(
            name="John Doe",
            professional_summary="Experienced software developer with a passion for creating innovative solutions.",
            skills=["Python", "Machine Learning", "Data Analysis"],
            work_experience=[
                WorkExperience(
                    job_title="Software Engineer",
                    company="Tech Solutions",
                    experience=3,
                    responsibilities=[
                        "Developed web applications using Python and Django.",
                        "Collaborated with cross-functional teams to define project requirements."
                    ]
                ),
                WorkExperience(
                    job_title="Data Analyst",
                    company="Data Insights",
                    experience=2,
                    responsibilities=[
                        "Analyzed large datasets to extract actionable insights.",
                        "Created visualizations to communicate findings to stakeholders."
                    ]
                )
            ],
            education=[
                Education(
                    degree="Bachelor of Science in Computer Science",
                    school="State University",
                    major="Computer Science",
                    year=2020
                ),
                Education(
                    degree="Master of Science in Data Science",
                    school="Tech Institute",
                    major="Data Science",
                    year=2022
                )
            ]
        )
