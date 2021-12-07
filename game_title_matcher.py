import re
from fuzzywuzzy import fuzz # Fuzzy string matching library
from Levenshtein import distance as lev

# Performs substitutions and simplifications to help fuzzy matching be more accurate
def prep_name(name):
    return re.sub('[\W_]+', '', name.lower().strip().replace("&", "and")).replace("the", "").replace("2", "ii").replace("3", "iii")

#Returns the item in search_list that is most similar to input_string in form (item, lev distance)
def find_best_match(input_string, search_list):
    best_distance = 99
    best_match = ""
    
    for item in search_list:
        current_distance = lev(prep_name(input_string), prep_name(item))
        
        if(current_distance < best_distance):
            best_distance = current_distance
            best_match = item

    return (best_match, best_distance)

#Similar to find_best_match, but returns None if we're not reasonably certain it's a match
def find_match(input_title, search_list):

    best_match = find_best_match(input_title, search_list)

    if(best_match[1] < 5):
        # If we have a match with a distance of less than 5, it might be a match, or it could be a different installment of the series.

        prepped1 = prep_name(input_title)
        prepped2 = prep_name(best_match[0])
        # Check the last few chars for an exact match to exclude different versions or years.
        if prepped1[-3:] == prepped2[-3:]:
            
            # Even if the last few chars match, these might just be games with similar, short names (e.g. FIFA 2000 to F1 2000 would still be valid at this point)
            # As a last line of defense against false positives, check the match ratio with fuzzywuzzy:
            ratio = fuzz.ratio(prepped1, prepped2)
            if(ratio > 88):
                return best_match[0]

    return None