import json
import uuid
from datetime import datetime
from typing import Optional


class UserSubscriptionPlan:
    class Builder:
        def __init__(self):
            self.instance = UserSubscriptionPlan()

        def with_u_id(self, u_id: uuid.UUID):
            self.instance.__u_id = u_id
            return self

        def with_u_email(self, u_email: str):
            self.instance.__u_email = u_email
            return self

        def with_u_password_hash(self, u_password_hash: str):
            self.instance.__u_password_hash = u_password_hash
            return self

        def with_u_display_name(self, u_display_name: str):
            self.instance.__u_display_name = u_display_name
            return self

        def with_u_avatar_url(self, u_avatar_url: str):
            self.instance.__u_avatar_url = u_avatar_url
            return self

        def with_u_payment_information(self, u_payment_information: str):
            self.instance.__u_payment_information = u_payment_information
            return self

        def with_u_is_verified(self, u_is_verified: bool):
            self.instance.__u_is_verified = u_is_verified
            return self

        def with_u_user_role(self, u_user_role: str):
            self.instance.__u_user_role = u_user_role
            return self

        def with_u_is_active(self, u_is_active: bool):
            self.instance.__u_is_active = u_is_active
            return self

        def with_u_created_at(self, u_created_at: datetime):
            self.instance.__u_created_at = u_created_at
            return self

        def with_u_updated_at(self, u_updated_at: datetime):
            self.instance.__u_updated_at = u_updated_at
            return self

        def with_u_deleted_at(self, u_deleted_at: Optional[datetime]):
            self.instance.__u_deleted_at = u_deleted_at
            return self

        def with_us_id(self, us_id: uuid.UUID):
            self.instance.__us_id = us_id
            return self

        def with_us_user_id(self, us_user_id: uuid.UUID):
            self.instance.__us_user_id = us_user_id
            return self

        def with_us_plan_id(self, us_plan_id: uuid.UUID):
            self.instance.__us_plan_id = us_plan_id
            return self

        def with_us_expire_at(self, us_expire_at: datetime):
            self.instance.__us_expire_at = us_expire_at
            return self

        def with_us_is_active(self, us_is_active: bool):
            self.instance.__us_is_active = us_is_active
            return self

        def with_us_created_at(self, us_created_at: datetime):
            self.instance.__us_created_at = us_created_at
            return self

        def with_us_updated_at(self, us_updated_at: datetime):
            self.instance.__us_updated_at = us_updated_at
            return self

        def with_us_deleted_at(self, us_deleted_at: Optional[datetime]):
            self.instance.__us_deleted_at = us_deleted_at
            return self

        def with_sp_id(self, sp_id: uuid.UUID):
            self.instance.__sp_id = sp_id
            return self

        def with_sp_plan_title(self, sp_plan_title: str):
            self.instance.__sp_plan_title = sp_plan_title
            return self

        def with_sp_plan_price(self, sp_plan_price: float):
            self.instance.__sp_plan_price = sp_plan_price
            return self

        def with_sp_available_model(self, sp_available_model: str):
            self.instance.__sp_available_model = sp_available_model
            return self

        def with_sp_message_credits(self, sp_message_credits: int):
            self.instance.__sp_message_credits = sp_message_credits
            return self

        def with_sp_number_of_chatbots(self, sp_number_of_chatbots: int):
            self.instance.__sp_number_of_chatbots = sp_number_of_chatbots
            return self

        def with_sp_max_character_per_chatbot(self, sp_max_character_per_chatbot: int):
            self.instance.__sp_max_character_per_chatbot = sp_max_character_per_chatbot
            return self

        def with_sp_live_agent_takeover(self, sp_live_agent_takeover: bool):
            self.instance.__sp_live_agent_takeover = sp_live_agent_takeover
            return self

        def with_sp_remove_label(self, sp_remove_label: bool):
            self.instance.__sp_remove_label = sp_remove_label
            return self

        def with_sp_is_active(self, sp_is_active: bool):
            self.instance.__sp_is_active = sp_is_active
            return self

        def with_sp_created_at(self, sp_created_at: datetime):
            self.instance.__sp_created_at = sp_created_at
            return self

        def with_sp_updated_at(self, sp_updated_at: datetime):
            self.instance.__sp_updated_at = sp_updated_at
            return self

        def with_sp_deleted_at(self, sp_deleted_at: Optional[datetime]):
            self.instance.__sp_deleted_at = sp_deleted_at
            return self

        def build(self):
            return self.instance

    # users
    __u_id: uuid.UUID
    __u_email: str
    __u_password_hash: str
    __u_display_name: str
    __u_avatar_url: str
    __u_payment_information: str
    __u_is_verified: bool
    __u_user_role: str
    __u_is_active: bool
    __u_created_at: datetime
    __u_updated_at: datetime
    __u_deleted_at: Optional[datetime]
    # user_subscriptions
    __us_id: uuid.UUID
    __us_user_id: uuid.UUID
    __us_plan_id: uuid.UUID
    __us_expire_at: datetime
    __us_is_active: bool
    __us_created_at: datetime
    __us_updated_at: datetime
    __us_deleted_at: Optional[datetime]
    # subscription_plans
    __sp_id: uuid.UUID
    __sp_plan_title: str
    __sp_plan_price: float
    __sp_available_model: str
    __sp_message_credits: int
    __sp_number_of_chatbots: int
    __sp_max_character_per_chatbot: int
    __sp_live_agent_takeover: bool
    __sp_remove_label: bool
    __sp_is_active: bool
    __sp_created_at: datetime
    __sp_updated_at: datetime
    __sp_deleted_at: Optional[datetime]

    def __init__(self):
        # users
        self.__u_id = None
        self.__u_email = None
        self.__u_password_hash = None
        self.__u_display_name = None
        self.__u_avatar_url = None
        self.__u_payment_information = None
        self.__u_is_verified = None
        self.__u_user_role = None
        self.__u_is_active = None
        self.__u_created_at = None
        self.__u_updated_at = None
        self.__u_deleted_at = None
        # user_subscriptions
        self.__us_id = None
        self.__us_user_id = None
        self.__us_plan_id = None
        self.__us_expire_at = None
        self.__us_is_active = None
        self.__us_created_at = None
        self.__us_updated_at = None
        self.__us_deleted_at = None
        # subscription_plans
        self.__sp_id = None
        self.__sp_plan_title = None
        self.__sp_plan_price = None
        self.__sp_available_model = None
        self.__sp_message_credits = None
        self.__sp_number_of_chatbots = None
        self.__sp_max_character_per_chatbot = None
        self.__sp_live_agent_takeover = None
        self.__sp_remove_label = None
        self.__sp_is_active = None
        self.__sp_created_at = None
        self.__sp_updated_at = None
        self.__sp_deleted_at = None

    def __eq__(self, other):
        if isinstance(other, UserSubscriptionPlan):
            return self.__u_id == other.__u_id  # Compare based on unique property
        return False

    def __hash__(self):
        return hash(self.__u_id)  # Hash based on unique property

    def __str__(self):
        non_none_fields = {k: v for k, v in self.__dict__.items() if v is not None}
        formatted_fields = json.dumps(non_none_fields, default=str, indent=4)
        return f'UserSubscriptionPlan(\n{formatted_fields}\n)'

    # Getters and Setters
    @property
    def u_id(self):
        return self.__u_id

    @u_id.setter
    def u_id(self, u_id: uuid.UUID):
        self.__u_id = u_id

    @property
    def u_email(self):
        return self.__u_email

    @u_email.setter
    def u_email(self, u_email: str):
        self.__u_email = u_email

    @property
    def u_password_hash(self):
        return self.__u_password_hash

    @u_password_hash.setter
    def u_password_hash(self, u_password_hash: str):
        self.__u_password_hash = u_password_hash

    @property
    def u_display_name(self):
        return self.__u_display_name

    @u_display_name.setter
    def u_display_name(self, u_display_name: str):
        self.__u_display_name = u_display_name

    @property
    def u_avatar_url(self):
        return self.__u_avatar_url

    @u_avatar_url.setter
    def u_avatar_url(self, u_avatar_url: str):
        self.__u_avatar_url = u_avatar_url

    @property
    def u_payment_information(self):
        return self.__u_payment_information

    @u_payment_information.setter
    def u_payment_information(self, u_payment_information: str):
        self.__u_payment_information = u_payment_information

    @property
    def u_is_verified(self):
        return self.__u_is_verified

    @u_is_verified.setter
    def u_is_verified(self, u_is_verified: bool):
        self.__u_is_verified = u_is_verified

    @property
    def u_user_role(self):
        return self.__u_user_role

    @u_user_role.setter
    def u_user_role(self, u_user_role: str):
        self.__u_user_role = u_user_role

    @property
    def u_is_active(self):
        return self.__u_is_active

    @u_is_active.setter
    def u_is_active(self, u_is_active: bool):
        self.__u_is_active = u_is_active

    @property
    def u_created_at(self):
        return self.__u_created_at

    @u_created_at.setter
    def u_created_at(self, u_created_at: datetime):
        self.__u_created_at = u_created_at

    @property
    def u_updated_at(self):
        return self.__u_updated_at

    @u_updated_at.setter
    def u_updated_at(self, u_updated_at: datetime):
        self.__u_updated_at = u_updated_at

    @property
    def u_deleted_at(self):
        return self.__u_deleted_at

    @u_deleted_at.setter
    def u_deleted_at(self, u_deleted_at: Optional[datetime]):
        self.__u_deleted_at = u_deleted_at

    @property
    def us_id(self):
        return self.__us_id

    @us_id.setter
    def us_id(self, us_id: uuid.UUID):
        self.__us_id = us_id

    @property
    def us_user_id(self):
        return self.__us_user_id

    @us_user_id.setter
    def us_user_id(self, us_user_id: uuid.UUID):
        self.__us_user_id = us_user_id

    @property
    def us_plan_id(self):
        return self.__us_plan_id

    @us_plan_id.setter
    def us_plan_id(self, us_plan_id: uuid.UUID):
        self.__us_plan_id = us_plan_id

    @property
    def us_expire_at(self):
        return self.__us_expire_at

    @us_expire_at.setter
    def us_expire_at(self, us_expire_at: datetime):
        self.__us_expire_at = us_expire_at

    @property
    def us_is_active(self):
        return self.__us_is_active

    @us_is_active.setter
    def us_is_active(self, us_is_active: bool):
        self.__us_is_active = us_is_active

    @property
    def us_created_at(self):
        return self.__us_created_at

    @us_created_at.setter
    def us_created_at(self, us_created_at: datetime):
        self.__us_created_at = us_created_at

    @property
    def us_updated_at(self):
        return self.__us_updated_at

    @us_updated_at.setter
    def us_updated_at(self, us_updated_at: datetime):
        self.__us_updated_at = us_updated_at

    @property
    def us_deleted_at(self):
        return self.__us_deleted_at

    @us_deleted_at.setter
    def us_deleted_at(self, us_deleted_at: Optional[datetime]):
        self.__us_deleted_at = us_deleted_at

    @property
    def sp_id(self):
        return self.__sp_id
    
    @sp_id.setter
    def sp_id(self, sp_id: uuid.UUID):
        self.__sp_id = sp_id

    @property
    def sp_plan_title(self):
        return self.__sp_plan_title

    @sp_plan_title.setter
    def sp_plan_title(self, sp_plan_title: str):
        self.__sp_plan_title = sp_plan_title

    @property
    def sp_plan_price(self):
        return self.__sp_plan_price

    @sp_plan_price.setter
    def sp_plan_price(self, sp_plan_price: float):
        self.__sp_plan_price = sp_plan_price

    @property
    def sp_available_model(self):
        return self.__sp_available_model

    @sp_available_model.setter
    def sp_available_model(self, sp_available_model: str):
        self.__sp_available_model = sp_available_model

    @property
    def sp_message_credits(self):
        return self.__sp_message_credits

    @sp_message_credits.setter
    def sp_message_credits(self, sp_message_credits: int):
        self.__sp_message_credits = sp_message_credits

    @property
    def sp_number_of_chatbots(self):
        return self.__sp_number_of_chatbots

    @sp_number_of_chatbots.setter
    def sp_number_of_chatbots(self, sp_number_of_chatbots: int):
        self.__sp_number_of_chatbots = sp_number_of_chatbots

    @property
    def sp_max_character_per_chatbot(self):
        return self.__sp_max_character_per_chatbot

    @sp_max_character_per_chatbot.setter
    def sp_max_character_per_chatbot(self, sp_max_character_per_chatbot: int):
        self.__sp_max_character_per_chatbot = sp_max_character_per_chatbot

    @property
    def sp_live_agent_takeover(self):
        return self.__sp_live_agent_takeover

    @sp_live_agent_takeover.setter
    def sp_live_agent_takeover(self, sp_live_agent_takeover: bool):
        self.__sp_live_agent_takeover = sp_live_agent_takeover

    @property
    def sp_remove_label(self):
        return self.__sp_remove_label

    @sp_remove_label.setter
    def sp_remove_label(self, sp_remove_label: bool):
        self.__sp_remove_label = sp_remove_label

    @property
    def sp_is_active(self):
        return self.__sp_is_active

    @sp_is_active.setter
    def sp_is_active(self, sp_is_active: bool):
        self.__sp_is_active = sp_is_active

    @property
    def sp_created_at(self):
        return self.__sp_created_at

    @sp_created_at.setter
    def sp_created_at(self, sp_created_at: datetime):
        self.__sp_created_at = sp_created_at

    @property
    def sp_updated_at(self):
        return self.__sp_updated_at

    @sp_updated_at.setter
    def sp_updated_at(self, sp_updated_at: datetime):
        self.__sp_updated_at = sp_updated_at

    @property
    def sp_deleted_at(self):
        return self.__sp_deleted_at

    @sp_deleted_at.setter
    def sp_deleted_at(self, sp_deleted_at: Optional[datetime]):
        self.__sp_deleted_at = sp_deleted_at


U_ID = "u_id"
U_EMAIL = "u_email"
U_PASSWORD_HASH = "u_password_hash"
U_DISPLAY_NAME = "u_display_name"
U_AVATAR_URL = "u_avatar_url"
U_PAYMENT_INFORMATION = "u_payment_information"
U_IS_VERIFIED = "u_is_verified"
U_USER_ROLE = "u_user_role"
U_IS_ACTIVE = "u_is_active"
U_CREATED_AT = "u_created_at"
U_UPDATED_AT = "u_updated_at"
U_DELETED_AT = "u_deleted_at"
US_ID = "us_id"
US_USER_ID = "us_user_id"
US_PLAN_ID = "us_plan_id"
US_EXPIRE_AT = "us_expire_at"
US_IS_ACTIVE = "us_is_active"
US_CREATED_AT = "us_created_at"
US_UPDATED_AT = "us_updated_at"
US_DELETED_AT = "us_deleted_at"
SP_ID = "sp_id"
SP_PLAN_TITLE = "sp_plan_title"
SP_PLAN_PRICE = "sp_plan_price"
SP_AVAILABLE_MODEL = "sp_available_model"
SP_MESSAGE_CREDITS = "sp_message_credits"
SP_NUMBER_OF_CHATBOTS = "sp_number_of_chatbots"
SP_MAX_CHARACTER_PER_CHATBOT = "sp_max_character_per_chatbot"
SP_LIVE_AGENT_TAKEOVER = "sp_live_agent_takeover"
SP_REMOVE_LABEL = "sp_remove_label"
SP_IS_ACTIVE = "sp_is_active"
SP_CREATED_AT = "sp_created_at"
SP_UPDATED_AT = "sp_updated_at"
SP_DELETED_AT = "sp_deleted_at"
