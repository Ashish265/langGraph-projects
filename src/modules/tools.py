from typing import Optional, Literal
from langchain_core.tools import tool

from src.modules.job import Job
from src.modules.resume import Resume

def process_job(job: Job) -> str:
    return job

def process_resume(resume: Resume) -> str:
    return resume

@tool
def get_job(field:Optional[Literal["title", "company", "location", "description", "salary", "responsibilities", "benefits", "employment_type", "posted_date"]]=None) -> str:
    """Get a job posting. If a field is specified, return only that field."""
    job = process_job()
    if field:
        return getattr(job, field)
    return job.dict()

@tool
def get_resume(field:Optional[Literal["name", "email", "phone", "summary", "skills", "experience", "education", "certifications"]]=None) -> str:
    """Get a resume. If a field is specified, return only that field."""
    resume = process_resume()
    if field:
        return getattr(resume, field)
    return resume.dict()
