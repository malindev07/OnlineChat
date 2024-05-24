import contextlib

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@contextlib.contextmanager
def lifespan():
    pass


uvicorn.run(app)
