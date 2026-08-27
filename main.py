import sys
import os
import uvicorn

# Root entrypoint for PayBridge application
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from backend.app.main import app

def main():
    """Run PayBridge FastAPI application server."""
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    print(f"Starting PayBridge Application Server on http://{host}:{port}...")
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    main()
