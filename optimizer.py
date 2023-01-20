import itertools
import requests
from datetime import datetime, timedelta
from PyEmission import EmissionCalculator

packing_list = {
    'event': {
        'Imola' : {
            'event_date': '2023-05-21',
            'coordinates': {
                'latitude': 44.34476471528354,
                'longitude': 11.715646750249338
            },
            'materials': {
                    'floor': {
                        'quantity': 20,
                        'length': 500,
                        'width': 250,
                        'height': 10,
                        'weight': 440
                    },
                    'tent': {
                        'quantity': 10,
                        'length': 500,
                        'width': 120,
                        'height': 110,
                        'weight': 500
                },
                    'pitstop': {
                        'quantity': 5,
                        'length': 180,
                        'width': 80,
                        'height': 180,
                        'weight': 300
                },
                    'shopfit': {
                        'quantity': 15,
                        'length': 240,
                        'width': 120,
                        'height': 50,
                        'weight': 300}
            },
        },
        'Monaco': {
            'event_date': '2023-05-28',
            'coordinates': {
                'latitude': 43.741259321422476,
                'longitude': 7.428875837919547
            },
            'materials': {
                'floor': {
                    'quantity': 10,
                    'length': 500,
                    'width': 250,
                    'height': 10,
                    'weight': 440
                },
                'tent': {
                    'quantity': 5,
                    'length': 500,
                    'width': 120,
                    'height': 110,
                    'weight': 500
                },
                'pitstop': {
                    'quantity': 7,
                    'length': 180,
                    'width': 80,
                    'height': 180,
                    'weight': 300
                },
                'shopfit': {
                    'quantity': 4,
                    'length': 240,
                    'width': 120,
                    'height': 50,
                    'weight': 300}
            },
            },
        'Barcelona' : {
            'event_date': '2023-06-04',
            'coordinates': {
                'latitude': 41.56978402719435,
                'longitude': 2.258749591000082
            },
            'materials': {
                'floor': {
                    'quantity': 124,
                    'length': 500,
                    'width': 250,
                    'height': 10,
                    'weight': 440
                },
                'tent': {
                    'quantity': 62,
                    'length': 500,
                    'width': 120,
                    'height': 110,
                    'weight': 500
                },
                'pitstop': {
                    'quantity': 22,
                    'length': 180,
                    'width': 80,
                    'height': 180,
                    'weight': 300
                },
                'shopfit': {
                    'quantity': 41,
                    'length': 240,
                    'width': 120,
                    'height': 50,
                    'weight': 300}
            },
            },
        'Spielberg' : {
            'event_date': '2023-07-02',
            'coordinates': {
                        'latitude': 43.741259321422476,
                        'longitude': 7.428875837919547
                    },
            'materials': {
                    'floor': {
                        'quantity': 136,
                        'length': 500,
                        'width': 250,
                        'height': 10,
                        'weight': 440
                    },
                    'tent': {
                        'quantity': 68,
                        'length': 500,
                        'width': 120,
                        'height': 110,
                        'weight': 500
                    },
                    'pitstop': {
                        'quantity': 13,
                        'length': 180,
                        'width': 80,
                        'height': 180,
                        'weight': 300
                    },
                    'shopfit': {
                        'quantity': 7,
                        'length': 240,
                        'width': 120,
                        'height': 50,
                        'weight': 300}
        }

            },
        'Silverstone' : {
            'event_date': '2023-07-09',
            'coordinates': {
                        'latitude': 52.072962236567086,
                        'longitude': -1.0151699777668515
                    },
            'materials' : {
                        'floor': {
                            'quantity': 320,
                            'length': 500,
                            'width': 250,
                            'height': 10,
                            'weight': 440
                        },
                        'tent': {
                            'quantity': 157,
                            'length': 500,
                            'width': 120,
                            'height': 110,
                            'weight': 500
                        },
                        'pitstop': {
                            'quantity': 29,
                            'length': 180,
                            'width': 80,
                            'height': 180,
                            'weight': 300
                        },
                        'shopfit': {
                            'quantity': 88,
                            'length': 240,
                            'width': 120,
                            'height': 50,
                            'weight': 300}
                    },
            },
        'Budapest' : {
            'event_date': '2023-07-23',
            'coordinates': {
                        'latitude': 47.5794940564561,
                        'longitude': 19.238891023173604
                    },
            'materials' : {
                        'floor': {
                            'quantity': 122,
                            'length': 500,
                            'width': 250,
                            'height': 10,
                            'weight': 440
                        },
                        'tent': {
                            'quantity': 61,
                            'length': 500,
                            'width': 120,
                            'height': 110,
                            'weight': 500
                        },
                        'pitstop': {
                            'quantity': 23,
                            'length': 180,
                            'width': 80,
                            'height': 180,
                            'weight': 300
                        },
                        'shopfit': {
                            'quantity': 36,
                            'length': 240,
                            'width': 120,
                            'height': 50,
                            'weight': 300}
                    },
            },
        'Spa': {
            'event_date': '2023-07-30',
            'coordinates': {
                        'latitude': 50.426838138646524,
                        'longitude': 5.97181375674147
                        },
            'materials': {
                        'floor': {
                            'quantity': 136,
                            'length': 500,
                            'width': 250,
                            'height': 10,
                            'weight': 440
                        },
                        'tent': {
                            'quantity': 68,
                            'length': 500,
                             'width': 120,
                            'height': 110,
                             'weight': 500
                            },
                        'pitstop': {
                            'quantity': 28,
                            'length': 180,
                            'width': 80,
                            'height': 180,
                            'weight': 300
                            },
                        'shopfit': {
                            'quantity': 49,
                            'length': 240,
                            'width': 120,
                            'height': 50,
                            'weight': 300}
                    },
            },
        'Zaandvort' : {
            'event_date': '2023-08-27',
            'coordinates': {
                            'latitude': 52.38740137114821,
                            'longitude': 4.538481470264232
                            },
            'materials': {
                        'floor': {
                                'quantity': 128,
                                'length': 500,
                                'width': 250,
                                'height': 10,
                                'weight': 440
                                },
                        'tent': {
                                'quantity': 64,
                                'length': 500,
                                'width': 120,
                                'height': 110,
                                'weight': 500
                                },
                        'pitstop': {
                                'quantity': 17,
                                'length': 180,
                                'width': 80,
                                'height': 180,
                                'weight': 300
                                },
                        'shopfit': {
                                'quantity': 47,
                                'length': 240,
                                'width': 120,
                                'height': 50,
                                'weight': 300}
                    },
            },
        'Monza': {
            'event_date': '2022-09-03',
            'coordinates': {
                        'latitude': 45.62278654248577,
                        'longitude': 9.276395389319703
                    },
            'materials': {
                        'floor': {
                            'quantity': 108,
                            'length': 500,
                            'width': 250,
                            'height': 10,
                            'weight': 440
                        },
                        'tent': {
                            'quantity': 54,
                            'length': 500,
                            'width': 120,
                            'height': 110,
                            'weight': 500
                        },
                        'pitstop': {
                            'quantity': 27,
                            'length': 180,
                            'width': 80,
                            'height': 180,
                            'weight': 300
                        },
                        'shopfit': {
                            'quantity': 40,
                            'length': 240,
                            'width': 120,
                            'height': 50,
                            'weight': 300}
                    },
            },
        'Warehouse': {
            'event_date': '2022-01-01',
            'coordinates': {
                        'latitude': 50.6785924062689,
                        'longitude': 6.040260591858885,
                    },
            'materials': {
                        'floor': {
                            'quantity': 508,
                            'length': 500,
                            'width': 250,
                            'height': 10,
                            'weight': 440
                        },
                        'tent': {
                            'quantity': 250,
                            'length': 500,
                            'width': 120,
                            'height': 110,
                            'weight': 500
                        },
                        'pitstop': {
                            'quantity': 300,
                            'length': 180,
                            'width': 80,
                            'height': 180,
                            'weight': 300
                        },
                        'shopfit': {
                            'quantity': 100,
                            'length': 240,
                            'width': 120,
                            'height': 50,
                            'weight': 300}
                    },
            }
        }}



def get_travel_info(packing_list):
    # Create an instance of the EmissionCalculator class
    emission_calculator = EmissionCalculator()
    event_combinations = list(itertools.combinations(packing_list['event'].keys(), 2))
    distances_and_transit_times = {}
    for event1, event2 in event_combinations:
        # check for same event
        if event1 == event2:
            continue
        event1_coordinates = packing_list['event'][event1]['coordinates']
        event2_coordinates = packing_list['event'][event2]['coordinates']
        event1_date = datetime.datetime.strptime(packing_list['event'][event1]['date'], '%Y-%m-%d')
        event2_date = datetime.datetime.strptime(packing_list['event'][event2]['date'], '%Y-%m-%d')
        transit_days = (event2_date - event1_date).days
        # check if the events have the same coordinates
        if event1_coordinates != event2_coordinates and transit_days > 3:
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
            # check if the driver can drive on that day
            if event1_date.weekday() < 5 and event2_date.weekday() < 5:
                transit_time += (transit_days - 2) * 9 # assuming truck driver can only drive 9 hours a day
            else:
                transit_time += (transit_days - 2) * 9 + 2 # assuming truck driver can only drive 9 hours a day
            # Calculate emissions
            emissions = emission_calculator.calculate_emissions_for_heavy_duty_vehicle(distance, transit_time)
            # add the emissions to the result dictionary
            distances_and_transit_times[f"{event1}-{event2}"] = {'distance': distance, 'transit_time': transit_time, 'emissions': emissions}
    return distances_and_transit_times,
def calculate_material_distribution(packing_list, distances_and_transit_times):
    event_materials = {}
    for event, materials in packing_list['materials'].items():
        event_materials[event] = sum(materials.values())
    event_distribution = {}
    for event1, event2 in distances_and_transit_times.keys():
        event1_materials = event_materials.get(event1, 0)
        event2_materials = event_materials.get(event2, 0)
        event1_distribution = event1_materials / (event1_materials + event2_materials)
        event2_distribution = event2_materials / (event1_materials + event2_materials)
        event_distribution[event1] = event1_distribution
        event_distribution[event2] = event2_distribution
    return event_distribution,
def initialize_logs():
    logs = {
        'route_distances': {},
        'material_distribution': {},
        'material_allocation': {},
        'departure_date': {},
        'arrival_date': {},
        'emissions': {}
    }
    return logs,
def best_event(packing_list, events, logs):
    for event in events:
        event_materials = event['materials']
        delivery_window_start = event['date'] - timedelta(days=15)
        delivery_window_end = event['date'] - timedelta(days=10)
        current_time = datetime.now()

        # check if event is within delivery window
        if current_time > delivery_window_start and current_time < delivery_window_end:
            for material, quantity in event_materials.items():
                if material in packing_list and packing_list[material] >= quantity:
                    packing_list[material] -= quantity
                    logs['material_allocation'][event['name']] = {material: quantity}
                else:
                    # check if other events have excess material
                    excess_material = check_excess_material(events, material, quantity)
                    if excess_material:
                        allocate_excess_material(excess_material, event, logs)
                    else:
                        # check if possible to source from warehouse
                        if material in packing_list and packing_list[material] > 0:
                            # allocate remaining material from warehouse
                            allocate_from_warehouse(packing_list, material, quantity, event, logs)
                        else:
                            # not enough material in warehouse
                            print(f"Not enough {material} to cover event {event['name']}")
                            return
        else:
            print(f"Event {event['name']} is not within the delivery window.")
            continue

    # check if all events have been covered successfully
        if check_events_covered(events, logs):
          logs['timestamps']['end_date'] = event['date']
          print("All events have been successfully covered")
        else:
          print("Not enough total material to cover all events"),
def distribute_materials(packing_list, events, logs, max_distance, max_time):
    for event in events:
        event_materials = event['materials']
        delivery_window_start = event['date'] - timedelta(days=15)
        delivery_window_end = event['date'] - timedelta(days=10)
        current_time = datetime.now()
        # check if event is within delivery window
        if current_time > delivery_window_start and current_time < delivery_window_end:
            for material, quantity in event_materials.items():
                if material in packing_list and packing_list[material] >= quantity:
                    packing_list[material] -= quantity
                    logs['material_allocation'][event['name']] = {material: quantity}
                else:
                    # check if other events have excess material
                    excess_material = check_excess_material(events, material, quantity)
                    if excess_material:
                        # check if excess material is within max_distance
                        if get_distance(excess_material['location'], event['location']) <= max_distance:
                            # check if excess material can be delivered within max_time
                            time_to_delivery = get_time_to_delivery(excess_material['location'], event['location'])
                            if time_to_delivery <= max_time:
                                allocate_excess_material(excess_material, event, logs)
                                continue
                    # check if possible to source from warehouse
                    if material in packing_list and packing_list[material] > 0:
                        # check if warehouse is within max_distance
                        if get_distance(warehouse_location, event['location']) <= max_distance:
                            # check if warehouse can deliver within max_time
                            time_to_delivery = get_time_to_delivery(warehouse_location, event['location'])
                            if time_to_delivery <= max_time:
                                # allocate remaining material from warehouse
                                allocate_from_warehouse(packing_list, material, quantity, event, logs)
                                continue
                    # not enough material in warehouse or other events
                    print(f"Not enough {material} to cover event {event['name']}")
                    return