#import pacakages needed
import itertools
import datetime as datetime
import requests

#dictionary that contains all the data, except the distance and transit_time
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


#constraints
# Initialize the warehouse_log and events_log dictionaries
warehouse_log = {material: packing_list['event']['Warehouse']['materials'][material]['quantity'] for material in packing_list['event']['Warehouse']['materials']}
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
      distances = {}
      distances[event_pair] = distance
      transit_time = distance / 70 # assuming a truck goes at 70kmph
      distances_and_transit_times[f"{event1}-{event2}"] = {'distance': distance, 'transit_time': transit_time}
      print(distances_and_transit_times)

# Iterate through the events to find the best event to transfer material to
for event1, event1_info in packing_list['event'].items():
    if event1 != 'Warehouse':
        for event2, event2_info in packing_list['event'].items():
            if event2 != 'Warehouse' and event1 != event2:
                event1_date = datetime.datetime.strptime(event1_info['event_date'], "%Y-%m-%d")
                event2_date =  date_difference = (datetime.datetime.strptime(event2_info['event_date'], "%Y-%m-%d") - event1_date).days
                if date_difference >= 3:
                    for material, material_info in event1_info['materials'].items():
                      material_difference = material_info['quantity'] - event2_info['materials'][material]['quantity']
                      if material_difference > 0:
                        best_event = None
                        best_distance = None
                        best_transit_time = None
                        for other_event, other_event_info in packing_list['event'].items():
                          other_event_material_difference = other_event_info['materials'][material]['quantity'] - event2_info['materials'][material]['quantity']
                          if best_event:
                            material_transfer_quantity = min(material_difference, warehouse_log[material])
                            warehouse_log[material] -= material_transfer_quantity
                            events_log[event1][material] -= material_transfer_quantity
                            events_log[best_event][material] += material_transfer_quantity
                            material_distribution[f"{event1}-{best_event}"] = {'material': material, 'quantity': material_transfer_quantity, 'distance': best_distance, 'transit_time': best_transit_time}
                          if other_event_material_difference > material_difference:
                            best_event = other_event
                            best_distance = distances_and_transit_times[f"{event1}-{other_event}"]['distance']
                            best_transit_time = distances_and_transit_times[f"{event1}-{other_event}"]['transit_time']
                          if other_event != event1 and other_event != event2 and other_event != "Warehouse":
                            other_event_date = datetime.strptime(other_event_info['event_date'], "%Y-%m-%d")
                            date_difference = (other_event_date - event2_date).days
                            if date_difference >= 3:
                              for material, material_info in event1_info['materials'].items():
                                material_difference = material_info['quantity'] - event2_info['materials'][material]['quantity']
                                if other_event_material_difference > 0:
                                  distance = distances_and_transit_times[f"{event1}-{other_event}"]['distance']
                                  transit_time = distances_and_transit_times[f"{event1}-{other_event}"]['transit_time']
                                  if best_event is None:
                                    best_event = other_event
                                    best_distance = distance
                                    best_transit_time = transit_time
                                  elif distance < best_distance:
                                    best_event = other_event
                                    best_distance = distance
                                    best_transit_time = transit_time
                            if best_event is not None:
                                # Update the warehouse and events logs
                                warehouse_log[material] += material_difference
                                events_log[event1][material] += material_difference
                                events_log[event2][material] -= material_difference
                                events_log[best_event][material] -= material_difference
                                # Add the distribution information to the material_distribution dictionary
                                material_distribution[material] = ('Warehouse', event1, event2, best_event, best_distance, best_transit_time)
                            elif warehouse_log[material] > abs(material_difference):
                                warehouse_log[material] -= material_difference
                                events_log[event1][material] += material_difference
                                events_log[event2][material] -= material_difference
                                # Add the distribution information to the material_distribution dictionary
                                material_distribution[material] = ('Warehouse', event1, event2, 0, 0)
                            else:
                                print(f"Not enough {material} in stock.")
print(material_distribution)
