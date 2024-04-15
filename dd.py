from IPython.display import display
from sqlalchemy.orm import Session

from app.crud.crud_user_subscription_plan import crud_user_subscription_plan
from app.db.session import SessionLocal
from app.schemas.user_subscription_plan import UserSubscriptionPlan

db: Session = SessionLocal()

res: UserSubscriptionPlan = crud_user_subscription_plan.get_user_subscription_plan(
    db=db,
    user_id='99abd82a-2686-4624-96b9-cc3c06c198ed'
)

display(res.__str__())
UserSubscriptionPlan(
    {
        "_Builder__u_id": "99abd82a-2686-4624-96b9-cc3c06c198ed",
        "_Builder__u_email": "admin@admin.com",
        "_Builder__us_expire_at": "2025-04-14 21:20:03.707099+07:00",
        "_Builder__sp_plan_title": "yearly_premium",
        "_Builder__sp_plan_price": 75.0,
        "_Builder__sp_available_model": "GPT-4 LLM",
        "_Builder__sp_message_credits": 6000,
        "_Builder__sp_number_of_chatbots": 5,
        "_Builder__sp_max_character_per_chatbot": 2000000,
        "_Builder__sp_live_agent_takeover": false,
        "_Builder__sp_remove_label": false
    }
)