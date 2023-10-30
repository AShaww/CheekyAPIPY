from datetime import datetime
from fastapi import APIRouter, HTTPException
from starlette import status
from api.app import models as m
from api.app.auth.auth import db_dependency, user_dependency
from datetime import timezone
from api.app.models import IssueDisplay

router = APIRouter(
    prefix="/issues",
    tags=["issue"]
)


@router.get('/', status_code=status.HTTP_200_OK)
async def get_all_issues(db: db_dependency):
    issues = db.query(m.Issue).all()

    issue_display_list = [IssueDisplay(
        id=issue.id,
        title=issue.title,
        description=issue.description,
        status=issue.status,
        created_at=issue.created_at,
        updated_at=issue.updated_at,
    ) for issue in issues]

    return issue_display_list


@router.get('/{issue_id}', status_code=status.HTTP_200_OK)
async def get_issue_by_id(issue_id: int, db: db_dependency):
    db_issue = db.query(m.Issue).filter(m.Issue.id == issue_id).first()
    if db_issue is None:
        raise HTTPException(status_code=404, detail='Post was not found')
    return db_issue


@router.post('/new', status_code=status.HTTP_201_CREATED)
async def create_issue(issue: m.IssueBase, db: db_dependency):
    db_issue = m.Issue(**issue.model_dump())
    db.add(db_issue)
    db.commit()

    return 'Issue created'


@router.put('/{issue_id}/edit', status_code=status.HTTP_202_ACCEPTED)
async def update_issue(issue_id: int, issue_update: m.IssueBase, db: db_dependency):
    db_issue = db.query(m.Issue).filter(m.Issue.id == issue_id).first()
    if db_issue is None:
        raise HTTPException(status_code=404, detail='Issue was not found')

    for key, value in issue_update.model_dump().items():
        setattr(db_issue, key, value)

    now = datetime.now(timezone.utc)

    db_issue.updated_at = now
    db.commit()

    return 'Issue updated'


@router.delete('/{issue_id}', status_code=status.HTTP_200_OK)
async def delete_issue(issue_id: int, db: db_dependency):
    db_issue = db.query(m.Issue).filter(m.Issue.id == issue_id).first()
    if db_issue is None:
        raise HTTPException(status_code=404, detail='Post was not found')
    db.delete(db_issue)
    db.commit()

    return 'Issue deleted'
