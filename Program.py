import json
import adh_sample_library_preview

# --- User specified variables ---
eventTypeId=""
deleteEventType=False
# --------------------------------

appsettings = {}
with open('appsettings.json', 'r') as f:
    appsettings = json.load(f)

adh_client = adh_sample_library_preview.ADHClient(
        appsettings.get('ApiVersion'),
        appsettings.get('TenantId'),
        appsettings.get('Resource'),
        appsettings.get('ClientId'),
        appsettings.get('ClientSecret')
    )
namespaceid = appsettings.get('NamespaceId')

print(f"Attempting to get events for EventTypeId {eventTypeId}. This may take some time for large numbers of events...")

def getEvents(namespaceid,selectedEventType,filter,continuation_token=""):
  result = []
  while True:
    response = adh_client.Events.getEvents(namespaceid,selectedEventType, fields="id", filter=filter,continuation_token=continuation_token)
    for event in response['Results']:
      result.append(event)
    continuation_token = response['ContinuationToken']
    if continuation_token == "":
      break
  return result

eventType = adh_client.EventTypes.getEventType(namespace_id=namespaceid, event_type_id=eventTypeId)
events = getEvents(namespaceid=namespaceid,selectedEventType=eventType.Id,filter=None)
print(f"Found {len(events)} events to delete for EventTypeId {eventType.Id}.  DeleteEventType: {deleteEventType}")

proceed = input("Continue? (y/n)")

if proceed in ["y", "Y", "yes", "Yes"]:
  for event in events:
    print(f"Deleting event with id: {event["id"]}")
    adh_client.Events.deleteEvent(namespace_id=namespaceid,event_type_id=eventType.Id,event_id=event["id"])
  if deleteEventType:
    print(f"Deleting event type with id: {eventType.Id}")
    # cannot delete the event type without marking it as "Deprecated" first
    eventType.State = adh_sample_library_preview.LifeCycleState.Deprecated
    adh_client.EventTypes.updateEventType(namespace_id=namespaceid, event_type_id=eventType.Id, event_type=eventType)
    adh_client.EventTypes.deleteEventType(namespace_id=namespaceid, event_type_id=eventType.Id)
else:
  print("Exiting...")