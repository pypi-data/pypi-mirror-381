# 辅助读书做笔记的插件服务
from fastapi import APIRouter, Depends, HTTPException, status, Header
import os
from db_help.mysql import MySQLManager
from datetime import datetime
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv(override = True)

async def check_current_user(token: str = Header(...)):
    if token != os.getenv("token"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid X-Token header")
    return {"username":"zxf"}

router = APIRouter(
    tags=["Reader"],
    dependencies = [Depends(check_current_user)]
)

db_manager = MySQLManager(database = "Reader")

@router.get('/')
async def get_status():
    return "running"

class BookTips(BaseModel):
    text: str

@router.post('/record')
async def record(request: BookTips):
    text = request.text
    db_manager.insert(table_name = "reader",
                      data={'time': datetime.now(),
                            "content":text})
    return "successful"


@router.get('/read')
async def read():
    contents = db_manager.select(table_name = "reader",
                      conditions="time > %s", params=(30,),
                      order_by="time DESC"
                      )
    if contents:
        content_list = [i.get("content") for i in contents]
        content = '\n\n'.join(content_list)
    return content


