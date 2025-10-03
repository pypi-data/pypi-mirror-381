"""
The MIT License (MIT)

Copyright (c) 2024-present MCausc78

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations

import typing

from attrs import define, field

from .base import Base
from .cache import CacheContextType, UserThroughBotOwnerCacheContext, _USER_THROUGH_BOT_OWNER
from .core import UNDEFINED, UndefinedOr
from .errors import NoData
from .flags import BotFlags

if typing.TYPE_CHECKING:
    from . import raw
    from .enums import OAuth2Scope
    from .http import HTTPOverrideOptions
    from .oauth2 import OAuth2ScopeReasoning
    from .user import User

_new_bot_flags = BotFlags.__new__


@define(slots=True)
class BaseBot(Base):
    """Represents a base bot on Stoat.

    This inherits from :class:`Base`.
    """

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, BaseBot) and self.id == other.id

    async def delete(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> None:
        """|coro|

        Deletes the bot.

        Fires :class:`.UserUpdateEvent` for all users who `are subscribed <server_subscriptions>_` to bot user.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------+----------------------------------------+
            | Value               | Reason                                 |
            +---------------------+----------------------------------------+
            | ``InvalidSession``  | The current bot/user token is invalid. |
            +---------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+--------------------------------------------------------------+
            | Value        | Reason                                                       |
            +--------------+--------------------------------------------------------------+
            | ``NotFound`` | The bot was not found, or the current user does not own bot. |
            +--------------+--------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.state.http.delete_bot(self.id, http_overrides=http_overrides)

    async def edit(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        name: UndefinedOr[str] = UNDEFINED,
        public: UndefinedOr[bool] = UNDEFINED,
        analytics: UndefinedOr[bool] = UNDEFINED,
        interactions_url: UndefinedOr[typing.Optional[str]] = UNDEFINED,
        oauth2: UndefinedOr[typing.Optional[BotOAuth2Edit]] = UNDEFINED,
        reset_oauth2_client_secret: bool = False,
        reset_token: bool = False,
    ) -> Bot:
        """|coro|

        Edits the bot.

        Fires :class:`UserUpdateEvent` for all users who `are subscribed <server_subscriptions>`_ to bot user.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        name: UndefinedOr[:class:`str`]
            The new bot name. Must be between 2 and 32 characters and not contain whitespace characters.
        public: UndefinedOr[:class:`bool`]
            Whether the bot should be public (could be invited by anyone).
        analytics: UndefinedOr[:class:`bool`]
            Whether to allow Stoat collect analytics about the bot.
        interactions_url: UndefinedOr[Optional[:class:`str`]]
            The new bot interactions URL. For now, this parameter is reserved and does not do anything.
        oauth2: UndefinedOr[Optional[:class:`BotOAuth2Edit`]]
            The new bot's OAuth2 settings.
        reset_oauth2_client_secret: :class:`bool`
            Whether to reset bot's OAuth2 client secret. The new client secret can be accessed via :attr:`BotOAuth2.secret`.
        reset_token: :class:`bool`
            Whether to reset bot token. The new token can be accessed via ``bot.token``.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+---------------------------------------------------------+
            | Value                | Reason                                                  |
            +----------------------+---------------------------------------------------------+
            | ``FailedValidation`` | The bot's name exceeded length or contained whitespace. |
            +----------------------+---------------------------------------------------------+
            | ``InvalidUsername``  | The bot's name had forbidden characters/substrings.     |
            +----------------------+---------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+--------------------------------------------------------------+
            | Value        | Reason                                                       |
            +--------------+--------------------------------------------------------------+
            | ``NotFound`` | The bot was not found, or the current user does not own bot. |
            +--------------+--------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`Bot`
            The updated bot.
        """
        return await self.state.http.edit_bot(
            self.id,
            http_overrides=http_overrides,
            name=name,
            public=public,
            analytics=analytics,
            interactions_url=interactions_url,
            oauth2=oauth2,
            reset_token=reset_token,
            reset_oauth2_client_secret=reset_oauth2_client_secret,
        )


@define(slots=True)
class Bot(BaseBot):
    """Represents a bot on Stoat.

    This inherits from :class:`BaseBot`.
    """

    owner_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's ID who owns this bot."""

    token: str = field(repr=False)
    """:class:`str`: The bot's token used to authenticate requests."""

    public: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the bot is public (may be invited by anyone)."""

    analytics: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether to enable analytics."""

    discoverable: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the bot is publicly discoverable."""

    interactions_url: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The URL to send interactions to.
    
    .. note::
        This attribute is reserved.
    """

    terms_of_service_url: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The Terms of Service's URL."""

    privacy_policy_url: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The privacy policy URL."""

    oauth2: typing.Optional[BotOAuth2] = field(repr=True, kw_only=True)
    """Optional[:class:`BotOAuth2`]: The bot's OAuth2 settings.
    
    .. versionadded:: 1.2
    """

    raw_flags: int = field(repr=True, kw_only=True)
    """:class:`int`: The bot's flags raw value."""

    user: User = field(repr=True, kw_only=True)
    """:class:`User`: The user associated with this bot."""

    def get_owner(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user who owns this bot."""
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughBotOwnerCacheContext(
                type=CacheContextType.user_through_bot_owner,
                bot=self,
            )
            if state.provide_cache_context('Bot.owner')
            else _USER_THROUGH_BOT_OWNER
        )

        return cache.get_user(self.owner_id, ctx)

    @property
    def flags(self) -> BotFlags:
        """:class:`BotFlags`: The bot's flags."""
        ret = _new_bot_flags(BotFlags)
        ret.value = self.raw_flags
        return ret

    @property
    def owner(self) -> User:
        """:class:`User`: The user who owns this bot."""
        owner = self.get_owner()
        if owner is None:
            raise NoData(what=self.owner_id, type='Bot.owner')
        return owner

    def to_dict(self) -> raw.Bot:
        """:class:`dict`: Convert bot to raw data."""
        payload: raw.Bot = {
            '_id': self.id,
            'owner': self.owner_id,
            'token': self.token,
            'public': self.public,
        }
        if self.analytics:
            payload['analytics'] = self.analytics
        if self.discoverable:
            payload['discoverable'] = self.discoverable
        if self.interactions_url is not None:
            payload['interactions_url'] = self.interactions_url
        if self.terms_of_service_url is not None:
            payload['terms_of_service_url'] = self.terms_of_service_url
        if self.privacy_policy_url is not None:
            payload['privacy_policy_url'] = self.privacy_policy_url
        if self.oauth2 is not None:
            payload['oauth2'] = self.oauth2.to_dict()
        if self.raw_flags != 0:
            payload['flags'] = self.raw_flags
        return payload


@define(slots=True)
class PublicBot(BaseBot):
    """Represents public bot on Stoat.

    This inherits from :class:`BaseBot`.
    """

    name: str = field(repr=True, kw_only=True)
    """:class:`str`: The bot's name."""

    internal_avatar_id: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The bot's avatar ID."""

    description: str = field(repr=True, kw_only=True)
    """:class:`str`: The bot's description."""

    def to_dict(self) -> raw.PublicBot:
        """:class:`dict`: Convert public bot to raw data."""
        payload: raw.PublicBot = {
            '_id': self.id,
            'username': self.name,
        }
        if self.internal_avatar_id is not None:
            payload['avatar'] = self.internal_avatar_id
        if len(self.description):
            payload['description'] = self.description
        return payload


@define(slots=True)
class BotOAuth2:
    """Represents how the bot does use OAuth2.

    .. versionadded:: 1.2
    """

    public: bool = field(repr=True, kw_only=True, eq=True)
    """:class:`bool`: Whether bot users do not need to invoke server to exchange code."""

    secret: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The client secret, only available if :attr:`public` is ``False``."""

    redirect_uris: list[str] = field(repr=True, kw_only=True, eq=True)
    """List[:class:`str`]: The whitelisted URIs for redirecting to during OAuth2 authorization."""

    allowed_scopes: dict[str, OAuth2ScopeReasoning] = field(repr=True, kw_only=True, eq=True)
    """Dict[:class:`str`, :class:`OAuth2ScopeReasoning`]: A mapping of OAuth2 scopes to reasoning why would it be requested."""

    def to_dict(self) -> raw.BotOauth2:
        return {
            'public': self.public,
            'secret': self.secret,
            'redirects': self.redirect_uris,
            'allowed_scopes': {k: v.to_dict() for k, v in self.allowed_scopes.items()},  # type: ignore
        }


class BotOAuth2Edit:
    """Represents new bot's OAuth2 settings.

    .. versionadded:: 1.2

    Attributes
    ----------
    public: UndefinedOr[:class:`bool`
        Whether the bot is a public client.
    redirect_uris: UndefinedOr[List[:class:`str`]]
        The whitelisted URIs for redirecting to during OAuth2 authorization. Must be between 1 and 10 items.
    allowed_scopes: UndefinedOr[Dict[Union[:class:`OAuth2Scope`, :class:`str`], :class:`OAuth2ScopeReasoning`]]
        A mapping of OAuth2 scopes to reasoning why would it be requested.
    """

    __slots__ = (
        'public',
        'redirect_uris',
        'allowed_scopes',
    )

    def __init__(
        self,
        *,
        public: UndefinedOr[bool] = UNDEFINED,
        redirect_uris: UndefinedOr[list[str]] = UNDEFINED,
        allowed_scopes: UndefinedOr[dict[typing.Union[OAuth2Scope, str], OAuth2ScopeReasoning]] = UNDEFINED,
    ) -> None:
        self.public: UndefinedOr[bool] = public
        self.redirect_uris: UndefinedOr[list[str]] = redirect_uris
        self.allowed_scopes: UndefinedOr[dict[typing.Union[OAuth2Scope, str], OAuth2ScopeReasoning]] = allowed_scopes

    @property
    def remove(self) -> list[raw.FieldsBot]:
        return []

    def to_dict(self) -> raw.DataEditBotOauth2:
        payload: raw.DataEditBotOauth2 = {}
        if self.public is not UNDEFINED:
            payload['public'] = self.public
        if self.redirect_uris is not UNDEFINED:
            payload['redirects'] = self.redirect_uris
        if self.allowed_scopes is not UNDEFINED:
            payload['allowed_scopes'] = {  # type: ignore
                k.value if isinstance(k, OAuth2Scope) else k: v.to_dict() for k, v in self.allowed_scopes.items()
            }

        return payload


__all__ = (
    'BaseBot',
    'Bot',
    'PublicBot',
    'BotOAuth2',
    'BotOAuth2Edit',
)
