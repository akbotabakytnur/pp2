import json

with open("/Users/akbota/Desktop/pp2/practice4/sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':8} {'MTU'}")
print("-" * 80)

for item in data["imdata"]:
    dn=item["l1PhysIf"]["attributes"]["dn"]
    descr=item["l1PhysIf"]["attributes"]["descr"]
    speed=item["l1PhysIf"]["attributes"]["speed"]
    mtu=item["l1PhysIf"]["attributes"]["mtu"]
   
    print(f"{dn:50} {descr:20} {speed:8} {mtu}")