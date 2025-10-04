"""Tests for the CLI module."""

import os
import sys
from typing import Callable
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from hanzo_mcp.cli import main, install_claude_desktop_config


class TestCLI:
    """Test the CLI module."""

    def test_main_server_run(self) -> None:
        """Test the main function running the server."""
        with patch("argparse.ArgumentParser.parse_args") as mock_parse_args, patch(
            "hanzo_mcp.cli.HanzoMCPServer"
        ) as mock_server_class:
            # Mock parsed arguments
            mock_args = MagicMock()
            mock_args.name = "test-server"
            mock_args.transport = "stdio"
            mock_args.allowed_paths = ["/test/path"]
            mock_args.project_dir = "/test/project"
            mock_args.install = False
            mock_args.agent_model = "anthropic/claude-3-sonnet"
            mock_args.agent_max_tokens = 2000
            mock_args.agent_api_key = "test_api_key"
            mock_args.agent_base_url = None
            mock_args.agent_max_iterations = 10
            mock_args.agent_max_tool_uses = 30
            mock_args.enable_agent_tool = False
            mock_args.disable_write_tools = False
            mock_args.disable_search_tools = False
            mock_args.log_level = "INFO"
            mock_args.host = "127.0.0.1"
            mock_args.port = 3000
            mock_args.project_paths = None
            mock_args.command_timeout = 120.0
            mock_args.dev = False
            mock_parse_args.return_value = mock_args

            # Mock server instance
            mock_server = MagicMock()
            mock_server_class.return_value = mock_server

            # Call main
            main()

            # Verify server was created with correct arguments
            # Project dir should be added to allowed paths and project_paths
            expected_paths = ["/test/path", "/test/project"]
            mock_server_class.assert_called_once_with(
                name="test-server",
                allowed_paths=expected_paths,
                project_paths=["/test/project"],
                project_dir="/test/project",
                agent_model="anthropic/claude-3-sonnet",
                agent_max_tokens=2000,
                agent_api_key="test_api_key",
                agent_base_url=mock_args.agent_base_url,
                agent_max_iterations=10,
                agent_max_tool_uses=30,
                enable_agent_tool=False,
                command_timeout=120.0,
                disable_write_tools=False,
                disable_search_tools=False,
                host=mock_args.host,
                port=mock_args.port,
            )
            mock_server.run.assert_called_once_with(transport="stdio")

    def test_main_with_install(self) -> None:
        """Test the main function with install option."""
        with patch("argparse.ArgumentParser.parse_args") as mock_parse_args, patch(
            "hanzo_mcp.cli.install_claude_desktop_config"
        ) as mock_install:
            # Mock parsed arguments
            mock_args = MagicMock()
            mock_args.name = "test-server"
            mock_args.install = True
            mock_args.allowed_paths = ["/test/path"]
            mock_args.project_dir = None
            mock_args.disable_write_tools = False
            mock_args.disable_search_tools = False
            mock_args.log_level = "INFO"
            mock_args.host = "127.0.0.1"
            mock_args.port = 3000
            mock_parse_args.return_value = mock_args

            # Call main
            main()

            # Verify install function was called
            mock_install.assert_called_once_with(
                "test-server",
                ["/test/path"],
                mock_args.disable_write_tools,
                mock_args.disable_search_tools,
                mock_args.host,
                mock_args.port,
            )

    def test_main_without_allowed_paths(self) -> None:
        """Test the main function without specified allowed paths."""
        with patch("argparse.ArgumentParser.parse_args") as mock_parse_args, patch(
            "hanzo_mcp.cli.HanzoMCPServer"
        ) as mock_server_class, patch("os.getcwd", return_value="/current/dir"):
            # Mock parsed arguments
            mock_args = MagicMock()
            mock_args.name = "test-server"
            mock_args.transport = "stdio"
            mock_args.allowed_paths = None
            mock_args.project_dir = None
            mock_args.install = False
            mock_args.agent_model = None
            mock_args.agent_max_tokens = None
            mock_args.agent_api_key = None
            mock_args.agent_base_url = None
            mock_args.agent_max_iterations = 10
            mock_args.agent_max_tool_uses = 30
            mock_args.enable_agent_tool = False
            mock_args.disable_write_tools = False
            mock_args.disable_search_tools = False
            mock_args.log_level = "INFO"
            mock_args.host = "127.0.0.1"
            mock_args.port = 3000
            mock_args.project_paths = None
            mock_args.command_timeout = 120.0
            mock_args.dev = False
            mock_parse_args.return_value = mock_args

            # Mock server instance
            mock_server = MagicMock()
            mock_server_class.return_value = mock_server

            # Call main
            main()

            # Verify server was created with current directory as allowed path
            mock_server_class.assert_called_once_with(
                name="test-server",
                allowed_paths=["/current/dir"],
                project_paths=[],
                project_dir=None,
                agent_model=None,
                agent_max_tokens=None,
                agent_api_key=None,
                agent_base_url=None,
                agent_max_iterations=10,
                agent_max_tool_uses=30,
                enable_agent_tool=False,
                command_timeout=120.0,
                disable_write_tools=False,
                disable_search_tools=False,
                host=mock_args.host,
                port=mock_args.port,
            )
            mock_server.run.assert_called_once_with(transport="stdio")

    def test_main_with_disable_write_tools(self) -> None:
        """Test the main function with disable_write_tools=True."""
        with patch("argparse.ArgumentParser.parse_args") as mock_parse_args, patch(
            "hanzo_mcp.cli.HanzoMCPServer"
        ) as mock_server_class:
            # Mock parsed arguments
            mock_args = MagicMock()
            mock_args.name = "test-server"
            mock_args.transport = "stdio"
            mock_args.allowed_paths = ["/test/path"]
            mock_args.project_dir = "/test/project"
            mock_args.install = False
            mock_args.agent_model = None
            mock_args.agent_max_tokens = None
            mock_args.agent_api_key = None
            mock_args.agent_base_url = None
            mock_args.agent_max_iterations = 10
            mock_args.agent_max_tool_uses = 30
            mock_args.enable_agent_tool = False
            mock_args.disable_write_tools = True
            mock_args.disable_search_tools = False
            mock_args.log_level = "INFO"
            mock_args.host = "127.0.0.1"
            mock_args.port = 3000
            mock_args.project_paths = None
            mock_args.command_timeout = 120.0
            mock_args.dev = False
            mock_parse_args.return_value = mock_args

            # Mock server instance
            mock_server = MagicMock()
            mock_server_class.return_value = mock_server

            # Call main
            main()

            # Verify server was created with disable_write_tools=True
            expected_paths = ["/test/path", "/test/project"]
            mock_server_class.assert_called_once_with(
                name="test-server",
                allowed_paths=expected_paths,
                project_paths=["/test/project"],
                project_dir="/test/project",
                agent_model=None,
                agent_max_tokens=None,
                agent_api_key=None,
                agent_base_url=None,
                agent_max_iterations=10,
                agent_max_tool_uses=30,
                enable_agent_tool=False,
                command_timeout=120.0,
                disable_write_tools=True,
                disable_search_tools=False,
                host=mock_args.host,
                port=mock_args.port,
            )
            mock_server.run.assert_called_once_with(transport="stdio")

    def test_main_with_disable_search_tools(self) -> None:
        """Test the main function with disable_search_tools=True."""
        with patch("argparse.ArgumentParser.parse_args") as mock_parse_args, patch(
            "hanzo_mcp.cli.HanzoMCPServer"
        ) as mock_server_class:
            # Mock parsed arguments
            mock_args = MagicMock()
            mock_args.name = "test-server"
            mock_args.transport = "stdio"
            mock_args.allowed_paths = ["/test/path"]
            mock_args.project_dir = "/test/project"
            mock_args.install = False
            mock_args.agent_model = None
            mock_args.agent_max_tokens = None
            mock_args.agent_api_key = None
            mock_args.agent_base_url = None
            mock_args.agent_max_iterations = 10
            mock_args.agent_max_tool_uses = 30
            mock_args.enable_agent_tool = False
            mock_args.disable_write_tools = False
            mock_args.disable_search_tools = True
            mock_args.log_level = "INFO"
            mock_args.host = "127.0.0.1"
            mock_args.port = 3000
            mock_args.project_paths = None
            mock_args.command_timeout = 120.0
            mock_args.dev = False
            mock_parse_args.return_value = mock_args

            # Mock server instance
            mock_server = MagicMock()
            mock_server_class.return_value = mock_server

            # Call main
            main()

            # Verify server was created with disable_search_tools=True
            expected_paths = ["/test/path", "/test/project"]
            mock_server_class.assert_called_once_with(
                name="test-server",
                allowed_paths=expected_paths,
                project_paths=["/test/project"],
                project_dir="/test/project",
                agent_model=None,
                agent_max_tokens=None,
                agent_api_key=None,
                agent_base_url=None,
                agent_max_iterations=10,
                agent_max_tool_uses=30,
                enable_agent_tool=False,
                command_timeout=120.0,
                disable_write_tools=False,
                disable_search_tools=True,
                host=mock_args.host,
                port=mock_args.port,
            )
            mock_server.run.assert_called_once_with(transport="stdio")


class TestInstallClaudeDesktopConfig:
    """Test the install_claude_desktop_config function."""

    @pytest.fixture
    def mock_platform(self, monkeypatch) -> Callable[[str], str]:
        """Mock the sys.platform value."""
        original_platform = sys.platform

        def _set_platform(plat):
            monkeypatch.setattr(sys, "platform", plat)
            return plat

        yield _set_platform

        # Restore original platform
        monkeypatch.setattr(sys, "platform", original_platform)

    def test_install_config_macos(self, mock_platform: Callable[[str], str], tmp_path: Path) -> None:
        """Test installing config on macOS."""
        # Set platform to macOS
        mock_platform("darwin")

        # Mock home directory and config path
        with patch("pathlib.Path.home", return_value=Path(tmp_path)), patch(
            "sys.executable", "/usr/bin/python3"
        ), patch("json.dump") as mock_json_dump, patch("builtins.open", create=True) as mock_open, patch(
            "pathlib.Path.exists", return_value=False
        ), patch("pathlib.Path.mkdir") as mock_mkdir:
            # Construct expected config path
            config_dir = tmp_path / "Library" / "Application Support" / "Claude"
            config_file = config_dir / "claude_desktop_config.json"

            # Mock file opening
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            # Call the install function
            install_claude_desktop_config("test-server", allowed_paths=["/test/path"])

            # Verify config directory was created
            mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)

            # Verify file was opened correctly
            mock_open.assert_called_once()
            args, kwargs = mock_open.call_args
            assert str(config_file) in str(args[0])
            assert kwargs.get("mode") == "w"
            # Note: The mode parameter is set via a positional argument, not a keyword
            # so we're not checking it here

            # Verify correct config was written
            mock_json_dump.assert_called_once()
            config_data = mock_json_dump.call_args[0][0]
            assert "mcpServers" in config_data
            assert "test-server" in config_data["mcpServers"]
            assert "/usr/bin/python3" in config_data["mcpServers"]["test-server"]["command"]
            assert "--allow-path" in str(config_data["mcpServers"]["test-server"]["args"])
            assert "/test/path" in str(config_data["mcpServers"]["test-server"]["args"])

    def test_install_config_windows(self, mock_platform: Callable[[str], str], tmp_path: Path) -> None:
        """Test installing config on Windows."""
        # Set platform to Windows
        mock_platform("win32")

        # Mock environment variable
        with patch.dict(os.environ, {"APPDATA": str(tmp_path)}), patch(
            "sys.executable", "C:\\Python\\python.exe"
        ), patch("json.dump") as mock_json_dump, patch("builtins.open", create=True) as mock_open, patch(
            "pathlib.Path.exists", return_value=False
        ), patch("pathlib.Path.mkdir") as mock_mkdir:
            # Construct expected config path
            config_dir = Path(tmp_path) / "Claude"
            config_file = config_dir / "claude_desktop_config.json"

            # Mock file opening
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            # Call the install function
            install_claude_desktop_config("test-server")

            # Verify config directory was created
            mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)

            # Verify file was opened correctly
            mock_open.assert_called_once()
            args, kwargs = mock_open.call_args
            assert str(config_file) in str(args[0])

            # Verify correct config was written
            mock_json_dump.assert_called_once()
            config_data = mock_json_dump.call_args[0][0]
            assert "mcpServers" in config_data
            assert "test-server" in config_data["mcpServers"]

    def test_install_config_merge_existing(self, mock_platform: Callable[[str], str], tmp_path: Path) -> None:
        """Test merging with existing config file."""
        # Set platform to Linux
        mock_platform("linux")

        # Create a mock existing config
        existing_config = {
            "mcpServers": {
                "existing-server": {
                    "command": "/usr/bin/python3",
                    "args": ["-m", "existing_module"],
                }
            },
            "otherSetting": "value",
        }

        # Mock home directory and config path
        with patch("pathlib.Path.home", return_value=Path(tmp_path)), patch(
            "sys.executable", "/usr/bin/python3"
        ), patch("json.dump") as mock_json_dump, patch("json.load", return_value=existing_config), patch(
            "builtins.open", create=True
        ) as mock_open, patch("pathlib.Path.exists", return_value=True), patch("pathlib.Path.mkdir") as mock_mkdir:
            # Construct expected config path
            config_dir = tmp_path / ".config" / "claude"
            config_dir / "claude_desktop_config.json"

            # Mock file opening
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            # Call the install function
            install_claude_desktop_config("test-server")

            # Verify config directory was created
            mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)

            # Verify file was opened correctly for reading and writing
            assert mock_open.call_count == 2

            # Verify correct config was written
            mock_json_dump.assert_called_once()
            config_data = mock_json_dump.call_args[0][0]
            assert "mcpServers" in config_data
            assert "existing-server" in config_data["mcpServers"]
            assert "test-server" in config_data["mcpServers"]
            assert "otherSetting" in config_data

    def test_install_config_default_paths(self, mock_platform: Callable[[str], str], tmp_path: Path) -> None:
        """Test installing config with default allowed paths."""
        # Set platform to macOS
        mock_platform("darwin")

        # Mock home directory and config path
        with patch("pathlib.Path.home", return_value=Path(tmp_path)), patch(
            "sys.executable", "/usr/bin/python3"
        ), patch("json.dump") as mock_json_dump, patch("builtins.open", create=True) as mock_open, patch(
            "pathlib.Path.exists", return_value=False
        ), patch("pathlib.Path.mkdir"):
            # Mock file opening
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            # Call the install function without specifying allowed_paths
            install_claude_desktop_config("test-server")

            # Verify correct config was written with home directory as allowed path
            mock_json_dump.assert_called_once()
            config_data = mock_json_dump.call_args[0][0]
            server_args = config_data["mcpServers"]["test-server"]["args"]

            # Verify home directory was added as an allowed path
            assert "--allow-path" in server_args
            home_path_index = server_args.index("--allow-path") + 1
            assert str(tmp_path) in server_args[home_path_index]

            # Verify --disable-write-tools flag is not present
            assert "--disable-write-tools" not in server_args

    def test_install_config_with_disable_write_tools(self, mock_platform: Callable[[str], str], tmp_path: Path) -> None:
        """Test installing config with disable_write_tools=True."""
        # Set platform to macOS
        mock_platform("darwin")

        # Mock home directory and config path
        with patch("pathlib.Path.home", return_value=Path(tmp_path)), patch(
            "sys.executable", "/usr/bin/python3"
        ), patch("json.dump") as mock_json_dump, patch("builtins.open", create=True) as mock_open, patch(
            "pathlib.Path.exists", return_value=False
        ), patch("pathlib.Path.mkdir"):
            # Mock file opening
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            # Call the install function with disable_write_tools=True
            install_claude_desktop_config("test-server", allowed_paths=["/test/path"], disable_write_tools=True)

            # Verify correct config was written
            mock_json_dump.assert_called_once()
            config_data = mock_json_dump.call_args[0][0]
            server_args = config_data["mcpServers"]["test-server"]["args"]

            # Verify allowed path was added
            assert "--allow-path" in server_args
            path_index = server_args.index("--allow-path") + 1
            assert "/test/path" in server_args[path_index]

            # Verify --disable-write-tools flag is present
            assert "--disable-write-tools" in server_args

    def test_install_config_with_disable_search_tools(
        self, mock_platform: Callable[[str], str], tmp_path: Path
    ) -> None:
        """Test installing config with disable_search_tools=True."""
        # Set platform to macOS
        mock_platform("darwin")

        # Mock home directory and config path
        with patch("pathlib.Path.home", return_value=Path(tmp_path)), patch(
            "sys.executable", "/usr/bin/python3"
        ), patch("json.dump") as mock_json_dump, patch("builtins.open", create=True) as mock_open, patch(
            "pathlib.Path.exists", return_value=False
        ), patch("pathlib.Path.mkdir"):
            # Mock file opening
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            # Call the install function with disable_search_tools=True
            install_claude_desktop_config("test-server", allowed_paths=["/test/path"], disable_search_tools=True)

            # Verify correct config was written
            mock_json_dump.assert_called_once()
            config_data = mock_json_dump.call_args[0][0]
            server_args = config_data["mcpServers"]["test-server"]["args"]

            # Verify allowed path was added
            assert "--allow-path" in server_args
            path_index = server_args.index("--allow-path") + 1
            assert "/test/path" in server_args[path_index]

            # Verify --disable-search-tools flag is present
            assert "--disable-search-tools" in server_args

    def test_install_config_with_both_flags(self, mock_platform: Callable[[str], str], tmp_path: Path) -> None:
        """Test installing config with both disable_write_tools and disable_search_tools set to True."""
        # Set platform to macOS
        mock_platform("darwin")

        # Mock home directory and config path
        with patch("pathlib.Path.home", return_value=Path(tmp_path)), patch(
            "sys.executable", "/usr/bin/python3"
        ), patch("json.dump") as mock_json_dump, patch("builtins.open", create=True) as mock_open, patch(
            "pathlib.Path.exists", return_value=False
        ), patch("pathlib.Path.mkdir"):
            # Mock file opening
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            # Call the install function with both flags set to True
            install_claude_desktop_config(
                "test-server",
                allowed_paths=["/test/path"],
                disable_write_tools=True,
                disable_search_tools=True,
            )

            # Verify correct config was written
            mock_json_dump.assert_called_once()
            config_data = mock_json_dump.call_args[0][0]
            server_args = config_data["mcpServers"]["test-server"]["args"]

            # Verify allowed path was added
            assert "--allow-path" in server_args
            path_index = server_args.index("--allow-path") + 1
            assert "/test/path" in server_args[path_index]

            # Verify both flags are present
            assert "--disable-write-tools" in server_args
            assert "--disable-search-tools" in server_args
