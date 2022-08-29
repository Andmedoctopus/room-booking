from dataclasses import replace

def sync_ids_with_enitities(ids, entities):
    return [
        replace(room_entity, room_id=new_id)
        for room_entity, new_id in zip(entities, ids)
    ]
