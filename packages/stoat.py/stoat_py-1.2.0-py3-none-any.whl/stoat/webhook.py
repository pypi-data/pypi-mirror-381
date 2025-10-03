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
from .cache import (
    CacheContextType,
    MemberOrUserThroughWebhookCreatorCacheContext,
    MemberThroughWebhookCreatorCacheContext,
    UserThroughWebhookCreatorCacheContext,
    ChannelThroughWebhookChannelCacheContext,
    _MEMBER_OR_USER_THROUGH_WEBHOOK_CREATOR,
    _MEMBER_THROUGH_WEBHOOK_CREATOR,
    _USER_THROUGH_WEBHOOK_CREATOR,
    _CHANNEL_THROUGH_WEBHOOK_CHANNEL,
)
from .cdn import StatelessAsset, Asset, ResolvableResource
from .channel import GroupChannel, BaseServerChannel, TextChannel
from .core import (
    UNDEFINED,
    UndefinedOr,
    ULIDOr,
)
from .errors import NoData
from .message import (
    Reply,
    MessageInteractions,
    MessageMasquerade,
    SendableEmbed,
    BaseMessage,
    Message,
)
from .permissions import Permissions

if typing.TYPE_CHECKING:
    from . import raw
    from .http import HTTPOverrideOptions
    from .server import Member
    from .user import User

_new_permissions = Permissions.__new__


@define(slots=True)
class BaseWebhook(Base):
    """Represents a webhook on Stoat.

    This inherits from :class:`BaseWebhook`.
    """

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, BaseWebhook) and self.id == other.id

    def _token(self) -> typing.Optional[str]:
        return None

    async def delete(
        self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None, by_token: bool = False
    ) -> None:
        """|coro|

        Deletes the webhook.

        Fires :class:`WebhookDeleteEvent` for all users who can see webhook channel.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        by_token: :class:`bool`
            Whether to use webhook token, if possible.

            You must have :attr:`~Permissions.manage_webhooks` to provide ``False``.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+---------------------------------------------------------------------------+
            | Value                | Reason                                                                    |
            +----------------------+---------------------------------------------------------------------------+
            | ``InvalidSession``   | The current bot/user token is invalid.                                    |
            +----------------------+---------------------------------------------------------------------------+
            | ``NotAuthenticated`` | The webhook token is invalid. Only applicable when ``token`` is provided. |
            +----------------------+---------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The webhook was not found. |
            +--------------+----------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        if by_token:
            token = self._token()
            return await self.state.http.delete_webhook(self.id, http_overrides=http_overrides, token=token)
        else:
            return await self.state.http.delete_webhook(self.id, http_overrides=http_overrides)

    async def edit(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        by_token: bool = False,
        name: UndefinedOr[str] = UNDEFINED,
        avatar: UndefinedOr[typing.Optional[ResolvableResource]] = UNDEFINED,
        permissions: UndefinedOr[Permissions] = UNDEFINED,
    ) -> Webhook:
        """|coro|

        Edits the webhook.

        Fires :class:`WebhookUpdateEvent` for all users who can see webhook channel.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        by_token: :class:`bool`
            Whether to use webhook token, if possible.

            You must have :attr:`~Permissions.manage_webhooks` to provide ``False``.
        name: UndefinedOr[:class:`str`]
            The new webhook name. Must be between 1 and 32 chars long.
        avatar: UndefinedOr[Optional[:class:`ResolvableResource`]]
            The new webhook avatar.
        permissions: UndefinedOr[:class:`Permissions`]
            The new webhook permissions.

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

            +----------------------+------------------------------------------------------------------------------+
            | Value                | Reason                                                                       |
            +----------------------+------------------------------------------------------------------------------+
            | ``InvalidSession``   | The current bot/user token is invalid.                                       |
            +----------------------+------------------------------------------------------------------------------+
            | ``NotAuthenticated`` | The webhook token is invalid. Only applicable when ``by_token`` is ``True``. |
            +----------------------+------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------------+
            | Value        | Reason                          |
            +--------------+---------------------------------+
            | ``NotFound`` | The webhook/file was not found. |
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
            The newly updated webhook.
        """

        if by_token:
            token = self._token()

            return await self.state.http.edit_webhook(
                self.id,
                http_overrides=http_overrides,
                token=token,
                name=name,
                avatar=avatar,
                permissions=permissions,
            )
        else:
            return await self.state.http.edit_webhook(
                self.id, http_overrides=http_overrides, name=name, avatar=avatar, permissions=permissions
            )

    async def execute(
        self,
        content: typing.Optional[str] = None,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        nonce: typing.Optional[str] = None,
        attachments: typing.Optional[list[ResolvableResource]] = None,
        replies: typing.Optional[list[typing.Union[Reply, ULIDOr[BaseMessage]]]] = None,
        embeds: typing.Optional[list[SendableEmbed]] = None,
        masquerade: typing.Optional[MessageMasquerade] = None,
        interactions: typing.Optional[MessageInteractions] = None,
        silent: typing.Optional[bool] = None,
        mention_everyone: typing.Optional[bool] = None,
        mention_online: typing.Optional[bool] = None,
    ) -> Message:
        """|coro|

        Executes a webhook.

        The webhook must have :attr:`~Permissions.send_messages` to do this.

        If message mentions "\\@everyone" or "\\@online", the webhook must have :attr:`~Permissions.mention_everyone` to do that.

        If message mentions any roles, the webhook must have :attr:`~Permissions.mention_roles` to do that.

        Fires :class:`MessageCreateEvent` and optionally :class:`MessageAppendEvent`, both for all users who can see target channel.

        Parameters
        ----------
        webhook: ULIDOr[:class:`BaseWebhook`]
            The webhook to execute.
        token: :class:`str`
            The webhook token.
        content: Optional[:class:`str`]
            The message content.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        nonce: Optional[:class:`str`]
            The message nonce.
        attachments: Optional[List[:class:`ResolvableResource`]]
            The attachments to send the message with.

            Webhook must have :attr:`~Permissions.upload_files` to provide this.
        replies: Optional[List[Union[:class:`Reply`, ULIDOr[:class:`BaseMessage`]]]]
            The message replies.
        embeds: Optional[List[:class:`SendableEmbed`]]
            The embeds to send the message with.

            Webhook must have :attr:`~Permissions.send_embeds` to provide this.
        masquerade: Optional[:class:`MessageMasquerade`]
            The masquerade for the message.

            Webhook must have :attr:`~Permissions.use_masquerade` to provide this.

            If :attr:`.MessageMasquerade.color` is provided, :attr:`~Permissions.manage_roles` is also required.
        interactions: Optional[:class:`MessageInteractions`]
            The message interactions.

            If :attr:`.MessageInteractions.reactions` is provided, :attr:`~Permissions.react` is required.
        silent: Optional[:class:`bool`]
            Whether to suppress notifications or not.
        mention_everyone: Optional[:class:`bool`]
            Whether to mention all users who can see the channel. This cannot be mixed with ``mention_online`` parameter.
        mention_online: Optional[:class:`bool`]
            Whether to mention all users who are online and can see the channel. This cannot be mixed with ``mention_everyone`` parameter.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | Value                  | Reason                                                                                                             |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``EmptyMessage``       | The message was empty.                                                                                             |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``FailedValidation``   | The payload was invalid.                                                                                           |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``InvalidFlagValue``   | Both ``mention_everyone`` and ``mention_online`` were ``True``.                                                    |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``InvalidOperation``   | The passed nonce was already used. One of :attr:`.MessageInteractions.reactions` elements was invalid.             |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``InvalidProperty``    | :attr:`.MessageInteractions.restrict_reactions` was ``True`` but :attr:`.MessageInteractions.reactions` was empty. |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``PayloadTooLarge``    | The message was too large.                                                                                         |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``TooManyAttachments`` | You provided more attachments than allowed on this instance.                                                       |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``TooManyEmbeds``      | You provided more embeds than allowed on this instance.                                                            |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``TooManyReplies``     | You were replying to more messages than was allowed on this instance.                                              |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+-------------------------------+
            | Value                | Reason                        |
            +----------------------+-------------------------------+
            | ``NotAuthenticated`` | The webhook token is invalid. |
            +----------------------+-------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+------------------------------------------------------------------+
            | Value                 | Reason                                                           |
            +-----------------------+------------------------------------------------------------------+
            | ``MissingPermission`` | The webhook do not have the proper permissions to send messages. |
            +-----------------------+------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-----------------------------------------------+
            | Value        | Reason                                        |
            +--------------+-----------------------------------------------+
            | ``NotFound`` | The channel/file/reply/webhook was not found. |
            +--------------+-----------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+-------------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                                | Populated attributes                                                |
            +-------------------+-------------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database.        | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+-------------------------------------------------------+---------------------------------------------------------------------+
            | ``InternalError`` | Somehow something went wrong during message creation. |                                                                     |
            +-------------------+-------------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`Message`
            The message that was sent.
        """

        token = self._token()
        assert token is not None, 'No token'
        return await self.state.http.execute_webhook(
            self.id,
            token,
            content=content,
            http_overrides=http_overrides,
            nonce=nonce,
            attachments=attachments,
            replies=replies,
            embeds=embeds,
            masquerade=masquerade,
            interactions=interactions,
            silent=silent,
            mention_everyone=mention_everyone,
            mention_online=mention_online,
        )

    async def fetch(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        token: typing.Optional[str] = None,
    ) -> Webhook:
        """|coro|

        Retrieves a webhook.

        If webhook token wasn't given, the library will attempt get webhook with bot/user token.

        You must have :attr:`~Permissions.manage_webhooks` to do this.

        .. note::
            Due to Stoat limitation, the webhook avatar information will be partial if no token is provided.
            Fields are guaranteed to be non-zero/non-empty are ``id`` and ``user_id``.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        token: Optional[:class:`str`]
            The webhook token.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+---------------------------------------------------------------------------+
            | Value                | Reason                                                                    |
            +----------------------+---------------------------------------------------------------------------+
            | ``InvalidSession``   | The current bot/user token is invalid.                                    |
            +----------------------+---------------------------------------------------------------------------+
            | ``NotAuthenticated`` | The webhook token is invalid. Only applicable when ``token`` is provided. |
            +----------------------+---------------------------------------------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+------------------------------------------------------------------+
            | Value                 | Reason                                                           |
            +-----------------------+------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to retrieve this webhook. |
            +-----------------------+------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The webhook was not found. |
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
        :class:`Webhook`
            The retrieved webhook.
        """
        return await self.state.http.get_webhook(self.id, http_overrides=http_overrides, token=token or self._token())


@define(slots=True)
class PartialWebhook(BaseWebhook):
    """Represents a partial webhook on Stoat.

    Unmodified fields will have :data:`.UNDEFINED` as their value.

    This inherits from :class:`BaseWebhook`.
    """

    name: UndefinedOr[str] = field(repr=True, hash=True, kw_only=True, eq=True)
    """UndefinedOr[:class:`str`]: The new webhook's name."""

    internal_avatar: UndefinedOr[typing.Optional[StatelessAsset]] = field(repr=True, hash=True, kw_only=True, eq=True)
    """UndefinedOr[Optional[:class:`StatelessAsset`]]: The new webhook's stateless avatar."""

    raw_permissions: UndefinedOr[int] = field(repr=True, hash=True, kw_only=True, eq=True)
    """UndefinedOr[:class:`int`]: The new webhook's permissions raw value."""

    @property
    def avatar(self) -> UndefinedOr[typing.Optional[Asset]]:
        """UndefinedOr[Optional[:class:`Asset`]]: The new avatar of the webhook."""
        return self.internal_avatar and self.internal_avatar.attach_state(self.state, 'avatars')

    @property
    def permissions(self) -> UndefinedOr[Permissions]:
        """UndefinedOr[:class:`Permissions`]: The new webhook's permissions."""
        if self.raw_permissions is UNDEFINED:
            return self.raw_permissions
        ret = _new_permissions(Permissions)
        ret.value = self.raw_permissions
        return ret


@define(slots=True)
class Webhook(BaseWebhook):
    """Represents a webhook on Stoat.

    This inherits from :class:`BaseWebhook`.
    """

    name: str = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`str`: The webhook's name."""

    internal_avatar: typing.Optional[StatelessAsset] = field(repr=True, hash=True, kw_only=True, eq=True)
    """Optional[:class:`StatelessAsset`]: The webhook's stateless avatar."""

    creator_id: str = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`str`: The user's ID who created this webhook.
    
    .. warning::

        This is available only since API v0.7.17 and only not from ``GET /webhooks/{webhook.id}`` endpoints.
        The attribute will be empty string if unavailable.
    """

    channel_id: str = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`str`: The channel's ID the webhook in."""

    raw_permissions: int = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`int`: The webhook's permissions raw value."""

    token: typing.Optional[str] = field(repr=True, hash=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The webhook's private token."""

    def get_creator(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user who created this webhook."""
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        creator_id = self.creator_id
        if not creator_id:
            return None

        ctx = (
            MemberOrUserThroughWebhookCreatorCacheContext(
                type=CacheContextType.member_or_user_through_webhook_creator,
                webhook=self,
            )
            if state.provide_cache_context('Webhook.creator')
            else _MEMBER_OR_USER_THROUGH_WEBHOOK_CREATOR
        )

        channel = cache.get_channel(self.channel_id, ctx)

        ret = None
        if isinstance(channel, BaseServerChannel):
            ret = cache.get_server_member(channel.server_id, self.creator_id, ctx)

        if ret is None:
            return cache.get_user(creator_id, ctx)
        return ret

    def get_creator_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user who created this webhook."""
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        creator_id = self.creator_id
        if not creator_id:
            return None

        ctx = (
            MemberThroughWebhookCreatorCacheContext(
                type=CacheContextType.member_through_webhook_creator,
                webhook=self,
            )
            if state.provide_cache_context('Webhook.creator_as_member')
            else _MEMBER_THROUGH_WEBHOOK_CREATOR
        )

        channel = cache.get_channel(self.channel_id, ctx)

        if isinstance(channel, BaseServerChannel):
            return cache.get_server_member(channel.server_id, self.creator_id, ctx)
        return None

    def get_creator_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user who created this webhook."""
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        creator_id = self.creator_id
        if not creator_id:
            return None

        ctx = (
            UserThroughWebhookCreatorCacheContext(
                type=CacheContextType.user_through_webhook_creator,
                webhook=self,
            )
            if state.provide_cache_context('Webhook.creator_as_user')
            else _USER_THROUGH_WEBHOOK_CREATOR
        )

        return cache.get_user(creator_id, ctx)

    def get_channel(self) -> typing.Optional[typing.Union[GroupChannel, TextChannel]]:
        """Optional[Union[:class:`GroupChannel`, :class:`TextChannel`]]: The channel the webhook belongs to."""
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ChannelThroughWebhookChannelCacheContext(
                type=CacheContextType.channel_through_webhook_channel,
                webhook=self,
            )
            if state.provide_cache_context('Webhook.channel')
            else _CHANNEL_THROUGH_WEBHOOK_CHANNEL
        )

        channel = cache.get_channel(self.channel_id, ctx)
        if channel is not None:
            assert isinstance(channel, (GroupChannel, TextChannel))
        return channel

    def _token(self) -> typing.Optional[str]:
        return self.token

    def locally_update(self, data: PartialWebhook, /) -> None:
        """Locally updates webhook with provided data.

        .. warning::

            This is called by library internally to keep cache up to date.

        Parameters
        ----------
        data: :class:`PartialWebhook`
            The data to update webhook with.
        """
        if data.name is not UNDEFINED:
            self.name = data.name
        if data.internal_avatar is not UNDEFINED:
            self.internal_avatar = data.internal_avatar
        if data.raw_permissions is not UNDEFINED:
            self.raw_permissions = data.raw_permissions

    @property
    def avatar(self) -> typing.Optional[Asset]:
        """Optional[:class:`Asset`]: The webhook's avatar."""
        return self.internal_avatar and self.internal_avatar.attach_state(self.state, 'avatars')

    @property
    def creator(self) -> typing.Union[Member, User]:
        """Union[:class:`Member`, :class:`User`]: The user who created this webhook."""
        creator = self.get_creator()
        if creator is None:
            raise NoData(what=self.creator_id, type='Webhook.creator')
        return creator

    @property
    def creator_as_member(self) -> Member:
        """:class:`Member`: The user who created this webhook."""
        creator = self.get_creator_as_member()
        if creator is None:
            raise NoData(what=self.creator_id, type='Webhook.creator_as_member')
        return creator

    @property
    def creator_as_user(self) -> User:
        """:class:`User`: The user who created this webhook."""
        creator = self.get_creator_as_user()
        if creator is None:
            raise NoData(what=self.creator_id, type='Webhook.creator_as_user')
        return creator

    @property
    def channel(self) -> typing.Union[GroupChannel, TextChannel]:
        """Union[:class:`GroupChannel`, :class:`TextChannel`]: The channel the webhook belongs to."""
        channel = self.get_channel()
        if channel is None:
            raise NoData(what=self.channel_id, type='Webhook.channel')
        return channel

    @property
    def permissions(self) -> Permissions:
        """:class:`Permissions`: The webhook's permissions."""
        ret = _new_permissions(Permissions)
        ret.value = self.raw_permissions
        return ret

    def to_dict(self) -> raw.Webhook:
        """:class:`dict`: Convert webhook to raw data."""
        payload: dict[str, typing.Any] = {
            'id': self.id,
            'name': self.name,
        }
        if self.internal_avatar is not None:
            payload['avatar'] = self.internal_avatar.to_dict('avatars')
        if len(self.creator_id):
            payload['creator_id'] = self.creator_id
        payload['channel_id'] = self.channel_id
        payload['permissions'] = self.raw_permissions
        payload['token'] = self.token
        return payload  # type: ignore


__all__ = (
    'BaseWebhook',
    'PartialWebhook',
    'Webhook',
)
