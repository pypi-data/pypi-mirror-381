from typing import Optional
from dotenv import get_key, set_key, unset_key

from nifty_anilist.utils.auth_utils import get_token, save_token, delete_token, generate_new_token, get_user_from_token, is_token_expired
from nifty_anilist.logging import anilist_logger as logger


DOTENV_PATH = ".env"
GLOBAL_USER_ENV_VAR = "ANILIST_CURRENT_USER"


class AuthInfo:
    user_id: str
    token: str

    def __init__(self, user_id: str, token: str) -> None:
        self.user_id = user_id
        self.token = token

def sign_in(set_global: bool = False) -> AuthInfo:
    """Manually sign into Anilist.

    Args:
        set_global: If `True`, the user signed which signed will be set as the global user.

    Returns:
        auth_info: Auth info for the user, including an auth token that can be used in Anilist requests.
    """

    # Generate auth token from this auth code.
    auth_token = generate_new_token()

    # Get the user ID of the user to whom the auth token belongs.
    user_id = get_user_from_token(auth_token)

    # Save the auth token under this user.
    save_token(user_id, auth_token)

    # Make this the global user if needed.
    if set_global:
        set_global_user(user_id)

    return AuthInfo(user_id, auth_token)


def sign_in_if_no_global() -> Optional[AuthInfo]:
    """Manually sign into Anilist if there is currently no global user.
    Will do nothing if there is already a global user.
    Run this near the start of your program to setup a global user (if you plan to use one).
    
    Returns:
        auth_info: Auth info for the user, if there 
    """
    if get_global_user() is None:
        return sign_in(set_global=True)
    else:
        return None


def get_auth_info(user_id: Optional[str] = None) -> AuthInfo:
    """Get auth info for Anilist requests. Required for any write operations.
    This token lasts 1 year and will be securely stored on your machine.
    If the token does not exist on your machine or is expired, this function will generate a new one.

    Args:
        user_id: Optional ID of the user to get the auth token for.
            If not provided, will try getting the auth token of the global user.
    
    Returns:
        auth_info: Auth info for the user, including an auth token that can be used in Anilist requests.
    """
    auth_token: Optional[str] = None

    # If a user was provided, user their ID.
    if user_id:
        auth_token = get_token(user_id)
    # Otherwise, get the current global user from .env.
    else:
        user_id = get_global_user()
        if user_id:
            auth_token = get_token(user_id)
        else:
            raise Exception("No global user was found!")

    # If token was not found or is expired, make a new one.
    if auth_token is None or is_token_expired(auth_token):
        logger.warning("No auth token was found. Generating a new one!")

        return sign_in()

    return AuthInfo(user_id, auth_token)


def get_global_user() -> Optional[str]:
    """Get the current global user('s ID).
    
    Returns:
        user_id: ID of the global user or `None` if there is no global user.
    """
    return get_key(DOTENV_PATH, GLOBAL_USER_ENV_VAR)


def set_global_user(user_id: str) -> AuthInfo:
    """Set the global user.
    **Note:** This does *not* remove the previous user's auth token from your machine.
    
    Args:
        user_id: ID of the user to set the global user to.

    Returns:
        auth: Auth info of this user.
    """
    set_key(DOTENV_PATH, GLOBAL_USER_ENV_VAR, user_id)
    return get_auth_info(user_id)


def logout_global_user():
    """Log out the global user.
    **Note:** This does *not* remove their auth token from your machine.
    """
    unset_key(DOTENV_PATH, GLOBAL_USER_ENV_VAR)


def remove_user(user_to_remove: Optional[str] = None) -> str:
    """Removes a user. This will remove their auth token from your machine.
    
    Args:
        user_to_remove: Optional ID of user to sign out.
            If not provided, will try signing out the global user.

    Returns:
        user_id: ID of the user that was removed.
    """
    # If no user provided, try removing the global user.
    if not user_to_remove:
        user_to_remove = get_global_user()

        # If the current global user was the one being signed out, remove their status as the global user.
        if user_to_remove:
            logout_global_user()
        else:
            raise Exception("No global user was found to remove.") 

    delete_token(user_to_remove)

    return user_to_remove

