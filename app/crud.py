from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas

def get_any_profile(db: Session):
    return db.query(models.Profile).first()


def create_profile(db: Session, profile: schemas.ProfileCreate):
    db_profile = models.Profile(name=profile.name, email=profile.email, education=profile.education)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    for s in profile.skills:
        db_skill = models.Skill(name=s.name, profile_id=db_profile.id)
        db.add(db_skill)
    for p in profile.projects:
        db_project = models.Project(title=p.title, description=p.description, links=p.links, profile_id=db_profile.id)
        db.add(db_project)
    for w in profile.work:
        db_work = models.Work(title=w.title, company=w.company, description=w.description, profile_id=db_profile.id)
        db.add(db_work)
    for l in profile.links:
        db_link = models.Link(github=l.github, linkedin=l.linkedin, portfolio=l.portfolio, profile_id=db_profile.id)
        db.add(db_link)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_profile(db: Session, profile_id: int):
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()

def update_profile(db: Session, profile_id: int, profile: schemas.ProfileUpdate):
    db_profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()
    if not db_profile:
        return None
    db_profile.name = profile.name
    db_profile.email = profile.email
    db_profile.education = profile.education
    db.query(models.Skill).filter(models.Skill.profile_id == profile_id).delete()
    db.query(models.Project).filter(models.Project.profile_id == profile_id).delete()
    db.query(models.Work).filter(models.Work.profile_id == profile_id).delete()
    db.query(models.Link).filter(models.Link.profile_id == profile_id).delete()
    for s in profile.skills:
        db.add(models.Skill(name=s.name, profile_id=profile_id))
    for p in profile.projects:
        db.add(models.Project(title=p.title, description=p.description, links=p.links, profile_id=profile_id))
    for w in profile.work:
        db.add(models.Work(title=w.title, company=w.company, description=w.description, profile_id=profile_id))
    for l in profile.links:
        db.add(models.Link(github=l.github, linkedin=l.linkedin, portfolio=l.portfolio, profile_id=profile_id))
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_projects_by_skill(db: Session, skill: str):
    return db.query(models.Project).join(models.Profile).join(models.Skill).filter(models.Skill.name.ilike(f"%{skill}%")).all()

def get_top_skills(db: Session, limit: int = 5):
    return db.query(models.Skill.name, func.count(models.Skill.id).label("count")).group_by(models.Skill.name).order_by(func.count(models.Skill.id).desc()).limit(limit).all()

def search(db: Session, q: str):
    return db.query(models.Project).filter(models.Project.title.ilike(f"%{q}%") | models.Project.description.ilike(f"%{q}%")).all()
