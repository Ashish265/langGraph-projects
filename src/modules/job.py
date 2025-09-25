from typing import List, Optional
from pydantic import BaseModel, Field

class Job(BaseModel):
    titlle: str = Field(description="The title of the job position")
    company: str = Field(description="The name of the company offering the job")
    location: Optional[str] = Field(default=None, description="The location of the job")
    description: str = Field(description="A detailed description of the job responsibilities and requirements")
    salary: Optional[str] = Field(description="The salary range for the job position")
    responsilities: List[str] = Field(description="A list of key responsibilities for the job")
    benifits: Optional[List[str]] = Field(description="A list of benefits offered with the job")
    employment_type: Optional[str] = Field(description="The type of employment (e.g., full-time, part-time, contract)")
    posted_date: Optional[str] = Field(description="The date the job was posted")


    @classmethod
    def mock(cls):
        return cls(
            titlle="Software Engineer",
            company="Tech Innovators Inc.",
            location="San Francisco, CA",
            description="We are looking for a skilled Software Engineer to join our dynamic team. The ideal candidate will have experience in developing scalable applications and a passion for technology.",
            salary="$100,000 - $120,000",
            responsilities=[
                "Develop and maintain web applications",
                "Collaborate with cross-functional teams",
                "Write clean, efficient, and well-documented code",
                "Participate in code reviews and contribute to team knowledge sharing"
            ],
            benifits=[
                "Health insurance",
                "401(k) matching",
                "Flexible work hours",
                "Professional development opportunities"
            ],
            employment_type="Full-time",
            posted_date="2024-06-01"
        )
