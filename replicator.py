from typing import List


def last_segment_orientation(enzyme):
    pass


def binding_preference(enzyme):
    """
    Calculate an enzyme's shape, and returns its preferred binding base.
    :param enzyme:
    :return:
    """
    # Preference is based off of the assumption that the first segment is orientated to the right.
    binding_pref = {
        'right': 'A',
        'up': 'C',
        'down': 'G',
        'left': 'T'
    }

    return binding_pref[last_segment_orientation(enzyme)]


# class Enzyme:
#     def __init__(self, commands: List):
#         self.commands = commands
#
#     def last_segment_orientation(self):
#         pass
#
#     def binding_preference(self):
#         """
#         Calculate an enzyme's shape, and returns its preferred binding base.
#         :param enzyme:
#         :return:
#         """
#         # Preference is based off of the assumption that the first segment is orientated to the right.
#         binding_pref = {
#             'right': 'A',
#             'up': 'C',
#             'down': 'G',
#             'left': 'T'
#         }
#
#         return binding_pref[self.last_segment_orientation()]