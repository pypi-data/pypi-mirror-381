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

from attrs import define, field
import typing

from . import routes
from .abc import Messageable, Connectable
from .base import Base
from .cache import (
    CacheContextType,
    UserThroughUserBotOwnerCacheContext,
    ChannelThroughUserDMChannelIDCacheContext,
    ChannelIDThroughUserDMChannelIDCacheContext,
    _USER_THROUGH_USER_BOT_OWNER,
    _CHANNEL_THROUGH_USER_DM_CHANNEL,
    _CHANNEL_ID_THROUGH_USER_DM_CHANNEL_ID,
)
from .cdn import StatelessAsset, Asset, ResolvableResource, resolve_resource
from .core import (
    UNDEFINED,
    UndefinedOr,
    ULIDOr,
)
from .flags import UserPermissions, UserBadges, UserFlags
from .enums import UserReportReason, Presence, RelationshipStatus
from .errors import NoData

if typing.TYPE_CHECKING:
    from datetime import datetime

    from . import raw
    from .channel import SavedMessagesChannel, DMChannel
    from .http import HTTPOverrideOptions
    from .message import BaseMessage
    from .state import State

_new_user_badges = UserBadges.__new__
_new_user_flags = UserFlags.__new__


@define(slots=True)
class UserStatus:
    """Represents user's active status."""

    text: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The custom status text."""

    presence: typing.Optional[Presence] = field(repr=True, kw_only=True)
    """Optional[:class:`Presence`]: The current presence option."""

    def locally_update(self, data: UserStatusEdit, /) -> None:
        """Locally updates user status with provided data.

        .. warning::
            This is called by library internally to keep cache up to date.
        """
        if data.text is not UNDEFINED:
            self.text = data.text
        if data.presence is not UNDEFINED:
            self.presence = data.presence

    def to_dict(self) -> raw.UserStatus:
        """:class:`dict`: Convert user status to raw data."""

        payload: raw.UserStatus = {}
        if self.text is not None:
            payload['text'] = self.text
        if self.presence is not None:
            payload['presence'] = self.presence.value
        return payload


class UserStatusEdit:
    """Represents partial user's status.

    Attributes
    ----------
    text: UndefinedOr[Optional[:class:`str`]]
        The new custom status text.
    presence: UndefinedOr[Optional[:class:`Presence`]]
        The presence to use.
    """

    __slots__ = ('text', 'presence')

    def __init__(
        self,
        *,
        text: UndefinedOr[typing.Optional[str]] = UNDEFINED,
        presence: UndefinedOr[typing.Optional[Presence]] = UNDEFINED,
    ) -> None:
        self.text: UndefinedOr[typing.Optional[str]] = text
        self.presence: UndefinedOr[typing.Optional[Presence]] = presence

    @property
    def remove(self) -> list[raw.FieldsUser]:
        remove: list[raw.FieldsUser] = []
        if self.text is None:
            remove.append('StatusText')
        if self.presence is None:
            remove.append('StatusPresence')
        return remove

    def to_dict(self) -> raw.UserStatus:
        payload: raw.UserStatus = {}
        if self.text not in (None, UNDEFINED):
            payload['text'] = self.text
        if self.presence not in (None, UNDEFINED):
            payload['presence'] = self.presence.value
        return payload


@define(slots=True)
class StatelessUserProfile:
    r"""Represents Stoat :class:`User`\'s stateless profile."""

    content: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The user's profile content."""

    internal_background: typing.Optional[StatelessAsset] = field(repr=True, kw_only=True)
    """Optional[:class:`StatelessAsset`]: The stateless background visible on user's profile."""

    def attach_state(self, state: State, user_id: str, /) -> UserProfile:
        """:class:`UserProfile`: Attach a state to user profile.

        Parameters
        ----------
        state: :class:`State`
            The state to attach.
        user_id: :class:`str`
            The user's ID to attach.
        """
        return UserProfile(
            content=self.content,
            internal_background=self.internal_background,
            state=state,
            user_id=user_id,
        )


@define(slots=True)
class UserProfile(StatelessUserProfile):
    r"""Represents Stoat :class:`User`\'s profile.

    This inherits from :class:`StatelessUserProfile`.
    """

    state: State = field(repr=False, kw_only=True)
    """:class:`State`: The internal state used to attach state to other fields."""

    user_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's ID who holds this profile."""

    @property
    def background(self) -> typing.Optional[Asset]:
        """Optional[:class:`Asset`]: The background visible on user's profile."""
        return self.internal_background and self.internal_background.attach_state(self.state, 'backgrounds')


@define(slots=True)
class PartialUserProfile:
    """Represents partial user's profile."""

    state: State = field(repr=False, kw_only=True)
    """:class:`State`: The state."""

    content: UndefinedOr[typing.Optional[str]] = field(repr=True, kw_only=True)
    """Undefined[Optional[:class:`str`]]: The user's profile content."""

    internal_background: UndefinedOr[typing.Optional[StatelessAsset]] = field(repr=True, kw_only=True)
    """Undefined[Optional[:class:`StatelessAsset`]]: The new stateless background visible on user's profile."""

    @property
    def background(self) -> UndefinedOr[typing.Optional[Asset]]:
        """UndefinedOr[Optional[:class:`Asset`]]: The new background visible on user's profile."""
        return self.internal_background and self.internal_background.attach_state(self.state, 'backgrounds')


class UserProfileEdit:
    """Partially represents user's profile.

    Attributes
    ----------
    content: UndefinedOr[Optional[:class:`str`]]
        The text to use in user profile description.
    background: UndefinedOr[Optional[:class:`ResolvableResource`]]
        The background to use on user's profile.
    """

    __slots__ = ('content', 'background')

    def __init__(
        self,
        content: UndefinedOr[typing.Optional[str]] = UNDEFINED,
        *,
        background: UndefinedOr[typing.Optional[ResolvableResource]] = UNDEFINED,
    ) -> None:
        self.content: UndefinedOr[typing.Optional[str]] = content
        self.background: UndefinedOr[typing.Optional[ResolvableResource]] = background

    @property
    def remove(self) -> list[raw.FieldsUser]:
        remove: list[raw.FieldsUser] = []
        if self.content is None:
            remove.append('ProfileContent')
        if self.background is None:
            remove.append('ProfileBackground')
        return remove

    async def to_dict(self, state: State, /) -> raw.DataUserProfile:
        """Convert user profile edit to raw data.

        Parameters
        ----------
        state: :class:`State`
            The state. Required to resolve :attr:`~UserProfileEdit.media` attribute into file ID.

        Returns
        -------
        :class:`dict`
            The raw data.
        """
        payload: raw.DataUserProfile = {}
        if self.content not in (None, UNDEFINED):
            payload['content'] = self.content
        if self.background not in (None, UNDEFINED):
            payload['background'] = await resolve_resource(state, self.background, tag='backgrounds')
        return payload


@define(slots=True)
class Relationship:
    """Represents a relationship entry indicating current status with other user."""

    id: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's ID the relationship with."""

    status: RelationshipStatus = field(repr=True, kw_only=True)
    """:class:`RelationshipStatus`: The relationship status with them."""

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, Relationship) and self.id == other.id and self.status == other.status

    def to_dict(self) -> raw.Relationship:
        """:class:`dict`: Convert relationship to raw data."""

        return {
            '_id': self.id,
            'status': self.status.value,
        }


@define(slots=True)
class Mutuals:
    """Mutual friends and servers response."""

    user_ids: list[str] = field(repr=True, kw_only=True)
    """List[:class:`str`]: The user's IDs that both you and target user are friends with."""

    server_ids: list[str] = field(repr=True, kw_only=True)
    """List[:class:`str`]: The server's IDs that both users are in."""

    channel_ids: list[str] = field(repr=True, kw_only=True)
    """List[:class:`str`]: The private channel's IDs that both users are in.
    
    .. versionadded:: 1.2
    """


@define(slots=True)
class BaseUser(Base, Connectable, Messageable):
    """Represents an user on Stoat.

    This inherits from :class:`Base`, :class:`~stoat.abc.Connectable` and :class:`~stoat.abc.Messageable`.
    """

    def get_channel_id(self) -> str:
        return self.dm_channel_id or ''

    def is_sentinel(self) -> bool:
        """:class:`bool`: Returns whether the user is sentinel (Stoat#0000)."""
        return self is self.state.system

    def __eq__(self, other: object, /) -> bool:
        if self is other:
            return True

        from .server import BaseMember

        return isinstance(other, (BaseMember, BaseUser)) and self.id == other.id

    def __ne__(self, other: object, /) -> bool:
        if self is other:
            return False

        from .server import BaseMember

        if isinstance(other, (BaseMember, BaseUser)):
            return self.id != other.id
        return True

    @property
    def mention(self) -> str:
        """:class:`str`: The user mention."""
        return f'<@{self.id}>'

    @property
    def default_avatar_url(self) -> str:
        """:class:`str`: The URL to user's default avatar."""
        return self.state.http.url_for(routes.USERS_GET_DEFAULT_AVATAR.compile(user_id=self.id))

    @property
    def dm_channel_id(self) -> typing.Optional[str]:
        """Optional[:class:`str`]: The ID of the private channel with this user."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ChannelIDThroughUserDMChannelIDCacheContext(
                type=CacheContextType.channel_id_through_user_dm_channel_id,
                user=self,
            )
            if state.provide_cache_context('User.dm_channel_id')
            else _CHANNEL_ID_THROUGH_USER_DM_CHANNEL_ID
        )

        return cache.get_private_channel_by_user(self.id, ctx)

    pm_id = dm_channel_id

    @property
    def dm_channel(self) -> typing.Optional[DMChannel]:
        """Optional[:class:`DMChannel`]: The private channel with this user."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ChannelThroughUserDMChannelIDCacheContext(
                type=CacheContextType.channel_through_user_dm_channel,
                user=self,
            )
            if state.provide_cache_context('User.dm_channel')
            else _CHANNEL_THROUGH_USER_DM_CHANNEL
        )

        channel_id = cache.get_private_channel_by_user(self.id, ctx)
        if channel_id is None:
            return None

        channel = cache.get_channel(channel_id, ctx)
        if channel is not None:
            from .channel import DMChannel

            assert isinstance(channel, DMChannel)

        return channel

    pm = dm_channel

    async def accept_friend_request(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> User:
        """|coro|

        Accept another user's friend request.

        Fires :class:`UserRelationshipUpdateEvent` for the current user and user you accepted friend request from.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------------------+-------------------------------------------------------------------------------------------+
            | Value                            | Reason                                                                                    |
            +----------------------------------+-------------------------------------------------------------------------------------------+
            | ``IsBot``                        | Either the current user or user you tried to accept friend request from are bot accounts. |
            +----------------------------------+-------------------------------------------------------------------------------------------+
            | ``TooManyPendingFriendRequests`` | You sent too many outgoing friend requests.                                               |
            +----------------------------------+-------------------------------------------------------------------------------------------+
        :class:`NoEffect`
            You tried to accept friend request from yourself.
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +------------------+--------------------------------------------------------------------+
            | Value            | Reason                                                             |
            +------------------+--------------------------------------------------------------------+
            | ``BlockedOther`` | The user you tried to accept friend request from have blocked you. |
            +------------------+--------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`Conflict`
            Possible values for :attr:`~HTTPException.type`:

            +------------------------+---------------------------------------------------------------------------+
            | Value                  | Reason                                                                    |
            +------------------------+---------------------------------------------------------------------------+
            | ``AlreadyFriends``     | You're already friends with user you tried to accept friend request from. |
            +------------------------+---------------------------------------------------------------------------+
            | ``AlreadySentRequest`` | You already sent friend request to this user.                             |
            +------------------------+---------------------------------------------------------------------------+
            | ``Blocked``            | You have blocked the user you tried to accept friend request from.        |
            +------------------------+---------------------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`User`
            The user you accepted friend request from.
        """
        return await self.state.http.accept_friend_request(self.id, http_overrides=http_overrides)

    async def block(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> User:
        """|coro|

        Blocks an user.

        Fires :class:`UserRelationshipUpdateEvent` for the current user and blocked user.

        .. note::
            This is not supposed to be used by bot accounts.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`NoEffect`
            You tried to block yourself or someone that you already had blocked.
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`User`
            The blocked user.
        """

        return await self.state.http.block_user(self.id, http_overrides=http_overrides)

    async def deny_friend_request(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> User:
        """|coro|

        Denies another user's friend request.

        Fires :class:`UserRelationshipUpdateEvent` for the current user and user you denide friend request from.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +-----------+-----------------------------------------------------------------------------------------+
            | Value     | Reason                                                                                  |
            +-----------+-----------------------------------------------------------------------------------------+
            | ``IsBot`` | Either the current user or user you tried to deny friend request from are bot accounts. |
            +-----------+-----------------------------------------------------------------------------------------+
        :class:`NoEffect`
            You tried to deny friend request from user you had no friend request sent from/to.
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`User`
            The user you denied friend request from.
        """

        return await self.state.http.deny_friend_request(self.id, http_overrides=http_overrides)

    async def edit(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        display_name: UndefinedOr[typing.Optional[str]] = UNDEFINED,
        avatar: UndefinedOr[typing.Optional[ResolvableResource]] = UNDEFINED,
        status: UndefinedOr[UserStatusEdit] = UNDEFINED,
        profile: UndefinedOr[UserProfileEdit] = UNDEFINED,
        badges: UndefinedOr[UserBadges] = UNDEFINED,
        flags: UndefinedOr[UserFlags] = UNDEFINED,
    ) -> User:
        """|coro|

        Edits the user.

        Fires :class:`UserUpdateEvent` for all users who `are subscribed <server_subscriptions>`_ to target user.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        display_name: UndefinedOr[Optional[:class:`str`]]
            The new display name. Must be between 2 and 32 characters and not contain zero width space, newline or carriage return characters.
        avatar: UndefinedOr[Optional[:class:`ResolvableResource`]]
            The new avatar. Could be ``None`` to remove avatar.
        status: UndefinedOr[:class:`UserStatusEdit`]
            The new user status.
        profile: UndefinedOr[:class:`UserProfileEdit`]
            The new user profile data. This is applied as a partial.
        badges: UndefinedOr[:class:`UserBadges`]
            The new user badges. You must be privileged user to provide this.
        flags: UndefinedOr[:class:`UserFlags`]
            The new user flags. You must be privileged user to provide this.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+--------------------------+
            | Value                | Reason                   |
            +----------------------+--------------------------+
            | ``FailedValidation`` | The payload was invalid. |
            +----------------------+--------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+--------------------------------------------------------------------------------------------------+
            | Value             | Reason                                                                                           |
            +-------------------+--------------------------------------------------------------------------------------------------+
            | ``NotPrivileged`` | You tried to edit fields that require you to be privileged, or tried to edit bot you do not own. |
            +-------------------+--------------------------------------------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`User`
            The newly updated user.
        """
        return await self.state.http.edit_user(
            self.id,
            http_overrides=http_overrides,
            display_name=display_name,
            avatar=avatar,
            status=status,
            profile=profile,
            badges=badges,
            flags=flags,
        )

    async def fetch(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> User:
        """|coro|

        Retrieve user's information.

        You must have :attr:`~UserPermissions.access` to do this.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +------------------------+----------------------------------------+
            | Value                  | Reason                                 |
            +------------------------+----------------------------------------+
            | ``InvalidSession``     | The current bot/user token is invalid. |
            +------------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+------------------------------------------------------------------+
            | Value                     | Reason                                                           |
            +---------------------------+------------------------------------------------------------------+
            | ``MissingUserPermission`` | You do not have the proper permissions to view access user data. |
            +---------------------------+------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+

        Returns
        -------
        :class:`User`
            The retrieved user.
        """
        return await self.state.http.get_user(self.id, http_overrides=http_overrides)

    async def fetch_channel_id(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> str:
        channel_id = self.dm_channel_id
        if channel_id:
            return channel_id

        channel = await self.open_dm(http_overrides=http_overrides)
        return channel.id

    async def fetch_default_avatar(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> bytes:
        """|coro|

        Return a default user avatar based on the given ID.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Returns
        -------
        :class:`bytes`
            The image in PNG format.
        """
        return await self.state.http.get_default_avatar(self.id, http_overrides=http_overrides)

    async def fetch_flags(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> UserFlags:
        """|coro|

        Retrieves flags for user.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Returns
        -------
        :class:`UserFlags`
            The retrieved flags.
        """
        return await self.state.http.get_user_flags(self.id, http_overrides=http_overrides)

    async def fetch_profile(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> UserProfile:
        """|coro|

        Retrieve profile of an user.

        You must have :attr:`~UserPermissions.view_profile` to do this.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +------------------------+----------------------------------------+
            | Value                  | Reason                                 |
            +------------------------+----------------------------------------+
            | ``InvalidSession``     | The current bot/user token is invalid. |
            +------------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+--------------------------------------------------------------+
            | Value                     | Reason                                                       |
            +---------------------------+--------------------------------------------------------------+
            | ``MissingUserPermission`` | You do not have the proper permissions to view user profile. |
            +---------------------------+--------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+

        Returns
        -------
        :class:`UserProfile`
            The retrieved user profile.
        """

        return await self.state.http.get_user_profile(self.id, http_overrides=http_overrides)

    async def mutual_friend_ids(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> list[str]:
        """|coro|

        Retrieves a list of mutual friend user IDs with another user.

        You must have :attr:`~UserPermissions.view_profile` to do this.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+----------------------------------------------+
            | Value                | Reason                                       |
            +----------------------+----------------------------------------------+
            | ``InvalidOperation`` | You tried to retrieve mutuals with yourself. |
            +----------------------+----------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+--------------------------------------------------------------+
            | Value                     | Reason                                                       |
            +---------------------------+--------------------------------------------------------------+
            | ``MissingUserPermission`` | You do not have the proper permissions to view user profile. |
            +---------------------------+--------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        List[:class:`str`]
            The found mutual friend user IDs.
        """

        mutuals = await self.state.http.get_mutuals_with(self.id, http_overrides=http_overrides)
        return mutuals.user_ids

    async def mutual_server_ids(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> list[str]:
        """|coro|

        Retrieves a list of mutual server IDs with another user.

        You must have :attr:`~UserPermissions.view_profile` to do this.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+----------------------------------------------+
            | Value                | Reason                                       |
            +----------------------+----------------------------------------------+
            | ``InvalidOperation`` | You tried to retrieve mutuals with yourself. |
            +----------------------+----------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+--------------------------------------------------------------+
            | Value                     | Reason                                                       |
            +---------------------------+--------------------------------------------------------------+
            | ``MissingUserPermission`` | You do not have the proper permissions to view user profile. |
            +---------------------------+--------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        List[:class:`str`]
            The found mutual server IDs.
        """
        mutuals = await self.state.http.get_mutuals_with(self.id, http_overrides=http_overrides)
        return mutuals.server_ids

    async def mutuals(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> Mutuals:
        """|coro|

        Retrieves a list of mutual friends and servers with another user.

        You must have :attr:`~UserPermissions.view_profile` to do this.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+----------------------------------------------+
            | Value                | Reason                                       |
            +----------------------+----------------------------------------------+
            | ``InvalidOperation`` | You tried to retrieve mutuals with yourself. |
            +----------------------+----------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+--------------------------------------------------------------+
            | Value                     | Reason                                                       |
            +---------------------------+--------------------------------------------------------------+
            | ``MissingUserPermission`` | You do not have the proper permissions to view user profile. |
            +---------------------------+--------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`Mutuals`
            The found mutuals.
        """
        return await self.state.http.get_mutuals_with(self.id, http_overrides=http_overrides)

    async def open_dm(
        self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None
    ) -> typing.Union[SavedMessagesChannel, DMChannel]:
        """|coro|

        Retrieve a DM (or create if it doesn't exist) with another user.

        If target is current user, a :class:`SavedMessagesChannel` is always returned.

        You must have :attr:`~UserPermissions.send_messages` to do this.

        May fire :class:`PrivateChannelCreateEvent` for the current user and user you opened DM with.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+-------------------------------------------------------------------+
            | Value                     | Reason                                                            |
            +---------------------------+-------------------------------------------------------------------+
            | ``MissingUserPermission`` | You do not have the proper permissions to open DM with this user. |
            +---------------------------+-------------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        Union[:class:`SavedMessagesChannel`, :class:`DMChannel`]
            The private channel.
        """

        return await self.state.http.open_dm(self.id, http_overrides=http_overrides)

    async def remove_friend(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> User:
        """|coro|

        Removes the user from friend list.

        Fires :class:`UserRelationshipUpdateEvent` for the current user and user you removed from friend list.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +-----------+-----------------------------------------------------------------------------------------+
            | Value     | Reason                                                                                  |
            +-----------+-----------------------------------------------------------------------------------------+
            | ``IsBot`` | Either the current user or user you tried to deny friend request from are bot accounts. |
            +-----------+-----------------------------------------------------------------------------------------+
        :class:`NoEffect`
            You tried to deny friend request from user you had no friend request sent from/to.
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`User`
            The user you removed from friend list.
        """

        return await self.state.http.remove_friend(self.id, http_overrides=http_overrides)

    async def report(
        self,
        reason: UserReportReason,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        additional_context: typing.Optional[str] = None,
        message_context: typing.Optional[ULIDOr[BaseMessage]] = None,
    ) -> None:
        """|coro|

        Report the user to the instance moderation team.

        Fires :class:`ReportCreateEvent` internally (but not fired over WebSocket).

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        reason: :class:`UserReportReason`
            The reason for reporting user.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        additional_context: Optional[:class:`str`]
            The additional context for moderation team. Can be only up to 1000 characters.
        message_context: Optional[ULIDOr[:class:`BaseMessage`]]
            The message context.

            Internally, 15 messages around provided message will be snapshotted for context. All attachments of provided message are snapshotted as well.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------------+-------------------------------+
            | Value                    | Reason                        |
            +--------------------------+-------------------------------+
            | ``CannotReportYourself`` | You tried to report yourself. |
            +--------------------------+-------------------------------+
            | ``FailedValidation``     | The payload was invalid.      |
            +--------------------------+-------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------------+
            | Value        | Reason                          |
            +--------------+---------------------------------+
            | ``NotFound`` | The user/message was not found. |
            +--------------+---------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.state.http.report_user(
            self.id,
            reason,
            http_overrides=http_overrides,
            additional_context=additional_context,
            message_context=message_context,
        )

    async def unblock(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> User:
        """|coro|

        Unblocks an user.

        Fires :class:`UserRelationshipUpdateEvent` for the current user and unblocked user.

        .. note::
            This is not supposed to be used by bot accounts.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`NoEffect`
            You tried to block yourself or someone that you didn't had blocked.
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                               | Populated attributes                                                |
            +-------------------+------------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database.       | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------------+---------------------------------------------------------------------+
            | ``InternalError`` | Somehow something went wrong during unblocking user. |                                                                     |
            +-------------------+------------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`User`
            The unblocked user.
        """
        return await self.state.http.unblock_user(self.id, http_overrides=http_overrides)


@define(slots=True)
class PartialUser(BaseUser):
    """Represents a partial user on Stoat.

    This inherits from :class:`BaseUser`.
    """

    name: UndefinedOr[str] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`str`]: The new user's name."""

    discriminator: UndefinedOr[str] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`str`]: The new user's discriminator."""

    display_name: UndefinedOr[typing.Optional[str]] = field(repr=True, kw_only=True)
    """UndefinedOr[Optional[:class:`str`]]: The new user's display name."""

    internal_avatar: UndefinedOr[typing.Optional[StatelessAsset]] = field(repr=True, kw_only=True)
    """UndefinedOr[Optional[:class:`StatelessAsset`]]: The new user's stateless avatar."""

    raw_badges: UndefinedOr[int] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`int`]: The new user's badges raw value."""

    status: UndefinedOr[UserStatusEdit] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`UserStatusEdit`]: The new user's status."""

    # internal_profile: UndefinedOr[PartialUserProfile] = field(repr=True, kw_only=True)
    # """The new user's profile page."""

    raw_flags: UndefinedOr[int] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`int`]: The user's flags raw value."""

    bot: UndefinedOr[BotUserMetadata] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`BotUserMetadata`]: The information about the bot."""

    online: UndefinedOr[bool] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`bool`]: Whether the user came online."""

    @property
    def avatar(self) -> UndefinedOr[typing.Optional[Asset]]:
        """UndefinedOr[Optional[:class:`Asset`]]: The new user's avatar."""
        if self.internal_avatar in (None, UNDEFINED):
            return self.internal_avatar  # pyright: ignore[reportReturnType]
        return self.internal_avatar.attach_state(self.state, 'avatars')

    @property
    def badges(self) -> UndefinedOr[UserBadges]:
        """UndefinedOr[:class:`UserBadges`]: The new user's badges."""
        if self.raw_badges is UNDEFINED:
            return self.raw_badges
        ret = _new_user_badges(UserBadges)
        ret.value = self.raw_badges
        return ret

    @property
    def flags(self) -> UndefinedOr[UserFlags]:
        """UndefinedOr[:class:`UserFlags`]: The user's flags."""
        if self.raw_flags is UNDEFINED:
            return self.raw_flags
        ret = _new_user_flags(UserFlags)
        ret.value = self.raw_flags
        return ret


@define(slots=True)
class DisplayUser(BaseUser):
    """Represents an user on Stoat that can be easily displayed in UI.

    This inherits from :class:`BaseUser`.
    """

    name: str = field(repr=True, kw_only=True)
    """:class:`str`: The username of the user."""

    discriminator: str = field(repr=True, kw_only=True)
    """:class:`str`: The discriminator of the user."""

    internal_avatar: typing.Optional[StatelessAsset] = field(repr=True, kw_only=True)
    """Optional[:class:`StatelessAsset`]: The stateless avatar of the user."""

    def __str__(self) -> str:
        return self.name

    @property
    def avatar(self) -> typing.Optional[Asset]:
        """Optional[:class:`Asset`]: The avatar of the user."""
        return self.internal_avatar and self.internal_avatar.attach_state(self.state, 'avatars')

    @property
    def tag(self) -> str:
        """:class:`str`: The tag of the user.

        Assuming that :attr:`User.name` is ``'kotlin.Unit'`` and :attr:`User.discriminator` is ``'3510'``,
        example output would be ``'kotlin.Unit#3510'``.
        """
        return f'{self.name}#{self.discriminator}'

    async def send_friend_request(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> User:
        """|coro|

        Sends a friend request to this user.

        Fires :class:`UserRelationshipUpdateEvent` for the current user and user you sent friend request to.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------------------+-------------------------------------------------------------------------------------------+
            | Value                            | Reason                                                                                    |
            +----------------------------------+-------------------------------------------------------------------------------------------+
            | ``InvalidProperty``              | You did not provide a discriminator.                                                      |
            +----------------------------------+-------------------------------------------------------------------------------------------+
            | ``IsBot``                        | Either the current user or user you tried to accept friend request from are bot accounts. |
            +----------------------------------+-------------------------------------------------------------------------------------------+
            | ``TooManyPendingFriendRequests`` | You sent too many outgoing friend requests.                                               |
            +----------------------------------+-------------------------------------------------------------------------------------------+
        :class:`NoEffect`
            You tried to accept friend request from yourself.
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +------------------+----------------------------------------------------------------+
            | Value            | Reason                                                         |
            +------------------+----------------------------------------------------------------+
            | ``BlockedOther`` | The user you tried to send friend request to have blocked you. |
            +------------------+----------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`Conflict`
            Possible values for :attr:`~HTTPException.type`:

            +------------------------+-----------------------------------------------------------------------+
            | Value                  | Reason                                                                |
            +------------------------+-----------------------------------------------------------------------+
            | ``AlreadyFriends``     | You're already friends with user you tried to send friend request to. |
            +------------------------+-----------------------------------------------------------------------+
            | ``AlreadySentRequest`` | You already sent friend request to this user.                         |
            +------------------------+-----------------------------------------------------------------------+
            | ``Blocked``            | You have blocked the user you tried to send friend request to.        |
            +------------------------+-----------------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`User`
            The user you sent friend request to.
        """

        return await self.state.http.send_friend_request(self.name, self.discriminator, http_overrides=http_overrides)


@define(slots=True)
class BotUserMetadata:
    """Represents a bot-specific metadata for an user."""

    owner_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's ID who owns bot."""

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, BotUserMetadata) and self.owner_id == other.owner_id

    def to_dict(self) -> raw.BotInformation:
        """:class:`dict`: Convert bot user metadata to raw data."""
        return {
            'owner': self.owner_id,
        }


def calculate_user_permissions(
    user_id: str,
    user_relationship: RelationshipStatus,
    user_bot: typing.Optional[BotUserMetadata],
    /,
    *,
    perspective_id: str,
    perspective_bot: typing.Optional[BotUserMetadata],
    perspective_privileged: bool,
) -> UserPermissions:
    """Calculates the permissions between two users.

    Parameters
    ----------
    user_id: :class:`str`
        The target ID.
    user_relationship: :class:`RelationshipStatus`
        The relationship between us and target user (:attr:`.User.relationship`).
    user_bot: Optional[:class:`BotUserMetadata`]
        The bot information about the user (:attr:`.User.bot`), if applicable.
    perspective_id: :class:`str`
        The ID of the current user.
    perspective_bot: Optional[:class:`BotUserMetadata`]
        The bot information about the current user (:attr:`.User.bot`), if applicable.
    perspective_privileged: :class:`bool`
        Whether the current user is privileged (:attr:`.User.privileged`).

    Returns
    -------
    :class:`UserPermissions`
        The calculated permissions.
    """
    if perspective_privileged or user_id == perspective_id or user_relationship is RelationshipStatus.friend:
        return UserPermissions.all()

    if user_relationship in (
        RelationshipStatus.blocked,
        RelationshipStatus.blocked_other,
    ):
        return UserPermissions(access=True)

    return UserPermissions(
        access=user_relationship in (RelationshipStatus.incoming, RelationshipStatus.outgoing),
        send_messages=bool(user_bot or perspective_bot),
    )


@define(slots=True)
class User(DisplayUser):
    """Represents an user on Stoat.

    This inherits from :class:`DisplayUser`.
    """

    display_name: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The user's display name."""

    raw_badges: int = field(repr=True, kw_only=True)
    """:class:`int`: The user's badges raw value."""

    status: typing.Optional[UserStatus] = field(repr=True, kw_only=True)
    """Optional[:class:`UserStatus`]: The current user's status."""

    raw_flags: int = field(repr=True, kw_only=True)
    """:class:`int`: The user's flags raw value."""

    privileged: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the user is privileged."""

    bot: typing.Optional[BotUserMetadata] = field(repr=True, kw_only=True)
    """Optional[:class:`BotUserMetadata`]: The information about the bot."""

    relationship: RelationshipStatus = field(repr=True, kw_only=True)
    """:class:`RelationshipStatus`: The current user's relationship with this user."""

    online: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the user is currently online."""

    def get_bot_owner(self) -> tuple[typing.Optional[User], str]:
        """Returns the user who created this bot user.

        Returns
        -------
        Tuple[Optional[:class:`User`], :class:`str`]
            The bot owner and their ID (may be empty if user is not a bot).
        """
        bot = self.bot
        if bot is None:
            return (None, '')

        state = self.state
        cache = state.cache

        if cache is None:
            return (None, bot.owner_id)

        ctx = (
            UserThroughUserBotOwnerCacheContext(
                type=CacheContextType.user_through_user_bot_owner,
                user=self,
            )
            if state.provide_cache_context('User.bot_owner')
            else _USER_THROUGH_USER_BOT_OWNER
        )

        return (cache.get_user(bot.owner_id, ctx), bot.owner_id)

    def locally_update(self, data: PartialUser, /) -> None:
        """Locally updates user with provided data.

        .. warning::
            This is called by library internally to keep cache up to date.
        """
        if data.name is not UNDEFINED:
            self.name = data.name
        if data.discriminator is not UNDEFINED:
            self.discriminator = data.discriminator
        if data.display_name is not UNDEFINED:
            self.display_name = data.display_name
        if data.internal_avatar is not UNDEFINED:
            self.internal_avatar = data.internal_avatar
        if data.raw_badges is not UNDEFINED:
            self.raw_badges = data.raw_badges
        if data.status is not UNDEFINED:
            status = data.status
            if status.text is not UNDEFINED and status.presence is not UNDEFINED:
                self.status = UserStatus(
                    text=status.text,
                    presence=status.presence,
                )
            elif self.status is not None:
                self.status.locally_update(status)
        if data.raw_flags is not UNDEFINED:
            self.raw_flags = data.raw_flags
        if data.bot is not UNDEFINED:
            self.bot = data.bot
        if data.online is not UNDEFINED:
            self.online = data.online

    @property
    def badges(self) -> UserBadges:
        """:class:`UserBadges`: The user's badges."""
        ret = _new_user_badges(UserBadges)
        ret.value = self.raw_badges
        return ret

    @property
    def bot_owner(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: Returns the user who created this bot user."""

        bot_owner, bot_owner_id = self.get_bot_owner()
        if bot_owner is None and len(bot_owner_id):
            raise NoData(
                what=bot_owner_id,
                type='User.bot_owner',
            )
        return bot_owner

    @property
    def flags(self) -> UserFlags:
        """:class:`UserFlags`: The user's badges."""
        ret = _new_user_flags(UserFlags)
        ret.value = self.raw_flags
        return ret

    # flags
    def is_suspended(self) -> bool:
        """:class:`bool`: Whether this user has been suspended from the platform."""
        return self.flags.suspended

    def is_deleted(self) -> bool:
        """:class:`bool`: Whether this user is deleted his account."""
        return self.flags.deleted

    def is_banned(self) -> bool:
        """:class:`bool`: Whether this user is banned off the platform."""
        return self.flags.banned

    def is_spammer(self) -> bool:
        """:class:`bool`: Whether this user was marked as spam and removed from platform."""
        return self.flags.spam

    # badges
    def is_developer(self) -> bool:
        """:class:`bool`: Whether this user is Stoat developer."""
        return self.badges.developer

    def is_translator(self) -> bool:
        """:class:`bool`: Whether this user helped translate Stoat."""
        return self.badges.translator

    def is_supporter(self) -> bool:
        """:class:`bool`: Whether this user monetarily supported Stoat."""
        return self.badges.supporter

    def is_responsible_disclosure(self) -> bool:
        """:class:`bool`: Whether this user responsibly disclosed a security issue."""
        return self.badges.responsible_disclosure

    def is_founder(self) -> bool:
        """:class:`bool`: Whether this user is Stoat founder."""
        return self.badges.founder

    def is_platform_moderator(self) -> bool:
        """:class:`bool`: Whether this user is platform moderator."""
        return self.badges.platform_moderation

    def is_active_supporter(self) -> bool:
        """:class:`bool`: Whether this user is active monetary supporter."""
        return self.badges.active_supporter

    def is_paw(self) -> bool:
        """:class:`bool`: Whether this user likes fox/raccoon (🦊🦝)."""
        return self.badges.paw

    def is_early_adopter(self) -> bool:
        """:class:`bool`: Whether this user have joined Stoat as one of the first 1000 users in 2021."""
        return self.badges.early_adopter

    def is_relevant_joke_1(self) -> bool:
        """:class:`bool`: Whether this user have given funny joke (Called "sus", displayed as Amogus in Revite)."""
        return self.badges.reserved_relevant_joke_badge_1

    def is_relevant_joke_2(self) -> bool:
        """:class:`bool`: Whether this user have given other funny joke (Called as "It's Morbin Time" in Revite)."""
        return self.badges.reserved_relevant_joke_badge_2

    def to_dict(self) -> raw.User:
        """:class:`dict`: Convert user to raw data."""
        payload: dict[str, typing.Any] = {
            '_id': self.id,
            'username': self.name,
            'discriminator': self.discriminator,
        }
        if self.display_name is not None:
            payload['display_name'] = self.display_name
        if self.internal_avatar is not None:
            payload['avatar'] = self.internal_avatar.to_dict('avatars')
        if self.raw_badges != 0:
            payload['badges'] = self.raw_badges
        if self.status is not None:
            payload['status'] = self.status.to_dict()
        if self.raw_flags != 0:
            payload['flags'] = self.raw_flags
        if self.privileged:
            payload['privileged'] = self.privileged
        if self.bot is not None:
            payload['bot'] = self.bot.to_dict()
        payload['relationship'] = self.relationship.value
        payload['online'] = self.online
        return payload  # type: ignore


@define(slots=True)
class OwnUser(User):
    """Represents a current user on Stoat.

    This inherits from :class:`User`.
    """

    relations: dict[str, Relationship] = field(repr=True, kw_only=True)
    """Dict[:class:`str`, :class:`Relationship`]: The dictionary of relationships with other users."""

    async def edit(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        display_name: UndefinedOr[typing.Optional[str]] = UNDEFINED,
        avatar: UndefinedOr[typing.Optional[ResolvableResource]] = UNDEFINED,
        status: UndefinedOr[UserStatusEdit] = UNDEFINED,
        profile: UndefinedOr[UserProfileEdit] = UNDEFINED,
        badges: UndefinedOr[UserBadges] = UNDEFINED,
        flags: UndefinedOr[UserFlags] = UNDEFINED,
    ) -> User:
        """|coro|

        Edits the current user.

        Fires :class:`UserUpdateEvent` for all users who `are subscribed <server_subscriptions>`_ to you.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        display_name: UndefinedOr[Optional[:class:`str`]]
            The new display name. Must be between 2 and 32 characters and not contain zero width space, newline or carriage return characters.
        avatar: UndefinedOr[Optional[:class:`ResolvableResource`]]
            The new avatar. Could be ``None`` to remove avatar.
        status: UndefinedOr[:class:`UserStatusEdit`]
            The new user status.
        profile: UndefinedOr[:class:`UserProfileEdit`]
            The new user profile data. This is applied as a partial.
        badges: UndefinedOr[:class:`UserBadges`]
            The new user badges. You must be privileged user to provide this.
        flags: UndefinedOr[:class:`UserFlags`]
            The new user flags. You must be privileged user to provide this.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+--------------------------+
            | Value                | Reason                   |
            +----------------------+--------------------------+
            | ``FailedValidation`` | The payload was invalid. |
            +----------------------+--------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+-------------------------------------------------------------+
            | Value             | Reason                                                      |
            +-------------------+-------------------------------------------------------------+
            | ``NotPrivileged`` | You tried to edit fields that require you to be privileged. |
            +-------------------+-------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`OwnUser`
            The newly updated authenticated user.
        """

        return await self.state.http.edit_my_user(
            http_overrides=http_overrides,
            display_name=display_name,
            avatar=avatar,
            status=status,
            profile=profile,
            badges=badges,
            flags=flags,
        )

    def to_dict(self) -> raw.User:
        """:class:`dict`: Convert user to raw data."""
        payload: dict[str, typing.Any] = {
            '_id': self.id,
            'username': self.name,
            'discriminator': self.discriminator,
        }
        if self.display_name is not None:
            payload['display_name'] = self.display_name
        if self.internal_avatar is not None:
            payload['avatar'] = self.internal_avatar.to_dict('avatars')
        if len(self.relations):
            payload['relations'] = [relationship.to_dict() for relationship in self.relations.values()]
        if self.raw_badges != 0:
            payload['badges'] = self.raw_badges
        if self.status is not None:
            payload['status'] = self.status.to_dict()
        if self.raw_flags != 0:
            payload['flags'] = self.raw_flags
        if self.privileged:
            payload['privileged'] = self.privileged
        if self.bot is not None:
            payload['bot'] = self.bot.to_dict()
        payload['relationship'] = self.relationship.value
        payload['online'] = self.online
        return payload  # type: ignore


@define(slots=True)
class UserVoiceState:
    """Represents a voice state for the user."""

    user_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's ID this voice state belongs to."""

    joined_at: datetime = field(repr=True, kw_only=True)
    """:class:`~datetime.datetime`: When the voice state was created.
    
    .. versionadded:: 1.2
    """

    can_publish: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the user can send voice data."""

    can_receive: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the user can receive voice data."""

    screensharing: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the user is sharing their screen."""

    camera: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the user is sharing their camera."""

    def locally_update(self, data: PartialUserVoiceState, /) -> None:
        """Locally updates voice state with provided data.

        .. warning::
            This is called by library internally to keep cache up to date.
        """

        if data.can_publish is not UNDEFINED:
            self.can_publish = data.can_publish

        if data.can_receive is not UNDEFINED:
            self.can_receive = data.can_receive

        if data.screensharing is not UNDEFINED:
            self.screensharing = data.screensharing

        if data.camera is not UNDEFINED:
            self.camera = data.camera


@define(slots=True)
class PartialUserVoiceState:
    """Represents a partial voice state for the user.

    Unmodified fields will have :data:`.UNDEFINED` as their value.
    """

    user_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's ID this voice state belongs to."""

    can_publish: UndefinedOr[bool] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`bool`]: Whether the user can send voice data."""

    can_receive: UndefinedOr[bool] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`bool`]: Whether the user can receive voice data."""

    screensharing: UndefinedOr[bool] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`bool`]: Whether the user is sharing their screen."""

    camera: UndefinedOr[bool] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`bool`]: Whether the user is sharing their camera."""


__all__ = (
    'UserStatus',
    'UserStatusEdit',
    'StatelessUserProfile',
    'UserProfile',
    'PartialUserProfile',
    'UserProfileEdit',
    'Relationship',
    'Mutuals',
    'BaseUser',
    'PartialUser',
    'DisplayUser',
    'BotUserMetadata',
    'calculate_user_permissions',
    'User',
    'OwnUser',
    'UserVoiceState',
    'PartialUserVoiceState',
)
