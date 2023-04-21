from flask import Blueprint, request, jsonify
from drone_inventory.helpers import token_required, random_joke_generator
from drone_inventory.models import db, Drone, drone_schema, drones_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
@token_required
def getdata(our_user):
    return {'some': 'value'}

# create Drone endpoint
@api.route('/drones', methods=['POST'])
@token_required
def create_drone(our_user):
    name = request.json['name'] #type: ignore
    description = request.json['description'] #type: ignore
    price = request.json['price'] #type: ignore
    camera_quality = request.json['camera_quality'] #type: ignore
    flight_time = request.json['flight_time'] #type: ignore
    max_speed = request.json['max_speed'] #type: ignore
    dimensions = request.json['dimensions'] #type: ignore
    weight = request.json['weight'] #type: ignore
    cost_of_production = request.json['cost_of_production'] #type: ignore
    series = request.json['series'] #type: ignore
    random_joke = random_joke_generator()
    user_token = our_user.token
    
    print(f'User Token: {our_user.token}')
    
    drone = Drone(name, description, price, camera_quality, flight_time, max_speed, dimensions, weight, cost_of_production, series, random_joke, user_token=user_token)
    
    db.session.add(drone)
    db.session.commit()
    
    response = drone_schema.dump(drone)
    return jsonify(response)

# retrieve (READ) all drones drones
@api.route('/drones', methods=['GET'])
@token_required
def get_drones(our_user):
    owner = our_user.token
    drones = Drone.query.filter_by(user_token=owner).all()
    response = drones_schema.dump(drones)
    return jsonify(response)

# retrieve one singular individual lonely drone
@api.route('/drones/<id>', methods=['GET'])
@token_required
def get_drone(our_user, id):
    if id:
        drone = Drone.query.get(id)
        response = drone_schema.dump(drone)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid ID Required'}), 401
 
# update drone by id
@api.route('/drones/<id>', methods=['PUT'])
@token_required
def update_drone(our_user, id):
    drone = Drone.query.get(id)
    drone.name = request.json['name'] #type: ignore
    drone.description = request.json['description'] #type: ignore
    drone.price = request.json['price'] #type: ignore
    drone.camera_quality = request.json['camera_quality'] #type: ignore
    drone.flight_time = request.json['flight_time'] #type: ignore
    drone.max_speed = request.json['max_speed'] #type: ignore
    drone.dimensions = request.json['dimensions'] #type: ignore
    drone.weight = request.json['weight'] #type: ignore
    drone.cost_of_production = request.json['cost_of_production'] #type: ignore
    drone.series = request.json['series'] #type: ignore
    drone.random_joke = random_joke_generator()
    drone.user_token = our_user.token
    
    db.session.commit()
    
    response = drone_schema.dump(drone)
    return jsonify(response)

# delete drone by id
@api.route('/drones/<id>', methods=['DELETE'])
@token_required
def delete_drone(our_user, id):
    drone = Drone.query.get(id)
    db.session.delete(drone)
    db.session.commit()
    
    response = drone_schema.dump(drone)
    return jsonify(response)