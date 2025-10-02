#!/usr/bin/env python3
# vim: fileencoding=utf-8 ts=4
# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: © Copyright 2024, 2025 by Christian Dönges. All rights reserved.
# SPDXID: SPDXRef-test-chunkystreamsocket-py
"""Unit tests for ChunkyStreamSocket."""

from dataclasses import dataclass
import socket
import threading
import time

import pytest
from pymisclib.chunkystreamsocket import ChunkyStreamSocket


@dataclass
class EchoServer:
    """Simple test server that accepts connections and echos all input."""
    _backlog: int = 0  # allow no connection backlog
    _loop_time: float = 0.1
    _running: bool = False
    _sock: socket.socket|None = None
    _thread: threading.Thread|None = None

    @property
    def port(self) -> int|None:
        """Return the server port."""
        if self._sock is None:
            return None
        return self._sock.getsockname()[1]

    @property
    def running(self) -> bool:
        """True if the loop is running."""
        return self._running

    @property
    def sock(self) -> socket.socket|None:
        """Return the OS socket or None if there is none."""
        return self._sock

    def _client_loop(self,
                     client_sock: socket.socket):
        """Handle client connections while running."""
        client_sock.settimeout(self._loop_time)
        while self._running:
            try:
                msg = client_sock.recv(1)
                client_sock.sendall(msg)
            except socket.timeout:
                pass
            except OSError:
                break
        try:
            client_sock.close()
        except OSError:
            pass

    def _run_loop(self):
        """While running, accept client connections."""
        if self._running:
            raise RuntimeError('Server is already running.')
        self._sock = socket.socket()
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.bind(('localhost', 0))  # bind to a free port
        self.sock.listen(self._backlog)
        self._running = True
        self._sock.settimeout(0.1)  # all socket operations time out after 100 ms
        while self._running:
            try:
                client_sock, client_addr = self._sock.accept()
                self._client_loop(client_sock)
            except socket.timeout:
                pass  # ignore to allow checking for shutdown
        self._sock.close()
        self._sock = None

    def run(self):
        """Run server in a new thread."""
        self._thread = threading.Thread(target=self._run_loop)
        self._thread.start()
        while not self._running:
            time.sleep(0.001)

    def stop(self):
        """Stop the server."""
        self._running = False
        self._thread.join(5.0)
        self._thread = None


@pytest.fixture(autouse=True)
def server() -> EchoServer:
    """Fixture to start an EchoServer before running the test function."""
    server = EchoServer()
    server.run()
    yield server  # run test function
    server.stop()


@pytest.fixture()
def used_port() -> int:
    """Fixture that creates a socket to block a port.

    The fixture returns the port number. Since the socket on the port
    is not serviced, connections to it will be refused.
    """
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('localhost', 0))  # bind to a free port
    yield s.getsockname()[1]  # run test function
    s.close()


def connect_and_check(es: EchoServer,
                      css: ChunkyStreamSocket,
                      timeout: float|None):
    """Connect and validate the connection.

    :param EchoServer es: EchoServer instance to connect to.
    :param ChunkyStreamSocket css: Socket instance to connect from.
    :param float timeout: Timeout to wait for the connection.
    """
    css.connect(timeout)
    addr, port = css.sock.getpeername()
    assert addr == '127.0.0.1'
    assert port == es.port


@pytest.mark.parametrize('timeout', [1.0, 0, None])
def test_connect_ok(server, timeout):
    """Test connection to an existing server for various client socket timeouts."""
    with ChunkyStreamSocket(host='127.0.0.1', port=server.port) as c:
        try:
            connect_and_check(server, c, timeout=timeout)
        except BlockingIOError:
            # A non-blocking connection attempt, e.g. connect(timeout=0),
            # will almost always fail on the first try. So we give it some
            # time and try again.
            assert timeout == 0
            time.sleep(0.1)  # since this is local, 100 ms should be plenty.
            connect_and_check(server, c, timeout=timeout)


@pytest.mark.parametrize('timeout', [0.2, 0, None])
def test_connect_err_connection(server, timeout):
    """Test connection with a timeout to a non-existing IP address."""
    with ChunkyStreamSocket(host='192.0.2.1', port=server.port) as c:
        with pytest.raises(ConnectionError):
            try:
                c.connect(timeout)
            except BlockingIOError:
                # A non-blocking connection attempt, e.g. connect(timeout=0),
                # will almost always fail on the first try. So we give it some
                # time and try again.
                assert timeout == 0
                time.sleep(0.1)  # since this is local, 100 ms should be plenty.
                c.connect(timeout)


@pytest.mark.parametrize('timeout', [0.2, 0, None])
def test_connect_err_refused(server, timeout, used_port):
    """Test connection that is refused."""
    with ChunkyStreamSocket(host='127.0.0.1', port=used_port) as c:
        with pytest.raises(ConnectionError):
            try:
                c.connect(timeout)
            except BlockingIOError:
                # A non-blocking connection attempt, e.g. connect(timeout=0),
                # will almost always fail on the first try. So we give it some
                # time and try again.
                assert timeout == 0
                time.sleep(0.1)  # since this is local, 100 ms should be plenty.
                c.connect(timeout)


def test_connect_err_timout(server):
    """Test connection request timing out."""
    # Implementation note: this relies on socket.listen(backlog=N)
    # to actually limit the socket backlog to N. This assumption
    # is not necessarily true, so we set the backlog to zero and
    # create a large number of connections.
    css = []
    with pytest.raises(TimeoutError):
        for i in range(4096):
            c = ChunkyStreamSocket(host='127.0.0.1', port=server.port)
            c.connect(timeout=0.1)
            css.append(c)


def test_method_connection_ok(server):
    """Test the connection() method."""
    with ChunkyStreamSocket(host='127.0.0.1', port=server.port) as c:
        assert isinstance(c.connection, str)
        c.connect()
        assert isinstance(c.connection, str)
        c.close()
        assert isinstance(c.connection, str)


def test_property_connected_ok(server):
    """Test the connected property."""
    with ChunkyStreamSocket(host='127.0.0.1', port=server.port) as c:
        assert not c.connected
        c.connect()
        assert c.connected
        c.close()
        assert not c.connected


def test_property_server_socket_ok():
    with ChunkyStreamSocket(host='127.0.0.1', port=0) as c:
        assert not c.server_socket
        c.bind_and_listen(0)
        assert c.server_socket
        c.close()
        assert not c.server_socket


@pytest.mark.parametrize('timeout', [0.1, 0, None])
def test_send_and_receive_ok(server, timeout):
    """Test sending and receiving messages."""
    messages = [
        b'',
        b'abc',
        b'\x00\x01\x02\x03\x04',
        bytes(range(256)),
        b'The quick brown fox jumps over the lazy dog' * 1024,
    ]
    with ChunkyStreamSocket(host='127.0.0.1', port=server.port) as c:
        try:
            connect_and_check(server, c, timeout=timeout)
        except BlockingIOError:
            # A non-blocking connection attempt, e.g. connect(timeout=0),
            # will almost always fail on the first try. So we give it some
            # time and try again.
            assert timeout == 0
            time.sleep(0.1)  # since this is local, 100 ms should be plenty.
            connect_and_check(server, c, timeout=timeout)
        for message in messages:
            c.send(message)
            rx_msg = c.recv(len(message))
            assert rx_msg == message


def test_method_close_ok():
    """Test the close() method."""
    c = ChunkyStreamSocket(host='127.0.0.1', port=0)
    c.close()
    assert c.sock is None
