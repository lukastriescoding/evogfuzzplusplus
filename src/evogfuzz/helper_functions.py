# For the new fitness functions we need to define some helper functions.

def count_expansions(children):
    """
   Calculate the number of expansions of the Derivation Trees.
   :param children: A List of Derivation Trees
   :return: The total number of expansions of all children.
    """
    if children == []:
        return 0

    counter = 1
    for child in children:
        _, next_children = child
        counter += count_expansions(next_children)

    return counter


def calculate_height_and_degrees(children, height):
    """
   Calculate the maximal height and the sum of the degrees of the Derivation Trees.
   :param children: A List of Derivation Trees
   :param height: The current height of the Sub Derivation Tree.
   :return: The maximal height and the sum of the degrees.
    """
    max_height = height
    degrees = 0

    for child in children:
        _, next_children = child
        degrees += len(next_children) ** height
        next_score, next_height = calculate_height_and_degrees(next_children, height + 1)
        degrees += next_score
        if next_height > max_height:
            max_height = next_height

    return max_height, degrees


def get_diff_expansions(children, exp_set):
    """
   Calculate a set of used production rules of Derivation Trees.
   :param children: A List of Derivation Trees
   :param exp_set: The current set of seen expansions.
   :return: The set of all used production rules.
    """
    expansion = ""
    for child in children:
        node, _ = child
        expansion += node

    exp_set.add(expansion)

    for child in children:
        _, next_children = child
        exp_set.update(get_diff_expansions(next_children, exp_set))

    return exp_set
