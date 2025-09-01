from pydantic import BaseModel
from typing import List, Optional

class SkillBase(BaseModel):
    name: str

class SkillCreate(SkillBase):
    pass

class Skill(SkillBase):
    id: int
    class Config:
        from_attributes = True

class ProjectBase(BaseModel):
    title: str
    description: str
    links: list[str]

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    class Config:
        from_attributes = True

class WorkBase(BaseModel):
    title: str
    company: str
    description: str

class WorkCreate(WorkBase):
    pass

class Work(WorkBase):
    id: int
    class Config:
        from_attributes = True

class LinkBase(BaseModel):
    github: Optional[str]
    linkedin: Optional[str]
    portfolio: Optional[str]

class LinkCreate(BaseModel):
    github: str
    linkedin: str
    portfolio: Optional[str] = None

    class Config:
        from_attributes = True

class Link(LinkBase):
    id: int
    class Config:
        from_attributes = True

class ProfileBase(BaseModel):
    name: str
    email: str
    education: Optional[str]

class ProfileCreate(ProfileBase):
    skills: List[SkillCreate] = []
    projects: List[ProjectCreate] = []
    work: List[WorkCreate] = []
    links: List[LinkCreate] = []

class ProfileUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    education: Optional[str]
    skills: Optional[List[SkillCreate]] = None
    projects: Optional[List[ProjectCreate]] = None
    work: Optional[List[WorkCreate]] = None
    links: Optional[List[LinkCreate]] = None

    class Config:
        from_attributes = True


class Profile(ProfileBase):
    id: int
    skills: List[Skill] = []
    projects: List[Project] = []
    work: List[Work] = []
    links: List[Link] = []
    class Config:
        from_attributes = True
