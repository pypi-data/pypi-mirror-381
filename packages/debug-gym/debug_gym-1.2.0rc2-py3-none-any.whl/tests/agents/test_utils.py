import logging
from unittest.mock import patch

import pytest

from debug_gym.agents.utils import load_config, trim, trim_prompt_messages


def test_trim_prompt_messages():
    def count_tokens(text):
        return len(text)

    # Test basic validation
    with pytest.raises(AssertionError, match="messages should not be empty"):
        trim_prompt_messages([], 5, count_tokens)

    with pytest.raises(
        AssertionError, match="the last message should be from the user or the tool"
    ):
        messages = [
            {"role": "system", "content": "System message"},
            {"role": "assistant", "content": "Assistant message"},
        ]
        trim_prompt_messages(messages, 20, count_tokens)

    with pytest.raises(AssertionError, match="context_length should be non-negative"):
        messages = [{"role": "user", "content": "User message"}]
        trim_prompt_messages(messages, -1, count_tokens)

    # Test system message too long
    with pytest.raises(
        AssertionError, match="System message tokens exceed context length"
    ):
        messages = [
            {"role": "system", "content": "Very long system message"},
            {"role": "user", "content": "Hi"},
        ]
        trim_prompt_messages(messages, 10, count_tokens)

    # Test simple case: just user message
    messages = [{"role": "user", "content": "Hello"}]
    result = trim_prompt_messages(messages, 10, count_tokens)
    assert result == messages

    # Test case: system + user, fits completely
    messages = [
        {"role": "system", "content": "Sys"},  # 3 tokens
        {"role": "user", "content": "Hi"},  # 2 tokens
    ]
    result = trim_prompt_messages(messages, 10, count_tokens)
    assert result == messages

    # Test case: system + user + assistant + tool, fits completely
    messages = [
        {"role": "system", "content": "Sys"},  # 3 tokens
        {"role": "user", "content": "Hi"},  # 2 tokens
        {"role": "assistant", "content": "Hello"},  # 5 tokens
        {"role": "tool", "content": "Result"},  # 6 tokens
    ]
    result = trim_prompt_messages(messages, 20, count_tokens)
    assert result == messages

    # Test case: Keep system + most recent assistant-tool pair, drop user
    messages = [
        {"role": "system", "content": "Sys"},  # 3 tokens
        {"role": "user", "content": "Hi"},  # 2 tokens
        {"role": "assistant", "content": "Hello"},  # 5 tokens
        {"role": "tool", "content": "Result"},  # 6 tokens
    ]
    expected = [
        {"role": "system", "content": "Sys"},
        {"role": "assistant", "content": "Hello"},
        {"role": "tool", "content": "Result"},
    ]
    result = trim_prompt_messages(
        messages, 14, count_tokens
    )  # Just enough for sys + assistant + tool
    assert result == expected

    # Test case: Multiple assistant-tool pairs, keep most recent ones
    messages = [
        {"role": "system", "content": "Sys"},  # 3 tokens
        {"role": "user", "content": "Hi"},  # 2 tokens
        {"role": "assistant", "content": "Hello1"},  # 6 tokens
        {"role": "tool", "content": "Result1"},  # 7 tokens
        {"role": "assistant", "content": "Hello2"},  # 6 tokens
        {"role": "tool", "content": "Result2"},  # 7 tokens
    ]
    # Keep system + most recent assistant-tool pair only
    expected = [
        {"role": "system", "content": "Sys"},
        {"role": "assistant", "content": "Hello2"},
        {"role": "tool", "content": "Result2"},
    ]
    result = trim_prompt_messages(
        messages, 16, count_tokens
    )  # sys(3) + hello2(6) + result2(7) = 16
    assert result == expected

    # Test case: Can fit all assistant-tool pairs + user message
    messages = [
        {"role": "system", "content": "Sys"},  # 3 tokens
        {"role": "user", "content": "Hi"},  # 2 tokens
        {"role": "assistant", "content": "Hello1"},  # 6 tokens
        {"role": "tool", "content": "Result1"},  # 7 tokens
        {"role": "assistant", "content": "Hello2"},  # 6 tokens
        {"role": "tool", "content": "Result2"},  # 7 tokens
    ]
    # All pairs fit, so include user message too
    result = trim_prompt_messages(messages, 50, count_tokens)
    assert result == messages

    # Test case: Can fit all assistant-tool pairs but not user message
    messages = [
        {"role": "system", "content": "Sys"},  # 3 tokens
        {"role": "user", "content": "Hi"},  # 2 tokens
        {"role": "assistant", "content": "Hello1"},  # 6 tokens
        {"role": "tool", "content": "Result1"},  # 7 tokens
        {"role": "assistant", "content": "Hello2"},  # 6 tokens
        {"role": "tool", "content": "Result2"},  # 7 tokens
    ]
    expected = [
        {"role": "system", "content": "Sys"},
        {"role": "assistant", "content": "Hello1"},
        {"role": "tool", "content": "Result1"},
        {"role": "assistant", "content": "Hello2"},
        {"role": "tool", "content": "Result2"},
    ]
    result = trim_prompt_messages(
        messages, 29, count_tokens
    )  # sys(3) + all pairs(26) = 29, no room for user(2)
    assert result == expected

    # Test case: No system message
    messages = [
        {"role": "user", "content": "Hi"},  # 2 tokens
        {"role": "assistant", "content": "Hello"},  # 5 tokens
        {"role": "tool", "content": "Result"},  # 6 tokens
    ]
    result = trim_prompt_messages(messages, 20, count_tokens)
    assert result == messages

    # Test case: No assistant-tool pairs, just system and user
    messages = [
        {"role": "system", "content": "Sys"},  # 3 tokens
        {"role": "user", "content": "Hi"},  # 2 tokens
    ]
    result = trim_prompt_messages(messages, 10, count_tokens)
    assert result == messages

    # Test case: No system, no assistant-tool pairs, just user
    messages = [{"role": "user", "content": "Hi"}]  # 2 tokens
    result = trim_prompt_messages(messages, 10, count_tokens)
    assert result == messages

    # Test case: Tool message without preceding assistant (edge case)
    messages = [
        {"role": "system", "content": "Sys"},  # 3 tokens
        {"role": "user", "content": "Hi"},  # 2 tokens
        {"role": "tool", "content": "Result"},  # 6 tokens
    ]
    expected = [
        {"role": "system", "content": "Sys"},
        {"role": "user", "content": "Hi"},
    ]
    result = trim_prompt_messages(messages, 10, count_tokens)
    assert result == expected

    # Test case: Message with tool_calls instead of content
    messages = [
        {"role": "system", "content": "Sys"},  # 3 tokens
        {"role": "user", "content": "Hi"},  # 2 tokens
        {
            "role": "assistant",
            "tool_calls": [{"function": {"name": "test"}}],
        },  # ~30 tokens (str representation)
        {"role": "tool", "content": "Result"},  # 6 tokens
    ]
    result = trim_prompt_messages(messages, 100, count_tokens)
    assert len(result) == 4  # Should keep all messages if context is large enough


def test_load_config():
    import atexit
    import tempfile
    from pathlib import Path

    import yaml

    # do the test in a tmp folder
    tempdir = tempfile.TemporaryDirectory(prefix="TestLoadConfig-")
    working_dir = Path(tempdir.name)
    config_file = working_dir / "config.yaml"
    atexit.register(tempdir.cleanup)  # Make sure to cleanup that folder once done.

    config_contents = {}
    config_contents["base"] = {
        "random_seed": 42,
        "max_steps": 100,
    }
    config_contents["pdb_agent"] = {
        "llm_name": "gpt2",
    }
    config_contents["rewrite_only"] = {
        "cot_style": "standard",
        "llm_name": "gpt20",
    }

    # write the config file into yaml
    with open(config_file, "w") as f:
        yaml.dump(config_contents, f)

    # now test
    with patch(
        "sys.argv",
        [
            "config_file",
            str(config_file),
            "--agent",
            "pdb_agent",
            "-p",
            "base.random_seed=123",
            "-v",
            "--debug",
        ],
    ):
        _config, _args = load_config()
    assert _args.agent == "pdb_agent"
    expected_config = {
        "agent_type": "pdb_agent",
        "random_seed": 123,
        "max_steps": 100,
        "llm_name": "gpt2",
    }
    assert _config == expected_config
    assert _args.debug is True
    assert _args.logging_level == logging.INFO

    # another test
    with patch(
        "sys.argv",
        [
            "config_file",
            str(config_file),
            "--agent",
            "rewrite_only",
            "-p",
            "base.random_seed=123",
            "rewrite_only.random_seed=456",
            "-v",
            "--debug",
        ],
    ):
        _config, _args = load_config()
    assert _args.agent == "rewrite_only"
    expected_config = {
        "agent_type": "rewrite_only",
        "random_seed": 456,
        "max_steps": 100,
        "cot_style": "standard",
        "llm_name": "gpt20",
    }
    assert _config == expected_config
    assert _args.debug is True
    assert _args.logging_level == logging.INFO


def test_trim():
    def count_tokens(text):
        return len(text)

    # Test basic cases - no trimming needed
    assert trim("Hello world", 11, count_tokens) == "Hello world"
    assert trim("Hello world", 20, count_tokens) == "Hello world"
    assert trim("Hi", 2, count_tokens) == "Hi"
    assert trim("Hi", 10, count_tokens) == "Hi"
    assert trim("A", 1, count_tokens) == "A"  # Exactly fits, no trimming needed

    # Test edge cases
    assert trim("Hello world", 0, count_tokens) == ""
    assert trim("", 5, count_tokens) == ""
    assert trim("", 0, count_tokens) == ""

    # Test cases requiring trimming to single token (ellipsis only)
    assert trim("Hello world", 1, count_tokens) == "…"
    assert trim("Hi", 1, count_tokens) == "…"
    assert trim("ABC", 1, count_tokens) == "…"

    # Test trimming from the middle (default behavior)
    assert trim("Hello world", 5, count_tokens) == "He…ld"
    assert trim("Hello world", 6, count_tokens) == "He…rld"
    assert trim("Hello world", 7, count_tokens) == "Hel…rld"
    assert trim("123456789", 5, count_tokens) == "12…89"
    assert trim("123456789", 7, count_tokens) == "123…789"

    # Test trimming from the end
    assert trim("Hello world", 5, count_tokens, where="end") == "Hell…"
    assert trim("Hello world", 6, count_tokens, where="end") == "Hello…"
    assert trim("Hello world", 7, count_tokens, where="end") == "Hello …"
    assert trim("123456789", 5, count_tokens, where="end") == "1234…"

    # Test trimming from the start
    assert trim("Hello world", 5, count_tokens, where="start") == "…orld"
    assert trim("Hello world", 6, count_tokens, where="start") == "…world"
    assert trim("Hello world", 7, count_tokens, where="start") == "… world"
    assert trim("123456789", 5, count_tokens, where="start") == "…6789"

    # Test invalid `where` value
    with pytest.raises(ValueError, match="Invalid value for `where`"):
        trim("Hello world", 5, count_tokens, where="invalid")

    # Test with different token counter
    def another_count_tokens(text):
        return len(text) // 2

    # For "1234567890" (10 chars), another_count_tokens returns 5 tokens
    # Original text has 5 tokens, so no trimming needed when max_tokens >= 5
    assert trim("1234567890", 5, another_count_tokens) == "1234567890"
    assert trim("1234567890", 6, another_count_tokens) == "1234567890"

    # When max_tokens < 5, trimming is needed
    # With max_tokens=4, we need 3 tokens for content + 1 for ellipsis
    assert (
        trim("1234567890", 4, another_count_tokens) == "123…67890"
    )  # Result has 4 tokens
    assert (
        trim("1234567890", 3, another_count_tokens) == "123…890"
    )  # Result has 3 tokens
    assert trim("1234567890", 2, another_count_tokens) == "1…890"  # Result has 2 tokens
    assert trim("1234567890", 1, another_count_tokens) == "1…0"  # Result has 1 token

    # Test with different trimming positions using the alternative counter
    assert (
        trim("1234567890", 3, another_count_tokens, where="end") == "12345…"
    )  # Result has 3 tokens
    assert (
        trim("1234567890", 3, another_count_tokens, where="start") == "…67890"
    )  # Result has 3 tokens

    # Test edge case with very short text and alternative counter
    assert trim("AB", 1, another_count_tokens) == "AB"  # "AB" has 1 token, fits exactly
    assert (
        trim("ABCD", 1, another_count_tokens) == "A…D"
    )  # "ABCD" has 2 tokens, needs trimming to 1

    # Test boundary conditions with precise scenarios
    def word_count_tokens(text):
        # Count words as tokens
        return len(text.split())

    text = "Hello world test example"  # 4 words = 4 tokens
    assert trim(text, 4, word_count_tokens) == text  # No trimming needed
    assert (
        trim(text, 3, word_count_tokens, where="middle") == "Hello … example"
    )  # Should fit in 3 tokens
    assert (
        trim(text, 2, word_count_tokens, where="end") == "Hello …"
    )  # Should fit in 2 tokens
    assert (
        trim(text, 2, word_count_tokens, where="start") == "… example"
    )  # Should fit in 2 tokens

    # Test very short max_tokens with word counter
    assert trim("Hello world", 1, word_count_tokens) == "…"  # Only ellipsis fits
