import itertools
import requests
import datetime

def distribute_materials(packing_list, warehouse_materials):
    # Initialize the warehouse_log and events_log dictionaries
    warehouse_log = warehouse_materials
    events_log = {event: {material: packing_list['event'][event]['materials'][material]['quantity'] for material in packing_list['event'][event]['materials']} for event in packing_list['event'] if event != 'Warehouse'}
    material_distribution = {}

    # Create all the combinations of events and calculate the distance
    events = list(packing_list['event'].keys())
    event_combinations = list(itertools.combinations(events, 2))

    distances_and_transit_times = {}
    for event1, event2 in event_combinations:
        if event1 == event2:
            continue
        event1_coordinates = packing_list['event'][event1]['coordinates']
        event2_coordinates = packing_list['event'][event2]['coordinates']
        if event1_coordinates != event2_coordinates:
            # Make the API request
            api_key = 'AnHQFhGPMT1HY3GFaRxegUsta7C81GqDAA8u5LFGZxeGd0iZM1Vz6cj2HUYQ1xTq'
            origin = f'{event1_coordinates["latitude"]}, {event1_coordinates["longitude"]}'
            destination = f'{event2_coordinates["latitude"]}, {event2_coordinates["longitude"]}'
            url = f'https://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0={origin}&wp.1={destination}&key={api_key}'
            response = requests.get(url)
            data = response.json()['resourceSets'][0]['resources'][0]
            # Extract the distance from the API response
            distance = data['travelDistance']
            transit_time = distance / 70 # assuming a truck goes at 70kmph
            distances_and_transit_times[f"{event1}-{event2}"] = {'distance': distance, 'transit_time': transit_time}
    print(distances_and_transit_times)

    ...
material_distribution = {}

# Iterate through the events to find the best event to transfer material to
for event1, event1_info in packing_list['event'].items():
    if event1 != 'Warehouse':
        for event2, event2_info in packing_list['event'].items():
            if event2 != 'Warehouse' and event1 != event2:
                event1_date = datetime.datetime.strptime(event1_info['event_date'], "%Y-%m-%d")
                event2_date = datetime.datetime.strptime(event2_info['event_date'], "%Y-%m-%d")
                date_difference = (event2_date - event1_date).days
                if date_difference >= 3:
                    for material, material_info in event1_info['materials'].items():
                        material_difference = material_info['quantity'] - event2_info['materials'][material]['quantity']
                        if material_difference > 0:
                            best_event = None
                            best_distance = None
                            best_transit_time = None
                            for other_event, other_event_info in packing_list['event'].items():
                                if other_event != event1 and other_event != event2 and other_event != "Warehouse":
                                    other_event_date = datetime.strptime(other_event_info['event_date'], "%Y-%m-%d")
                                    date_difference = (other_event_date - event2_date).days
                                    if date_difference >= 3:
                                        for material, material_info in other_event_info['materials'].items():
                                            other_material_difference = material_info['quantity'] - event2_info['materials'][material]['quantity']
                                            if other_material_difference < material_difference:
                                                material_key = f"{material}-{event2}"
                                                if material_key in material_distribution:
                                                    material_distribution[material_key]["quantity"] += material_difference
                                                else:
                                                    material_distribution[material_key] = {"event_from": event1, "event_to": event2, "quantity": material_difference}
                                                # update warehouse_log
                                                warehouse_log[material] -= material_difference
                                                # update events_log
                                                events_log[event1][material]["quantity"] -= material_difference
                                                events_log[event2][material]["quantity"] += material_difference
                                                material_difference = other_material_difference
    return material_distribution
