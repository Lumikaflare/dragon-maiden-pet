"""Serve this asset package locally. No third-party dependencies."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    handler = partial(SimpleHTTPRequestHandler, directory=str(root))
    print('Preview: http://127.0.0.1:8780 (Ctrl+C to stop)')
    with ThreadingHTTPServer(('127.0.0.1', 8780), handler) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
