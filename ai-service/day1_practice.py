old_payload ={
    "type" : "order.created",
    "data" :{
        "order_id":"ord_123",
        "amount" : 500
    }
}

def repair_payload(payload):
    if not isinstance(payload,dict):
        raise TypeError("payload muse be a dictionary")

    if "type" not in payload:
        raise ValueError("missing feild required type")

    repaired = {
        "event_type" : payload["type"],
        "data": payload.get("data")
    }

    return repaired
repaired = repair_payload(old_payload)
print("original", old_payload)
print("repaired", repaired)

