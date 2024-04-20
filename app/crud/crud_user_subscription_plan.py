import uuid
from typing import Optional

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.common.logger import setup_logger
from app.schemas.user_subscription_plan import UserSubscriptionPlan

logger = setup_logger()

GET_USER_MEMBERSHIP_INFO = f"""
            SELECT 
                u.id AS {UserSubscriptionPlan.U_ID}, 
                u.email AS {UserSubscriptionPlan.U_EMAIL}, 
                u.password_hash AS {UserSubscriptionPlan.U_PASSWORD_HASH}, 
                u.display_name AS {UserSubscriptionPlan.U_DISPLAY_NAME}, 
                u.avatar_url AS {UserSubscriptionPlan.U_AVATAR_URL}, 
                u.payment_information AS {UserSubscriptionPlan.U_PAYMENT_INFORMATION}, 
                u.is_verified AS {UserSubscriptionPlan.U_IS_VERIFIED}, 
                u.user_role AS {UserSubscriptionPlan.U_USER_ROLE}, 
                u.is_active AS {UserSubscriptionPlan.U_IS_ACTIVE}, 
                u.created_at AS {UserSubscriptionPlan.U_CREATED_AT}, 
                u.updated_at AS {UserSubscriptionPlan.U_UPDATED_AT}, 
                u.deleted_at AS {UserSubscriptionPlan.U_DELETED_AT}, 
                us.id AS {UserSubscriptionPlan.US_ID}, 
                us.user_id AS {UserSubscriptionPlan.US_USER_ID}, 
                us.plan_id AS {UserSubscriptionPlan.US_PLAN_ID}, 
                us.expire_at AS {UserSubscriptionPlan.US_EXPIRE_AT}, 
                us.is_active AS {UserSubscriptionPlan.US_IS_ACTIVE}, 
                us.created_at AS {UserSubscriptionPlan.US_CREATED_AT}, 
                us.updated_at AS {UserSubscriptionPlan.US_UPDATED_AT}, 
                us.deleted_at AS {UserSubscriptionPlan.US_DELETED_AT}, 
                sp.id AS {UserSubscriptionPlan.SP_ID}, 
                sp.plan_title AS {UserSubscriptionPlan.SP_PLAN_TITLE}, 
                sp.plan_price AS {UserSubscriptionPlan.SP_PLAN_PRICE}, 
                sp.available_model AS {UserSubscriptionPlan.SP_AVAILABLE_MODEL}, 
                sp.message_credits AS {UserSubscriptionPlan.SP_MESSAGE_CREDITS}, 
                sp.number_of_chatbots AS {UserSubscriptionPlan.SP_NUMBER_OF_CHATBOTS}, 
                sp.max_character_per_chatbot AS {UserSubscriptionPlan.SP_MAX_CHARACTER_PER_CHATBOT}, 
                sp.live_agent_takeover AS {UserSubscriptionPlan.SP_LIVE_AGENT_TAKEOVER}, 
                sp.remove_label AS {UserSubscriptionPlan.SP_REMOVE_LABEL}, 
                sp.is_active AS {UserSubscriptionPlan.SP_IS_ACTIVE}, 
                sp.created_at AS {UserSubscriptionPlan.SP_CREATED_AT}, 
                sp.updated_at AS {UserSubscriptionPlan.SP_UPDATED_AT}, 
                sp.deleted_at AS {UserSubscriptionPlan.SP_DELETED_AT} 
            FROM users AS u 
            LEFT JOIN user_subscriptions AS us ON u.id = us.user_id 
            LEFT JOIN subscription_plans AS sp ON us.plan_id = sp.id 
            WHERE u.id = :user_id 
            AND u.deleted_at IS NULL 
            AND us.deleted_at IS NULL 
            AND sp.deleted_at IS NULL;
            """


class CRUDUserSubscriptionPlan:
    def get_user_membership_info(
        self, db: Session, user_id: uuid.UUID
    ) -> Optional[UserSubscriptionPlan]:

        result_proxy = db.execute(text(GET_USER_MEMBERSHIP_INFO), {"user_id": user_id})
        column_names = result_proxy.keys()
        result = result_proxy.fetchone()
        if result:
            result_dict = dict(zip(column_names, result))       
            builder = UserSubscriptionPlan.builder()
            builder \
                .with_u_id(result_dict[UserSubscriptionPlan.U_ID]) \
                .with_u_email(result_dict[UserSubscriptionPlan.U_EMAIL]) \
                .with_us_expire_at(result_dict[UserSubscriptionPlan.US_EXPIRE_AT]) \
                .with_sp_plan_title(result_dict[UserSubscriptionPlan.SP_PLAN_TITLE]) \
                .with_sp_plan_price(result_dict[UserSubscriptionPlan.SP_PLAN_PRICE]) \
                .with_sp_available_model(result_dict[UserSubscriptionPlan.SP_AVAILABLE_MODEL]) \
                .with_sp_message_credits(result_dict[UserSubscriptionPlan.SP_MESSAGE_CREDITS]) \
                .with_sp_number_of_chatbots(result_dict[UserSubscriptionPlan.SP_NUMBER_OF_CHATBOTS]) \
                .with_sp_max_character_per_chatbot(result_dict[UserSubscriptionPlan.SP_MAX_CHARACTER_PER_CHATBOT]) \
                .with_sp_live_agent_takeover(result_dict[UserSubscriptionPlan.SP_LIVE_AGENT_TAKEOVER]) \
                .with_sp_remove_label(result_dict[UserSubscriptionPlan.SP_REMOVE_LABEL])

            user_subscription_plan = builder.build()
            return user_subscription_plan
            
        else:
            return None


crud_user_subscription_plan = CRUDUserSubscriptionPlan()