from sqlalchemy.orm import Session  # type: ignore

from app.common.logger import setup_logger
from app.db.session import SessionLocal
from app.services.membership_service_impl import MembershipServiceImpl

logger = setup_logger()

db: Session = SessionLocal()

membership_service = MembershipServiceImpl()

re=  membership_service.get_user_membership_by_user_id(
    db=db,
    user_id="0c1f0f6f-095c-49cc-9333-91105a0647a1"
)

logger.info(re)