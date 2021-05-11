from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field, validator

from app.encryptor import CYPHER_TYPE_ERR_MSG, CypherType, get_encryptor

app = FastAPI()


class DataToEncrypt(BaseModel):
    data: bytes = Field()
    key: str = Field()
    cypher_type: Optional[str] = Field(default="aes", description=CYPHER_TYPE_ERR_MSG)

    @validator("cypher_type")
    def cypher_type_validator(cls, v):
        if v.lower() not in CypherType.names():
            raise ValueError(CYPHER_TYPE_ERR_MSG)
        return v


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/encrypt", status_code=201)
def encrypt(req: DataToEncrypt):
    """
    Encrypt data using key
    """
    cypher, ok = get_encryptor(req.cypher_type)
    if not ok:
        raise HTTPException(status_code=421, detail=CYPHER_TYPE_ERR_MSG)
    cypher_text = cypher.encrypt(req.data, req.key)
    return {"data": cypher_text}


@app.post("/decrypt", status_code=201)
def decrypt(req: DataToEncrypt):
    """
    Encrypt data using key
    """
    cypher, ok = get_encryptor(req.cypher_type)
    if not ok:
        raise HTTPException(status_code=421, detail=CYPHER_TYPE_ERR_MSG)
    plain_text = cypher.decrypt(req.data, req.key)
    return {"data": plain_text}

