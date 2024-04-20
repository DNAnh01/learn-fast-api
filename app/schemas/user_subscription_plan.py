import json
import uuid
from datetime import datetime
from typing import Optional


class UserSubscriptionPlan:
    # Define keys for accessing properties
    U_ID = "_u_id"
    U_EMAIL = "_u_email"
    U_PASSWORD_HASH = "_u_password_hash"
    U_DISPLAY_NAME = "_u_display_name"
    U_AVATAR_URL = "_u_avatar_url"
    U_PAYMENT_INFORMATION = "_u_payment_information"
    U_IS_VERIFIED = "_u_is_verified"
    U_USER_ROLE = "_u_user_role"
    U_IS_ACTIVE = "_u_is_active"
    U_CREATED_AT = "_u_created_at"
    U_UPDATED_AT = "_u_updated_at"
    U_DELETED_AT = "_u_deleted_at"
    US_ID = "_us_id"
    US_USER_ID = "_us_user_id"
    US_PLAN_ID = "_us_plan_id"
    US_EXPIRE_AT = "_us_expire_at"
    US_IS_ACTIVE = "_us_is_active"
    US_CREATED_AT = "_us_created_at"
    US_UPDATED_AT = "_us_updated_at"
    US_DELETED_AT = "_us_deleted_at"
    SP_ID = "_sp_id"
    SP_PLAN_TITLE = "_sp_plan_title"
    SP_PLAN_PRICE = "_sp_plan_price"
    SP_AVAILABLE_MODEL = "_sp_available_model"
    SP_MESSAGE_CREDITS = "_sp_message_credits"
    SP_NUMBER_OF_CHATBOTS = "_sp_number_of_chatbots"
    SP_MAX_CHARACTER_PER_CHATBOT = "_sp_max_character_per_chatbot"
    SP_LIVE_AGENT_TAKEOVER = "_sp_live_agent_takeover"
    SP_REMOVE_LABEL = "_sp_remove_label"
    SP_IS_ACTIVE = "_sp_is_active"
    SP_CREATED_AT = "_sp_created_at"
    SP_UPDATED_AT = "_sp_updated_at"
    SP_DELETED_AT = "_sp_deleted_at"

    # Initialize properties
    _u_id: uuid.UUID
    _u_email: str
    _u_password_hash: Optional[str]
    _u_display_name: str
    _u_avatar_url: str
    _u_payment_information: str
    _u_is_verified: bool
    _u_user_role: str
    _u_is_active: bool
    _u_created_at: datetime
    _u_updated_at: datetime
    _u_deleted_at: Optional[datetime]
    _us_id: uuid.UUID
    _us_user_id: uuid.UUID
    _us_plan_id: uuid.UUID
    _us_expire_at: datetime
    _us_is_active: bool
    _us_created_at: datetime
    _us_updated_at: datetime
    _us_deleted_at: Optional[datetime]
    _sp_id: uuid.UUID
    _sp_plan_title: str
    _sp_plan_price: float
    _sp_available_model: str
    _sp_message_credits: int
    _sp_number_of_chatbots: int
    _sp_max_character_per_chatbot: int
    _sp_live_agent_takeover: bool
    _sp_remove_label: bool
    _sp_is_active: bool
    _sp_created_at: datetime
    _sp_updated_at: datetime
    _sp_deleted_at: Optional[datetime]

    # Constructor
    def __init__(self, builder: 'UserSubscriptionPlan.Builder'):
        # Set properties
        self._u_id = builder._u_id
        self._u_email = builder._u_email
        self._u_password_hash = builder._u_password_hash
        self._u_display_name = builder._u_display_name
        self._u_avatar_url = builder._u_avatar_url
        self._u_payment_information = builder._u_payment_information
        self._u_is_verified = builder._u_is_verified
        self._u_user_role = builder._u_user_role
        self._u_is_active = builder._u_is_active
        self._u_created_at = builder._u_created_at
        self._u_updated_at = builder._u_updated_at
        self._u_deleted_at = builder._u_deleted_at
        self._us_id = builder._us_id
        self._us_user_id = builder._us_user_id
        self._us_plan_id = builder._us_plan_id
        self._us_expire_at = builder._us_expire_at
        self._us_is_active = builder._us_is_active
        self._us_created_at = builder._us_created_at
        self._us_updated_at = builder._us_updated_at
        self._us_deleted_at = builder._us_deleted_at
        self._sp_id = builder._sp_id
        self._sp_plan_title = builder._sp_plan_title
        self._sp_plan_price = builder._sp_plan_price
        self._sp_available_model = builder._sp_available_model
        self._sp_message_credits = builder._sp_message_credits
        self._sp_number_of_chatbots = builder._sp_number_of_chatbots
        self._sp_max_character_per_chatbot = builder._sp_max_character_per_chatbot
        self._sp_live_agent_takeover = builder._sp_live_agent_takeover
        self._sp_remove_label = builder._sp_remove_label
        self._sp_is_active = builder._sp_is_active
        self._sp_created_at = builder._sp_created_at
        self._sp_updated_at = builder._sp_updated_at
        self._sp_deleted_at = builder._sp_deleted_at

    # Builder method
    @staticmethod
    def builder() -> 'UserSubscriptionPlan.Builder':
        return UserSubscriptionPlan.Builder()

    # Getters
    @property
    def u_id(self) -> uuid.UUID:
        return self._u_id

    @property
    def u_email(self) -> str:
        return self._u_email

    @property
    def u_password_hash(self) -> Optional[str]:
        return self._u_password_hash

    @property
    def u_display_name(self) -> str:
        return self._u_display_name

    @property
    def u_avatar_url(self) -> str:
        return self._u_avatar_url

    @property
    def u_payment_information(self) -> str:
        return self._u_payment_information

    @property
    def u_is_verified(self) -> bool:
        return self._u_is_verified

    @property
    def u_user_role(self) -> str:
        return self._u_user_role

    @property
    def u_is_active(self) -> bool:
        return self._u_is_active

    @property
    def u_created_at(self) -> datetime:
        return self._u_created_at

    @property
    def u_updated_at(self) -> datetime:
        return self._u_updated_at

    @property
    def u_deleted_at(self) -> Optional[datetime]:
        return self._u_deleted_at

    @property
    def us_id(self) -> uuid.UUID:
        return self._us_id

    @property
    def us_user_id(self) -> uuid.UUID:
        return self._us_user_id

    @property
    def us_plan_id(self) -> uuid.UUID:
        return self._us_plan_id

    @property
    def us_expire_at(self) -> datetime:
        return self._us_expire_at

    @property
    def us_is_active(self) -> bool:
        return self._us_is_active

    @property
    def us_created_at(self) -> datetime:
        return self._us_created_at

    @property
    def us_updated_at(self) -> datetime:
        return self._us_updated_at

    @property
    def us_deleted_at(self) -> Optional[datetime]:
        return self._us_deleted_at

    @property
    def sp_id(self) -> uuid.UUID:
        return self._sp_id

    @property
    def sp_plan_title(self) -> str:
        return self._sp_plan_title

    @property
    def sp_plan_price(self) -> float:
        return self._sp_plan_price

    @property
    def sp_available_model(self) -> str:
        return self._sp_available_model

    @property
    def sp_message_credits(self) -> int:
        return self._sp_message_credits

    @property
    def sp_number_of_chatbots(self) -> int:
        return self._sp_number_of_chatbots

    @property
    def sp_max_character_per_chatbot(self) -> int:
        return self._sp_max_character_per_chatbot

    @property
    def sp_live_agent_takeover(self) -> bool:
        return self._sp_live_agent_takeover

    @property
    def sp_remove_label(self) -> bool:
        return self._sp_remove_label

    @property
    def sp_is_active(self) -> bool:
        return self._sp_is_active

    @property
    def sp_created_at(self) -> datetime:
        return self._sp_created_at

    @property
    def sp_updated_at(self) -> datetime:
        return self._sp_updated_at

    @property
    def sp_deleted_at(self) -> Optional[datetime]:
        return self._sp_deleted_at

    # Define equality and hash methods
    def __eq__(self, other) -> bool:
        if isinstance(other, UserSubscriptionPlan):
            return self._u_id == other._u_id  # Compare based on unique property
        return False

    def __hash__(self) -> int:
        return hash(self._u_id)  # Hash based on unique property

    # String representation
    def __str__(self) -> str:
        def default(o):
            if isinstance(o, uuid.UUID):
                return str(o)
            elif isinstance(o, datetime):
                return o.isoformat()
            return o

        non_none_fields = {
            k.replace("_Builder_", ""): v
            for k, v in self.__dict__.items()
            if v is not None
        }
        formatted_fields = json.dumps(non_none_fields, default=default, indent=4)
        return f"{formatted_fields}"

    # Builder class
    class Builder:
        _u_id: uuid.UUID
        _u_email: str
        _u_password_hash: Optional[str]
        _u_display_name: str
        _u_avatar_url: str
        _u_payment_information: str
        _u_is_verified: bool
        _u_user_role: str
        _u_is_active: bool
        _u_created_at: datetime
        _u_updated_at: datetime
        _u_deleted_at: Optional[datetime]
        _us_id: uuid.UUID
        _us_user_id: uuid.UUID
        _us_plan_id: uuid.UUID
        _us_expire_at: datetime
        _us_is_active: bool
        _us_created_at: datetime
        _us_updated_at: datetime
        _us_deleted_at: Optional[datetime]
        _sp_id: uuid.UUID
        _sp_plan_title: str
        _sp_plan_price: float
        _sp_available_model: str
        _sp_message_credits: int
        _sp_number_of_chatbots: int
        _sp_max_character_per_chatbot: int
        _sp_live_agent_takeover: bool
        _sp_remove_label: bool
        _sp_is_active: bool
        _sp_created_at: datetime
        _sp_updated_at: datetime
        _sp_deleted_at: Optional[datetime]

        def __init__(self):
            self._u_id = None
            self._u_email = None
            self._u_password_hash = None
            self._u_display_name = None
            self._u_avatar_url = None
            self._u_payment_information = None
            self._u_is_verified = None
            self._u_user_role = None
            self._u_is_active = None
            self._u_created_at = None
            self._u_updated_at = None
            self._u_deleted_at = None
            self._us_id = None
            self._us_user_id = None
            self._us_plan_id = None
            self._us_expire_at = None
            self._us_is_active = None
            self._us_created_at = None
            self._us_updated_at = None
            self._us_deleted_at = None
            self._sp_id = None
            self._sp_plan_title = None
            self._sp_plan_price = None
            self._sp_available_model = None
            self._sp_message_credits = None
            self._sp_number_of_chatbots = None
            self._sp_max_character_per_chatbot = None
            self._sp_live_agent_takeover = None
            self._sp_remove_label = None
            self._sp_is_active = None
            self._sp_created_at = None
            self._sp_updated_at = None
            self._sp_deleted_at = None


        # Methods to set properties
        def with_u_id(self, u_id: uuid.UUID) -> 'UserSubscriptionPlan.Builder':
            self._u_id = u_id
            return self
        
        def with_u_email(self, u_email: str) -> 'UserSubscriptionPlan.Builder':
            self._u_email = u_email
            return self
        
        def with_u_password_hash(self, u_password_hash: Optional[str]) -> 'UserSubscriptionPlan.Builder':
            self._u_password_hash = u_password_hash
            return self
        
        def with_u_display_name(self, u_display_name: str) -> 'UserSubscriptionPlan.Builder':
            self._u_display_name = u_display_name
            return self
        
        def with_u_avatar_url(self, u_avatar_url: str) -> 'UserSubscriptionPlan.Builder':
            self._u_avatar_url = u_avatar_url
            return self
        
        def with_u_payment_information(self, u_payment_information: str) -> 'UserSubscriptionPlan.Builder':
            self._u_payment_information = u_payment_information
            return self
        
        def with_u_is_verified(self, u_is_verified: bool) -> 'UserSubscriptionPlan.Builder':
            self._u_is_verified = u_is_verified
            return self
        
        def with_u_user_role(self, u_user_role: str) -> 'UserSubscriptionPlan.Builder':
            self._u_user_role = u_user_role
            return self
        
        def with_u_is_active(self, u_is_active: bool) -> 'UserSubscriptionPlan.Builder':
            self._u_is_active = u_is_active
            return self
        
        def with_u_created_at(self, u_created_at: datetime) -> 'UserSubscriptionPlan.Builder':
            self._u_created_at = u_created_at
            return self
        
        def with_u_updated_at(self, u_updated_at: datetime) -> 'UserSubscriptionPlan.Builder':
            self._u_updated_at = u_updated_at
            return self
        
        def with_u_deleted_at(self, u_deleted_at: Optional[datetime]) -> 'UserSubscriptionPlan.Builder':
            self._u_deleted_at = u_deleted_at
            return self
        
        def with_us_id(self, us_id: uuid.UUID) -> 'UserSubscriptionPlan.Builder':
            self._us_id = us_id
            return self
        
        def with_us_user_id(self, us_user_id: uuid.UUID) -> 'UserSubscriptionPlan.Builder':
            self._us_user_id = us_user_id
            return self

        def with_us_plan_id(self, us_plan_id: uuid.UUID) -> 'UserSubscriptionPlan.Builder':
            self._us_plan_id = us_plan_id
            return self
        
        def with_us_expire_at(self, us_expire_at: datetime) -> 'UserSubscriptionPlan.Builder':
            self._us_expire_at = us_expire_at
            return self

        def with_us_is_active(self, us_is_active: bool) -> 'UserSubscriptionPlan.Builder':
            self._us_is_active = us_is_active
            return self
        
        def with_us_created_at(self, us_created_at: datetime) -> 'UserSubscriptionPlan.Builder':
            self._us_created_at = us_created_at
            return self
        
        def with_us_updated_at(self, us_updated_at: datetime) -> 'UserSubscriptionPlan.Builder':
            self._us_updated_at = us_updated_at
            return self
        
        def with_us_deleted_at(self, us_deleted_at: Optional[datetime]) -> 'UserSubscriptionPlan.Builder':
            self._us_deleted_at = us_deleted_at
            return self

        def with_sp_id(self, sp_id: uuid.UUID) -> 'UserSubscriptionPlan.Builder':
            self._sp_id = sp_id
            return self
        
        def with_sp_plan_title(self, sp_plan_title: str) -> 'UserSubscriptionPlan.Builder':
            self._sp_plan_title = sp_plan_title
            return self
        
        def with_sp_plan_price(self, sp_plan_price: float) -> 'UserSubscriptionPlan.Builder':
            self._sp_plan_price = sp_plan_price
            return self

        def with_sp_available_model(self, sp_available_model: str) -> 'UserSubscriptionPlan.Builder':
            self._sp_available_model = sp_available_model
            return self
        
        def with_sp_message_credits(self, sp_message_credits: int) -> 'UserSubscriptionPlan.Builder':
            self._sp_message_credits = sp_message_credits
            return self
        
        def with_sp_number_of_chatbots(self, sp_number_of_chatbots: int) -> 'UserSubscriptionPlan.Builder':
            self._sp_number_of_chatbots = sp_number_of_chatbots
            return self
        
        def with_sp_max_character_per_chatbot(self, sp_max_character_per_chatbot: int) -> 'UserSubscriptionPlan.Builder':
            self._sp_max_character_per_chatbot = sp_max_character_per_chatbot
            return self
        
        def with_sp_live_agent_takeover(self, sp_live_agent_takeover: bool) -> 'UserSubscriptionPlan.Builder':
            self._sp_live_agent_takeover = sp_live_agent_takeover
            return self
        
        def with_sp_remove_label(self, sp_remove_label: bool) -> 'UserSubscriptionPlan.Builder':
            self._sp_remove_label = sp_remove_label
            return self
        
        def with_sp_is_active(self, sp_is_active: bool) -> 'UserSubscriptionPlan.Builder':
            self._sp_is_active = sp_is_active
            return self
        
        def with_sp_created_at(self, sp_created_at: datetime) -> 'UserSubscriptionPlan.Builder':
            self._sp_created_at = sp_created_at
            return self
        
        def with_sp_updated_at(self, sp_updated_at: datetime) -> 'UserSubscriptionPlan.Builder':
            self._sp_updated_at = sp_updated_at
            return self
        
        def with_sp_deleted_at(self, sp_deleted_at: Optional[datetime]) -> 'UserSubscriptionPlan.Builder':
            self._sp_deleted_at = sp_deleted_at
            return self
        
        # Build method
        def build(self) -> 'UserSubscriptionPlan':
            return UserSubscriptionPlan(self)
