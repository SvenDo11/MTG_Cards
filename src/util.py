from typing import Dict, Any

def dictAddX(dictionary: Dict, key: Any, X: Any) -> Dict:
    """Add X to key in dictionary. If key does not exist, add (key: X) to dictionary.

    :param dictionary: Dict object to add X to.
    :type dictionary: Dict
    :param key: Key of value in dictionary to add X to.
    :type key: Any
    :param X: Value to add to key in dictionary.
    :type X: Any
    :return: Dictionary with X added.
    :rtype: Dict
    """
    dictionary[key] = dictionary[key] + X if key in dictionary else X
    return dictionary

def dictAddOne(dictionary: Dict, key: Any) -> Dict:
    """Add one to key in dictionary. If key does not exist, add (key: 1) to dictionary

    :param dictionary: Dict object to add X to.
    :type dictionary: Dict
    :param key: Key of value in dictionary to add X to.
    :type key: Any
    :return: Dictionary with one added to key.
    :rtype: Dict
    """
    return dictAddX(dictionary, key, 1)