from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from apps.api.db.session import get_session
from apps.api.db.models import Job
from apps.api.schemas import JobOut, JobSearchRequest, JobMatchRequest

router = APIRouter()


@router.post("/search", response_model=List[JobOut])
async def search_jobs(req: JobSearchRequest, session: AsyncSession = Depends(get_session)):
    # TODO: implement pgvector semantic search + PostgreSQL full-text hybrid
    result = await session.execute(
        select(Job).where(Job.is_active == True).limit(req.limit)
    )
    jobs = result.scalars().all()
    return jobs


@router.post("/match", response_model=List[JobOut])
async def match_jobs(req: JobMatchRequest, session: AsyncSession = Depends(get_session)):
    # TODO: load user profile, hybrid search, LLM rerank, return structured explanations
    result = await session.execute(
        select(Job).where(Job.is_active == True).limit(req.limit)
    )
    jobs = result.scalars().all()
    return jobs