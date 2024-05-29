from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args) -> list:
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    
    if not args:
        return USERS
    
    matched_users = []

    if 'id' in args:
        user_id = args['id']
        user = next((user for user in USERS if user["id"] == user_id), None)
        if user:
            matched_users.append(user)

    if 'name' in args:
        name = args['name'].lower()
        for user in USERS:
            if name in user["name"].lower():
                matched_users.append(user)

    if 'age' in args:
        age = int(args['age'])
        for user in USERS:
            if user["age"] in range(age - 1, age + 2):
                matched_users.append(user)

    if 'occupation' in args:
        occupation = args['occupation'].lower()
        for user in USERS:
            if occupation in user["occupation"].lower():
                matched_users.append(user)
                
    unique_users = []
    for user in matched_users:
        if user not in unique_users:
            unique_users.append(user)

    return unique_users
