import os

import pytest

from chatlas import ChatOpenRouter

from .conftest import (
    assert_data_extraction,
    assert_images_inline,
    assert_images_remote,
    assert_list_models,
    assert_tools_simple,
)

api_key = os.getenv("OPENROUTER_API_KEY")
if api_key is None:
    pytest.skip(
        "OPENROUTER_API_KEY is not set; skipping tests", allow_module_level=True
    )


def test_openrouter_simple_request():
    chat = ChatOpenRouter(
        model="openai/gpt-4o-mini-2024-07-18",
        system_prompt="Be as terse as possible; no punctuation",
    )
    chat.chat("What is 1 + 1?")
    turn = chat.get_last_turn()
    assert turn is not None
    assert turn.tokens is not None
    assert len(turn.tokens) == 3
    assert turn.tokens[0] >= 1
    assert turn.finish_reason == "stop"


@pytest.mark.asyncio
async def test_openrouter_simple_streaming_request():
    chat = ChatOpenRouter(
        model="openai/gpt-4o-mini-2024-07-18",
        system_prompt="Be as terse as possible; no punctuation",
    )
    res = []
    async for x in await chat.stream_async("What is 1 + 1?"):
        res.append(x)
    assert "2" in "".join(res)
    turn = chat.get_last_turn()
    assert turn is not None
    assert turn.finish_reason == "stop"


def test_openrouter_tool_variations():
    def chat_fun(**kwargs):
        return ChatOpenRouter(model="openai/gpt-4o-mini-2024-07-18", **kwargs)

    assert_tools_simple(chat_fun)


def test_data_extraction():
    def chat_fun(**kwargs):
        return ChatOpenRouter(model="openai/gpt-4o-mini-2024-07-18", **kwargs)

    assert_data_extraction(chat_fun)


def test_openrouter_images():
    def chat_fun(**kwargs):
        return ChatOpenRouter(model="openai/gpt-4o-mini-2024-07-18", **kwargs)

    assert_images_inline(chat_fun)
    assert_images_remote(chat_fun)


def test_openrouter_list_models():
    assert_list_models(ChatOpenRouter)
