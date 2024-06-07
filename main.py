from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RuleInputs(BaseModel):
    action: str
    protocol: str
    source_ip: str
    source_port: int
    dest_ip: str
    dest_port: int
    sid: str
    rev_num: int
    msg: str

# Snort Rule Generator
@app.post('/rule/')
async def make_rule(inputs: RuleInputs):
    try:
        final_rule = ""
        final_rule += inputs.action
        final_rule += " " + inputs.protocol
        final_rule += " " + inputs.source_ip
        final_rule += " " + str(inputs.source_port)
        final_rule += " -> " + inputs.dest_ip
        final_rule += " " + str(inputs.dest_port)
        final_rule += " (msg:\"" + inputs.msg
        final_rule += "\"; sid:" + inputs.sid
        final_rule += "; rev:" + str(inputs.rev_num) + ";)"
        return {'final_rule': final_rule}
    except:
        raise Exception("Incorrect values entered.")

# Example usage
if __name__ == "__main__":
    from fastapi.testclient import TestClient

    client = TestClient(app)

    # Example request
    response = client.post("/rule/", json={
        "action": "ALLOW",
        "protocol": "TCP",
        "source_ip": "192.168.1.1",
        "source_port": 8080,
        "dest_ip": "192.168.1.2",
        "dest_port": 80,
        "sid": "12345",
        "rev_num": 1,
        "msg": "Sample Rule"
    })

    # Check the response
    if response.status_code == 200:
        print(response.json()['final_rule'])
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
