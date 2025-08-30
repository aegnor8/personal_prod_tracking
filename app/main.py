from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
from producer import send_unlock_event

app = FastAPI(title="Personal Productivity Tracker API ", version="1.0.0")

class UnlockEvent(BaseModel):
    device_id: str
    timestamp: float # epoch
    event_id: str = None

@app.post("/unlock", status_code=201)
async def receive_unlock(event: UnlockEvent):
    if not event.event_id:
        event.event_id = str(uuid4())
    
    send_unlock_event(key=event.event_id, value=event.model_dump_json())
    return {"status": "success", "event_id": event.event_id}
# To run the app, use the command: uvicorn app.main:app --reload