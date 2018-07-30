

# class Genetic_Command:
#     def __init__(self, name: str, action: function, kink: str):
#         self.name = name
#         self.action = action
#         self.kink = kink

def end_operation(strand: str, cur_pos: int):
    """
    Signifies the end of a chain of commands.
    :param strand:
    :param cur_pos:
    :return:
    """
    pass

def cut(strand: str, cur_pos: int):
    """
    Cut the strand.
    :param strand:
    :return: A new strand
    """
    pass

def del_base(strand: str, cur_pos: int):
    """
    Deletes a base from the strand.
    :param strand:
    :return:
    """
    pass

def swi(strand: str, cur_pos: int):
    """
    Switch enzyme to the other strand.
    :param strand:
    :param current_position:
    :return:
    """
    pass

commands = {
    'AA': [end_operation, 'n'],
    'AC': [cut, 's'],
    'AG': [del_base, 's'],
    'AT': [swi, 'r']
}