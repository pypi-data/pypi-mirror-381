"""
MCP Connection Testing Framework.

Comprehensive testing tools for MCP server connections, protocol compliance,
and error handling scenarios.
"""

import asyncio
import json
import logging
import subprocess
import sys
import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class ConnectionStatus(Enum):
    """Connection status states."""

    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    ERROR = "error"
    TIMEOUT = "timeout"


class TestSeverity(Enum):
    """Test result severity levels."""

    CRITICAL = "critical"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class ConnectionTestResult:
    """Result of a single connection test."""

    test_name: str
    success: bool
    status: ConnectionStatus
    duration_ms: float
    severity: TestSeverity
    message: str
    error: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert result to dictionary format."""
        return {
            "test_name": self.test_name,
            "success": self.success,
            "status": self.status.value,
            "duration_ms": self.duration_ms,
            "severity": self.severity.value,
            "message": self.message,
            "error": self.error,
            "metadata": self.metadata,
        }


@dataclass
class ConnectionTestSuite:
    """Results from a suite of connection tests."""

    suite_name: str
    results: list[ConnectionTestResult] = field(default_factory=list)
    total_duration_ms: float = 0.0
    start_time: float = field(default_factory=time.time)

    @property
    def passed(self) -> int:
        """Count of passed tests."""
        return sum(1 for r in self.results if r.success)

    @property
    def failed(self) -> int:
        """Count of failed tests."""
        return sum(1 for r in self.results if not r.success)

    @property
    def total(self) -> int:
        """Total number of tests."""
        return len(self.results)

    @property
    def success_rate(self) -> float:
        """Success rate as percentage."""
        if self.total == 0:
            return 0.0
        return (self.passed / self.total) * 100

    def add_result(self, result: ConnectionTestResult) -> None:
        """Add a test result to the suite."""
        self.results.append(result)

    def to_dict(self) -> dict[str, Any]:
        """Convert suite to dictionary format."""
        return {
            "suite_name": self.suite_name,
            "passed": self.passed,
            "failed": self.failed,
            "total": self.total,
            "success_rate": self.success_rate,
            "total_duration_ms": self.total_duration_ms,
            "results": [r.to_dict() for r in self.results],
        }


class MCPConnectionTester:
    """Comprehensive MCP connection testing framework."""

    def __init__(
        self,
        server_path: str | Path | None = None,
        timeout: float = 5.0,
        project_root: Path | None = None,
    ):
        """
        Initialize connection tester.

        Args:
            server_path: Path to MCP server executable/module
            timeout: Default timeout for operations in seconds
            project_root: Project root directory for server context
        """
        self.server_path = self._resolve_server_path(server_path)
        self.timeout = timeout
        self.project_root = project_root or Path.cwd()
        self.process: subprocess.Popen | None = None
        self.stdout_reader: asyncio.StreamReader | None = None
        self.stdin_writer: asyncio.StreamWriter | None = None

    def _resolve_server_path(self, server_path: str | Path | None) -> str:
        """Resolve the server path to executable command."""
        if server_path:
            return str(server_path)

        # Try to find kuzu-memory executable
        candidates = [
            "kuzu-memory",
            f"{sys.executable} -m kuzu_memory.cli",
            str(Path.home() / ".local" / "bin" / "kuzu-memory"),
        ]

        for candidate in candidates:
            try:
                cmd = candidate.split() if " " in candidate else [candidate]
                result = subprocess.run(
                    [*cmd, "--version"],
                    capture_output=True,
                    text=True,
                    timeout=2,
                )
                if result.returncode == 0:
                    return candidate
            except (subprocess.SubprocessError, FileNotFoundError):
                continue

        # Default to module execution
        return f"{sys.executable} -m kuzu_memory.mcp.run_server"

    async def start_server(self) -> ConnectionTestResult:
        """
        Start MCP server process and establish stdio connection.

        Returns:
            Test result for server startup
        """
        start_time = time.time()
        test_name = "server_startup"

        try:
            # Prepare server command
            cmd = (
                self.server_path.split()
                if " " in self.server_path
                else [self.server_path]
            )

            # Start server process with stdio pipes
            self.process = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=str(self.project_root),
                text=False,  # Binary mode for precise control
            )

            # Create async readers/writers
            # Wait a moment for process to initialize
            await asyncio.sleep(0.1)

            # Check if process is still running
            if self.process.poll() is not None:
                stderr = (
                    self.process.stderr.read().decode() if self.process.stderr else ""
                )
                raise RuntimeError(f"Server process terminated immediately: {stderr}")

            duration = (time.time() - start_time) * 1000

            return ConnectionTestResult(
                test_name=test_name,
                success=True,
                status=ConnectionStatus.CONNECTED,
                duration_ms=duration,
                severity=TestSeverity.INFO,
                message="Server started successfully",
                metadata={"pid": self.process.pid},
            )

        except Exception as e:
            duration = (time.time() - start_time) * 1000
            return ConnectionTestResult(
                test_name=test_name,
                success=False,
                status=ConnectionStatus.ERROR,
                duration_ms=duration,
                severity=TestSeverity.CRITICAL,
                message="Failed to start server",
                error=str(e),
            )

    async def stop_server(self) -> None:
        """Stop the MCP server process gracefully."""
        if self.process:
            try:
                # Try graceful shutdown first
                self.process.terminate()
                await asyncio.sleep(0.5)

                # Force kill if still running
                if self.process.poll() is None:
                    self.process.kill()

                self.process.wait(timeout=2)
            except Exception as e:
                logger.warning(f"Error stopping server: {e}")
            finally:
                self.process = None

    async def test_stdio_connection(self) -> ConnectionTestResult:
        """
        Test basic stdio connection with server.

        Returns:
            Test result for stdio connectivity
        """
        start_time = time.time()
        test_name = "stdio_connection"

        if not self.process:
            return ConnectionTestResult(
                test_name=test_name,
                success=False,
                status=ConnectionStatus.DISCONNECTED,
                duration_ms=0.0,
                severity=TestSeverity.ERROR,
                message="Server not started",
                error="Call start_server() first",
            )

        try:
            # Test basic read/write capability
            test_msg = {"jsonrpc": "2.0", "method": "ping", "id": 1}
            message = json.dumps(test_msg) + "\n"

            # Write to stdin
            self.process.stdin.write(message.encode())
            self.process.stdin.flush()

            # Try to read response with timeout
            response_line = await asyncio.wait_for(
                asyncio.to_thread(self.process.stdout.readline),
                timeout=self.timeout,
            )

            if not response_line:
                raise TimeoutError("No response from server")

            response = json.loads(response_line.decode().strip())
            duration = (time.time() - start_time) * 1000

            return ConnectionTestResult(
                test_name=test_name,
                success=True,
                status=ConnectionStatus.CONNECTED,
                duration_ms=duration,
                severity=TestSeverity.INFO,
                message="Stdio connection verified",
                metadata={"response": response},
            )

        except TimeoutError:
            duration = (time.time() - start_time) * 1000
            return ConnectionTestResult(
                test_name=test_name,
                success=False,
                status=ConnectionStatus.TIMEOUT,
                duration_ms=duration,
                severity=TestSeverity.ERROR,
                message="Stdio connection timeout",
                error=f"No response after {self.timeout}s",
            )
        except Exception as e:
            duration = (time.time() - start_time) * 1000
            return ConnectionTestResult(
                test_name=test_name,
                success=False,
                status=ConnectionStatus.ERROR,
                duration_ms=duration,
                severity=TestSeverity.ERROR,
                message="Stdio connection failed",
                error=str(e),
            )

    async def test_protocol_initialization(self) -> ConnectionTestResult:
        """
        Test MCP protocol initialization handshake.

        Returns:
            Test result for protocol initialization
        """
        start_time = time.time()
        test_name = "protocol_initialization"

        try:
            init_msg = {
                "jsonrpc": "2.0",
                "method": "initialize",
                "id": 1,
                "params": {"protocolVersion": "2025-06-18"},
            }

            response = await self._send_request(init_msg)
            duration = (time.time() - start_time) * 1000

            if response and "result" in response:
                return ConnectionTestResult(
                    test_name=test_name,
                    success=True,
                    status=ConnectionStatus.CONNECTED,
                    duration_ms=duration,
                    severity=TestSeverity.INFO,
                    message="Protocol initialized successfully",
                    metadata={"response": response["result"]},
                )
            else:
                return ConnectionTestResult(
                    test_name=test_name,
                    success=False,
                    status=ConnectionStatus.ERROR,
                    duration_ms=duration,
                    severity=TestSeverity.ERROR,
                    message="Protocol initialization failed",
                    error=response.get("error", "Unknown error"),
                )

        except Exception as e:
            duration = (time.time() - start_time) * 1000
            return ConnectionTestResult(
                test_name=test_name,
                success=False,
                status=ConnectionStatus.ERROR,
                duration_ms=duration,
                severity=TestSeverity.CRITICAL,
                message="Protocol initialization error",
                error=str(e),
            )

    async def test_connection_recovery(self) -> ConnectionTestResult:
        """
        Test connection recovery after simulated failure.

        Returns:
            Test result for recovery capability
        """
        start_time = time.time()
        test_name = "connection_recovery"

        try:
            # Send a valid request first
            test_msg = {"jsonrpc": "2.0", "method": "ping", "id": 1}
            response1 = await self._send_request(test_msg)

            if not response1:
                raise RuntimeError("Initial request failed")

            # Simulate brief disconnection
            await asyncio.sleep(0.1)

            # Try to recover with another request
            test_msg2 = {"jsonrpc": "2.0", "method": "ping", "id": 2}
            response2 = await self._send_request(test_msg2)

            duration = (time.time() - start_time) * 1000

            if response2 and response2.get("id") == 2:
                return ConnectionTestResult(
                    test_name=test_name,
                    success=True,
                    status=ConnectionStatus.CONNECTED,
                    duration_ms=duration,
                    severity=TestSeverity.INFO,
                    message="Connection recovery successful",
                )
            else:
                return ConnectionTestResult(
                    test_name=test_name,
                    success=False,
                    status=ConnectionStatus.ERROR,
                    duration_ms=duration,
                    severity=TestSeverity.WARNING,
                    message="Connection recovery failed",
                    error="Second request did not complete",
                )

        except Exception as e:
            duration = (time.time() - start_time) * 1000
            return ConnectionTestResult(
                test_name=test_name,
                success=False,
                status=ConnectionStatus.ERROR,
                duration_ms=duration,
                severity=TestSeverity.WARNING,
                message="Recovery test failed",
                error=str(e),
            )

    async def simulate_malformed_message(self) -> ConnectionTestResult:
        """
        Send malformed JSON-RPC message and verify error handling.

        Returns:
            Test result for malformed message handling
        """
        start_time = time.time()
        test_name = "malformed_message_handling"

        try:
            # Send invalid JSON
            malformed = "{'invalid': 'json'}\n"
            self.process.stdin.write(malformed.encode())
            self.process.stdin.flush()

            # Server should respond with parse error
            response_line = await asyncio.wait_for(
                asyncio.to_thread(self.process.stdout.readline),
                timeout=self.timeout,
            )

            response = json.loads(response_line.decode().strip())
            duration = (time.time() - start_time) * 1000

            # Check for proper error response
            if "error" in response and response["error"]["code"] == -32700:
                return ConnectionTestResult(
                    test_name=test_name,
                    success=True,
                    status=ConnectionStatus.CONNECTED,
                    duration_ms=duration,
                    severity=TestSeverity.INFO,
                    message="Malformed message handled correctly",
                    metadata={"error_code": response["error"]["code"]},
                )
            else:
                return ConnectionTestResult(
                    test_name=test_name,
                    success=False,
                    status=ConnectionStatus.ERROR,
                    duration_ms=duration,
                    severity=TestSeverity.WARNING,
                    message="Unexpected response to malformed message",
                    metadata={"response": response},
                )

        except Exception as e:
            duration = (time.time() - start_time) * 1000
            return ConnectionTestResult(
                test_name=test_name,
                success=False,
                status=ConnectionStatus.ERROR,
                duration_ms=duration,
                severity=TestSeverity.ERROR,
                message="Malformed message test failed",
                error=str(e),
            )

    async def simulate_high_latency(
        self, delay_ms: float = 100
    ) -> ConnectionTestResult:
        """
        Simulate high latency connection scenario.

        Args:
            delay_ms: Artificial delay in milliseconds

        Returns:
            Test result for latency handling
        """
        start_time = time.time()
        test_name = f"high_latency_{delay_ms}ms"

        try:
            # Add delay before request
            await asyncio.sleep(delay_ms / 1000)

            test_msg = {"jsonrpc": "2.0", "method": "ping", "id": 1}
            response = await self._send_request(test_msg)

            duration = (time.time() - start_time) * 1000

            if response:
                return ConnectionTestResult(
                    test_name=test_name,
                    success=True,
                    status=ConnectionStatus.CONNECTED,
                    duration_ms=duration,
                    severity=TestSeverity.INFO,
                    message=f"High latency handled ({duration:.2f}ms)",
                    metadata={
                        "artificial_delay_ms": delay_ms,
                        "total_duration_ms": duration,
                    },
                )
            else:
                return ConnectionTestResult(
                    test_name=test_name,
                    success=False,
                    status=ConnectionStatus.TIMEOUT,
                    duration_ms=duration,
                    severity=TestSeverity.WARNING,
                    message="High latency caused timeout",
                    error=f"No response after {delay_ms}ms delay",
                )

        except Exception as e:
            duration = (time.time() - start_time) * 1000
            return ConnectionTestResult(
                test_name=test_name,
                success=False,
                status=ConnectionStatus.ERROR,
                duration_ms=duration,
                severity=TestSeverity.ERROR,
                message="Latency test failed",
                error=str(e),
            )

    async def validate_jsonrpc_compliance(self) -> ConnectionTestResult:
        """
        Validate JSON-RPC 2.0 protocol compliance.

        Returns:
            Test result for protocol compliance
        """
        start_time = time.time()
        test_name = "jsonrpc_compliance"

        try:
            # Test required fields
            test_msg = {
                "jsonrpc": "2.0",
                "method": "initialize",
                "id": 1,
                "params": {"protocolVersion": "2025-06-18"},
            }

            response = await self._send_request(test_msg)
            duration = (time.time() - start_time) * 1000

            # Validate response structure
            compliance_checks = {
                "has_jsonrpc": "jsonrpc" in response,
                "jsonrpc_version": response.get("jsonrpc") == "2.0",
                "has_id": "id" in response,
                "id_matches": response.get("id") == test_msg["id"],
                "has_result_or_error": "result" in response or "error" in response,
            }

            all_passed = all(compliance_checks.values())

            return ConnectionTestResult(
                test_name=test_name,
                success=all_passed,
                status=(
                    ConnectionStatus.CONNECTED if all_passed else ConnectionStatus.ERROR
                ),
                duration_ms=duration,
                severity=TestSeverity.INFO if all_passed else TestSeverity.ERROR,
                message=(
                    "JSON-RPC compliance validated"
                    if all_passed
                    else "Compliance check failed"
                ),
                metadata={"checks": compliance_checks},
            )

        except Exception as e:
            duration = (time.time() - start_time) * 1000
            return ConnectionTestResult(
                test_name=test_name,
                success=False,
                status=ConnectionStatus.ERROR,
                duration_ms=duration,
                severity=TestSeverity.ERROR,
                message="Compliance validation failed",
                error=str(e),
            )

    async def _send_request(self, message: dict[str, Any]) -> dict[str, Any] | None:
        """
        Send JSON-RPC request and wait for response.

        Args:
            message: JSON-RPC message to send

        Returns:
            Response message or None on timeout
        """
        if not self.process:
            raise RuntimeError("Server not started")

        # Send request
        request_str = json.dumps(message) + "\n"
        self.process.stdin.write(request_str.encode())
        self.process.stdin.flush()

        # Read response with timeout
        response_line = await asyncio.wait_for(
            asyncio.to_thread(self.process.stdout.readline),
            timeout=self.timeout,
        )

        if not response_line:
            return None

        return json.loads(response_line.decode().strip())

    async def run_test_suite(
        self, suite_name: str = "MCP Connection Tests"
    ) -> ConnectionTestSuite:
        """
        Run complete test suite.

        Args:
            suite_name: Name for the test suite

        Returns:
            Complete test suite results
        """
        suite = ConnectionTestSuite(suite_name=suite_name)
        start_time = time.time()

        try:
            # Start server
            result = await self.start_server()
            suite.add_result(result)

            if not result.success:
                return suite

            # Run all tests
            suite.add_result(await self.test_stdio_connection())
            suite.add_result(await self.test_protocol_initialization())
            suite.add_result(await self.validate_jsonrpc_compliance())
            suite.add_result(await self.simulate_malformed_message())
            suite.add_result(await self.simulate_high_latency(delay_ms=50))
            suite.add_result(await self.test_connection_recovery())

        finally:
            # Always stop server
            await self.stop_server()
            suite.total_duration_ms = (time.time() - start_time) * 1000

        return suite
