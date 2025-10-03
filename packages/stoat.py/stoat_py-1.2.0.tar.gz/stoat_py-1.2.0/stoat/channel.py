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

from .abc import Messageable, Connectable
from .base import Base
from .cache import (
    CacheContextType,
    UserThroughDMChannelInitiatorCacheContext,
    MessageThroughDMChannelLastMessageCacheContext,
    ReadStateThroughDMChannelReadStateCacheContext,
    UserThroughDMChannelRecipientCacheContext,
    UserThroughDMChannelRecipientsCacheContext,
    MessageThroughGroupChannelLastMessageCacheContext,
    ReadStateThroughGroupChannelReadStateCacheContext,
    UserThroughGroupChannelOwnerCacheContext,
    UserThroughGroupChannelRecipientsCacheContext,
    ServerThroughServerChannelCategoryCacheContext,
    MemberThroughServerChannelMeCacheContext,
    ServerThroughServerChannelServerCacheContext,
    MessageThroughTextChannelLastMessageCacheContext,
    ReadStateThroughTextChannelReadStateCacheContext,
    ChannelVoiceStateContainerThroughTextChannelVoiceStatesCacheContext,
    ChannelVoiceStateContainerThroughVoiceChannelVoiceStatesCacheContext,
    _USER_THROUGH_DM_CHANNEL_INITIATOR,
    _MESSAGE_THROUGH_DM_CHANNEL_LAST_MESSAGE,
    _READ_STATE_THROUGH_DM_CHANNEL_READ_STATE,
    _USER_THROUGH_DM_CHANNEL_RECIPIENT,
    _USER_THROUGH_DM_CHANNEL_RECIPIENTS,
    _MESSAGE_THROUGH_GROUP_CHANNEL_LAST_MESSAGE,
    _USER_THROUGH_GROUP_CHANNEL_OWNER,
    _READ_STATE_THROUGH_GROUP_CHANNEL_READ_STATE,
    _USER_THROUGH_GROUP_CHANNEL_RECIPIENTS,
    _SERVER_THROUGH_SERVER_CHANNEL_CATEGORY,
    _MEMBER_THROUGH_SERVER_CHANNEL_ME,
    _SERVER_THROUGH_SERVER_CHANNEL_SERVER,
    _MESSAGE_THROUGH_TEXT_CHANNEL_LAST_MESSAGE,
    _READ_STATE_THROUGH_TEXT_CHANNEL_READ_STATE,
    _CHANNEL_VOICE_STATE_CONTAINER_THROUGH_TEXT_CHANNEL_VOICE_STATES,
    _CHANNEL_VOICE_STATE_CONTAINER_THROUGH_VOICE_CHANNEL_VOICE_STATES,
)
from .core import (
    UNDEFINED,
    UndefinedOr,
    ULIDOr,
    resolve_id,
)
from .enums import ChannelType
from .errors import NoData
from .flags import (
    Permissions,
    UserPermissions,
    ALLOW_PERMISSIONS_IN_TIMEOUT,
    VIEW_ONLY_PERMISSIONS,
    DEFAULT_SAVED_MESSAGES_PERMISSIONS,
    DEFAULT_DM_PERMISSIONS,
)
from .read_state import ReadState

if typing.TYPE_CHECKING:
    from . import raw
    from .bot import BaseBot
    from .cdn import StatelessAsset, Asset, ResolvableResource
    from .http import HTTPOverrideOptions
    from .invite import Invite
    from .message import BaseMessage, Message
    from .permissions import PermissionOverride
    from .server import Category, BaseRole, Role, Server, Member
    from .state import State
    from .user import BaseUser, User, UserVoiceState
    from .webhook import Webhook

_new_permissions = Permissions.__new__


@define(slots=True)
class BaseChannel(Base):
    """Represents channel on Stoat.

    This inherits from :class:`Base`.
    """

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, BaseChannel) and self.id == other.id

    def message(self, message: ULIDOr[BaseMessage], /) -> BaseMessage:
        """:class:`BaseMessage`: Returns a partial message with specified ID."""
        from .message import BaseMessage

        return BaseMessage(state=self.state, id=resolve_id(message), channel_id=self.id)

    @property
    def mention(self) -> str:
        """:class:`str`: Returns the channel's mention."""

        return f'<#{self.id}>'

    async def close(
        self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None, silent: typing.Optional[bool] = None
    ) -> None:
        """|coro|

        Deletes a server channel, leaves a group or closes a group.

        You must have :attr:`~Permissions.view_channel` to do this. If target channel is server channel, :attr:`~Permissions.manage_channels` is also required.

        For DMs, fires :class:`ChannelUpdateEvent` for the current user and DM recipient.
        For groups, if the current user is group owner, fires :class:`PrivateChannelDeleteEvent` for all group recipients (including group owner),
        otherwise :class:`PrivateChannelDeleteEvent` is fired for the current user,
        and :class:`GroupRecipientRemoveEvent` is fired for rest of group recipients.
        For server channels, :class:`ServerChannelDeleteEvent` is fired for all users who could see target channel, and :class:`ServerUpdateEvent` for all server members.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        silent: Optional[:class:`bool`]
            Whether to not send message when leaving.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+---------------------------------------------------------------------------+
            | Value                 | Reason                                                                    |
            +-----------------------+---------------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to view and/or delete the channel. |
            +-----------------------+---------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The channel was not found. |
            +--------------+----------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.state.http.close_channel(self.id, http_overrides=http_overrides, silent=silent)

    async def edit(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        name: UndefinedOr[str] = UNDEFINED,
        description: UndefinedOr[typing.Optional[str]] = UNDEFINED,
        owner: UndefinedOr[ULIDOr[BaseUser]] = UNDEFINED,
        icon: UndefinedOr[typing.Optional[ResolvableResource]] = UNDEFINED,
        nsfw: UndefinedOr[bool] = UNDEFINED,
        archived: UndefinedOr[bool] = UNDEFINED,
        voice: UndefinedOr[ChannelVoiceMetadata] = UNDEFINED,
        default_permissions: UndefinedOr[None] = UNDEFINED,
    ) -> Channel:
        """|coro|

        Edits the channel.

        You must have :attr:`~Permissions.manage_channels` to do this.

        Fires :class:`ChannelUpdateEvent` for all users who still can see target channel,
        optionally :class:`ServerChannelCreateEvent` for all users who now can see target server channel, and
        optionally :class:`ChannelDeleteEvent` for users who no longer can see target server channel.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        name: UndefinedOr[:class:`str`]
            The new channel name. Only applicable when target channel is :class:`GroupChannel`, or :class:`ServerChannel`.
        description: UndefinedOr[Optional[:class:`str`]]
            The new channel description. Only applicable when target channel is :class:`GroupChannel`, or :class:`ServerChannel`.
        owner: UndefinedOr[ULIDOr[:class:`BaseUser`]]
            The new channel owner. Only applicable when target channel is :class:`GroupChannel`.
        icon: UndefinedOr[Optional[:class:`ResolvableResource`]]
            The new channel icon. Only applicable when target channel is :class:`GroupChannel`, or :class:`ServerChannel`.
        nsfw: UndefinedOr[:class:`bool`]
            To mark the channel as NSFW or not. Only applicable when target channel is :class:`GroupChannel`, or :class:`ServerChannel`.
        archived: UndefinedOr[:class:`bool`]
            To mark the channel as archived or not.
        voice: UndefinedOr[:class:`ChannelVoiceMetadata`]
            The new voice-specific metadata for this channel.

            .. versionadded:: 1.2
        default_permissions: UndefinedOr[None]
            To remove default permissions or not. Only applicable when target channel is :class:`GroupChannel`, or :class:`ServerChannel`.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+------------------------------------------------------+
            | Value                | Reason                                               |
            +----------------------+------------------------------------------------------+
            | ``FailedValidation`` | The payload was invalid.                             |
            +----------------------+------------------------------------------------------+
            | ``InvalidOperation`` | The target channel was not group/text/voice channel. |
            +----------------------+------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+-------------------------------------------------------------+
            | Value                 | Reason                                                      |
            +-----------------------+-------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to edit the channel. |
            +-----------------------+-------------------------------------------------------------+
            | ``NotOwner``          | You do not own the group.                                   |
            +-----------------------+-------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +----------------+---------------------------------+
            | Value          | Reason                          |
            +----------------+---------------------------------+
            | ``NotFound``   | The channel was not found.      |
            +----------------+---------------------------------+
            | ``NotInGroup`` | The new owner was not in group. |
            +----------------+---------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`Channel`
            The newly updated channel.
        """
        return await self.state.http.edit_channel(
            self.id,
            http_overrides=http_overrides,
            name=name,
            description=description,
            owner=owner,
            icon=icon,
            nsfw=nsfw,
            archived=archived,
            voice=voice,
            default_permissions=default_permissions,
        )

    def permissions_for(self, _target: typing.Union[User, Member], /) -> Permissions:
        """Calculate permissions for given user.

        By default, this returns no permissions.

        Parameters
        ----------
        target: Union[:class:`User`, :class:`Member`]
            The member or user to calculate permissions for.

        Returns
        -------
        :class:`Permissions`
            The calculated permissions.
        """
        return Permissions.none()


@define(slots=True)
class PartialChannel(BaseChannel):
    """Represents a partial channel on Stoat.

    This inherits from :class:`BaseChannel`.
    """

    name: UndefinedOr[str] = field(repr=True, kw_only=True, eq=True)
    """UndefinedOr[:class:`str`]: The new channel name, if applicable. Only for :class:`GroupChannel` and :class:`BaseServerChannel`'s."""

    owner_id: UndefinedOr[str] = field(repr=True, kw_only=True, eq=True)
    """UndefinedOr[:class:`str`]: The ID of new group owner, if applicable. Only for :class:`GroupChannel`."""

    description: UndefinedOr[typing.Optional[str]] = field(repr=True, kw_only=True, eq=True)
    """UndefinedOr[Optional[:class:`str`]]: The new channel's description, if applicable. Only for :class:`GroupChannel` and :class:`BaseServerChannel`'s."""

    internal_icon: UndefinedOr[typing.Optional[StatelessAsset]] = field(repr=True, kw_only=True, eq=True)
    """UndefinedOr[Optional[:class:`StatelessAsset`]]: The new channel's stateless icon, if applicable. Only for :class:`GroupChannel` and :class:`BaseServerChannel`'s."""

    nsfw: UndefinedOr[bool] = field(repr=True, kw_only=True, eq=True)
    """UndefinedOr[:class:`bool`]: Whether the channel have been marked as NSFW, if applicable. Only for :class:`GroupChannel` and :class:`BaseServerChannel`'s."""

    active: UndefinedOr[bool] = field(repr=True, kw_only=True, eq=True)
    """UndefinedOr[:class:`bool`]: Whether the DM channel is active now, if applicable. Only for :class:`DMChannel`'s."""

    raw_permissions: UndefinedOr[int] = field(repr=True, kw_only=True, eq=True)
    """UndefinedOr[:class:`int`]: The new channel's permissions raw value, if applicable. Only for :class:`GroupChannel`'s."""

    role_permissions: UndefinedOr[dict[str, PermissionOverride]] = field(repr=True, kw_only=True, eq=True)
    """UndefinedOr[Dict[:class:`str`, :class:`PermissionOverride`]]: The new channel's permission overrides for roles, if applicable. Only for :class:`BaseServerChannel`'s."""

    default_permissions: UndefinedOr[typing.Optional[PermissionOverride]] = field(repr=True, kw_only=True, eq=True)
    """UndefinedOr[Optional[:class:`PermissionOverride`]]: The new channel's permission overrides for everyone, if applicable. Only for :class:`BaseServerChannel`'s."""

    last_message_id: UndefinedOr[str] = field(repr=True, kw_only=True, eq=True)
    """UndefinedOr[:class:`str`]: The last message ID sent in the channel."""

    category_id: UndefinedOr[str] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`str`]: The new category ID the channel is in.
    
    .. versionadded:: 1.2
    """

    voice: UndefinedOr[ChannelVoiceMetadata] = field(repr=True, kw_only=True, eq=True)
    """UndefinedOr[:class:`ChannelVoiceMetadata`]: The new voice-specific metadata for this channel.
    
    .. versionadded:: 1.2
    """

    @property
    def icon(self) -> UndefinedOr[typing.Optional[Asset]]:
        r"""UndefinedOr[Optional[:class:`Asset`]]: The new channel's icon, if applicable. Only for :class:`GroupChannel` and :class:`BaseServerChannel`\'s."""
        if self.internal_icon in (None, UNDEFINED):
            return self.internal_icon  # pyright: ignore[reportReturnType]
        return self.internal_icon.attach_state(self.state, 'icons')

    @property
    def permissions(self) -> UndefinedOr[Permissions]:
        r"""UndefinedOr[:class:`Permissions`]: The new channel's permissions, if applicable. Only for :class:`GroupChannel`\'s."""
        if self.raw_permissions is UNDEFINED:
            return self.raw_permissions
        ret = _new_permissions(Permissions)
        ret.value = self.raw_permissions
        return ret


def calculate_saved_messages_channel_permissions(perspective_id: str, user_id: str, /) -> Permissions:
    """Calculates the permissions in :class:`SavedMessagesChannel` scope.

    Parameters
    ----------
    perspective_id: :class:`str`
        The ID of perspective user.
    user_id: :class:`str`
        The ID of channel owner (:attr:`.SavedMessagesChannel.owner_id`).

    Returns
    -------
    :class:`Permissions`
        The calculated permissions.
    """
    if perspective_id == user_id:
        return DEFAULT_SAVED_MESSAGES_PERMISSIONS
    return Permissions.none()


def calculate_dm_channel_permissions(
    permissions: UserPermissions,
    /,
) -> Permissions:
    """Calculates the permissions in :class:`DMChannel` scope.

    Parameters
    ----------
    permissions: :class:`UserPermissions`
        The user permissions.

    Returns
    -------
    :class:`Permissions`
        The calculated permissions.
    """
    if permissions.send_messages:
        return DEFAULT_DM_PERMISSIONS
    return VIEW_ONLY_PERMISSIONS


def calculate_group_channel_permissions(
    perspective_id: str,
    /,
    *,
    group_owner_id: str,
    group_permissions: typing.Optional[Permissions],
    group_recipients: list[str],
) -> Permissions:
    """Calculates the permissions in :class:`GroupChannel` scope.

    Parameters
    ----------
    perspective_id: :class:`str`
        The ID of perspective user.
    group_owner_id: :class:`str`
        The ID of group owner (:attr:`.GroupChannel.owner_id`).
    group_permissions: Optional[:class:`Permissions`]
        The default group permissions (:attr:`.GroupChannel.permissions`).
    group_recipients: List[:class:`str`]
        The IDs of group recipients (:attr:`.GroupChannel.recipient_ids`).

    Returns
    -------
    :class:`Permissions`
        The calculated permissions.
    """
    if perspective_id == group_owner_id:
        return Permissions.all()
    elif perspective_id in group_recipients:
        if group_permissions is None:
            group_permissions = DEFAULT_DM_PERMISSIONS
        return VIEW_ONLY_PERMISSIONS | group_permissions
    return Permissions.none()


def calculate_server_channel_permissions(
    initial_permissions: Permissions,
    roles: list[Role],
    *,
    default_permissions: typing.Optional[PermissionOverride],
    role_permissions: dict[str, PermissionOverride],
) -> Permissions:
    """Calculates the permissions in :class:`BaseServerChannel` scope.

    Parameters
    ----------
    initial_permissions: :class:`str`
        The initial permissions to use. Should be ``server.permissions_for(member)`` for members
        and :attr:`Server.default_permissions` for users.
    roles: List[:class:`Role`]
        The member's roles. Should be empty list if calculating for :class:`User`.
    default_permissions: :class:`str`
        The default channel permissions (:attr:`.BaseServerChannel.default_permissions`).
    role_permissions: Dict[:class:`str`, :class:`Permissions`]
        The permissions overrides for roles in the channel (:attr:`.BaseServerChannel.role_permissions`).

    Returns
    -------
    :class:`Permissions`
        The calculated permissions.
    """
    result = initial_permissions.value

    if default_permissions:
        result |= default_permissions.allow.value
        result &= ~default_permissions.deny.value

    for role in roles:
        override = role_permissions.get(role.id)
        if override:
            result |= override.allow.value
            result &= ~override.deny.value

    return Permissions(result)


@define(slots=True)
class SavedMessagesChannel(BaseChannel, Messageable):
    """Represents a personal "Saved Notes" channel which allows users to save messages.

    This inherits from :class:`BaseChannel` and :class:`~stoat.abc.Messageable`.
    """

    user_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The ID of the user this channel belongs to."""

    def get_channel_id(self) -> str:
        return self.id

    def get_me(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The own user."""
        return self.state.me

    def locally_update(self, data: PartialChannel, /) -> None:
        """Locally updates channel with provided data.

        .. warning::
            This is called by library internally to keep cache up to date.

        Parameters
        ----------
        data: :class:`PartialChannel`
            The data to update channel with.
        """
        # PartialChannel has no fields that are related to SavedMessages yet
        pass

    @property
    def me(self) -> User:
        """:class:`User`: The own user."""
        me = self.get_me()
        if me is None:
            raise NoData(what='', type='GroupChannel.me')
        return me

    @property
    def server(self) -> None:
        """Optional[:class:`Server`]: The server this channel belongs to."""
        return None

    @property
    def type(self) -> typing.Literal[ChannelType.saved_messages]:
        """Literal[:attr:`ChannelType.saved_messages`]: The channel's type."""
        return ChannelType.saved_messages

    def permissions_for(self, target: typing.Union[User, Member], /) -> Permissions:
        """Calculate permissions for given member.

        Parameters
        ----------
        target: Union[:class:`User`, :class:`Member`]
            The user to calculate permissions for.

        Returns
        -------
        :class:`Permissions`
            The calculated permissions.
        """

        return calculate_saved_messages_channel_permissions(target.id, self.user_id)

    def to_dict(self) -> raw.SavedMessagesChannel:
        """:class:`dict`: Convert channel to raw data."""

        payload: raw.SavedMessagesChannel = {
            'channel_type': 'SavedMessages',
            '_id': self.id,
            'user': self.user_id,
        }
        return payload


@define(slots=True)
class DMChannel(BaseChannel, Connectable, Messageable):
    """Represents a private channel between two users.

    This inherits from :class:`BaseChannel`, :class:`~stoat.abc.Connectable` and :class:`~stoat.abc.Messageable`.
    """

    active: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the DM channel is currently open on both sides."""

    recipient_ids: tuple[str, str] = field(repr=True, kw_only=True)
    """Tuple[:class:`str`, :class:`str`]: The tuple of user IDs participating in DM."""

    last_message_id: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The last message ID sent in the channel."""

    def get_channel_id(self) -> str:
        return self.id

    def get_initiator(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that initiated this PM."""
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughDMChannelInitiatorCacheContext(
                type=CacheContextType.user_through_dm_channel_initiator,
                channel=self,
            )
            if state.provide_cache_context('DMChannel.initiator')
            else _USER_THROUGH_DM_CHANNEL_INITIATOR
        )

        return cache.get_user(self.initiator_id, ctx)

    def get_last_message(self) -> typing.Optional[Message]:
        """Optional[:class:`Message`]: The last message sent in the channel."""
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        last_message_id = self.last_message_id

        if last_message_id is None:
            return None

        ctx = (
            MessageThroughDMChannelLastMessageCacheContext(
                type=CacheContextType.message_through_dm_channel_last_message,
                channel=self,
            )
            if state.provide_cache_context('DMChannel.last_message')
            else _MESSAGE_THROUGH_DM_CHANNEL_LAST_MESSAGE
        )

        return cache.get_message(self.id, last_message_id, ctx)

    def get_me(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The own user."""
        return self.state.me

    @typing.overload
    def get_read_state(
        self,
        *,
        default_acked_message_id: typing.Optional[str] = None,
        create_if_not_exists: typing.Literal[True] = ...,
    ) -> ReadState: ...

    @typing.overload
    def get_read_state(
        self,
        *,
        default_acked_message_id: typing.Optional[str] = None,
        create_if_not_exists: typing.Literal[False] = ...,
    ) -> typing.Optional[ReadState]: ...

    def get_read_state(
        self,
        *,
        default_acked_message_id: typing.Optional[str] = None,
        create_if_not_exists: bool = True,
    ) -> typing.Optional[ReadState]:
        """Optional[:class:`ReadState`]: Returns the channel's read state.

        Parameters
        ----------
        default_acked_message_id: Optional[:class:`str`]
            The default acked message ID to use if read state is not found.
        create_if_not_exists: :class:`bool`
            Whether to create a read state and store it if existing was not found.
        """

        state = self.state
        cache = state.cache

        if cache is None:
            if create_if_not_exists:
                return ReadState(
                    state=state,
                    channel_id=self.id,
                    user_id=state.my_id,
                    last_acked_id=default_acked_message_id,
                    mentioned_in=[],
                )
            return None

        ctx = (
            ReadStateThroughDMChannelReadStateCacheContext(
                type=CacheContextType.read_state_through_dm_channel_read_state,
                channel=self,
            )
            if state.provide_cache_context('DMChannel.read_state')
            else _READ_STATE_THROUGH_DM_CHANNEL_READ_STATE
        )

        read_state = cache.get_read_state(self.id, ctx)
        if read_state is None and create_if_not_exists:
            read_state = ReadState(
                state=state,
                channel_id=self.id,
                user_id=state.my_id,
                last_acked_id=default_acked_message_id,
                mentioned_in=[],
            )
            cache.store_read_state(read_state, ctx)
        return read_state

    def get_recipient(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The recipient."""
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughDMChannelRecipientCacheContext(
                type=CacheContextType.user_through_dm_channel_recipient,
                channel=self,
            )
            if state.provide_cache_context('DMChannel.recipient')
            else _USER_THROUGH_DM_CHANNEL_RECIPIENT
        )

        return cache.get_user(self.initiator_id, ctx)

    def get_recipients(
        self,
    ) -> tuple[
        typing.Optional[User],
        typing.Optional[User],
    ]:
        """Tuple[Optional[:class:`User`], Optional[:class:`User`]]: The recipient."""
        state = self.state
        cache = state.cache

        if cache is None:
            return (None, None)

        ctx = (
            UserThroughDMChannelRecipientsCacheContext(
                type=CacheContextType.user_through_dm_channel_recipients,
                channel=self,
            )
            if state.provide_cache_context('DMChannel.recipients')
            else _USER_THROUGH_DM_CHANNEL_RECIPIENTS
        )

        a = cache.get_user(self.recipient_ids[0], ctx)
        b = cache.get_user(self.recipient_ids[1], ctx)

        return (a, b)

    @property
    def initiator_id(self) -> str:
        """:class:`str`: The user's ID that started this PM."""
        return self.recipient_ids[0]

    @property
    def last_message(self) -> typing.Optional[Message]:
        """Optional[:class:`Message`]: The last message sent in the channel."""

        message = self.get_last_message()
        if message is None:
            if self.last_message_id is None:
                return None
            raise NoData(what=self.last_message_id, type='DMChannel.last_message')
        return message

    @property
    def me(self) -> User:
        """:class:`User`: The own user."""
        me = self.get_me()
        if me is None:
            raise NoData(what='', type='GroupChannel.me')
        return me

    @property
    def read_state(self) -> ReadState:
        """:class:`ReadState`: Returns the channel's read state."""
        return self.get_read_state()

    @property
    def recipient(self) -> User:
        """:class:`User`: The recipient."""
        recipient = self.get_recipient()
        if recipient is None:
            raise NoData(what=self.recipient_id, type='DMChannel.recipient')
        return recipient

    @property
    def recipient_id(self) -> str:
        """:class:`str`: The recipient's ID."""
        me = self.state.me

        if me is None:
            return ''

        a = self.recipient_ids[0]
        b = self.recipient_ids[1]

        return a if me.id != a else b

    @property
    def server(self) -> None:
        """Optional[:class:`Server`]: The server this channel belongs to."""
        return None

    @property
    def type(self) -> typing.Literal[ChannelType.private]:
        """Literal[:attr:`.ChannelType.private`]: The channel's type."""
        return ChannelType.private

    def locally_update(self, data: PartialChannel, /) -> None:
        """Locally updates channel with provided data.

        .. warning::
            This is called by library internally to keep cache up to date.

        Parameters
        ----------
        data: :class:`PartialChannel`
            The data to update channel with.
        """
        if data.active is not UNDEFINED:
            self.active = data.active
        if data.last_message_id is not UNDEFINED:
            self.last_message_id = data.last_message_id

    def permissions_for(self, target: typing.Union[User, Member], /) -> Permissions:
        """Calculate permissions for given user.

        Parameters
        ----------
        target: Union[:class:`User`, :class:`Member`]
            The member or user to calculate permissions for.

        Returns
        -------
        :class:`Permissions`
            The calculated permissions.
        """
        me = self.state.me
        if not me:
            raise TypeError('Missing own user')

        from .server import Member
        from .user import calculate_user_permissions

        if isinstance(target, Member):
            target = target.user

        return calculate_dm_channel_permissions(
            calculate_user_permissions(
                target.id,
                target.relationship,
                target.bot,
                perspective_id=me.id,
                perspective_bot=me.bot,
                perspective_privileged=me.privileged,
            )
        )

    def to_dict(self) -> raw.DirectMessageChannel:
        """:class:`dict`: Convert channel to raw data."""

        payload: raw.DirectMessageChannel = {
            'channel_type': 'DirectMessage',
            '_id': self.id,
            'active': self.active,
            'recipients': list(self.recipient_ids),
        }
        if self.last_message_id is not None:
            payload['last_message_id'] = self.last_message_id
        return payload


@define(slots=True)
class GroupChannel(BaseChannel, Connectable, Messageable):
    """Represesnts a Stoat group channel between 1 or more participants.

    This inherits from :class:`BaseChannel`, :class:`~stoat.abc.Connectable` and :class:`~stoat.abc.Messageable`.
    """

    name: str = field(repr=True, kw_only=True)
    """:class:`str`: The group's name."""

    owner_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's ID who owns this group."""

    description: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The group description."""

    _recipients: typing.Union[
        tuple[typing.Literal[True], list[str]],
        tuple[typing.Literal[False], list[User]],
    ] = field(repr=True, kw_only=True, alias='internal_recipients')

    internal_icon: typing.Optional[StatelessAsset] = field(repr=True, kw_only=True)
    """Optional[:class:`StatelessAsset`]: The stateless group icon."""

    last_message_id: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The last message ID sent in the channel."""

    raw_permissions: typing.Optional[int] = field(repr=True, kw_only=True)
    """Optional[:class:`int`]: The permissions assigned to members of this group.
    
    .. note::
        This attribute does not apply to the owner of the group.
    """

    nsfw: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether this group is marked as not safe for work."""

    def get_channel_id(self) -> str:
        return self.id

    def get_last_message(self) -> typing.Optional[Message]:
        """Optional[:class:`Message`]: The last message sent in the channel."""
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        last_message_id = self.last_message_id

        if last_message_id is None:
            return None

        ctx = (
            MessageThroughGroupChannelLastMessageCacheContext(
                type=CacheContextType.message_through_group_channel_last_message,
                channel=self,
            )
            if state.provide_cache_context('GroupChannel.last_message')
            else _MESSAGE_THROUGH_GROUP_CHANNEL_LAST_MESSAGE
        )

        return cache.get_message(self.id, last_message_id, ctx)

    def get_me(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The own user."""
        return self.state.me

    def get_owner(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user who owns this group."""
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughGroupChannelOwnerCacheContext(
                type=CacheContextType.user_through_dm_channel_recipient,
                channel=self,
            )
            if state.provide_cache_context('GroupChannel.owner')
            else _USER_THROUGH_GROUP_CHANNEL_OWNER
        )

        return cache.get_user(self.owner_id, ctx)

    @typing.overload
    def get_read_state(
        self,
        *,
        default_acked_message_id: typing.Optional[str] = None,
        create_if_not_exists: typing.Literal[True] = ...,
    ) -> ReadState: ...

    @typing.overload
    def get_read_state(
        self,
        *,
        default_acked_message_id: typing.Optional[str] = None,
        create_if_not_exists: typing.Literal[False] = ...,
    ) -> typing.Optional[ReadState]: ...

    def get_read_state(
        self,
        *,
        default_acked_message_id: typing.Optional[str] = None,
        create_if_not_exists: bool = True,
    ) -> typing.Optional[ReadState]:
        """Optional[:class:`ReadState`]: Returns the channel's read state.

        Parameters
        ----------
        default_acked_message_id: Optional[:class:`str`]
            The default acked message ID to use if read state is not found.
        create_if_not_exists: :class:`bool`
            Whether to create a read state and store it if existing was not found.
        """

        state = self.state
        cache = state.cache

        if cache is None:
            if create_if_not_exists:
                return ReadState(
                    state=state,
                    channel_id=self.id,
                    user_id=state.my_id,
                    last_acked_id=default_acked_message_id,
                    mentioned_in=[],
                )
            return None

        ctx = (
            ReadStateThroughGroupChannelReadStateCacheContext(
                type=CacheContextType.read_state_through_group_channel_read_state,
                channel=self,
            )
            if state.provide_cache_context('GroupChannel.read_state')
            else _READ_STATE_THROUGH_GROUP_CHANNEL_READ_STATE
        )

        read_state = cache.get_read_state(self.id, ctx)
        if read_state is None and create_if_not_exists:
            read_state = ReadState(
                state=state,
                channel_id=self.id,
                user_id=state.my_id,
                last_acked_id=default_acked_message_id,
                mentioned_in=[],
            )
            cache.store_read_state(read_state, ctx)
        return read_state

    def locally_update(self, data: PartialChannel, /) -> None:
        """Locally updates channel with provided data.

        .. warning::
            This is called by library internally to keep cache up to date.

        Parameters
        ----------
        data: :class:`PartialChannel`
            The data to update channel with.
        """
        if data.name is not UNDEFINED:
            self.name = data.name
        if data.owner_id is not UNDEFINED:
            self.owner_id = data.owner_id
        if data.description is not UNDEFINED:
            self.description = data.description
        if data.internal_icon is not UNDEFINED:
            self.internal_icon = data.internal_icon
        if data.last_message_id is not UNDEFINED:
            self.last_message_id = data.last_message_id
        if data.raw_permissions is not UNDEFINED:
            self.raw_permissions = data.raw_permissions
        if data.nsfw is not UNDEFINED:
            self.nsfw = data.nsfw

    def _join(self, user_id: str, /) -> None:
        if self._recipients[0]:
            self._recipients[1].append(user_id)  # type: ignore # Pyright doesn't understand `if`
        else:
            self._recipients = (True, [u.id for u in self._recipients[1]])  # type: ignore
            self._recipients[1].append(user_id)

    def _leave(self, user_id: str, /) -> None:
        if self._recipients[0]:
            try:
                self._recipients[1].remove(user_id)  # type: ignore
            except ValueError:
                pass
        else:
            self._recipients = (
                True,
                [u.id for u in self._recipients[1] if u.id != user_id],  # type: ignore
            )

    @property
    def icon(self) -> typing.Optional[Asset]:
        """Optional[:class:`Asset`]: The group icon."""
        return self.internal_icon and self.internal_icon.attach_state(self.state, 'icons')

    @property
    def last_message(self) -> typing.Optional[Message]:
        """Optional[:class:`Message`]: The last message sent in the channel."""

        message = self.get_last_message()
        if message is None:
            if self.last_message_id is None:
                return None
            raise NoData(what=self.last_message_id, type='GroupChannel.last_message')
        return message

    @property
    def me(self) -> User:
        """:class:`User`: The own user."""
        me = self.get_me()
        if me is None:
            raise NoData(what='', type='GroupChannel.me')
        return me

    @property
    def owner(self) -> User:
        """:class:`User`: The user who owns this group."""
        owner = self.get_owner()
        if owner is None:
            raise NoData(what=self.owner_id, type='GroupChannel.owner')
        return owner

    @property
    def permissions(self) -> typing.Optional[Permissions]:
        """Optional[:class:`Permissions`]: The permissions assigned to members of this group.

        .. note::
            This attribute does not apply to the owner of the group.
        """
        if self.raw_permissions is None:
            return None
        ret = _new_permissions(Permissions)
        ret.value = self.raw_permissions
        return ret

    @property
    def read_state(self) -> ReadState:
        """:class:`ReadState`: Returns the channel's read state."""
        return self.get_read_state()

    @property
    def recipient_ids(self) -> list[str]:
        """List[:class:`str`]: The IDs of users participating in channel."""
        if self._recipients[0]:
            return self._recipients[1]  # type: ignore
        else:
            return [u.id for u in self._recipients[1]]  # type: ignore

    @property
    def recipients(self) -> list[User]:
        """List[:class:`User`]: The users participating in channel."""
        if self._recipients[0]:
            state = self.state
            cache = state.cache

            if cache is None:
                return []

            recipient_ids: list[str] = self._recipients[1]  # type: ignore
            recipients = []

            ctx = (
                UserThroughGroupChannelRecipientsCacheContext(
                    type=CacheContextType.user_through_group_channel_recipients,
                    channel=self,
                )
                if state.provide_cache_context('GroupChannel.recipients')
                else _USER_THROUGH_GROUP_CHANNEL_RECIPIENTS
            )

            for recipient_id in recipient_ids:
                user = cache.get_user(recipient_id, ctx)
                if user is not None:
                    recipients.append(user)
            return recipients
        else:
            return self._recipients[1]  # type: ignore

    @property
    def server(self) -> None:
        """Optional[:class:`Server`]: The server this channel belongs to."""
        return None

    @property
    def type(self) -> typing.Literal[ChannelType.group]:
        """Literal[:attr:`.ChannelType.group`]: The channel's type."""
        return ChannelType.group

    async def add(
        self,
        user: ULIDOr[BaseUser],
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
    ) -> None:
        """|coro|

        Adds another user to the group.

        You must have :attr:`~Permissions.create_invites` to do this.

        Fires :class:`PrivateChannelCreateEvent` for added recipient, and :class:`GroupRecipientAddEvent` for rest of group recipients.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        user: ULIDOr[:class:`BaseUser`]
            The user to add.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +-----------+-------------------------------------------+
            | Value     | Reason                                    |
            +-----------+-------------------------------------------+
            | ``IsBot`` | The current token belongs to bot account. |
            +-----------+-------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+--------------------------------------------------------------+
            | Value                 | Reason                                                       |
            +-----------------------+--------------------------------------------------------------+
            | ``GroupTooLarge``     | The group exceeded maximum count of recipients.              |
            +-----------------------+--------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to add the recipient. |
            +-----------------------+--------------------------------------------------------------+
            | ``NotFriends``        | You're not friends with the user you want to add.            |
            +-----------------------+--------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------------------+
            | Value        | Reason                              |
            +--------------+-------------------------------------+
            | ``NotFound`` | The channel or user were not found. |
            +--------------+-------------------------------------+
        :class:`Conflict`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------+-------------------------------+
            | Value               | Reason                        |
            +---------------------+-------------------------------+
            | ``AlreadyInGroup``  | The user is already in group. |
            +---------------------+-------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """
        return await self.state.http.add_group_recipient(self.id, user, http_overrides=http_overrides)

    async def add_bot(
        self,
        bot: ULIDOr[typing.Union[BaseBot, BaseUser]],
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
    ) -> None:
        """|coro|

        Invites a bot to a group.

        You must have :attr:`~Permissions.create_invites` to do this.

        Fires :class:`PrivateChannelCreateEvent` for bot, :class:`GroupRecipientAddEvent` and :class:`MessageCreateEvent` for all group recipients.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        bot: ULIDOr[Union[:class:`BaseBot`, :class:`BaseUser`]]
            The bot.
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
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+------------------------------------------------------+
            | Value                | Reason                                               |
            +----------------------+------------------------------------------------------+
            | ``IsBot``            | The current token belongs to bot account.            |
            +----------------------+------------------------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+-----------------------------------------------------+
            | Value                 | Reason                                              |
            +-----------------------+-----------------------------------------------------+
            | ``BotIsPrivate``      | You do not own the bot to add it.                   |
            +-----------------------+-----------------------------------------------------+
            | ``GroupTooLarge``     | The group exceeded maximum count of recipients.     |
            +-----------------------+-----------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to add bots. |
            +-----------------------+-----------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------------------+
            | Value        | Reason                              |
            +--------------+-------------------------------------+
            | ``NotFound`` | The bot/group/server was not found. |
            +--------------+-------------------------------------+
        :class:`Conflict`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------+-------------------------------+
            | Value               | Reason                        |
            +---------------------+-------------------------------+
            | ``AlreadyInGroup``  | The bot is already in group.  |
            +---------------------+-------------------------------+
            | ``AlreadyInServer`` | The bot is already in server. |
            +---------------------+-------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        :class:`TypeError`
            You specified ``server`` and ``group`` parameters, or passed no parameters.
        """
        return await self.state.http.invite_bot(bot, http_overrides=http_overrides, group=self.id)

    async def create_invite(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> Invite:
        """|coro|

        Creates an invite to group channel.

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

            +----------------------+----------------------------------------------------+
            | Value                | Reason                                             |
            +----------------------+----------------------------------------------------+
            | ``InvalidOperation`` | The target channel is not group or server channel. |
            +----------------------+----------------------------------------------------+
            | ``IsBot``            | The current token belongs to bot account.          |
            +----------------------+----------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+----------------------------------------------------------------------+
            | Value                 | Reason                                                               |
            +-----------------------+----------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to create invites in channel. |
            +-----------------------+----------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +----------------+-----------------------------------+
            | Value          | Reason                            |
            +----------------+-----------------------------------+
            | ``NotFound``   | The target channel was not found. |
            +----------------+-----------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`Invite`
            The invite that was created.
        """

        return await self.state.http.create_channel_invite(self.id, http_overrides=http_overrides)

    async def create_webhook(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        name: str,
        avatar: typing.Optional[ResolvableResource] = None,
    ) -> Webhook:
        """|coro|

        Creates a webhook which 3rd party platforms can use to send.

        You must have :attr:`~Permissions.manage_webhooks` permission to do this.

        Fires :class:`WebhookCreateEvent` for all users who can see target channel.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        name: :class:`str`
            The webhook name. Must be between 1 and 32 chars long.
        avatar: Optional[:class:`ResolvableResource`]
            The webhook avatar.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+--------------------------------------------------------------------------------------+
            | Value                     | Reason                                                                               |
            +---------------------------+--------------------------------------------------------------------------------------+
            | ``InvalidOperation``      | The channel was not type of :attr:`~ChannelType.group` or :attr:`~ChannelType.text`. |
            +---------------------------+--------------------------------------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------------------+-------------------------------------------------------------+
            | Value                            | Reason                                                      |
            +----------------------------------+-------------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to create a webhook. |
            +----------------------------------+-------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------------+
            | Value        | Reason                          |
            +--------------+---------------------------------+
            | ``NotFound`` | The channel/file was not found. |
            +--------------+---------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`Webhook`
            The created webhook.
        """
        return await self.state.http.create_webhook(self.id, http_overrides=http_overrides, name=name, avatar=avatar)

    async def fetch_recipients(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
    ) -> list[User]:
        """|coro|

        Retrieves all recipients who are part of this group.

        .. versionadded:: 1.2

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+----------------------------------+
            | Value                | Reason                           |
            +----------------------+----------------------------------+
            | ``InvalidOperation`` | The target channel is not group. |
            +----------------------+----------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+-----------------------------------------------------------+
            | Value                 | Reason                                                    |
            +-----------------------+-----------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to view the group. |
            +-----------------------+-----------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +----------------+-----------------------------------+
            | Value          | Reason                            |
            +----------------+-----------------------------------+
            | ``NotFound``   | The target channel was not found. |
            +----------------+-----------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        List[:class:`User`]
            The group recipients.
        """
        return await self.state.http.get_group_recipients(self.id, http_overrides=http_overrides)

    async def leave(
        self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None, silent: typing.Optional[bool] = None
    ) -> None:
        """|coro|

        Leaves a group or closes a group.

        You must have :attr:`~Permissions.view_channel` to do this.

        Fires :class:`PrivateChannelDeleteEvent` for all group recipients (including group owner) if the current user is group owner,
        otherwise :class:`PrivateChannelDeleteEvent` is fired for the current user,
        and :class:`GroupRecipientRemoveEvent` is fired for rest of group recipients.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        silent: Optional[:class:`bool`]
            Whether to not send message when leaving.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+---------------------------------------------------------------------------+
            | Value                 | Reason                                                                    |
            +-----------------------+---------------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to view and/or delete the channel. |
            +-----------------------+---------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The channel was not found. |
            +--------------+----------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.close(http_overrides=http_overrides, silent=silent)

    async def set_default_permissions(
        self, permissions: Permissions, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None
    ) -> GroupChannel:
        """|coro|

        Sets default permissions for everyone in a channel.

        You must have :attr:`~Permissions.manage_permissions` to do this.

        Fires :class:`ChannelUpdateEvent` for all group recipients.

        Parameters
        ----------
        permissions: :class:`Permissions`
            The new permissions.
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
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------------------+--------------------------------------------------------------------------------------+
            | Value                            | Reason                                                                               |
            +----------------------------------+--------------------------------------------------------------------------------------+
            | ``CannotGiveMissingPermissions`` | Your new provided permissions contained permissions you didn't have.                 |
            +----------------------------------+--------------------------------------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to edit default permissions for this channel. |
            +----------------------------------+--------------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The channel was not found. |
            +--------------+----------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`GroupChannel`
            The updated group with new permissions.
        """

        result = await self.state.http.set_default_channel_permissions(
            self.id, permissions, http_overrides=http_overrides
        )
        assert isinstance(result, GroupChannel)
        return result

    def permissions_for(self, target: typing.Union[User, Member], /) -> Permissions:
        """Calculate permissions for given user.

        Parameters
        ----------
        target: Union[:class:`User`, :class:`Member`]
            The member or user to calculate permissions for.

        Returns
        -------
        :class:`Permissions`
            The calculated permissions.
        """
        me = self.state.me
        if not me:
            raise TypeError('Missing own user')

        return calculate_group_channel_permissions(
            target.id,
            group_owner_id=self.owner_id,
            group_permissions=self.permissions,
            group_recipients=self.recipient_ids,
        )

    def to_dict(self) -> raw.GroupChannel:
        """:class:`dict`: Convert channel to raw data."""

        payload: dict[str, typing.Any] = {
            'channel_type': 'Group',
            '_id': self.id,
            'name': self.name,
            'owner': self.owner_id,
        }
        if self.description is not None:
            payload['description'] = self.description
        payload['recipients'] = self.recipient_ids
        if self.internal_icon is not None:
            payload['icon'] = self.internal_icon.to_dict('icons')
        if self.last_message_id is not None:
            payload['last_message_id'] = self.last_message_id
        if self.raw_permissions is not None:
            payload['permissions'] = self.raw_permissions
        if self.nsfw:
            payload['nsfw'] = self.nsfw
        return payload  # type: ignore


@define(slots=True)
class UnknownPrivateChannel(BaseChannel):
    """Represents a private channel that is not recognized by library yet.

    This inherits from :class:`BaseChannel`.
    """

    payload: dict[str, typing.Any] = field(repr=True, kw_only=True)
    """Dict[:class:`str`, Any]: The raw channel data."""

    def get_me(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The own user."""
        return self.state.me

    @property
    def me(self) -> User:
        """:class:`User`: The own user."""
        me = self.get_me()
        if me is None:
            raise NoData(what='', type='GroupChannel.me')
        return me

    @property
    def server(self) -> None:
        """Optional[:class:`Server`]: The server this channel belongs to."""
        return None

    @property
    def type(self) -> typing.Literal[ChannelType.unknown]:
        """Literal[:attr:`.ChannelType.unknown`]: The channel's type."""
        return ChannelType.unknown

    def to_dict(self) -> dict[str, typing.Any]:
        """:class:`dict`: Convert channel to raw data."""

        return self.payload


PrivateChannel = typing.Union[SavedMessagesChannel, DMChannel, GroupChannel, UnknownPrivateChannel]


@define(slots=True)
class BaseServerChannel(BaseChannel):
    """A base class for server channels.

    This inherits from :class:`BaseChannel`.
    """

    server_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The server ID that channel belongs to."""

    name: str = field(repr=True, kw_only=True)
    """:class:`str`: The display name of the channel."""

    description: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The channel description."""

    internal_icon: typing.Optional[StatelessAsset] = field(repr=True, kw_only=True)
    """Optional[:class:`StatelessAsset`]: The stateless custom channel icon."""

    default_permissions: typing.Optional[PermissionOverride] = field(repr=True, kw_only=True)
    """Optional[:class:`PermissionOverride`]: Default permissions assigned to users in this channel."""

    role_permissions: dict[str, PermissionOverride] = field(repr=True, kw_only=True)
    """Dict[:class:`str`, :class:`PermissionOverride`]: The permissions assigned based on role to this channel."""

    category_id: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The category ID the channel is in.
    
    .. versionadded:: 1.2
    """

    nsfw: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether this channel is marked as not safe for work."""

    def get_category(self) -> typing.Optional[Category]:
        """Optional[:class:`Category`]: The category the channel is in.

        .. versionadded:: 1.2
        """
        if self.category_id is None:
            return None

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ServerThroughServerChannelCategoryCacheContext(
                type=CacheContextType.server_through_server_channel_category,
                channel=self,
            )
            if state.provide_cache_context('BaseServerChannel.category')
            else _SERVER_THROUGH_SERVER_CHANNEL_CATEGORY
        )

        server = cache.get_server(self.server_id, ctx)
        if server is None:
            return None

        return server.get_category(self.category_id)

    def get_me(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The own user for this server."""
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MemberThroughServerChannelMeCacheContext(
                type=CacheContextType.member_through_server_channel_me,
                channel=self,
            )
            if state.provide_cache_context('BaseServerChannel.me')
            else _MEMBER_THROUGH_SERVER_CHANNEL_ME
        )

        return cache.get_server_member(self.server_id, state.my_id, ctx)

    def get_server(self) -> typing.Optional[Server]:
        """Optional[:class:`Server`]: The server this channel belongs to."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ServerThroughServerChannelServerCacheContext(
                type=CacheContextType.server_through_server_channel_server,
                channel=self,
            )
            if state.provide_cache_context('BaseServerChannel.server')
            else _SERVER_THROUGH_SERVER_CHANNEL_SERVER
        )

        return cache.get_server(self.server_id, ctx)

    @property
    def category(self) -> typing.Optional[Category]:
        """Optional[:class:`Category`]: The category the channel is in."""
        category = self.get_category()
        if category is None and self.category_id is not None:
            raise NoData(what=self.category_id, type='BaseServerChannel.category')
        return category

    @property
    def icon(self) -> typing.Optional[Asset]:
        """Optional[:class:`Asset`]: The custom channel icon."""
        return self.internal_icon and self.internal_icon.attach_state(self.state, 'icons')

    @property
    def me(self) -> Member:
        """Optional[:class:`Member`]: The own user for this server."""
        me = self.get_me()
        if me is None:
            raise NoData(what='', type='BaseServerChannel.me')
        return me

    @property
    def server(self) -> Server:
        """:class:`Server`: The server this channel belongs to."""
        server = self.get_server()
        if server is None:
            raise NoData(what=self.server_id, type='BaseServerChannel.server')
        return server

    async def create_invite(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> Invite:
        """|coro|

        Creates an invite to server channel.

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

            +----------------------+----------------------------------------------------+
            | Value                | Reason                                             |
            +----------------------+----------------------------------------------------+
            | ``InvalidOperation`` | The target channel is not group or server channel. |
            +----------------------+----------------------------------------------------+
            | ``IsBot``            | The current token belongs to bot account.          |
            +----------------------+----------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+----------------------------------------------------------------------+
            | Value                 | Reason                                                               |
            +-----------------------+----------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to create invites in channel. |
            +-----------------------+----------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +----------------+-----------------------------------+
            | Value          | Reason                            |
            +----------------+-----------------------------------+
            | ``NotFound``   | The target channel was not found. |
            +----------------+-----------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`Invite`
            The invite that was created.
        """

        return await self.state.http.create_channel_invite(self.id, http_overrides=http_overrides)

    async def delete(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> None:
        """|coro|

        Deletes a server channel.

        You must have :attr:`~Permissions.view_channel` and :attr:`~Permissions.manage_channels` to do this.

        For server channels, :class:`ServerChannelDeleteEvent` is fired for all users who could see target channel, and :class:`ServerUpdateEvent` for all server members.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+---------------------------------------------------------------------------+
            | Value                 | Reason                                                                    |
            +-----------------------+---------------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to view and/or delete the channel. |
            +-----------------------+---------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The channel was not found. |
            +--------------+----------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.close(http_overrides=http_overrides)

    async def fetch_webhooks(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> list[Webhook]:
        """|coro|

        Retrieves all webhooks in a channel.

        You must have :attr:`~Permissions.manage_webhooks` permission to do this.

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
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------------------+--------------------------------------------------------------------------------------+
            | Value                            | Reason                                                                               |
            +----------------------------------+--------------------------------------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to view webhooks that belong to this channel. |
            +----------------------------------+--------------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The channel was not found. |
            +--------------+----------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        List[:class:`Webhook`]
            The webhooks for this channel.
        """
        return await self.state.http.get_channel_webhooks(self.id, http_overrides=http_overrides)

    async def set_role_permissions(
        self,
        role: ULIDOr[BaseRole],
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        allow: Permissions = Permissions.none(),
        deny: Permissions = Permissions.none(),
    ) -> ServerChannel:
        """|coro|

        Sets permissions for the specified role in a channel.

        You must have :attr:`~Permissions.manage_permissions` to do this.

        Fires :class:`ChannelUpdateEvent` for all users who still see target channel,
        :class:`ServerChannelCreateEvent` for all users who now can see target channel,
        and :class:`ChannelDeleteEvent` for users who no longer can see target channel.

        Parameters
        ----------
        role: ULIDOr[:class:`BaseRole`]
            The role.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        allow: :class:`Permissions`
            The permissions to allow for role in channel.
        deny: :class:`Permissions`
            The permissions to deny for role in channel.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------------------+--------------------------------------------------------------------------------------+
            | Value                            | Reason                                                                               |
            +----------------------------------+--------------------------------------------------------------------------------------+
            | ``CannotGiveMissingPermissions`` | Your new provided permissions contained permissions you didn't have.                 |
            +----------------------------------+--------------------------------------------------------------------------------------+
            | ``NotElevated``                  | Rank of your top role is higher than rank of role you're trying to set override for. |
            +----------------------------------+--------------------------------------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to edit overrides for this channel.           |
            +----------------------------------+--------------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------------------+
            | Value        | Reason                                 |
            +--------------+----------------------------------------+
            | ``NotFound`` | The channel/server/role was not found. |
            +--------------+----------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`ServerChannel`
            The updated server channel with new permissions.
        """
        result = await self.state.http.set_channel_permissions_for_role(
            self.id, role, http_overrides=http_overrides, allow=allow, deny=deny
        )
        return result

    async def set_default_permissions(
        self, permissions: PermissionOverride, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None
    ) -> ServerChannel:
        """|coro|

        Sets default permissions for everyone in a channel.

        You must have :attr:`~Permissions.manage_permissions` to do this.

        Fires :class:`ChannelUpdateEvent` for all users who still see target channel,
        :class:`ServerChannelCreateEvent` for all users who now can see target channel,
        and :class:`ChannelDeleteEvent` is fired for users who no longer can see target channel.

        Parameters
        ----------
        permissions: :class:`PermissionOverride`
            The new permissions.
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
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------------------+--------------------------------------------------------------------------------------+
            | Value                            | Reason                                                                               |
            +----------------------------------+--------------------------------------------------------------------------------------+
            | ``CannotGiveMissingPermissions`` | Your new provided permissions contained permissions you didn't have.                 |
            +----------------------------------+--------------------------------------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to edit default permissions for this channel. |
            +----------------------------------+--------------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The channel was not found. |
            +--------------+----------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`ServerChannel`
            The updated server channel with new permissions.
        """

        result = await self.state.http.set_default_channel_permissions(
            self.id, permissions, http_overrides=http_overrides
        )
        return result  # type: ignore

    def locally_update(self, data: PartialChannel, /) -> None:
        """Locally updates channel with provided data.

        .. warning::
            This is called by library internally to keep cache up to date.

        Parameters
        ----------
        data: :class:`PartialChannel`
            The data to update channel with.
        """
        if data.name is not UNDEFINED:
            self.name = data.name
        if data.description is not UNDEFINED:
            self.description = data.description
        if data.internal_icon is not UNDEFINED:
            self.internal_icon = data.internal_icon
        if data.nsfw is not UNDEFINED:
            self.nsfw = data.nsfw
        if data.role_permissions is not UNDEFINED:
            self.role_permissions = data.role_permissions
        if data.default_permissions is not UNDEFINED:
            self.default_permissions = data.default_permissions
        if data.category_id is not UNDEFINED:
            self.category_id = data.category_id

    def permissions_for(
        self,
        target: typing.Union[User, Member],
        /,
        *,
        safe: bool = True,
        with_ownership: bool = True,
        include_timeout: bool = True,
    ) -> Permissions:
        """Calculate permissions for given user.

        Parameters
        ----------
        target: Union[:class:`User`, :class:`Member`]
            The member or user to calculate permissions for.
        safe: :class:`bool`
            Whether to raise exception or not if role is missing in cache.
        with_ownership: :class:`bool`
            Whether to account for ownership.
        include_timeout: :class:`bool`
            Whether to account for timeout.

        Raises
        ------
        :class:`NoData`
            The server or role is not found in cache.

        Returns
        -------
        :class:`Permissions`
            The calculated permissions.
        """
        server = self.get_server()
        if server is None:
            raise NoData(what=self.server_id, type='BaseServerChannel.server')

        if with_ownership and server.owner_id == target.id:
            return Permissions.all()

        category = self.get_category()
        if safe and category is None and self.category_id is not None:
            raise NoData(what=self.category_id, type='BaseServerChannel.category')

        from .server import sort_member_roles, calculate_server_permissions
        from .user import User

        if isinstance(target, User):
            initial_permissions = server.default_permissions
            if category is not None:
                override = category.default_permissions
                if override is not None:
                    initial_permissions |= override.allow
                    initial_permissions &= ~override.deny

            # No point in providing roles since user doesn't have roles.

            return calculate_server_channel_permissions(
                initial_permissions,
                [],
                default_permissions=self.default_permissions,
                role_permissions={},
            )

        initial_permissions = calculate_server_permissions(
            [],
            None,
            default_permissions=server.default_permissions,
            can_publish=True,
            can_receive=True,
            category=category,
        )
        roles = sort_member_roles(target.role_ids, safe=safe, server_roles=server.roles)
        result = calculate_server_channel_permissions(
            initial_permissions,
            roles,
            default_permissions=self.default_permissions,
            role_permissions=self.role_permissions,
        )
        if include_timeout and target.timed_out_until is not None:
            result &= ALLOW_PERMISSIONS_IN_TIMEOUT
        if not result.view_channel:
            return Permissions.none()
        return result


class ChannelVoiceMetadata:
    """Represents some voice-specific metadata for text channel.

    Attributes
    ----------
    max_users: :class:`int`
        The maximium amount of users allowed in the voice channel at once.

        Zero means an infinite amount of users can connect to voice channel.

    Parameters
    ----------
    max_users: :class:`int`
        The maximium amount of users allowed in the voice channel at once.

        Zero means an infinite amount of users can connect to voice channel.

        Must be greater than 1.
    """

    __slots__ = ('max_users',)

    def __init__(self, max_users: int = 0) -> None:
        self.max_users: int = max_users

    def to_dict(self) -> raw.VoiceInformation:
        """:class:`dict`: Convert channel voice state container to raw data."""
        return {
            'max_users': None if self.max_users == 0 else self.max_users,
        }


@define(slots=True)
class TextChannel(BaseServerChannel, Connectable, Messageable):
    """Represents a text channel that belongs to a server on Stoat.

    This inherits from :class:`BaseServerChannel`, :class:`~stoat.abc.Connectable` and :class:`~stoat.abc.Messageable`.
    """

    last_message_id: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The last message ID sent in the channel."""

    voice: typing.Optional[ChannelVoiceMetadata] = field(repr=True, kw_only=True)
    """Optional[:class:`ChannelVoiceMetadata`]: The voice's metadata in the channel.
    
    .. versionadded:: 1.2
    """

    def get_channel_id(self) -> str:
        return self.id

    def get_last_message(self) -> typing.Optional[Message]:
        """Optional[:class:`Message`]: The last message sent in the channel."""
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        last_message_id = self.last_message_id

        if last_message_id is None:
            return None

        ctx = (
            MessageThroughTextChannelLastMessageCacheContext(
                type=CacheContextType.message_through_text_channel_last_message,
                channel=self,
            )
            if state.provide_cache_context('DMChannel.last_message')
            else _MESSAGE_THROUGH_TEXT_CHANNEL_LAST_MESSAGE
        )

        return cache.get_message(self.id, last_message_id, ctx)

    @typing.overload
    def get_read_state(
        self,
        *,
        default_acked_message_id: typing.Optional[str] = None,
        create_if_not_exists: typing.Literal[True] = ...,
    ) -> ReadState: ...

    @typing.overload
    def get_read_state(
        self,
        *,
        default_acked_message_id: typing.Optional[str] = None,
        create_if_not_exists: typing.Literal[False] = ...,
    ) -> typing.Optional[ReadState]: ...

    def get_read_state(
        self,
        *,
        default_acked_message_id: typing.Optional[str] = None,
        create_if_not_exists: bool = True,
    ) -> typing.Optional[ReadState]:
        """Optional[:class:`ReadState`]: Returns the channel's read state.

        Parameters
        ----------
        default_acked_message_id: Optional[:class:`str`]
            The default acked message ID to use if read state is not found.
        create_if_not_exists: :class:`bool`
            Whether to create a read state and store it if existing was not found.
        """

        state = self.state
        cache = state.cache

        if cache is None:
            if create_if_not_exists:
                return ReadState(
                    state=state,
                    channel_id=self.id,
                    user_id=state.my_id,
                    last_acked_id=default_acked_message_id,
                    mentioned_in=[],
                )
            return None

        ctx = (
            ReadStateThroughTextChannelReadStateCacheContext(
                type=CacheContextType.read_state_through_text_channel_read_state,
                channel=self,
            )
            if state.provide_cache_context('TextChannel.read_state')
            else _READ_STATE_THROUGH_TEXT_CHANNEL_READ_STATE
        )

        read_state = cache.get_read_state(self.id, ctx)
        if read_state is None and create_if_not_exists:
            read_state = ReadState(
                state=state,
                channel_id=self.id,
                user_id=state.my_id,
                last_acked_id=default_acked_message_id,
                mentioned_in=[],
            )
            cache.store_read_state(read_state, ctx)
        return read_state

    def locally_update(self, data: PartialChannel, /) -> None:
        """Locally updates channel with provided data.

        .. warning::
            This is called by library internally to keep cache up to date.

        Parameters
        ----------
        data: :class:`PartialChannel`
            The data to update channel with.
        """
        BaseServerChannel.locally_update(self, data)
        if data.last_message_id is not UNDEFINED:
            self.last_message_id = data.last_message_id
        if data.voice is not UNDEFINED:
            self.voice = data.voice

    @property
    def type(self) -> typing.Literal[ChannelType.text]:
        """Literal[:attr:`.ChannelType.text`]: The channel's type."""
        return ChannelType.text

    @property
    def last_message(self) -> typing.Optional[Message]:
        """Optional[:class:`Message`]: The last message sent in the channel."""

        message = self.get_last_message()
        if message is None:
            if self.last_message_id is None:
                return None
            raise NoData(what=self.last_message_id, type='TextChannel.last_message')
        return message

    @property
    def read_state(self) -> ReadState:
        """:class:`ReadState`: Returns the channel's read state."""
        return self.get_read_state()

    @property
    def voice_states(self) -> ChannelVoiceStateContainer:
        """:class:`ChannelVoiceStateContainer`: Returns all voice states in the channel."""

        state = self.state
        cache = state.cache

        if cache is None:
            res = None
        else:
            ctx = (
                ChannelVoiceStateContainerThroughTextChannelVoiceStatesCacheContext(
                    type=CacheContextType.channel_voice_state_container_through_text_channel_voice_states,
                    channel=self,
                )
                if state.provide_cache_context('TextChannel.voice_states')
                else _CHANNEL_VOICE_STATE_CONTAINER_THROUGH_TEXT_CHANNEL_VOICE_STATES
            )
            res = cache.get_channel_voice_state(
                self.id,
                ctx,
            )

        return (
            ChannelVoiceStateContainer(
                channel_id=self.id,
                participants={},
                node='',
            )
            if res is None
            else res
        )

    async def create_webhook(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        name: str,
        avatar: typing.Optional[ResolvableResource] = None,
    ) -> Webhook:
        """|coro|

        Creates a webhook which 3rd party platforms can use to send.

        You must have :attr:`~Permissions.manage_webhooks` permission to do this.

        Fires :class:`WebhookCreateEvent` for all users who can see target channel.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        name: :class:`str`
            The webhook name. Must be between 1 and 32 chars long.
        avatar: Optional[:class:`ResolvableResource`]
            The webhook avatar.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+--------------------------------------------------------------------------------------+
            | Value                     | Reason                                                                               |
            +---------------------------+--------------------------------------------------------------------------------------+
            | ``InvalidOperation``      | The channel was not type of :attr:`~ChannelType.group` or :attr:`~ChannelType.text`. |
            +---------------------------+--------------------------------------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------------------+-------------------------------------------------------------+
            | Value                            | Reason                                                      |
            +----------------------------------+-------------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to create a webhook. |
            +----------------------------------+-------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------------+
            | Value        | Reason                          |
            +--------------+---------------------------------+
            | ``NotFound`` | The channel/file was not found. |
            +--------------+---------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`Webhook`
            The created webhook.
        """
        return await self.state.http.create_webhook(self.id, http_overrides=http_overrides, name=name, avatar=avatar)

    def to_dict(self) -> raw.TextChannel:
        """:class:`dict`: Convert channel to raw data."""

        payload: dict[str, typing.Any] = {
            'channel_type': 'TextChannel',
            '_id': self.id,
            'server': self.server_id,
            'name': self.name,
        }
        if self.description is not None:
            payload['description'] = self.description
        if self.internal_icon is not None:
            payload['icon'] = self.internal_icon.to_dict('icons')
        if self.last_message_id is not None:
            payload['last_message_id'] = self.last_message_id
        if self.default_permissions is not None:
            payload['default_permissions'] = self.default_permissions.to_field_dict()
        if len(self.role_permissions):
            payload['role_permissions'] = {k: v.to_field_dict() for k, v in self.role_permissions.items()}
        if self.nsfw:
            payload['nsfw'] = self.nsfw
        if self.voice is not None:
            payload['voice'] = self.voice.to_dict()
        return payload  # type: ignore


@define(slots=True)
class VoiceChannel(BaseServerChannel, Connectable, Messageable):
    """Represents a voice channel that belongs to a server on Stoat.

    This inherits from :class:`BaseServerChannel`, :class:`~stoat.abc.Connectable` and :class:`~stoat.abc.Messageable`.

    .. deprecated:: 0.7.0
        The voice channel type was deprecated in favour of :attr:`TextChannel.voice`.
    """

    def get_channel_id(self) -> str:
        return self.id

    def locally_update(self, data: PartialChannel, /) -> None:
        """Locally updates channel with provided data.

        .. warning::
            This is called by library internally to keep cache up to date.

        Parameters
        ----------
        data: :class:`PartialChannel`
            The data to update channel with.
        """
        BaseServerChannel.locally_update(self, data)
        if data.voice is not UNDEFINED:
            self.voice = data.voice

    @property
    def type(self) -> typing.Literal[ChannelType.voice]:
        """Literal[:attr:`.ChannelType.voice`]: The channel's type."""
        return ChannelType.voice

    @property
    def voice_states(self) -> ChannelVoiceStateContainer:
        """:class:`ChannelVoiceStateContainer`: Returns all voice states in the channel."""

        state = self.state
        cache = state.cache

        if cache is None:
            res = None
        else:
            ctx = (
                ChannelVoiceStateContainerThroughVoiceChannelVoiceStatesCacheContext(
                    type=CacheContextType.channel_voice_state_container_through_voice_channel_voice_states,
                    channel=self,
                )
                if state.provide_cache_context('VoiceChannel.voice_states')
                else _CHANNEL_VOICE_STATE_CONTAINER_THROUGH_VOICE_CHANNEL_VOICE_STATES
            )
            res = cache.get_channel_voice_state(
                self.id,
                ctx,
            )

        return (
            ChannelVoiceStateContainer(
                channel_id=self.id,
                participants={},
                node='',
            )
            if res is None
            else res
        )

    def to_dict(self) -> raw.VoiceChannel:
        """:class:`dict`: Convert channel to raw data."""

        payload: dict[str, typing.Any] = {
            'channel_type': 'VoiceChannel',
            '_id': self.id,
            'server': self.server_id,
            'name': self.name,
        }
        if self.description is not None:
            payload['description'] = self.description
        if self.internal_icon is not None:
            payload['icon'] = self.internal_icon.to_dict('icons')
        if self.default_permissions is not None:
            payload['default_permissions'] = self.default_permissions.to_field_dict()
        if len(self.role_permissions):
            payload['role_permissions'] = {k: v.to_field_dict() for k, v in self.role_permissions.items()}
        if self.nsfw:
            payload['nsfw'] = self.nsfw
        return payload  # type: ignore


@define(slots=True)
class UnknownServerChannel(BaseServerChannel):
    """Represents a server channel that is not recognized by library yet.

    This inherits from :class:`BaseServerChannel`.
    """

    payload: dict[str, typing.Any] = field(repr=True, kw_only=True)
    """Dict[:class:`str`, Any]: The raw channel data."""

    @property
    def type(self) -> typing.Literal[ChannelType.unknown]:
        """Literal[:attr:`.ChannelType.unknown`]: The channel's type."""
        return ChannelType.unknown

    def to_dict(self) -> dict[str, typing.Any]:
        """:class:`dict`: Convert channel to raw data."""
        return self.payload


ServerChannel = typing.Union[TextChannel, VoiceChannel]
TextableChannel = typing.Union[SavedMessagesChannel, DMChannel, GroupChannel, TextChannel, VoiceChannel]
UnknownChannel = typing.Union[UnknownPrivateChannel, UnknownServerChannel]
Channel = typing.Union[
    SavedMessagesChannel,
    DMChannel,
    GroupChannel,
    UnknownPrivateChannel,
    TextChannel,
    VoiceChannel,
    UnknownServerChannel,
]


@define(slots=True)
class ChannelVoiceStateContainer:
    """Represents voice state container for the channel."""

    channel_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The channel's ID."""

    participants: dict[str, UserVoiceState] = field(repr=True, kw_only=True)
    """Dict[:class:`str`, :class:`UserVoiceState`]: The channel's participants."""

    node: str = field(repr=True, kw_only=True)
    """:class:`str`: The node name."""

    def locally_add(self, state: UserVoiceState, /) -> None:
        """Locally adds user's voice state into this container.

        Parameters
        ----------
        state: :class:`UserVoiceState`
            The state to add.
        """
        self.participants[state.user_id] = state

    def locally_remove(self, user_id: str, /) -> typing.Optional[UserVoiceState]:
        """Locally removes user's voice state from this container.

        Parameters
        ----------
        user_id: :class:`str`
            The user's ID to remove state from.

        Returns
        -------
        Optional[:class:`UserVoiceState`]
            The removed user's voice state.
        """
        return self.participants.pop(user_id, None)


@define(slots=True)
class PartialMessageable(Messageable):
    """Represents a partial messageable to aid with working messageable channels when only a channel ID is present."""

    state: State = field(repr=False, kw_only=True)
    """:class:`State`: The state."""

    id: str = field(repr=True, kw_only=True)
    """:class:`str`: The channel's ID."""

    def get_channel_id(self) -> str:
        return self.id

    @property
    def server(self) -> None:
        """Optional[:class:`Server`]: The server this channel belongs to."""
        return None

    def permissions_for(self, _target: typing.Union[User, Member], /) -> Permissions:
        """Calculate permissions for given user.

        This is sentinel.

        Parameters
        ----------
        target: Union[:class:`User`, :class:`Member`]
            The member or user to calculate permissions for.

        Returns
        -------
        :class:`Permissions`
            The calculated permissions.
        """
        return Permissions.none()


__all__ = (
    'BaseChannel',
    'PartialChannel',
    'calculate_saved_messages_channel_permissions',
    'calculate_dm_channel_permissions',
    'calculate_group_channel_permissions',
    'calculate_server_channel_permissions',
    'SavedMessagesChannel',
    'DMChannel',
    'GroupChannel',
    'UnknownPrivateChannel',
    'PrivateChannel',
    'BaseServerChannel',
    'ChannelVoiceMetadata',
    'TextChannel',
    'VoiceChannel',
    'UnknownServerChannel',
    'ServerChannel',
    'TextableChannel',
    'UnknownChannel',
    'Channel',
    'ChannelVoiceStateContainer',
    'PartialMessageable',
)
