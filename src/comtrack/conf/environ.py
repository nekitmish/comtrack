"""Read .env file"""
import environ  # type: ignore

env = environ.Env(
    DEBUG=(bool, False),
)

environ.Env.read_env('comtrack/.env')  # reading .env file

__all__ = [
    env,
]
