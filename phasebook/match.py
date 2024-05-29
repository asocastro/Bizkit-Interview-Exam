import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2)->bool:
    fave_numbers_1 = sorted(fave_numbers_1)
    fave_numbers_2 = sorted(fave_numbers_2)
    i = 0
    j = 0
    """
    #Using pointers with element pop
    while j < len(fave_numbers_2):
        if i >= len(fave_numbers_1):
            return False
        if fave_numbers_1[i] == fave_numbers_2[j]:
            j += 1
            fave_numbers_1.pop(i)
        else:
            i += 1
    return True
    """
    
    #Using pointers  
    while j < len(fave_numbers_2):  
        if i >= len(fave_numbers_1):
            return False
        if fave_numbers_1[i] == fave_numbers_2[j]:
            j += 1
        i += 1
    return True

    """
    #original
    for number in fave_numbers_2:
        if number not in fave_numbers_1:
            return False
    return True
    """

    """
        First test on matches with no code changes:
        match/0: 0.0 secs; Match Found
        match/1: 0.0 secs; No Match
        match/2: 39.06 secs; Match Found
        match/3: 40.77 secs; No Match
        
        After Changes(Using pointers):
        match/0: 0.0 secs; Match Found
        match/1: 0.0 secs; No Match
        match/2: 0.07 secs; Match Found
        match/3: 0.08 secs; No Match
        
        After Changes(Using pointers + element pop):
        match/0: 0.0 secs; Match Found
        match/1: 0.0 secs; No Match
        match/2: 1.11 secs; Match Found
        match/3: 0.73 secs; No Match
    """