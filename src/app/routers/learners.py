"""Router for learner endpoints."""

from fastapi import APIRouter

from datetime import datetime

from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.learners import read_learners, create_learner
from app.models.learner import Learner, LearnerCreate

router = APIRouter()

# ===
# PART A: GET endpoint
# ===


@router.get("/", response_model=list[Learner])
async def get_learners(
    enrolled_after: datetime | None = None,
    session: AsyncSession = Depends(get_session),
) -> list[Learner]:
    """Get all learners (optionally filtered by enrolled_after)."""
    return await read_learners(session=session, enrolled_after=enrolled_after)


#
# Reference:
# items GET -> reads from items table, returns list[Item]
# learners GET -> reads from learners table, returns list[Learner]
# Query parameter: ?enrolled_after= filters learners by enrolled_at date

# ===
# PART B: POST endpoint
# ===


@router.post("/", response_model=Learner, status_code=201)
async def create_learner_endpoint(
    learner: LearnerCreate,
    session: AsyncSession = Depends(get_session),
) -> Learner:
    """Create a learner."""
    return await create_learner(session=session, name=learner.name, email=learner.email)


# Reference:
# items POST -> creates a row in items table, accepts ItemCreate, returns Item with status 201
# learners POST -> creates a row in learners table, accepts LearnerCreate, returns Learner with status 201
