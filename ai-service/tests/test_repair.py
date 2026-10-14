import pytest
from day1_practice import repair_payload

def test_repair_valid_payload():
    payload = {
        "type" : "order.created",
        "data" : {
            "order_id" : "ord_123"
        }
    }

    repaired  =  repair_payload(payload)

    assert repaired == {
        "event_type" :"order.created",
        "data" : {
            "order_id": "ord_123"
        }
    }

    def test_missing_type_raises_error():
        payload ={
            "data" :{
                "order_id": "ord_123"
            }
        }

        with pytest.raises(ValueError):
            repair_payload(payload)

    def test_non_dictionary_raises_error():
        with pytest.raises(TypeError):
            repair_payload(["not" ,"a" ,"dictionary"])
