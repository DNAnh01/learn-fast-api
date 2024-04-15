import uuid
from typing import Optional

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.common.logger import setup_logger
from app.schemas import user_subscription_plan as usp
from app.schemas.user_subscription_plan import UserSubscriptionPlan

logger = setup_logger()


class CRUDUserSubscriptionPlan:
    def get_user_subscription_plan(self, db: Session, user_id: uuid.UUID) -> Optional[UserSubscriptionPlan]:
        SQL_QUERY = f"""
            SELECT 
                u.id AS {usp.U_ID}, 
                u.email AS {usp.U_EMAIL}, 
                u.password_hash AS {usp.U_PASSWORD_HASH}, 
                u.display_name AS {usp.U_DISPLAY_NAME}, 
                u.avatar_url AS {usp.U_AVATAR_URL}, 
                u.payment_information AS {usp.U_PAYMENT_INFORMATION}, 
                u.is_verified AS {usp.U_IS_VERIFIED}, 
                u.user_role AS {usp.U_USER_ROLE}, 
                u.is_active AS {usp.U_IS_ACTIVE}, 
                u.created_at AS {usp.U_CREATED_AT}, 
                u.updated_at AS {usp.U_UPDATED_AT}, 
                u.deleted_at AS {usp.U_DELETED_AT}, 
                us.id AS {usp.US_ID}, 
                us.user_id AS {usp.US_USER_ID}, 
                us.plan_id AS {usp.US_PLAN_ID}, 
                us.expire_at AS {usp.US_EXPIRE_AT}, 
                us.is_active AS {usp.US_IS_ACTIVE}, 
                us.created_at AS {usp.US_CREATED_AT}, 
                us.updated_at AS {usp.US_UPDATED_AT}, 
                us.deleted_at AS {usp.US_DELETED_AT}, 
                sp.id AS {usp.SP_ID}, 
                sp.plan_title AS {usp.SP_PLAN_TITLE}, 
                sp.plan_price AS {usp.SP_PLAN_PRICE}, 
                sp.available_model AS {usp.SP_AVAILABLE_MODEL}, 
                sp.message_credits AS {usp.SP_MESSAGE_CREDITS}, 
                sp.number_of_chatbots AS {usp.SP_NUMBER_OF_CHATBOTS}, 
                sp.max_character_per_chatbot AS {usp.SP_MAX_CHARACTER_PER_CHATBOT}, 
                sp.live_agent_takeover AS {usp.SP_LIVE_AGENT_TAKEOVER}, 
                sp.remove_label AS {usp.SP_REMOVE_LABEL}, 
                sp.is_active AS {usp.SP_IS_ACTIVE}, 
                sp.created_at AS {usp.SP_CREATED_AT}, 
                sp.updated_at AS {usp.SP_UPDATED_AT}, 
                sp.deleted_at AS {usp.SP_DELETED_AT} 
            FROM users AS u 
            LEFT JOIN user_subscriptions AS us ON u.id = us.user_id 
            LEFT JOIN subscription_plans AS sp ON us.plan_id = sp.id 
            WHERE u.id = :user_id 
            AND u.deleted_at IS NULL 
            AND us.deleted_at IS NULL 
            AND sp.deleted_at IS NULL;
            """
        result_proxy = db.execute(text(SQL_QUERY), {"user_id": user_id})
        column_names = result_proxy.keys()
        result = result_proxy.fetchone()
        # logger.info(f"result: {result}")
        if result:
            result_dict = dict(zip(column_names, result))
            # logger.warning(f"result_dict: {result_dict}")
            return UserSubscriptionPlan \
                        .Builder() \
                            .with_u_id(result_dict[usp.U_ID]) \
                            .with_u_email(result_dict[usp.U_EMAIL]) \
                            .with_u_display_name(result_dict[usp.U_DISPLAY_NAME]) \
                            .with_us_expire_at(result_dict[usp.US_EXPIRE_AT]) \
                            .with_us_created_at(result_dict[usp.US_CREATED_AT]) \
                            .with_us_updated_at(result_dict[usp.US_UPDATED_AT]) \
                            .with_us_is_active(result_dict[usp.US_IS_ACTIVE]) \
                            .with_us_deleted_at(result_dict[usp.US_DELETED_AT]) \
                            .with_sp_plan_title(result_dict[usp.SP_PLAN_TITLE]) \
                            .with_sp_plan_price(result_dict[usp.SP_PLAN_PRICE]) \
                            .with_sp_available_model(result_dict[usp.SP_AVAILABLE_MODEL]) \
                            .with_sp_message_credits(result_dict[usp.SP_MESSAGE_CREDITS]) \
                            .with_sp_number_of_chatbots(result_dict[usp.SP_NUMBER_OF_CHATBOTS]) \
                            .with_sp_max_character_per_chatbot(result_dict[usp.SP_MAX_CHARACTER_PER_CHATBOT]) \
                            .with_sp_live_agent_takeover(result_dict[usp.SP_LIVE_AGENT_TAKEOVER]) \
                            .with_sp_remove_label(result_dict[usp.SP_REMOVE_LABEL]) \
                            .with_sp_created_at(result_dict[usp.SP_CREATED_AT]) \
                            .with_sp_updated_at(result_dict[usp.SP_UPDATED_AT]) \
                            .with_sp_is_active(result_dict[usp.SP_IS_ACTIVE]) \
                            .with_sp_deleted_at(result_dict[usp.SP_DELETED_AT]) \
                        .build()
        else:
            return None
crud_user_subscription_plan = CRUDUserSubscriptionPlan()
