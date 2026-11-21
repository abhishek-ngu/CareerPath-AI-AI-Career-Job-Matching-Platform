"""Stub: scrape job postings and insert raw records into the jobs table."""
import asyncio
import uuid
from datetime import datetime

from apps.api.db.session import async_session
from apps.api.db.models import Job

DEMO_JOBS = [
    {
        "title": "Backend Engineering Intern",
        "company": "TechCorp",
        "location": "Remote",
        "description": "Build REST APIs with Python and FastAPI. Work with PostgreSQL and Docker.",
        "requirements": ["Python", "FastAPI", "PostgreSQL", "SQL"],
        "source": "demo",
    },
    {
        "title": "Data Analyst",
        "company": "DataCo",
        "location": "New York, NY",
        "description": "Analyze user data using SQL and Python. Build dashboards and reports.",
        "requirements": ["SQL", "Python", "Tableau", "Excel"],
        "source": "demo",
    },
    {
        "title": "Frontend Developer",
        "company": "WebStudio",
        "location": "Remote",
        "description": "Build responsive UIs with React and TypeScript.",
        "requirements": ["React", "TypeScript", "JavaScript", "CSS"],
        "source": "demo",
    },
]


async def seed():
    async with async_session() as session:
        for j in DEMO_JOBS:
            job = Job(
                id=uuid.uuid4(),
                posted_at=datetime.utcnow(),
                is_active=True,
                **j,
            )
            session.add(job)
        await session.commit()
        print(f"Seeded {len(DEMO_JOBS)} demo jobs")


if __name__ == "__main__":
    asyncio.run(seed())