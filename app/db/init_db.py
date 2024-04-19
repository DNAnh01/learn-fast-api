import uuid
from datetime import datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.common.utils import hash
from app.core.config import settings
from app.crud.crud_subscription_plan import crud_subscription_plan
from app.crud.crud_user import crud_user
from app.crud.crud_user_subscription import crud_user_subscription
from app.db.base_class import Base
from app.schemas.subscription_plan import SubscriptionPlanCreate
from app.schemas.user import UserInDB
from app.schemas.user_subscription import UserSubscriptionCreate

engine = create_engine(
    f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)


def init_db():
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        # Check if tables are empty
        if (
            not session.query(crud_subscription_plan.model).count()
            and not session.query(crud_user.model).count()
            and not session.query(crud_user_subscription.model).count()
        ):

            # Initialize subscribe plan default
            monthly_free = crud_subscription_plan.create(
                db=session,
                obj_in=SubscriptionPlanCreate(
                    plan_title="monthly_free",
                    plan_price=0.0,
                    available_model="GPT-3.5-Turbo LLM",
                    message_credits=30,
                    number_of_chatbots=1,
                    max_character_per_chatbot=200000,
                    live_agent_takeover=False,
                    remove_label=False,
                    is_active=True,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None,
                ),
            )

            monthly_entry = crud_subscription_plan.create(
                db=session,
                obj_in=SubscriptionPlanCreate(
                    plan_title="monthly_entry",
                    plan_price=30.0,
                    available_model="GPT-4 LLM",
                    message_credits=2000,
                    number_of_chatbots=3,
                    max_character_per_chatbot=800000,
                    live_agent_takeover=False,
                    remove_label=False,
                    is_active=True,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None,
                ),
            )
            monthly_premium = crud_subscription_plan.create(
                db=session,
                obj_in=SubscriptionPlanCreate(
                    plan_title="monthly_premium",
                    plan_price=90.0,
                    available_model="GPT-4 LLM",
                    message_credits=6000,
                    number_of_chatbots=5,
                    max_character_per_chatbot=2000000,
                    live_agent_takeover=False,
                    remove_label=False,
                    is_active=True,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None,
                ),
            )

            yearly_free = crud_subscription_plan.create(
                db=session,
                obj_in=SubscriptionPlanCreate(
                    plan_title="yearly_free",
                    plan_price=0.0,
                    available_model="GPT-3.5-Turbo LLM",
                    message_credits=30,
                    number_of_chatbots=1,
                    max_character_per_chatbot=200000,
                    live_agent_takeover=False,
                    remove_label=False,
                    is_active=True,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None,
                ),
            )

            yearly_entry = crud_subscription_plan.create(
                db=session,
                obj_in=SubscriptionPlanCreate(
                    plan_title="yearly_entry",
                    plan_price=25.0,
                    available_model="GPT-4 LLM",
                    message_credits=2000,
                    number_of_chatbots=3,
                    max_character_per_chatbot=800000,
                    live_agent_takeover=False,
                    remove_label=False,
                    is_active=True,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None,
                ),
            )
            yearly_premium = crud_subscription_plan.create(
                db=session,
                obj_in=SubscriptionPlanCreate(
                    plan_title="yearly_premium",
                    plan_price=75.0,
                    available_model="GPT-4 LLM",
                    message_credits=6000,
                    number_of_chatbots=5,
                    max_character_per_chatbot=2000000,
                    live_agent_takeover=False,
                    remove_label=False,
                    is_active=True,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None,
                ),
            )
            # Initialize user default
            user_found = crud_user.get_one_by(
                session, filter={"email": "admin@admin.com"}
            )
            if not user_found:
                user_admin_default = crud_user.create(
                    db=session,
                    obj_in=UserInDB(
                        id=uuid.uuid4(),
                        email="admin@admin.com",
                        password_hash=hash("admin"),
                        display_name="admin",
                        avatar_url="https://raw.githubusercontent.com/DNAnh01/assets/main/default_user_avatar.png",
                        payment_information="",
                        is_verified=False,
                        user_role="admin",
                        is_active=True,
                        created_at=datetime.now(),
                        updated_at=datetime.now(),
                        deleted_at=None,
                    ),
                )
            # Initialize user subscription default
            user_subscription_default = crud_user_subscription.create(
                db=session,
                obj_in=UserSubscriptionCreate(
                    user_id=user_admin_default.id,
                    plan_id=yearly_premium.id,
                    expire_at=datetime.now() + timedelta(days=365),
                    is_active=True,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None,
                ),
            )