from .database import SessionLocal, engine, Base
from . import models, crud, schemas

Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()
    from sqlalchemy.exc import IntegrityError

    if not crud.get_any_profile(db):
        try:
            profile_data = schemas.ProfileCreate(
                name="Vishal Gupta",
                email="vishal@example.com",
                education="MCA",
                skills=[schemas.SkillCreate(name="Python"), schemas.SkillCreate(name="FastAPI")],
                projects=[schemas.ProjectCreate(title="ToDo App", description="Manage tasks", links=["https://github.com"])],
                work=[schemas.WorkCreate(title="Developer", company="ABC", description="Backend Dev")],
                links=[schemas.LinkCreate(github="https://github.com/vishal", linkedin="https://linkedin.com/in/vishal")]
            )
            crud.create_profile(db, profile_data)
        except IntegrityError:
            db.rollback()
    db.close()

if __name__ == "__main__":
    seed()
