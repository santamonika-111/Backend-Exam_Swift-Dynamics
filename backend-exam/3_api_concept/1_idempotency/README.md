## Question
![](/assets/q_idempotency.png)
## Response Section
Idempotency คือการเรียก API ซ้ำหลายครั้งแล้ว “ผลลัพธ์ต้องเหมือนเดิม” ไม่ว่าจะยิง request กี่ครั้ง ระบบต้องไม่เปลี่ยน state เกินครั้งแรก

Ex. Implement

from fastapi import FastAPI, Header
from typing import Optional

app = FastAPI()

# จำลอง storage
processed_requests = {}

@app.post("/create-order")
def create_order(amount: int, idempotency_key: Optional[str] = Header(None)):
    
    if idempotency_key in processed_requests:
        return {
            "status": "duplicate",
            "data": processed_requests[idempotency_key]
        }
    
    # simulate create order
    order = {
        "order_id": len(processed_requests) + 1,
        "amount": amount
    }
    
    processed_requests[idempotency_key] = order
    
    return {
        "status": "created",
        "data": order
    }