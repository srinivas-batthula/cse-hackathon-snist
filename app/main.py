# app/main.py
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded
from app.utils import limiter
from app.routes import router


load_dotenv()   # Load environment variables

app = FastAPI(title="Hackathon API")

# Setup rate-limiter
# app.state.limiter = limiter

# @app.exception_handler(RateLimitExceeded)
# async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
#     return JSONResponse(
#         status_code=429,
#         content={"detail": "Rate limit exceeded. Please try again later after 2-mins (30-reqs / 2-mins)."}
#     )

# Enable CORS for all origins (dev-friendly)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)
