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

import asyncio
import builtins
from inspect import isawaitable, signature
import logging
import typing

import aiohttp

from . import utils
from .cache import (
    CacheContextType,
    ClientCacheContext,
    _CHANNELS_THROUGH_CLIENT_GETTER,
    _EMOJIS_THROUGH_CLIENT_GETTER,
    _SERVER_MEMBERS_THROUGH_CLIENT_GETTER,
    _READ_STATES_THROUGH_CLIENT_GETTER,
    _SERVERS_THROUGH_CLIENT_GETTER,
    _USERS_THROUGH_CLIENT_GETTER,
    _VOICE_STATES_THROUGH_CLIENT_GETTER,
    _USER_IDS_THROUGH_CLIENT_DM_CHANNELS,
    _CHANNELS_THROUGH_CLIENT_DM_CHANNELS,
    _CHANNELS_THROUGH_CLIENT_PRIVATE_CHANNELS,
    _CHANNEL_THROUGH_CLIENT_GETTER,
    _EMOJI_THROUGH_CLIENT_GETTER,
    _READ_STATE_THROUGH_CLIENT_GETTER,
    _SERVER_THROUGH_CLIENT_GETTER,
    _USER_THROUGH_CLIENT_GETTER,
    Cache,
    MapCache,
)
from .cdn import CDNClient
from .channel import (
    SavedMessagesChannel,
    DMChannel,
    GroupChannel,
    Channel,
    ChannelVoiceStateContainer,
    PartialMessageable,
)
from .core import (
    UNDEFINED,
    UndefinedOr,
    ULIDOr,
)
from .emoji import Emoji
from .events import BaseEvent
from .http import HTTPOverrideOptions, HTTPClient
from .parser import Parser
from .server import BaseServer, Server, Member
from .shard import EventHandler, Shard, ShardImpl
from .state import State
from .user import BaseUser, User, OwnUser


if typing.TYPE_CHECKING:
    from collections.abc import Callable, Coroutine, Generator, Mapping
    from types import TracebackType
    from typing_extensions import Self

    from . import raw
    from .adapter import HTTPWebSocket
    from .cdn import ResolvableResource
    from .events import (
        AuthenticatedEvent,
        AuthifierEvent,
        BaseChannelCreateEvent,
        BaseEvent,
        MessageDeleteBulkEvent,
        ChannelDeleteEvent,
        ChannelUpdateEvent,
        GroupRecipientAddEvent,
        GroupRecipientRemoveEvent,
        ChannelStartTypingEvent,
        ChannelStopTypingEvent,
        MessageStartEditingEvent,
        MessageStopEditingEvent,
        LogoutEvent,
        MessageAckEvent,
        MessageAppendEvent,
        MessageClearReactionEvent,
        MessageCreateEvent,
        MessageDeleteEvent,
        MessageReactEvent,
        MessageUnreactEvent,
        MessageUpdateEvent,
        PrivateChannelCreateEvent,
        RawServerRoleUpdateEvent,
        ReadyEvent,
        ReportCreateEvent,
        ServerChannelCreateEvent,
        ServerCreateEvent,
        ServerDeleteEvent,
        ServerEmojiCreateEvent,
        ServerEmojiDeleteEvent,
        ServerMemberJoinEvent,
        ServerMemberRemoveEvent,
        ServerMemberUpdateEvent,
        ServerRoleDeleteEvent,
        ServerRoleRanksUpdateEvent,
        ServerUpdateEvent,
        SessionCreateEvent,
        SessionDeleteAllEvent,
        SessionDeleteEvent,
        UserPlatformWipeEvent,
        UserRelationshipUpdateEvent,
        UserSettingsUpdateEvent,
        UserUpdateEvent,
        WebhookCreateEvent,
        WebhookDeleteEvent,
        WebhookUpdateEvent,
        BeforeConnectEvent,
        AfterConnectEvent,
        VoiceChannelJoinEvent,
        VoiceChannelLeaveEvent,
        VoiceChannelMoveEvent,
        UserVoiceStateUpdateEvent,
    )
    from .message import Message
    from .read_state import ReadState
    from .settings import UserSettings


_L = logging.getLogger(__name__)


def _session_factory(_) -> aiohttp.ClientSession:
    return aiohttp.ClientSession()


class ClientEventHandler(EventHandler):
    """The default event handler for the client.

    Attributes
    ----------
    client: :class:`Client`
        The client the event handler is for.
    state: :class:`State`
        The client's state.
    dispatch: Callable[[:class:`BaseEvent`], :class:``asyncio.Task`]
        Alias for :meth:`.Client.dispatch`.
    handlers: Dict[:class:`str`, Callable[..., MaybeAwaitable[None]]]
        The handlers.

    Parameters
    ----------
    client: :class:`Client`
        The client.
    """

    __slots__ = (
        'client',
        'state',
        'dispatch',
        'handlers',
    )

    def __init__(self, client: Client) -> None:
        self.client: Client = client
        self.state: State = client.state
        self.dispatch: Callable[[BaseEvent], asyncio.Task[None]] = client.dispatch
        self.handlers: dict[str, Callable[..., utils.MaybeAwaitable[None]]] = {
            'Bulk': self.handle_bulk,
            'Authenticated': self.handle_authenticated,
            'Logout': self.handle_logout,
            'Ready': self.handle_ready,
            'Pong': self.handle_pong,
            'Message': self.handle_message,
            'MessageUpdate': self.handle_message_update,
            'MessageAppend': self.handle_message_append,
            'MessageDelete': self.handle_message_delete,
            'MessageReact': self.handle_message_react,
            'MessageUnreact': self.handle_message_unreact,
            'MessageRemoveReaction': self.handle_message_remove_reaction,
            'BulkMessageDelete': self.handle_bulk_message_delete,
            'ServerCreate': self.handle_server_create,
            'ServerUpdate': self.handle_server_update,
            'ServerDelete': self.handle_server_delete,
            'ServerMemberJoin': self.handle_server_member_join,
            'ServerMemberUpdate': self.handle_server_member_update,
            'ServerMemberLeave': self.handle_server_member_leave,
            'ServerRoleUpdate': self.handle_server_role_update,
            'ServerRoleDelete': self.handle_server_role_delete,
            'ServerRoleRanksUpdate': self.handle_server_role_ranks_update,
            'UserUpdate': self.handle_user_update,
            'UserRelationship': self.handle_user_relationship,
            'UserSettingsUpdate': self.handle_user_settings_update,
            'UserPlatformWipe': self.handle_user_platform_wipe,
            'EmojiCreate': self.handle_emoji_create,
            'EmojiDelete': self.handle_emoji_delete,
            'ReportCreate': self.handle_report_create,
            'ChannelCreate': self.handle_channel_create,
            'ChannelUpdate': self.handle_channel_update,
            'ChannelDelete': self.handle_channel_delete,
            'ChannelGroupJoin': self.handle_channel_group_join,
            'ChannelGroupLeave': self.handle_channel_group_leave,
            'ChannelStartTyping': self.handle_channel_start_typing,
            'ChannelStopTyping': self.handle_channel_stop_typing,
            'MessageStartEditing': self.handle_message_start_editing,
            'MessageStopEditing': self.handle_message_stop_editing,
            'ChannelAck': self.handle_channel_ack,
            'WebhookCreate': self.handle_webhook_create,
            'WebhookUpdate': self.handle_webhook_update,
            'WebhookDelete': self.handle_webhook_delete,
            'Auth': self.handle_auth,
            'VoiceChannelJoin': self.handle_voice_channel_join,
            'VoiceChannelLeave': self.handle_voice_channel_leave,
            'VoiceChannelMove': self.handle_voice_channel_move,
            'UserVoiceStateUpdate': self.handle_user_voice_state_update,
            'UserMoveVoiceChannel': self.handle_user_move_voice_channel,
        }

    async def handle_bulk(self, shard: Shard, payload: raw.ClientBulkEvent, /) -> None:
        """Handle ``Bulk`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        for v in payload['v']:
            await self.handle(shard, v)

    def handle_authenticated(self, shard: Shard, payload: raw.ClientAuthenticatedEvent, /) -> None:
        """Handle ``Authenticated`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        self.dispatch(self.state.parser.parse_authenticated_event(shard, payload))

    def handle_logout(self, shard: Shard, payload: raw.ClientLogoutEvent, /) -> None:
        """Handle ``Logout`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        self.dispatch(self.state.parser.parse_logout_event(shard, payload))

    def handle_ready(self, shard: Shard, payload: raw.ClientReadyEvent, /) -> None:
        """Handle ``Ready`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_ready_event(shard, payload)
        self.dispatch(event)

    def handle_pong(self, shard: Shard, payload: raw.ClientPongEvent, /) -> None:
        pass

    def handle_message(self, shard: Shard, payload: raw.ClientMessageEvent, /) -> None:
        """Handle ``Message`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_message_event(shard, payload)
        self.dispatch(event)

    def handle_message_update(self, shard: Shard, payload: raw.ClientMessageUpdateEvent, /) -> None:
        """Handle ``MessageUpdate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_message_update_event(shard, payload)
        self.dispatch(event)

    def handle_message_append(self, shard: Shard, payload: raw.ClientMessageAppendEvent, /) -> None:
        """Handle ``MessageAppend`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_message_append_event(shard, payload)
        self.dispatch(event)

    def handle_message_delete(self, shard: Shard, payload: raw.ClientMessageDeleteEvent, /) -> None:
        """Handle ``MessageDelete`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_message_delete_event(shard, payload)
        self.dispatch(event)

    def handle_message_react(self, shard: Shard, payload: raw.ClientMessageReactEvent, /) -> None:
        """Handle ``MessageReact`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_message_react_event(shard, payload)
        self.dispatch(event)

    def handle_message_unreact(self, shard: Shard, payload: raw.ClientMessageUnreactEvent, /) -> None:
        """Handle ``MessageUnreact`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_message_unreact_event(shard, payload)
        self.dispatch(event)

    def handle_message_remove_reaction(self, shard: Shard, payload: raw.ClientMessageRemoveReactionEvent, /) -> None:
        """Handle ``MessageRemoveReaction`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_message_remove_reaction_event(shard, payload)
        self.dispatch(event)

    def handle_bulk_message_delete(self, shard: Shard, payload: raw.ClientBulkMessageDeleteEvent, /) -> None:
        """Handle ``BulkMessageDelete`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_bulk_message_delete_event(shard, payload)
        self.dispatch(event)

    def handle_server_create(self, shard: Shard, payload: raw.ClientServerCreateEvent, /) -> None:
        """Handle ``ServerCreate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        joined_at = utils.utcnow()
        event = self.state.parser.parse_server_create_event(shard, payload, joined_at)
        self.dispatch(event)

    def handle_server_update(self, shard: Shard, payload: raw.ClientServerUpdateEvent, /) -> None:
        """Handle ``ServerUpdate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_server_update_event(shard, payload)
        self.dispatch(event)

    def handle_server_delete(self, shard: Shard, payload: raw.ClientServerDeleteEvent, /) -> None:
        """Handle ``ServerDelete`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_server_delete_event(shard, payload)
        self.dispatch(event)

    def handle_server_member_join(self, shard: Shard, payload: raw.ClientServerMemberJoinEvent, /) -> None:
        """Handle ``ServerMemberJoin`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        joined_at = utils.utcnow()
        event = self.state.parser.parse_server_member_join_event(shard, payload, joined_at)
        self.dispatch(event)

    def handle_server_member_update(self, shard: Shard, payload: raw.ClientServerMemberUpdateEvent, /) -> None:
        """Handle ``ServerMemberUpdate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_server_member_update_event(shard, payload)
        self.dispatch(event)

    def handle_server_member_leave(self, shard: Shard, payload: raw.ClientServerMemberLeaveEvent, /) -> None:
        """Handle ``ServerMemberLeave`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_server_member_leave_event(shard, payload)
        self.dispatch(event)

    def handle_server_role_update(self, shard: Shard, payload: raw.ClientServerRoleUpdateEvent, /) -> None:
        """Handle ``ServerRoleUpdate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_server_role_update_event(shard, payload)
        self.dispatch(event)

    def handle_server_role_delete(self, shard: Shard, payload: raw.ClientServerRoleDeleteEvent, /) -> None:
        """Handle ``ServerRoleDelete`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_server_role_delete_event(shard, payload)
        self.dispatch(event)

    def handle_server_role_ranks_update(self, shard: Shard, payload: raw.ClientServerRoleRanksUpdateEvent, /) -> None:
        """Handle ``ServerRoleRanksUpdate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_server_role_ranks_update_event(shard, payload)
        self.dispatch(event)

    def handle_user_update(self, shard: Shard, payload: raw.ClientUserUpdateEvent, /) -> None:
        """Handle ``UserUpdate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_user_update_event(shard, payload)
        self.dispatch(event)

    def handle_user_relationship(self, shard: Shard, payload: raw.ClientUserRelationshipEvent, /) -> None:
        """Handle ``UserRelationship`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_user_relationship_event(shard, payload)
        self.dispatch(event)

    def handle_user_settings_update(self, shard: Shard, payload: raw.ClientUserSettingsUpdateEvent, /) -> None:
        """Handle ``UserSettingsUpdate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_user_settings_update_event(shard, payload)
        self.dispatch(event)

    def handle_user_platform_wipe(self, shard: Shard, payload: raw.ClientUserPlatformWipeEvent, /) -> None:
        """Handle ``UserPlatformWipe`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_user_platform_wipe_event(shard, payload)
        self.dispatch(event)

    def handle_emoji_create(self, shard: Shard, payload: raw.ClientEmojiCreateEvent, /) -> None:
        """Handle ``EmojiCreate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_emoji_create_event(shard, payload)
        self.dispatch(event)

    def handle_emoji_delete(self, shard: Shard, payload: raw.ClientEmojiDeleteEvent, /) -> None:
        """Handle ``EmojiDelete`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_emoji_delete_event(shard, payload)
        self.dispatch(event)

    def handle_report_create(self, shard: Shard, payload: raw.ClientReportCreateEvent, /) -> None:
        """Handle ``ReportCreate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_report_create_event(shard, payload)
        self.dispatch(event)

    def handle_channel_create(self, shard: Shard, payload: raw.ClientChannelCreateEvent, /) -> None:
        """Handle ``ChannelCreate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_channel_create_event(shard, payload)
        self.dispatch(event)

    def handle_channel_update(self, shard: Shard, payload: raw.ClientChannelUpdateEvent, /) -> None:
        """Handle ``ChannelUpdate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_channel_update_event(shard, payload)
        self.dispatch(event)

    def handle_channel_delete(self, shard: Shard, payload: raw.ClientChannelDeleteEvent, /) -> None:
        """Handle ``ChannelDelete`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_channel_delete_event(shard, payload)
        self.dispatch(event)

    def handle_channel_group_join(self, shard: Shard, payload: raw.ClientChannelGroupJoinEvent, /) -> None:
        """Handle ``ChannelGroupJoin`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_channel_group_join_event(shard, payload)
        self.dispatch(event)

    def handle_channel_group_leave(self, shard: Shard, payload: raw.ClientChannelGroupLeaveEvent, /) -> None:
        """Handle ``ChannelGroupLeave`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_channel_group_leave_event(shard, payload)
        self.dispatch(event)

    def handle_channel_start_typing(self, shard: Shard, payload: raw.ClientChannelStartTypingEvent, /) -> None:
        """Handle ``ChannelStartTyping`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_channel_start_typing_event(shard, payload)
        self.dispatch(event)

    def handle_channel_stop_typing(self, shard: Shard, payload: raw.ClientChannelStopTypingEvent, /) -> None:
        """Handle ``ChannelStopTyping`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_channel_stop_typing_event(shard, payload)
        self.dispatch(event)

    def handle_message_start_editing(self, shard: Shard, payload: raw.ClientMessageStartEditingEvent, /) -> None:
        """Handle ``MessageStartEditing`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_message_start_edting(shard, payload)
        self.dispatch(event)

    def handle_message_stop_editing(self, shard: Shard, payload: raw.ClientMessageStopEditingEvent, /) -> None:
        """Handle ``MessageStopEditing`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_message_stop_edting(shard, payload)
        self.dispatch(event)

    def handle_channel_ack(self, shard: Shard, payload: raw.ClientChannelAckEvent, /) -> None:
        """Handle ``ChannelAck`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_channel_ack_event(shard, payload)
        self.dispatch(event)

    def handle_webhook_create(self, shard: Shard, payload: raw.ClientWebhookCreateEvent, /) -> None:
        """Handle ``WebhookCreate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_webhook_create_event(shard, payload)
        self.dispatch(event)

    def handle_webhook_update(self, shard: Shard, payload: raw.ClientWebhookUpdateEvent, /) -> None:
        """Handle ``WebhookUpdate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_webhook_update_event(shard, payload)
        self.dispatch(event)

    def handle_webhook_delete(self, shard: Shard, payload: raw.ClientWebhookDeleteEvent, /) -> None:
        """Handle ``WebhookDelete`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_webhook_delete_event(shard, payload)
        self.dispatch(event)

    def handle_auth(self, shard: Shard, payload: raw.ClientAuthEvent, /) -> None:
        """Handle ``Auth`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_auth_event(shard, payload)
        self.dispatch(event)

    def handle_voice_channel_join(self, shard: Shard, payload: raw.ClientVoiceChannelJoinEvent, /) -> None:
        """Handle ``VoiceChannelJoin`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_voice_channel_join_event(shard, payload)
        self.dispatch(event)

    def handle_voice_channel_leave(self, shard: Shard, payload: raw.ClientVoiceChannelLeaveEvent, /) -> None:
        """Handle ``VoiceChannelLeave`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_voice_channel_leave_event(shard, payload)
        self.dispatch(event)

    def handle_voice_channel_move(self, shard: Shard, payload: raw.ClientVoiceChannelMoveEvent, /) -> None:
        """Handle ``VoiceChannelMove`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_voice_channel_move_event(shard, payload)
        self.dispatch(event)

    def handle_user_voice_state_update(self, shard: Shard, payload: raw.ClientUserVoiceStateUpdateEvent, /) -> None:
        """Handle ``UserVoiceStateUpdate`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_user_voice_state_update_event(shard, payload)
        self.dispatch(event)

    def handle_user_move_voice_channel(self, shard: Shard, payload: raw.ClientUserMoveVoiceChannelEvent, /) -> None:
        """Handle ``UserMoveVoiceChannel`` WebSocket event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        event = self.state.parser.parse_user_move_voice_channel_event(shard, payload)
        self.dispatch(event)

    async def _handle_library_error(self, shard: Shard, payload: raw.ClientEvent, exc: Exception, name: str, /) -> None:
        try:
            r = self.client.on_library_error(shard, payload, exc)
            if isawaitable(r):
                await r
        except Exception:
            _L.exception('on_library_error (task: %s) raised an exception', name)

    async def handle(self, shard: Shard, payload: raw.ClientEvent, /) -> None:
        """Handle a WebSocket event, depending on value of ``type`` in ``payload``.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        type = payload['type']
        try:
            handler = self.handlers[type]
        except KeyError:
            _L.debug('Received unknown event: %s. Discarding.', type)
        else:
            _L.debug('Handling %s', type)
            try:
                r = handler(shard, payload)
                if isawaitable(r):
                    await r
            except Exception as exc:
                if type == 'Ready':
                    # This is fatal
                    raise

                _L.exception('%s handler raised an exception', type)

                name = f'stoat.py-dispatch-{self.client._get_i()}'
                asyncio.create_task(self._handle_library_error(shard, payload, exc, name), name=name)

    def handle_raw(self, shard: Shard, payload: raw.ClientEvent, /) -> utils.MaybeAwaitable[None]:
        return self.handle(shard, payload)

    def before_connect(self, shard: Shard, /) -> utils.MaybeAwaitable[None]:
        from .events import BeforeConnectEvent

        return self.dispatch(BeforeConnectEvent(shard=shard))

    def after_connect(self, shard: Shard, socket: HTTPWebSocket, /) -> utils.MaybeAwaitable[None]:
        from .events import AfterConnectEvent

        return self.dispatch(AfterConnectEvent(shard=shard, socket=socket))


# OOP in Python sucks.
ClientT = typing.TypeVar('ClientT', bound='Client')
EventT = typing.TypeVar('EventT', bound='BaseEvent')


def _parents_of(type: type[BaseEvent], /) -> tuple[type[BaseEvent], ...]:
    """Tuple[Type[:class:`BaseEvent`], ...]: Returns parents of BaseEvent, including BaseEvent itself."""
    if type is BaseEvent:
        return (BaseEvent,)
    tmp: typing.Any = type.__mro__[:-1]
    return tmp


class EventSubscription(typing.Generic[EventT]):
    """Represents an event subscription.

    Attributes
    ----------
    client: :class:`Client`
        The client that this subscription is tied to.
    id: :class:`int`
        The ID of the subscription.
    callback: MaybeAwaitableFunc[[EventT], None]
        The callback.
    """

    __slots__ = (
        'client',
        'id',
        'callback',
        'event',
    )

    def __init__(
        self,
        *,
        client: Client,
        id: int,
        callback: utils.MaybeAwaitableFunc[[EventT], None],
        event: type[EventT],
    ) -> None:
        self.client: Client = client
        self.id: int = id
        self.callback: utils.MaybeAwaitableFunc[[EventT], None] = callback
        self.event: type[EventT] = event

    def __call__(self, arg: EventT, /) -> utils.MaybeAwaitable[None]:
        return self.callback(arg)

    async def _handle(self, arg: EventT, name: str, /) -> None:
        await self.client._run_callback(self.callback, arg, name)

    def remove(self) -> None:
        """Removes the event subscription."""
        self.client._handlers[self.event][0].pop(self.id, None)


class TemporarySubscription(typing.Generic[EventT]):
    """Represents a temporary event subscription."""

    __slots__ = (
        'client',
        'id',
        'event',
        'future',
        'check',
        'coro',
        'manual_process',
        'stop_dispatching_on_success',
    )

    def __init__(
        self,
        *,
        client: Client,
        id: int,
        event: type[EventT],
        future: asyncio.Future[EventT],
        check: Callable[[EventT], utils.MaybeAwaitable[bool]],
        coro: Coroutine[typing.Any, typing.Any, EventT],
        manual_process: bool = False,
        stop_dispatching_on_success: bool = True,
    ) -> None:
        self.client: Client = client
        self.id: int = id
        self.event: type[EventT] = event
        self.future: asyncio.Future[EventT] = future
        self.check: Callable[[EventT], utils.MaybeAwaitable[bool]] = check
        self.coro: Coroutine[typing.Any, typing.Any, EventT] = coro
        self.manual_process: bool = manual_process
        self.stop_dispatching_on_success: bool = stop_dispatching_on_success

    def __await__(self) -> Generator[typing.Any, typing.Any, EventT]:
        return self.coro.__await__()

    async def _handle(self, arg: EventT, name: str, /) -> bool:
        try:
            can = self.check(arg)
            if isawaitable(can):
                can = await can

            if can:
                try:
                    self.future.set_result(arg)
                except asyncio.InvalidStateError:
                    # Sometimes self.future is already done and we somehow get here. That might
                    # be just a race condition, but I am not sure yet. For now, ignore the error and return True.
                    pass
            return can
        except Exception as exc:
            try:
                self.future.set_exception(exc)
            except asyncio.InvalidStateError:
                pass
            _L.exception('Checker function (task: %s) raised an exception', name)
            return True

    def cancel(self) -> None:
        """Cancels the subscription."""
        self.future.cancel()
        self.client._handlers[self.event][1].pop(self.id, None)


class TemporarySubscriptionListIterator(typing.Generic[EventT]):
    __slots__ = ('subscription',)

    def __init__(self, *, subscription: TemporarySubscriptionList[EventT]) -> None:
        self.subscription: TemporarySubscriptionList[EventT] = subscription

    async def __anext__(self) -> EventT:
        subscription = self.subscription

        if subscription.exception is not None:
            raise subscription.exception

        if subscription.done.is_set() and subscription.queue.empty():
            raise StopAsyncIteration

        while True:
            index = await subscription.queue.get()

            if subscription.exception is not None:
                raise subscription.exception

            if index >= 0:
                break

        return subscription.result[index]


class TemporarySubscriptionList(typing.Generic[EventT]):
    """Represents a temporary subscription on multiple events."""

    __slots__ = (
        'client',
        'id',
        'event',
        'done',
        'check',
        'result',
        'exception',
        'expected',
        'queue',
        'manual_process',
        'stop_dispatching_on_success',
    )

    def __init__(
        self,
        *,
        client: Client,
        expected: int,
        id: int,
        event: type[EventT],
        check: Callable[[EventT], utils.MaybeAwaitable[bool]],
        manual_process: bool = False,
        stop_dispatching_on_success: bool = True,
    ) -> None:
        self.client: Client = client
        self.id: int = id
        self.event: type[EventT] = event
        self.done: asyncio.Event = asyncio.Event()
        self.check: Callable[[EventT], utils.MaybeAwaitable[bool]] = check
        self.result: list[EventT] = []
        self.exception: typing.Optional[Exception] = None
        self.expected: int = expected
        self.queue: asyncio.Queue[int] = asyncio.Queue(expected)
        self.manual_process: bool = manual_process
        self.stop_dispatching_on_success: bool = stop_dispatching_on_success

    async def wait(self) -> list[EventT]:
        if len(self.result) < self.expected:
            await self.done.wait()

            if self.exception is not None:
                raise self.exception

            if len(self.result) < self.expected:
                raise asyncio.TimeoutError('Timed out waiting.')

        return self.result

    def __await__(self) -> Generator[typing.Any, typing.Any, list[EventT]]:
        return self.wait().__await__()

    def __aiter__(self) -> TemporarySubscriptionListIterator[EventT]:
        return TemporarySubscriptionListIterator(subscription=self)

    async def _handle(self, arg: EventT, name: str, /) -> bool:
        if self.exception is not None:
            pass

        try:
            can = self.check(arg)
            if isawaitable(can):
                can = await can

            if can:
                if len(self.result) >= self.expected:
                    self.done.set()
                else:
                    self.result.append(arg)
                    if len(self.result) >= self.expected:
                        self.done.set()
                    self.queue.put_nowait(len(self.result) - 1)

            return self.done.is_set()
        except Exception as exc:
            _L.exception('Checker function (task: %s) raised an exception', name)
            self.exception = exc
            self.done.set()
            self.queue.put_nowait(len(self.result) - 1)
            return True

    def cancel(self) -> None:
        """Cancels the subscription."""

        self.done.set()
        self.client._handlers[self.event][1].pop(self.id, None)


_DEFAULT_HANDLERS = ({}, {})


def _private_channel_sort_old(channel: typing.Union[DMChannel, GroupChannel], /) -> str:
    return channel.last_message_id or '0'


def _private_channel_sort_new(channel: typing.Union[DMChannel, GroupChannel], /) -> str:
    return channel.last_message_id or channel.id


class Client:
    """A Stoat client."""

    __slots__ = (
        '_handlers',
        '_i',
        '_state',
        'token',
        '_types',
        'bot',
        'closed',
        'extra',
    )

    @typing.overload
    def __init__(
        self,
        *,
        token: str = '',
        bot: bool = True,
        state: typing.Optional[typing.Union[Callable[[Client], State], State]] = None,
    ) -> None: ...

    @typing.overload
    def __init__(
        self,
        *,
        token: str = '',
        bot: bool = True,
        cache: typing.Union[
            Callable[[Client, State], UndefinedOr[typing.Optional[Cache]]], UndefinedOr[typing.Optional[Cache]]
        ] = UNDEFINED,
        cdn_base: typing.Optional[str] = None,
        cdn_client: typing.Optional[Callable[[Client, State], CDNClient]] = None,
        http_base: typing.Optional[str] = None,
        http: typing.Optional[Callable[[Client, State], HTTPClient]] = None,
        parser: typing.Optional[Callable[[Client, State], Parser]] = None,
        shard: typing.Optional[Callable[[Client, State], Shard]] = None,
        request_user_settings: typing.Optional[list[str]] = None,
        websocket_base: typing.Optional[str] = None,
    ) -> None: ...

    def __init__(
        self,
        *,
        token: str = '',
        bot: bool = True,
        cache: typing.Union[
            Callable[[Client, State], UndefinedOr[typing.Optional[Cache]]], UndefinedOr[typing.Optional[Cache]]
        ] = UNDEFINED,
        cdn_base: typing.Optional[str] = None,
        cdn_client: typing.Optional[Callable[[Client, State], CDNClient]] = None,
        http_base: typing.Optional[str] = None,
        http: typing.Optional[Callable[[Client, State], HTTPClient]] = None,
        parser: typing.Optional[Callable[[Client, State], Parser]] = None,
        shard: typing.Optional[Callable[[Client, State], Shard]] = None,
        state: typing.Optional[typing.Union[Callable[[Client], State], State, None]] = None,
        request_user_settings: typing.Optional[list[str]] = None,
        websocket_base: typing.Optional[str] = None,
    ) -> None:
        self.closed: bool = True
        # {Type[BaseEvent]: List[utils.MaybeAwaitableFunc[[BaseEvent], None]]}
        self._handlers: dict[
            type[BaseEvent],
            tuple[
                dict[int, EventSubscription[BaseEvent]],
                dict[int, typing.Union[TemporarySubscription[BaseEvent], TemporarySubscriptionList[BaseEvent]]],
            ],
        ] = {}
        self._i = 0
        self.token: str = token
        # {Type[BaseEvent]: Tuple[Type[BaseEvent], ...]}
        self._types: dict[type[BaseEvent], tuple[type[BaseEvent], ...]] = {}
        self.bot: bool = bot

        self.extra = {}
        if state:
            if callable(state):
                self._state: State = state(self)
            else:
                self._state = state
        else:
            state = State()

            c = None
            if callable(cache):
                cr = cache(self, state)
            else:
                cr = cache
            c = cr if cr is not UNDEFINED else MapCache()

            if parser:
                state.setup(parser=parser(self, state))
            state.setup(
                cache=c,
                cdn_client=(
                    cdn_client(self, state)
                    if cdn_client
                    else CDNClient(
                        base=cdn_base,
                        state=state,
                    )
                ),
                http=(
                    http(self, state)
                    if http
                    else HTTPClient(
                        token,
                        base=http_base,
                        bot=bot,
                        state=state,
                    )
                ),
            )
            self._state = state
            state.setup(
                shard=(
                    shard(self, state)
                    if shard
                    else ShardImpl(
                        token,
                        base_url=websocket_base,
                        handler=ClientEventHandler(self),
                        request_user_settings=request_user_settings,
                        state=state,
                    )
                )
            )

    def _get_i(self) -> int:
        self._i += 1
        return self._i

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException],
        exc_value: typing.Optional[BaseException],
        traceback: typing.Optional[TracebackType],
        /,
    ) -> None:
        await self.close()

    async def on_user_error(self, event: BaseEvent, /) -> None:
        """Handles user errors that came from handlers.
        You can get current exception being raised via :func:`sys.exc_info`.

        By default, this logs exception.
        """
        _L.exception(
            'One of %s handlers raised an exception',
            event.__class__.__name__,
        )

    async def on_library_error(self, shard: Shard, payload: raw.ClientEvent, exc: Exception, /) -> None:
        """Handles library errors. By default, this logs exception.

        .. note::
            This won't be called if handling ``Ready`` will raise an exception as it is fatal.
        """

        type = payload['type']

        _L.exception('%s handler raised an exception', type, exc_info=exc)

    async def _run_callback(
        self, callback: Callable[[EventT], utils.MaybeAwaitable[None]], arg: EventT, name: str, /
    ) -> None:
        try:
            r = callback(arg)
            if isawaitable(r):
                await r
        except Exception:
            try:
                r = self.on_user_error(arg)
                if isawaitable(r):
                    await r
            except Exception:
                _L.exception('on_user_error (task: %s) raised an exception', name)

    async def _dispatch(self, types: list[type[BaseEvent]], event: BaseEvent, name: str, /) -> None:
        event.before_dispatch()
        await event.abefore_dispatch()

        manual_process = False

        for _, type in enumerate(types):
            handlers, temporary_handlers = self._handlers.get(type, _DEFAULT_HANDLERS)
            if _L.isEnabledFor(logging.DEBUG):
                _L.debug(
                    'Dispatching %s (%i handlers, originating from %s)',
                    type.__name__,
                    len(handlers),
                    event.__class__.__name__,
                )

            remove = None
            stop_dispatching_on_success = True

            for handler in temporary_handlers.values():
                r = handler._handle(event, name)
                if isawaitable(r):
                    r = await r

                if r:
                    remove = handler.id
                    manual_process = handler.manual_process
                    stop_dispatching_on_success = handler.stop_dispatching_on_success
                    break

            if remove is not None:
                del temporary_handlers[remove]
                if stop_dispatching_on_success:
                    break

            for handler in handlers.values():
                r = handler._handle(event, name)
                if isawaitable(r):
                    await r

            event_name: typing.Optional[str] = getattr(type, 'event_name', None)
            if event_name:
                handler = getattr(self, 'on_' + event_name, None)
                if handler:
                    r = self._run_callback(handler, event, name)
                    if isawaitable(r):
                        await r

        handler = getattr(self, 'on_event', None)
        if handler:
            await self._run_callback(handler, event, name)

        if not manual_process:
            if event.is_canceled:
                _L.debug('%s processing was canceled', event.__class__.__name__)
            else:
                _L.debug('Processing %s', event.__class__.__name__)
                event.process()
                await event.aprocess()

        hook = getattr(event, 'call_object_handlers_hook', None)
        if not hook:
            return
        try:
            r = hook(self)
            if isawaitable(r):
                await r
        except Exception:
            try:
                r = self.on_user_error(event)
                if isawaitable(r):
                    await r
            except Exception:
                _L.exception('on_user_error (task: %s) raised an exception', name)

    def dispatch(self, event: BaseEvent, /) -> asyncio.Task[None]:
        """Dispatches an event.

        Examples
        --------

        Dispatch an event when someone sends silent message: ::

            from attrs import define, field
            import stoat

            # ...


            @define(slots=True)
            class SilentMessageEvent(stoat.BaseEvent):
                message: stoat.Message = field(repr=True, kw_only=True)


            @client.on(stoat.MessageCreateEvent)
            async def on_message_create(event):
                message = event.message
                if message.flags.suppress_notifications:
                    event = SilentMessageEvent(message=message)

                    # Block until event gets fully handled (run hooks, calling event handlers, cache received data).
                    await client.dispatch(event)

                    # Note, that `dispatch` returns `asyncio.Task`, as such you may just do `client.dispatch(event)`.

        Parameters
        ----------
        event: :class:`BaseEvent`
            The event to dispatch.

        Returns
        -------
        :class:`asyncio.Task`
            The asyncio task.
        """

        et = builtins.type(event)
        try:
            types = self._types[et]
        except KeyError:
            types = self._types[et] = _parents_of(et)

        name = f'stoat.py-dispatch-{self._get_i()}'
        return asyncio.create_task(self._dispatch(types, event, name), name=name)  # type: ignore

    def subscribe(
        self,
        event: type[EventT],
        /,
        callback: utils.MaybeAwaitableFunc[[EventT], None],
    ) -> EventSubscription[EventT]:
        """Subscribes to event.

        Parameters
        ----------
        event: Type[EventT]
            The type of the event.
        callback: MaybeAwaitableFunc[[EventT], None]
            The callback for the event.
        """
        sub: EventSubscription[EventT] = EventSubscription(
            client=self,
            id=self._get_i(),
            callback=callback,
            event=event,
        )

        # The actual generic of value type is same as key
        try:
            self._handlers[event][0][sub.id] = sub  # type: ignore
        except KeyError:
            self._handlers[event] = ({sub.id: sub}, {})  # type: ignore
        return sub

    def unsubscribe(
        self,
        event: type[EventT],
        callback: utils.MaybeAwaitableFunc[[EventT], None],
        /,
    ) -> list[EventSubscription[EventT]]:
        try:
            subscriptions = self._handlers[event][0]
        except KeyError:
            return []
        else:
            removed = []
            for k, subscription in subscriptions.items():
                if subscription.callback == callback:
                    removed.append(k)
                    break

            ret = []
            for remove in removed:
                ret.append(subscriptions.pop(remove))
            return ret

    def listen(
        self,
        event: typing.Optional[type[EventT]] = None,
        /,
    ) -> Callable[
        [utils.MaybeAwaitableFunc[[EventT], None]],
        EventSubscription[EventT],
    ]:
        """Register an event listener.

        There is an alias for this called :meth:`~.on`.

        Examples
        --------

        Ping Pong: ::

            @client.listen()
            async def on_message_create(event: stoat.MessageCreateEvent):
                message = event.message
                if message.content == '!ping':
                    await message.reply('pong!')


            # It returns :class:`EventSubscription`, so you can do ``on_message_create.remove()``

        Parameters
        ----------
        event: Optional[Type[EventT]]
            The event to listen to.
        """

        def decorator(callback: utils.MaybeAwaitableFunc[[EventT], None], /) -> EventSubscription[EventT]:
            tmp = event

            if tmp is None:
                fs = signature(callback)

                typ = list(fs.parameters.values())[0]

                if typ.annotation is None:
                    raise TypeError('Cannot use listen() without event annotation type')

                try:
                    globalns = utils.unwrap_function(callback).__globals__
                except AttributeError:
                    globalns = {}

                tmp = utils.evaluate_annotation(typ.annotation, globalns, globalns, {})

            return self.subscribe(tmp, callback)  # type: ignore

        return decorator

    def on(
        self,
        event: typing.Optional[type[EventT]] = None,
        /,
    ) -> Callable[
        [utils.MaybeAwaitableFunc[[EventT], None]],
        EventSubscription[EventT],
    ]:
        """Register an event listener.

        This is an alias of :meth:`~.listen`.

        Examples
        --------

        Ping Pong: ::

            @client.on()
            async def on_message_create(event: stoat.MessageCreateEvent):
                message = event.message
                if message.content == '!ping':
                    await message.reply('pong!')


            # It returns :class:`EventSubscription`, so you can do ``on_message_create.remove()``

        Parameters
        ----------
        event: Optional[Type[EventT]]
            The event to listen to.
        """
        return self.listen(event)

    @typing.overload
    def wait_for(  # pyright: ignore[reportOverlappingOverload]
        self,
        event: type[EventT],
        /,
        *,
        check: typing.Optional[Callable[[EventT], bool]] = None,
        count: typing.Literal[1] = ...,
        timeout: typing.Optional[float] = None,
        manual_process: bool = False,
        stop_dispatching_on_success: bool = True,
    ) -> TemporarySubscription[EventT]: ...

    @typing.overload
    def wait_for(  # pyright: ignore[reportOverlappingOverload]
        self,
        event: type[EventT],
        /,
        *,
        check: typing.Optional[Callable[[EventT], bool]] = None,
        count: typing.Literal[0] = ...,
        timeout: typing.Optional[float] = None,
        manual_process: bool = False,
        stop_dispatching_on_success: bool = True,
    ) -> typing.NoReturn: ...

    @typing.overload
    def wait_for(
        self,
        event: type[EventT],
        /,
        *,
        check: typing.Optional[Callable[[EventT], bool]] = None,
        count: int = 1,
        timeout: typing.Optional[float] = None,
        manual_process: bool = False,
        stop_dispatching_on_success: bool = True,
    ) -> TemporarySubscriptionList[EventT]: ...

    def wait_for(
        self,
        event: type[EventT],
        /,
        *,
        check: typing.Optional[Callable[[EventT], bool]] = None,
        count: int = 1,
        timeout: typing.Optional[float] = None,
        manual_process: bool = False,
        stop_dispatching_on_success: bool = True,
    ) -> typing.Union[TemporarySubscription[EventT], TemporarySubscriptionList[EventT]]:
        """|coro|

        Waits for a WebSocket event to be dispatched.

        This could be used to wait for an user to reply to a message,
        or to react to a message, or to edit a message in a self-contained
        way.

        The ``timeout`` parameter is passed onto :func:`asyncio.wait_for`. By default,
        it does not timeout. Note that this does propagate the
        :exc:`asyncio.TimeoutError` for you in case of timeout and is provided for
        ease of use.

        This function returns the **first event that meets the requirements**.

        Examples
        --------

        Waiting for an user reply: ::

            @client.on(stoat.MessageCreateEvent)
            async def on_message_create(event):
                message = event.message
                if message.content.startswith('$greet'):
                    channel = message.channel
                    await channel.send('Say hello!')

                    def check(event):
                        return event.message.content == 'hello' and event.message.channel.id == channel.id

                    msg = await client.wait_for(stoat.MessageCreateEvent, check=check)
                    await channel.send(f'Hello {msg.author}!')

        Waiting for a thumbs up reaction from the message author: ::

            @client.on(stoat.MessageCreateEvent)
            async def on_message_create(event):
                message = event.message
                if message.content.startswith('$thumb'):
                    channel = message.channel
                    await channel.send('Send me that \N{THUMBS UP SIGN} reaction, mate')

                    def check(event):
                        return event.user_id == message.author.id and event.emoji == '\N{THUMBS UP SIGN}'

                    try:
                        await client.wait_for(stoat.MessageReactEvent, timeout=60.0, check=check)
                    except asyncio.TimeoutError:
                        await channel.send('\N{THUMBS DOWN SIGN}')
                    else:
                        await channel.send('\N{THUMBS UP SIGN}')

        Parameters
        ----------
        event: Type[EventT]
            The event to wait for.
        check: Optional[Callable[[EventT], :class:`bool`]]
            A predicate to check what to wait for.
        timeout: Optional[:class:`float`]
            The number of seconds to wait before timing out and raising
            :exc:`asyncio.TimeoutError`.
        manual_process: :class:`bool`
            Whether to not process the event at all when it gets dispatched. Defaults to ``False``.
        stop_dispatching_on_success: :class:`bool`
            Whether to stop dispatching when event arrives. Defaults to ``True``.

        Raises
        ------
        :class:`TypeError`
            If ``count`` parameter was negative or zero.
        :class:`asyncio.TimeoutError`
            If a timeout is provided and it was reached.

        Returns
        -------
        Union[:class:`~stoat.TemporarySubscription`, :class:`~stoat.TemporarySubscriptionList`]
            The subscription. This can be ``await``'ed.
        """

        if count <= 0:
            raise TypeError('Cannot wait for zero events')

        if check is None:
            check = lambda _, /: True

        if count > 1:
            sub = TemporarySubscriptionList(
                client=self,
                expected=count,
                id=self._get_i(),
                event=event,
                check=check,
                manual_process=manual_process,
                stop_dispatching_on_success=stop_dispatching_on_success,
            )

            try:
                self._handlers[event][1][sub.id] = sub  # type: ignore
            except KeyError:
                self._handlers[event] = ({sub.id: sub}, {})  # type: ignore
            return sub

        future = asyncio.get_running_loop().create_future()

        coro = asyncio.wait_for(future, timeout=timeout)
        sub = TemporarySubscription(
            client=self,
            id=self._get_i(),
            event=event,
            future=future,
            check=check,
            coro=coro,
            manual_process=manual_process,
            stop_dispatching_on_success=stop_dispatching_on_success,
        )

        try:
            self._handlers[event][1][sub.id] = sub  # type: ignore
        except KeyError:
            self._handlers[event] = ({sub.id: sub}, {})  # type: ignore
        return sub

    def all_subscriptions(self) -> list[EventSubscription[BaseEvent]]:
        """List[EventSubscription[:class:`~stoat.BaseEvent`]]: Returns all event subscriptions."""
        ret = []
        for _, v in self._handlers.items():
            ret.extend(v[0].values())
        return ret

    def subscriptions_for(
        self, event: type[EventT], /, *, include_subclasses: bool = False
    ) -> list[EventSubscription[EventT]]:
        """List[EventSubscription[EventT]]: Returns the subscriptions for event.

        Parameters
        ----------
        event: Type[EventT]
            The event to get subscriptions to.
        include_subclasses: :class:`bool`
            Whether to include subclassed events. Defaults to ``False``.
        """
        if include_subclasses:
            ret = []
            for k, v in self._handlers.items():
                if issubclass(k, event):
                    ret.extend(v[0].values())
            return ret

        try:
            return list(self._handlers[event][0].values())  # type: ignore
        except KeyError:
            return []

    def subscriptions_count_for(self, event: type[EventT], /, *, include_subclasses: bool = False) -> int:
        """:class:`int`: Returns the subscriptions for event.

        Parameters
        ----------
        event: Type[EventT]
            The event to get subscription count to.
        include_subclasses: class:`bool`
            Whether to include subclassed events. Defaults to ``False``.
        """
        if include_subclasses:
            ret = 0
            for k, v in self._handlers.items():
                if issubclass(k, event):
                    ret += len(v[0])
            return ret

        try:
            return len(self._handlers[event][0])  # type: ignore
        except KeyError:
            return 0

    @property
    def me(self) -> typing.Optional[OwnUser]:
        """Optional[:class:`~stoat.OwnUser`]: The currently logged in user. ``None`` if not logged in."""
        return self._state._me

    @property
    def user(self) -> typing.Optional[OwnUser]:
        """Optional[:class:`~stoat.OwnUser`]: The currently logged in user. ``None`` if not logged in.

        Alias to :attr:`.me`.
        """
        return self._state._me

    @property
    def saved_notes(self) -> typing.Optional[SavedMessagesChannel]:
        """Optional[:class:`~stoat.SavedMessagesChannel`]: The Saved Notes channel."""
        return self._state._saved_notes

    @property
    def http(self) -> HTTPClient:
        """:class:`~stoat.HTTPClient`: The HTTP client."""
        return self._state.http

    @property
    def shard(self) -> Shard:
        """:class:`~stoat.Shard`: The Stoat WebSocket client."""
        return self._state.shard

    @property
    def state(self) -> State:
        """:class:`~stoat.State`: The controller for all entities and components."""
        return self._state

    @property
    def channels(self) -> Mapping[str, Channel]:
        """Mapping[:class:`str`, :class:`~stoat.Channel`]: Mapping of cached channels."""
        state = self.state
        cache = state.cache

        if cache is None:
            return {}

        ctx = (
            ClientCacheContext(
                type=CacheContextType.channels_through_client_getter,
                client=self,
            )
            if state.provide_cache_context('Client.channels')
            else _CHANNELS_THROUGH_CLIENT_GETTER
        )

        return cache.get_channels_mapping(ctx)

    @property
    def emojis(self) -> Mapping[str, Emoji]:
        """Mapping[:class:`str`, :class:`~stoat.Emoji`]: Mapping of cached emojis."""
        state = self.state
        cache = state.cache

        if cache is None:
            return {}

        ctx = (
            ClientCacheContext(
                type=CacheContextType.emojis_through_client_getter,
                client=self,
            )
            if state.provide_cache_context('Client.emojis')
            else _EMOJIS_THROUGH_CLIENT_GETTER
        )

        return cache.get_emojis_mapping(ctx)

    @property
    def members(self) -> Mapping[str, Mapping[str, Member]]:
        """Mapping[:class:`str`, Mapping[:class:`str`, :class:`~stoat.Member`]]: Mapping of cached server members."""
        state = self.state
        cache = state.cache

        if cache is None:
            return {}

        ctx = (
            ClientCacheContext(
                type=CacheContextType.server_members_through_client_getter,
                client=self,
            )
            if state.provide_cache_context('Client.members')
            else _SERVER_MEMBERS_THROUGH_CLIENT_GETTER
        )

        return cache.get_servers_member_mapping(ctx)

    @property
    def read_states(self) -> Mapping[str, ReadState]:
        """Mapping[:class:`str`, :class:`~stoat.ReadState`]: Mapping of cached read states."""
        state = self.state
        cache = state.cache

        if cache is None:
            return {}

        ctx = (
            ClientCacheContext(
                type=CacheContextType.read_states_through_client_getter,
                client=self,
            )
            if state.provide_cache_context('Client.read_states')
            else _READ_STATES_THROUGH_CLIENT_GETTER
        )

        return cache.get_read_states_mapping(ctx)

    @property
    def servers(self) -> Mapping[str, Server]:
        """Mapping[:class:`str`, :class:`~stoat.Server`]: Mapping of cached servers."""
        state = self.state
        cache = state.cache

        if cache is None:
            return {}

        ctx = (
            ClientCacheContext(
                type=CacheContextType.servers_through_client_getter,
                client=self,
            )
            if state.provide_cache_context('Client.servers')
            else _SERVERS_THROUGH_CLIENT_GETTER
        )

        return cache.get_servers_mapping(ctx)

    @property
    def users(self) -> Mapping[str, User]:
        """Mapping[:class:`str`, :class:`~stoat.User`]: Mapping of cached users."""
        state = self.state
        cache = state.cache

        if cache is None:
            return {}

        ctx = (
            ClientCacheContext(
                type=CacheContextType.users_through_client_getter,
                client=self,
            )
            if state.provide_cache_context('Client.users')
            else _USERS_THROUGH_CLIENT_GETTER
        )

        return cache.get_users_mapping(ctx)

    @property
    def voice_states(self) -> Mapping[str, ChannelVoiceStateContainer]:
        """Mapping[:class:`str`, :class:`~stoat.ChannelVoiceStateContainer`]: Mapping of cached voice states."""
        state = self.state
        cache = state.cache

        if cache is None:
            return {}

        ctx = (
            ClientCacheContext(
                type=CacheContextType.voice_states_through_client_getter,
                client=self,
            )
            if state.provide_cache_context('Client.voice_states')
            else _VOICE_STATES_THROUGH_CLIENT_GETTER
        )

        return cache.get_channel_voice_states_mapping(ctx)

    @property
    def dm_channel_ids(self) -> Mapping[str, str]:
        """Mapping[:class:`str`, :class:`str`]: Mapping of user IDs to cached DM channel IDs."""
        state = self.state
        cache = state.cache

        if cache is None:
            return {}

        ctx = (
            ClientCacheContext(
                type=CacheContextType.user_ids_through_client_dm_channel_ids,
                client=self,
            )
            if state.provide_cache_context('Client.dm_channel_ids')
            else _USER_IDS_THROUGH_CLIENT_DM_CHANNELS
        )

        return cache.get_private_channels_by_users_mapping(ctx)

    @property
    def dm_channels(self) -> Mapping[str, DMChannel]:
        """Mapping[:class:`str`, :class:`~stoat.DMChannel`]: Mapping of user IDs to cached DM channels."""

        state = self.state
        cache = state.cache

        if cache is None:
            return {}

        ctx = (
            ClientCacheContext(
                type=CacheContextType.channels_through_client_dm_channels,
                client=self,
            )
            if state.provide_cache_context('Client.dm_channels')
            else _CHANNELS_THROUGH_CLIENT_DM_CHANNELS
        )

        result: dict[str, DMChannel] = {}
        for k, v in cache.get_private_channels_by_users_mapping(ctx).items():
            channel = cache.get_channel(v, ctx)
            if channel and isinstance(channel, DMChannel):
                result[k] = channel
        return result

    @property
    def private_channels(self) -> Mapping[str, typing.Union[DMChannel, GroupChannel]]:
        """Mapping[:class:`str`, Union[:class:`~stoat.DMChannel`, :class:`~stoat.GroupChannel`]]: Mapping of channel IDs to private channels."""
        state = self.state
        cache = state.cache

        if cache is None:
            return {}

        ctx = (
            ClientCacheContext(
                type=CacheContextType.channels_through_client_private_channels,
                client=self,
            )
            if state.provide_cache_context('Client.private_channels')
            else _CHANNELS_THROUGH_CLIENT_PRIVATE_CHANNELS
        )

        return cache.get_private_channels_mapping(ctx)

    @property
    def ordered_private_channels_old(self) -> list[typing.Union[DMChannel, GroupChannel]]:
        """List[Union[:class:`~stoat.DMChannel`, :class:`~stoat.GroupChannel`]]: The list of private channels in Revite order."""
        return sorted(self.private_channels.values(), key=_private_channel_sort_old, reverse=True)

    @property
    def ordered_private_channels(self) -> list[typing.Union[DMChannel, GroupChannel]]:
        """List[Union[:class:`~stoat.DMChannel`, :class:`~stoat.GroupChannel`]]: The list of private channels in new client's order."""
        return sorted(self.private_channels.values(), key=_private_channel_sort_new, reverse=True)

    @typing.overload
    def get_channel(self, channel_id: str, /, *, partial: typing.Literal[False] = False) -> typing.Optional[Channel]:  # type: ignore
        ...

    @typing.overload
    def get_channel(
        self, channel_id: str, /, *, partial: typing.Literal[True] = ...
    ) -> typing.Union[Channel, PartialMessageable]: ...

    def get_channel(
        self, channel_id: str, /, *, partial: bool = False
    ) -> typing.Optional[typing.Union[Channel, PartialMessageable]]:
        """Retrieves a channel from cache.

        Parameters
        ----------
        channel_id: :class:`str`
            The channel ID.
        partial: :class:`bool`
            Whether to return :class:`~stoat.PartialMessageable` instead of ``None`` if server was not found.

        Returns
        -------
        Optional[Union[:class:`~stoat.Channel`, :class:`~stoat.PartialMessageable`]]
            The channel or ``None`` if not found.
        """
        state = self.state
        cache = state.cache

        if cache is None:
            if partial:
                return PartialMessageable(state=self.state, id=channel_id)
            return None

        ctx = (
            ClientCacheContext(
                type=CacheContextType.channel_through_client_getter,
                client=self,
            )
            if state.provide_cache_context('Client.get_channel()')
            else _CHANNEL_THROUGH_CLIENT_GETTER
        )

        channel = cache.get_channel(channel_id, ctx)
        if channel is None and partial:
            return PartialMessageable(state=self.state, id=channel_id)
        return channel

    async def fetch_channel(
        self, channel_id: str, /, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None
    ) -> Channel:
        """|coro|

        Fetch a :class:`~stoat.Channel` with the specified ID.

        You must have :attr:`~stoat.Permissions.view_channel` to do this.

        This is shortcut to :meth:`stoat.HTTPClient.get_channel`.

        Parameters
        ----------
        channel: ULIDOr[:class:`~stoat.BaseChannel`]
            The channel to fetch.
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

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The channel was not found. |
            +--------------+----------------------------+

        Returns
        -------
        :class:`~stoat.Channel`
            The retrieved channel.
        """

        return await self.http.get_channel(channel_id, http_overrides=http_overrides)

    def get_emoji(self, emoji_id: str, /) -> typing.Optional[Emoji]:
        """Retrieves an emoji from cache.

        Parameters
        ----------
        emoji_id: :class:`str`
            The emoji ID.

        Returns
        -------
        Optional[:class:`~stoat.Emoji`]
            The emoji or ``None`` if not found.
        """
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ClientCacheContext(
                type=CacheContextType.emoji_through_client_getter,
                client=self,
            )
            if state.provide_cache_context('Client.get_emoji()')
            else _EMOJI_THROUGH_CLIENT_GETTER
        )

        return cache.get_emoji(emoji_id, ctx)

    async def fetch_emoji(
        self, emoji_id: str, /, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None
    ) -> Emoji:
        """|coro|

        Retrieves a custom emoji.

        This is shortcut to :meth:`stoat.HTTPClient.get_emoji`.

        Parameters
        ----------
        emoji: ULIDOr[:class:`~stoat.BaseEmoji`]
            The emoji to retrieve.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`~stoat.NotFound`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +--------------+--------------------------+
            | Value        | Reason                   |
            +--------------+--------------------------+
            | ``NotFound`` | The emoji was not found. |
            +--------------+--------------------------+

        Returns
        -------
        :class:`~stoat.Emoji`
            The retrieved emoji.
        """

        return await self.http.get_emoji(emoji_id, http_overrides=http_overrides)

    def get_read_state(self, channel_id: str, /) -> typing.Optional[ReadState]:
        """Retrieves a read state from cache.

        Parameters
        ----------
        channel_id: :class:`str`
            The channel ID of read state.

        Returns
        -------
        Optional[:class:`~stoat.ReadState`]
            The read state or ``None`` if not found.
        """
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ClientCacheContext(
                type=CacheContextType.read_state_through_client_getter,
                client=self,
            )
            if state.provide_cache_context('Client.get_read_state()')
            else _READ_STATE_THROUGH_CLIENT_GETTER
        )

        return cache.get_read_state(channel_id, ctx)

    @typing.overload
    def get_server(self, server_id: str, /, *, partial: typing.Literal[False] = False) -> typing.Optional[Server]:  # type: ignore
        ...

    @typing.overload
    def get_server(
        self, server_id: str, /, *, partial: typing.Literal[True] = ...
    ) -> typing.Union[Server, BaseServer]: ...

    def get_server(
        self, server_id: str, /, *, partial: bool = False
    ) -> typing.Optional[typing.Union[Server, BaseServer]]:
        """Retrieves a server from cache.

        Parameters
        ----------
        server_id: :class:`str`
            The server ID.
        partial: :class:`bool`
            Whether to return :class:`~stoat.BaseServer` instead of ``None`` if server was not found.

        Returns
        -------
        Optional[Union[:class:`~stoat.Server`, :class:`~stoat.BaseServer`]]
            The server or ``None`` if not found.
        """
        state = self.state
        cache = state.cache

        if cache is None:
            if partial:
                return BaseServer(state=self.state, id=server_id)
            return None

        ctx = (
            ClientCacheContext(
                type=CacheContextType.server_through_client_getter,
                client=self,
            )
            if state.provide_cache_context('Client.get_server()')
            else _SERVER_THROUGH_CLIENT_GETTER
        )

        server = cache.get_server(server_id, ctx)
        if server is None and partial:
            return BaseServer(state=self.state, id=server_id)
        return server

    async def fetch_server(
        self,
        server_id: str,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        populate_channels: typing.Optional[bool] = None,
    ) -> Server:
        """|coro|

        Retrieves a :class:`~stoat.Server`.

        This is shortcut to :meth:`stoat.HTTPClient.get_server`.

        Parameters
        ----------
        server: ULIDOr[:class:`~stoat.BaseServer`]
            The server to retrieve.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        populate_channels: Optional[:class:`bool`]
            Whether to populate :attr:`~stoat.Server.channels`.

        Raises
        ------
        :class:`~stoat.Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`~stoat.NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+

        Returns
        -------
        :class:`stoat.Server`
            The retrieved server.
        """
        return await self.http.get_server(server_id, http_overrides=http_overrides, populate_channels=populate_channels)

    @typing.overload
    def get_user(self, user_id: str, /, *, partial: typing.Literal[False] = False) -> typing.Optional[User]:  # type: ignore
        ...

    @typing.overload
    def get_user(self, user_id: str, /, *, partial: typing.Literal[True] = ...) -> typing.Union[User, BaseUser]: ...

    def get_user(self, user_id: str, /, *, partial: bool = False) -> typing.Optional[typing.Union[User, BaseUser]]:
        """Retrieves an user from cache.

        Parameters
        ----------
        user_id: :class:`str`
            The user ID.
        partial: :class:`bool`
            Whether to return :class:`~stoat.BaseUser` instead of ``None`` if server was not found.

        Returns
        -------
        Optional[Union[:class:`~stoat.User`, :class:`~stoat.BaseUser`]]
            The user or ``None`` if not found.
        """
        state = self.state
        cache = state.cache

        if cache is None:
            if partial:
                return BaseUser(state=self.state, id=user_id)
            return None

        ctx = (
            ClientCacheContext(
                type=CacheContextType.user_through_client_getter,
                client=self,
            )
            if state.provide_cache_context('Client.get_user()')
            else _USER_THROUGH_CLIENT_GETTER
        )

        user = cache.get_user(user_id, ctx)
        if user is None and partial:
            return BaseUser(state=self.state, id=user_id)
        return user

    async def fetch_user(self, user_id: str, /, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> User:
        """|coro|

        Retrieves an user from API. This is shortcut to :meth:`stoat.HTTPClient.get_user`.

        Parameters
        ----------
        user_id: :class:`str`
            The user ID.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Returns
        -------
        :class:`~stoat.User`
            The user.
        """
        return await self.http.get_user(user_id, http_overrides=http_overrides)

    @property
    def settings(self) -> UserSettings:
        """:class:`~stoat.UserSettings`: The current user settings."""
        return self._state.settings

    @property
    def system(self) -> User:
        """:class:`~stoat.User`: The Stoat sentinel user."""
        return self._state.system

    async def setup_hook(self) -> None:
        """|coro|

        A hook that is called when client starts up.
        """

    async def start(self) -> None:
        """|coro|

        Starts up the client.

        Calls :meth:`.setup_hook` before connecting.
        """
        self.closed = False
        await self.setup_hook()
        await self._state.shard.connect()

    async def close(self, *, http: bool = True, cleanup_websocket: bool = True) -> None:
        """|coro|

        Closes all HTTP sessions, and WebSocket connections.

        Parameters
        ----------
        http: :class:`bool`
            Whether to clean up HTTP sessions.
        cleanup_websocket: :class:`bool`
            Whether to clean up WebSocket.
        """

        self.closed = True

        await self.shard.close()
        if cleanup_websocket:
            await self.shard.cleanup()

        if http:
            await self.http.cleanup()

    def run(
        self,
        token: str = '',
        *,
        bot: UndefinedOr[bool] = UNDEFINED,
        log_handler: UndefinedOr[typing.Optional[logging.Handler]] = UNDEFINED,
        log_formatter: UndefinedOr[logging.Formatter] = UNDEFINED,
        log_level: UndefinedOr[int] = UNDEFINED,
        root_logger: bool = False,
        asyncio_debug: bool = False,
        cleanup: bool = True,
    ) -> None:
        """A blocking call that abstracts away the event loop
        initialization from you.

        If you want more control over the event loop then this
        function should not be used. Use :meth:`.start` coroutine.

        This function also sets up the logging library to make it easier
        for beginners to know what is going on with the library. For more
        advanced users, this can be disabled by passing ``None`` to
        the ``log_handler`` parameter.

        .. warning::

            This function must be the last function to call due to the fact that it
            is blocking. That means that registration of events or anything being
            called after this function call will not execute until it returns.

        Parameters
        ----------
        log_handler: Optional[:class:`logging.Handler`]
            The log handler to use for the library's logger. If this is ``None``
            then the library will not set up anything logging related. Logging
            will still work if ``None`` is passed, though it is your responsibility
            to set it up.

            The default log handler if not provided is :class:`logging.StreamHandler`.
        log_formatter: :class:`logging.Formatter`
            The formatter to use with the given log handler. If not provided then it
            defaults to a color based logging formatter (if available).
        log_level: :class:`int`
            The default log level for the library's logger. This is only applied if the
            ``log_handler`` parameter is not ``None``. Defaults to ``logging.INFO``.
        root_logger: :class:`bool`
            Whether to set up the root logger rather than the library logger.
            By default, only the library logger (``'stoat'``) is set up. If this
            is set to ``True`` then the root logger is set up as well.

            Defaults to ``False``.
        asyncio_debug: :class:`bool`
            Whether to run with asyncio debug mode enabled or not.

            Defaults to ``False``.
        cleanup: :class:`bool`
            Whether to close aiohttp sessions or not.

            Defaults to ``True``.
        """

        if token:
            bot = self.bot if bot is UNDEFINED else bot

            self.http.with_credentials(token, bot=bot)
            self.shard.with_credentials(token, bot=bot)
        elif not self.token:
            raise TypeError('No token was provided')

        async def runner():
            await self.start()
            if cleanup and not self.closed:
                await self.close()
            self.closed = True

        if log_handler is not None:
            utils.setup_logging(
                handler=log_handler,
                formatter=log_formatter,
                level=log_level,
                root=root_logger,
            )

        try:
            asyncio.run(runner(), debug=asyncio_debug)
        except KeyboardInterrupt:
            # nothing to do here
            # `asyncio.run` handles the loop cleanup
            # NOTE: not true
            # > and `self.start` closes all sockets and the HTTPClient instance.
            return

    if typing.TYPE_CHECKING:

        def on_event(self, arg: BaseEvent, /) -> utils.MaybeAwaitable[None]: ...

        def on_authenticated(self, arg: AuthenticatedEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_authifier(self, arg: AuthifierEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_channel_create(self, arg: BaseChannelCreateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_message_delete_bulk(self, arg: MessageDeleteBulkEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_channel_delete(self, arg: ChannelDeleteEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_channel_update(self, arg: ChannelUpdateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_recipient_add(self, arg: GroupRecipientAddEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_recipient_remove(self, arg: GroupRecipientRemoveEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_channel_start_typing(self, arg: ChannelStartTypingEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_channel_stop_typing(self, arg: ChannelStopTypingEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_message_start_editing(self, arg: MessageStartEditingEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_message_stop_editing(self, arg: MessageStopEditingEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_logout(self, arg: LogoutEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_message_ack(self, arg: MessageAckEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_message_append(self, arg: MessageAppendEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_message_clear_reaction(self, arg: MessageClearReactionEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_message_create(self, arg: MessageCreateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_message_delete(self, arg: MessageDeleteEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_message_react(self, arg: MessageReactEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_message_unreact(self, arg: MessageUnreactEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_message_update(self, arg: MessageUpdateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_message(self, arg: Message, /) -> utils.MaybeAwaitable[None]: ...
        def on_private_channel_create(self, arg: PrivateChannelCreateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_raw_server_role_update(self, arg: RawServerRoleUpdateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_ready(self, arg: ReadyEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_report_create(self, arg: ReportCreateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_server_channel_create(self, arg: ServerChannelCreateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_server_create(self, arg: ServerCreateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_server_delete(self, arg: ServerDeleteEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_server_emoji_create(self, arg: ServerEmojiCreateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_server_emoji_delete(self, arg: ServerEmojiDeleteEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_server_member_join(self, arg: ServerMemberJoinEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_server_member_remove(self, arg: ServerMemberRemoveEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_server_member_update(self, arg: ServerMemberUpdateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_server_role_delete(self, arg: ServerRoleDeleteEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_server_role_ranks_update(self, arg: ServerRoleRanksUpdateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_server_update(self, arg: ServerUpdateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_session_create(self, arg: SessionCreateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_session_delete_all(self, arg: SessionDeleteAllEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_session_delete(self, arg: SessionDeleteEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_user_platform_wipe(self, arg: UserPlatformWipeEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_user_relationship_update(self, arg: UserRelationshipUpdateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_user_settings_update(self, arg: UserSettingsUpdateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_user_update(self, arg: UserUpdateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_webhook_create(self, arg: WebhookCreateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_webhook_delete(self, arg: WebhookDeleteEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_webhook_update(self, arg: WebhookUpdateEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_before_connect(self, arg: BeforeConnectEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_after_connect(self, arg: AfterConnectEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_voice_channel_join(self, arg: VoiceChannelJoinEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_voice_channel_leave(self, arg: VoiceChannelLeaveEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_voice_channel_move(self, arg: VoiceChannelMoveEvent, /) -> utils.MaybeAwaitable[None]: ...
        def on_user_voice_state_update(self, arg: UserVoiceStateUpdateEvent, /) -> utils.MaybeAwaitable[None]: ...

    async def create_group(
        self,
        name: str,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        description: typing.Optional[str] = None,
        icon: typing.Optional[ResolvableResource] = None,
        recipients: typing.Optional[list[ULIDOr[BaseUser]]] = None,
        nsfw: typing.Optional[bool] = None,
    ) -> GroupChannel:
        """|coro|

        Creates a new group.

        Fires :class:`PrivateChannelCreateEvent` for the current user and all specified recipients.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        name: :class:`str`
            The group name. Must be between 1 and 32 characters long.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        description: Optional[:class:`str`]
            The group description. Can be only up to 1024 characters.
        icon: Optional[:class:`~stoat.ResolvableResource`]
            The group's icon.
        recipients: Optional[List[ULIDOr[:class:`~stoat.BaseUser`]]]
            The users to create the group with, only up to 49 users. You must be friends with these users.
        nsfw: Optional[:class:`bool`]
            To mark the group as NSFW or not.

        Raises
        ------
        :class:`~stoat.HTTPException`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +----------------------+-------------------------------------------+
            | Value                | Reason                                    |
            +----------------------+-------------------------------------------+
            | ``FailedValidation`` | The payload was invalid.                  |
            +----------------------+-------------------------------------------+
            | ``IsBot``            | The current token belongs to bot account. |
            +----------------------+-------------------------------------------+
        :class:`~stoat.Unauthorized`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`~stoat.Forbidden`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +-----------------------+------------------------------------------------------------------+
            | Value                 | Reason                                                           |
            +-----------------------+------------------------------------------------------------------+
            | ``GroupTooLarge``     | The group exceeded maximum count of recipients.                  |
            +-----------------------+------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to add the recipient.     |
            +-----------------------+------------------------------------------------------------------+
            | ``NotFriends``        | You're not friends with the users you want to create group with. |
            +-----------------------+------------------------------------------------------------------+
        :class:`~stoat.NotFound`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +--------------+-------------------------------------------------------------------------------+
            | Value        | Reason                                                                        |
            +--------------+-------------------------------------------------------------------------------+
            | ``NotFound`` | One of recipients was not found, or the provided file for icon was not found. |
            +--------------+-------------------------------------------------------------------------------+
        :class:`~stoat.InternalServerError`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                              |
            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~stoat.HTTPException.collection`, :attr:`~stoat.HTTPException.operation` |
            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+

        Returns
        -------
        :class:`~stoat.GroupChannel`
            The new group.
        """

        return await self.http.create_group(
            name, http_overrides=http_overrides, description=description, icon=icon, recipients=recipients, nsfw=nsfw
        )

    async def create_server(
        self,
        name: str,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        description: typing.Optional[str] = None,
        nsfw: typing.Optional[bool] = None,
    ) -> Server:
        """|coro|

        Create a new server.

        Fires :class:`ServerCreateEvent` for the current user.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        name: :class:`str`
            The server name. Must be between 1 and 32 characters long.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        description: Optional[:class:`str`]
            The server description. Can be only up to 1024 characters.
        nsfw: Optional[:class:`bool`]
            Whether this server is age-restricted.

        Raises
        ------
        :class:`~stoat.HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+------------------------------------------------------+
            | Value                | Reason                                               |
            +----------------------+------------------------------------------------------+
            | ``FailedValidation`` | The payload was invalid.                             |
            +----------------------+------------------------------------------------------+
            | ``IsBot``            | The current token belongs to bot account.            |
            +----------------------+------------------------------------------------------+
            | ``TooManyChannels``  | The instance was incorrectly configured. (?)         |
            +----------------------+------------------------------------------------------+
            | ``TooManyServers``   | You're in too many servers than the instance allows. |
            +----------------------+------------------------------------------------------+
        :class:`~stoat.Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`~stoat.InternalServerError`
            Possible values for :attr:`~stoat.HTTPException.type`:

            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                              |
            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~stoat.HTTPException.collection`, :attr:`~stoat.HTTPException.operation` |
            +-------------------+------------------------------------------------+-----------------------------------------------------------------------------------+

        Returns
        -------
        :class:`~stoat.Server`
            The created server.
        """

        return await self.http.create_server(name, http_overrides=http_overrides, description=description, nsfw=nsfw)


__all__ = (
    'EventSubscription',
    'TemporarySubscription',
    'TemporarySubscriptionList',
    'ClientEventHandler',
    '_private_channel_sort_old',
    '_private_channel_sort_new',
    'Client',
)
