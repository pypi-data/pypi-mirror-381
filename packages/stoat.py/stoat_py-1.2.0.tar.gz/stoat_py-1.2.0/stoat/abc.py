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

from .cache import (
    CacheContextType,
    MessageThroughMessageableGetterCacheContext,
    MessagesThroughMessageableGetterCacheContext,
    _MESSAGE_THROUGH_MESSAGEABLE_GETTER,
    _MESSAGES_THROUGH_MESSAGEABLE_GETTER,
)
from .context_managers import Typing
from .core import (
    UNDEFINED,
    UndefinedOr,
    ULIDOr,
    ZID,
)
from .ulid import _ulid_new

if typing.TYPE_CHECKING:
    from collections.abc import Mapping
    from livekit.rtc import Room  # type: ignore

    from .cdn import ResolvableResource
    from .enums import MessageSort
    from .http import HTTPOverrideOptions
    from .message import Reply, MessageInteractions, MessageMasquerade, SendableEmbed, BaseMessage, Message
    from .state import State
    from .user import BaseUser


class Messageable:
    """An ABC that allows derived instances to send messages.

    The following classes implement this ABC:

    - :class:`SavedMessagesChannel`
    - :class:`DMChannel`
    - :class:`GroupChannel`
    - :class:`TextChannel`
    - :class:`VoiceChannel`
    - :class:`BaseMember`
    - :class:`BaseUser`
    - :class:`PartialMessageable`
    - :class:`stoat.ext.commands.Context`
    """

    __slots__ = ()

    state: State

    def _get_state(self) -> State:
        return self.state

    async def fetch_channel_id(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> str:
        """:class:`str`: Retrieves the channel's ID."""
        return self.get_channel_id()

    def get_channel_id(self) -> str:
        """:class:`str`: Retrieves the channel's ID, if possible."""
        return ''

    def get_message(self, message_id: str, /) -> typing.Optional[Message]:
        """Retrieves a channel message from cache.

        Parameters
        ----------
        message_id: :class:`str`
            The message ID.

        Returns
        -------
        Optional[:class:`~stoat.Message`]
            The message or ``None`` if not found.
        """
        state = self._get_state()
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MessageThroughMessageableGetterCacheContext(
                type=CacheContextType.message_through_messageable_getter,
                entity=self,
            )
            if state.provide_cache_context('Messageable.get_message()')
            else _MESSAGE_THROUGH_MESSAGEABLE_GETTER
        )

        return cache.get_message(self.get_channel_id(), message_id, ctx)

    @property
    def messages(self) -> Mapping[str, Message]:
        """Mapping[:class:`str`, :class:`~stoat.Message`]: Returns all messages in this channel."""

        state = self._get_state()
        cache = state.cache

        if cache is None:
            return {}

        ctx = (
            MessagesThroughMessageableGetterCacheContext(
                type=CacheContextType.messages_through_messageable_getter,
                entity=self,
            )
            if state.provide_cache_context('Messageable.messages')
            else _MESSAGES_THROUGH_MESSAGEABLE_GETTER
        )

        messages = cache.get_messages_mapping_of(self.get_channel_id(), ctx)

        if messages is None:
            return {}

        return messages

    async def begin_typing(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> None:
        """Begins typing in channel, until :meth:`~.end_typing` is called."""
        state = self._get_state()
        channel_id = await self.fetch_channel_id(http_overrides=http_overrides)
        return await state.shard.begin_typing(channel_id)

    async def end_typing(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> None:
        """Ends typing in channel."""
        state = self._get_state()
        channel_id = await self.fetch_channel_id(http_overrides=http_overrides)
        await state.shard.end_typing(channel_id)

    # We can't use normal references like :class:`HTTPException` or :class:`MessageInteractions`,
    # because it breaks references in commands extension.
    # Use :class:`~stoat.HTTPException` and :class:`~stoat.MessageInteractions` explicitly.

    async def acknowledge(
        self,
        message: UndefinedOr[typing.Optional[ULIDOr[BaseMessage]]] = UNDEFINED,
        *,
        channel_http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
    ) -> None:
        """|coro|

        Marks the destination channel as read.

        You must have :attr:`~Permissions.view_channel` to do this.

        Fires :class:`MessageAckEvent` for the current user.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        message: ULIDOr[:class:`BaseMessage`]
            The message to mark as read.
        channel_http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides for getting channel.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`~stoat.HTTPException`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +-----------+-------------------------------------------+
            | Value     | Reason                                    |
            +-----------+-------------------------------------------+
            | ``IsBot`` | The current token belongs to bot account. |
            +-----------+-------------------------------------------+
        :class:`~stoat.Unauthorized`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`~stoat.Forbidden`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +-----------------------+-------------------------------------------------------------+
            | Value                 | Reason                                                      |
            +-----------------------+-------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to view the channel. |
            +-----------------------+-------------------------------------------------------------+
        :class:`~stoat.NotFound`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The channel was not found. |
            +--------------+----------------------------+
        """

        state = self._get_state()
        channel_id = await self.fetch_channel_id(http_overrides=channel_http_overrides)

        if message is UNDEFINED:
            message = _ulid_new()
        elif message is None:
            message = ZID

        await state.http.acknowledge_message(channel_id, message, http_overrides=http_overrides)

    async def fetch_message(
        self,
        message: ULIDOr[BaseMessage],
        /,
        *,
        channel_http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
    ) -> Message:
        """|coro|

        Retrieves a message.

        Parameters
        ----------
        channel: ULIDOr[:class:`TextableChannel`]
            The channel the message is in.
        message: ULIDOr[:class:`BaseMessage`]
            The message to retrieve.
        channel_http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides for getting channel.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`~stoat.Unauthorized`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`~stoat.Forbidden`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +-----------------------+-------------------------------------------------------------+
            | Value                 | Reason                                                      |
            +-----------------------+-------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to view the channel. |
            +-----------------------+-------------------------------------------------------------+
        :class:`~stoat.NotFound`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +--------------+------------------------------------+
            | Value        | Reason                             |
            +--------------+------------------------------------+
            | ``NotFound`` | The channel/message was not found. |
            +--------------+------------------------------------+
        :class:`~stoat.InternalServerError`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                              |
            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~stoat.HTTPException.collection`, :attr:`~stoat.HTTPException.operation` |
            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+

        Returns
        -------
        :class:`~stoat.Message`
            The retrieved message.
        """

        channel = await self.fetch_channel_id(http_overrides=channel_http_overrides)
        return await self.state.http.get_message(channel, message, http_overrides=http_overrides)

    async def history(
        self,
        *,
        channel_http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        limit: typing.Optional[int] = None,
        before: typing.Optional[ULIDOr[BaseMessage]] = None,
        after: typing.Optional[ULIDOr[BaseMessage]] = None,
        sort: typing.Optional[MessageSort] = None,
        nearby: typing.Optional[ULIDOr[BaseMessage]] = None,
        populate_users: typing.Optional[bool] = None,
    ) -> list[Message]:
        """|coro|

        Retrieve message history from destination channel.

        You must have :attr:`~stoat.Permissions.read_message_history` to do this.

        Parameters
        ----------
        channel_http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides for getting channel.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        limit: Optional[:class:`int`]
            The maximum number of messages to get. Must be between 1 and 100. Defaults to 50.

            If ``nearby`` is provided, then this is ``(limit + 2)``.
        before: Optional[ULIDOr[:class:`~stoat.BaseMessage`]]
            The message before which messages should be fetched.
        after: Optional[ULIDOr[:class:`~stoat.BaseMessage`]]
            The message after which messages should be fetched.
        sort: Optional[:class:`~stoat.MessageSort`]
            The message sort direction. Defaults to :attr:`~stoat.MessageSort.latest`
        nearby: Optional[ULIDOr[:class:`~stoat.BaseMessage`]]
            The message to search around.

            Providing this parameter will discard ``before``, ``after`` and ``sort`` parameters.

            It will also take half of limit rounded as the limits to each side. It also fetches the message specified.
        populate_users: :class:`bool`
            Whether to populate user (and member, if server channel) objects.

        Raises
        ------
        :class:`~stoat.Unauthorized`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`~stoat.Forbidden`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +-----------------------+---------------------------------------------------------------------+
            | Value                 | Reason                                                              |
            +-----------------------+---------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to read the message history. |
            +-----------------------+---------------------------------------------------------------------+
        :class:`~stoat.NotFound`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The channel was not found. |
            +--------------+----------------------------+
        :class:`~stoat.InternalServerError`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                              |
            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~stoat.HTTPException.collection`, :attr:`~stoat.HTTPException.operation` |
            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+

        Returns
        -------
        List[:class:`~stoat.Message`]
            The messages retrieved.
        """
        channel = await self.fetch_channel_id(http_overrides=channel_http_overrides)
        return await self.state.http.get_messages(
            channel,
            http_overrides=http_overrides,
            limit=limit,
            before=before,
            after=after,
            sort=sort,
            nearby=nearby,
            populate_users=populate_users,
        )

    async def search(
        self,
        query: typing.Optional[str] = None,
        *,
        channel_http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        pinned: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        before: typing.Optional[ULIDOr[BaseMessage]] = None,
        after: typing.Optional[ULIDOr[BaseMessage]] = None,
        sort: typing.Optional[MessageSort] = None,
        populate_users: typing.Optional[bool] = None,
    ) -> list[Message]:
        """|coro|

        Searches for messages in destination channel.

        For ``query`` and ``pinned``, only one parameter can be provided, otherwise a :class:`~stoat.HTTPException` will
        be thrown with ``InvalidOperation`` type.

        You must have :attr:`~stoat.Permissions.read_message_history` to do this.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        query: Optional[:class:`str`]
            The full-text search query. See `MongoDB documentation <https://www.mongodb.com/docs/manual/text-search/>`_ for more information.
        channel_http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides for getting channel.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        pinned: Optional[:class:`bool`]
            Whether to search for (un-)pinned messages or not.
        limit: Optional[:class:`int`]
            The maximum number of messages to get. Must be between 1 and 100. Defaults to 50.

            If ``nearby`` is provided, then this is ``(limit + 2)``.
        before: Optional[ULIDOr[:class:`~stoat.BaseMessage`]]
            The message before which messages should be fetched.
        after: Optional[ULIDOr[:class:`~stoat.BaseMessage`]]
            The message after which messages should be fetched.
        sort: Optional[:class:`~stoat.MessageSort`]
            The message sort direction. Defaults to :attr:`~stoat.MessageSort.latest`
        nearby: Optional[ULIDOr[:class:`~stoat.BaseMessage`]]
            The message to search around.

            Providing this parameter will discard ``before``, ``after`` and ``sort`` parameters.

            It will also take half of limit rounded as the limits to each side. It also fetches the message specified.
        populate_users: :class:`bool`
            Whether to populate user (and member, if server channel) objects.

        Raises
        ------
        :class:`~stoat.HTTPException`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +----------------------+-------------------------------------------------------------------------+
            | Value                | Reason                                                                  |
            +----------------------+-------------------------------------------------------------------------+
            | ``FailedValidation`` | One of ``before``, ``after`` or ``nearby`` parameters were invalid IDs. |
            +----------------------+-------------------------------------------------------------------------+
            | ``InvalidOperation`` | You provided both ``query`` and ``pinned`` parameters.                  |
            +----------------------+-------------------------------------------------------------------------+
            | ``IsBot``            | The current token belongs to bot account.                               |
            +----------------------+-------------------------------------------------------------------------+
        :class:`~stoat.Unauthorized`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`~stoat.Forbidden`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +-----------------------+------------------------------------------------------------+
            | Value                 | Reason                                                     |
            +-----------------------+------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to search messages. |
            +-----------------------+------------------------------------------------------------+
        :class:`~stoat.NotFound`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The channel was not found. |
            +--------------+----------------------------+
        :class:`~stoat.InternalServerError`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                              |
            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~stoat.HTTPException.collection`, :attr:`~stoat.HTTPException.operation` |
            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+

        Returns
        -------
        List[:class:`~stoat.Message`]
            The messages matched.
        """

        state = self._get_state()
        channel_id = await self.fetch_channel_id(http_overrides=channel_http_overrides)

        return await state.http.search_for_messages(
            channel_id,
            query=query,
            http_overrides=http_overrides,
            pinned=pinned,
            limit=limit,
            before=before,
            after=after,
            sort=sort,
            populate_users=populate_users,
        )

    async def send(
        self,
        content: typing.Optional[str] = None,
        *,
        channel_http_overrides: typing.Optional[HTTPOverrideOptions] = None,
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

        Sends a message to destination channel.

        You must have :attr:`~stoat.Permissions.send_messages` to do this.

        If message mentions "\\@everyone" or "\\@online", you must have :attr:`~stoat.Permissions.mention_everyone` to do that.

        If message mentions any roles, you must :attr:`~stoat.Permission.mention_roles` to do that.

        Fires :class:`MessageCreateEvent` and optionally :class:`MessageAppendEvent`, both for all users who can see destination channel.

        Parameters
        ----------
        content: Optional[:class:`str`]
            The message content.
        channel_http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides for getting channel.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        nonce: Optional[:class:`str`]
            The message nonce.
        attachments: Optional[List[:class:`~stoat.ResolvableResource`]]
            The attachments to send the message with.

            You must have :attr:`~stoat.Permissions.upload_files` to provide this.
        replies: Optional[List[Union[:class:`Reply`, ULIDOr[:class:`~stoat.BaseMessage`]]]]
            The message replies.
        embeds: Optional[List[:class:`~stoat.SendableEmbed`]]
            The embeds to send the message with.

            You must have :attr:`~stoat.Permissions.send_embeds` to provide this.
        masquerade: Optional[:class:`~stoat.MessageMasquerade`]
            The message masquerade.

            You must have :attr:`~stoat.Permissions.use_masquerade` to provide this.

            If :attr:`~stoat.MessageMasquerade.color` is provided, :attr:`~Permissions.use_masquerade` is also required.
        interactions: Optional[:class:`~stoat.MessageInteractions`]
            The message interactions.

            If :attr:`~stoat.MessageInteractions.reactions` is provided, :attr:`~stoat.Permissions.react` is required.
        silent: Optional[:class:`bool`]
            Whether to suppress notifications or not.
        mention_everyone: Optional[:class:`bool`]
            Whether to mention all users who can see the channel. This cannot be mixed with ``mention_online`` parameter.

            .. note::

                User accounts cannot set this to ``True``.
        mention_online: Optional[:class:`bool`]
            Whether to mention all users who are online and can see the channel. This cannot be mixed with ``mention_everyone`` parameter.

            .. note::

                User accounts cannot set this to ``True``.

        Raises
        ------
        :class:`stoat.HTTPException`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +------------------------+----------------------------------------------------------------------------------------------------------------------------------+
            | Value                  | Reason                                                                                                                           |
            +------------------------+----------------------------------------------------------------------------------------------------------------------------------+
            | ``EmptyMessage``       | The message was empty.                                                                                                           |
            +------------------------+----------------------------------------------------------------------------------------------------------------------------------+
            | ``FailedValidation``   | The payload was invalid.                                                                                                         |
            +------------------------+----------------------------------------------------------------------------------------------------------------------------------+
            | ``InvalidFlagValue``   | Both ``mention_everyone`` and ``mention_online`` were ``True``.                                                                  |
            +------------------------+----------------------------------------------------------------------------------------------------------------------------------+
            | ``InvalidOperation``   | The passed nonce was already used. One of :attr:`~stoat.MessageInteractions.reactions` elements was invalid.                    |
            +------------------------+----------------------------------------------------------------------------------------------------------------------------------+
            | ``InvalidProperty``    | :attr:`~stoat.MessageInteractions.restrict_reactions` was ``True`` but :attr:`~stoat.MessageInteractions.reactions` was empty. |
            +------------------------+----------------------------------------------------------------------------------------------------------------------------------+
            | ``IsBot``              | The current token belongs to bot account.                                                                                        |
            +------------------------+----------------------------------------------------------------------------------------------------------------------------------+
            | ``IsNotBot``           | The current token belongs to user account.                                                                                       |
            +------------------------+----------------------------------------------------------------------------------------------------------------------------------+
            | ``PayloadTooLarge``    | The message was too large.                                                                                                       |
            +------------------------+----------------------------------------------------------------------------------------------------------------------------------+
            | ``TooManyAttachments`` | You provided more attachments than allowed on this instance.                                                                     |
            +------------------------+----------------------------------------------------------------------------------------------------------------------------------+
            | ``TooManyEmbeds``      | You provided more embeds than allowed on this instance.                                                                          |
            +------------------------+----------------------------------------------------------------------------------------------------------------------------------+
            | ``TooManyReplies``     | You were replying to more messages than was allowed on this instance.                                                            |
            +------------------------+----------------------------------------------------------------------------------------------------------------------------------+
        :class:`~stoat.Unauthorized`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`~stoat.Forbidden`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +-----------------------+----------------------------------------------------------+
            | Value                 | Reason                                                   |
            +-----------------------+----------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to send messages. |
            +-----------------------+----------------------------------------------------------+
        :class:`~stoat.NotFound`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +--------------+---------------------------------------+
            | Value        | Reason                                |
            +--------------+---------------------------------------+
            | ``NotFound`` | The channel/file/reply was not found. |
            +--------------+---------------------------------------+
        :class:`stoat.InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+-------------------------------------------------------+-----------------------------------------------------------------------------------+
            | Value             | Reason                                                | Populated attributes                                                              |
            +-------------------+-------------------------------------------------------+-----------------------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database.        | :attr:`~stoat.HTTPException.collection`, :attr:`~stoat.HTTPException.operation` |
            +-------------------+-------------------------------------------------------+-----------------------------------------------------------------------------------+
            | ``InternalError`` | Somehow something went wrong during message creation. |                                                                                   |
            +-------------------+-------------------------------------------------------+-----------------------------------------------------------------------------------+

        Returns
        -------
        :class:`~stoat.Message`
            The message that was sent.
        """

        state = self._get_state()
        channel_id = await self.fetch_channel_id(http_overrides=channel_http_overrides)

        return await state.http.send_message(
            channel_id,
            content,
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

    def typing(self) -> Typing:
        """Returns an asynchronous context manager that allows you to send a typing indicator in destination channel for an indefinite period of time."""

        return Typing(
            destination=self,
            shard=self._get_state().shard,
        )


class Connectable:
    """An ABC that allows derived instances to connect to voice call.

    The following classes implement this ABC:

    - :class:`DMChannel`
    - :class:`GroupChannel`
    - :class:`TextChannel`
    - :class:`VoiceChannel`
    - :class:`User`
    """

    __slots__ = ()

    state: State

    async def fetch_channel_id(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> str:
        """:class:`str`: Retrieves the channel's ID."""
        return self.get_channel_id()

    def get_channel_id(self) -> str:
        """:class:`str`: Retrieves the channel's ID, if possible."""
        return ''

    async def join_call(
        self,
        *,
        channel_http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        node: UndefinedOr[typing.Optional[str]] = UNDEFINED,
        force_disconnect: UndefinedOr[typing.Optional[bool]] = UNDEFINED,
        recipients: UndefinedOr[typing.Optional[list[ULIDOr[BaseUser]]]] = UNDEFINED,
    ) -> tuple[str, str]:
        """|coro|

        Asks the voice server for a token to join the call in destination channel.

        You must have :attr:`~Permissions.connect` to do this.

        For Livekit instances, fires :class:`MessageCreateEvent` and :class:`VoiceChannelJoinEvent` / :class:`VoiceChannelMoveEvent`
        for all users who can see target channel.

        Parameters
        ----------
        channel_http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides for getting channel.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        node: UndefinedOr[Optional[:class:`str`]]
            The node's name to use for starting a call.

            Can be ``None`` to tell server choose the node automatically.
        force_disconnect: UndefinedOr[Optional[:class:`bool`]]
            Whether to force disconnect any other existing voice connections.
            Useful for disconnecting on another device and joining on a new.

            .. versionadded:: 1.2
        recipients: UndefinedOr[Optional[List[ULIDOr[:class:`BaseUser`]]]]
            A list of users which should be notified of the call starting.
            Only used when the user is the first one connected.

            .. versionadded:: 1.2

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | Value                  | Reason                                                                                                                            |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | ``AlreadyConnected``   | The current user was already connected to this voice channel.                                                                     |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | ``CannotJoinCall``     | The channel was type of :attr:`~ChannelType.saved_messages` (or if instance uses legacy voice server, :attr:`~ChannelType.text`). |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | ``InvalidOperation``   | The voice server is unavailable.                                                                                                  |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | ``LivekitUnavailable`` | The voice server is unavailable. Only applicable to instances using Livekit.                                                      |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | ``NotConnected``       | The current user was already connected to other voice channel.                                                                    |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | ``NotAVoiceChannel``   | ???. Only applicable to instances using Livekit                                                                                   |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | ``VosoUnavailable``    | The voice server is unavailable. Not applicable to instances using Livekit.                                                       |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------------------+--------------------------------------------------------+
            | Value                            | Reason                                                 |
            +----------------------------------+--------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to join a call. |
            +----------------------------------+--------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The channel was not found. |
            +--------------+----------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+-------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                          | Populated attributes                                                |
            +-------------------+-------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database.  | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+-------------------------------------------------+---------------------------------------------------------------------+
            | ``InternalError`` | Somehow something went during retrieving token. |                                                                     |
            +-------------------+-------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        Tuple[:class:`str`, :class:`str`]
            The token for authenticating with the voice server, and node WebSocket URL (can be empty if instance does not use Livekit).
        """

        channel_id = await self.fetch_channel_id(http_overrides=channel_http_overrides)
        state = self.state

        return await state.http.join_call(
            channel_id,
            http_overrides=http_overrides,
            node=node,
            force_disconnect=force_disconnect,
            recipients=recipients,
        )

    async def connect(
        self,
        *,
        channel_http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        node: typing.Optional[str] = None,
    ) -> Room:
        """Connects to a destination voice channel and returns a `Room <https://docs.livekit.io/python/livekit/rtc/room.html#livekit.rtc.room.Room>`_ associated with destination.

        Parameters
        ----------
        channel_http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides for getting channel.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        node: Optional[:class:`str`]
            The node's name to use for starting a call.

            Defaults to ``None``, which tells server choose the node automatically.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | Value                  | Reason                                                                                                                            |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | ``AlreadyConnected``   | The current user was already connected to this voice channel.                                                                     |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | ``CannotJoinCall``     | The channel was type of :attr:`~ChannelType.saved_messages` (or if instance uses legacy voice server, :attr:`~ChannelType.text`). |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | ``InvalidOperation``   | The voice server is unavailable.                                                                                                  |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | ``LivekitUnavailable`` | The voice server is unavailable. Only applicable to instances using Livekit.                                                      |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | ``NotConnected``       | The current user was already connected to other voice channel.                                                                    |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | ``NotAVoiceChannel``   | ???. Only applicable to instances using Livekit                                                                                   |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
            | ``VosoUnavailable``    | The voice server is unavailable. Not applicable to instances using Livekit.                                                       |
            +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------------------+--------------------------------------------------------+
            | Value                            | Reason                                                 |
            +----------------------------------+--------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to join a call. |
            +----------------------------------+--------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The channel was not found. |
            +--------------+----------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+-------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                          | Populated attributes                                                |
            +-------------------+-------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database.  | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+-------------------------------------------------+---------------------------------------------------------------------+
            | ``InternalError`` | Somehow something went during retrieving token. |                                                                     |
            +-------------------+-------------------------------------------------+---------------------------------------------------------------------+
        :class:`TypeError`
            If livekit dependency is not installed.
        """

        try:
            from livekit.rtc import Room  # type: ignore
        except ImportError:
            raise TypeError('Livekit is unavailable') from None
        else:
            channel_id = await self.fetch_channel_id(http_overrides=channel_http_overrides)

            state = self.state

            room = Room()
            token, url = await state.http.join_call(channel_id, http_overrides=http_overrides, node=node)

            await room.connect(url, token)
            return room


__all__ = (
    'Messageable',
    'Connectable',
)
