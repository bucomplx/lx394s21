test = {   'name': 'q5',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> hey_robot('reset');\n"
                                               ">>> hey_robot('put a thing on a red thing');\n"
                                               '>>> assert (\'e\', \'a\') in m.valuation[\'on\'], "Was unable to deposit a pyramid on something else."\n'
                                               'World reset to initial state.\n'
                                               'Already holding a thing of the right kind.\n'
                                               'Placed.\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> hey_robot('reset');\n"
                                               ">>> hey_robot('take a green pyramid');\n"
                                               '>>> assert obj_in_hand == \'c\', "Was unable to take a pyramid."\n'
                                               'World reset to initial state.\n'
                                               'Taken.\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> hey_robot('reset');\n"
                                               ">>> hey_robot('put a thing on a green pyramid');\n"
                                               ">>> on_state = m.valuation['on'].copy();\n"
                                               '>>> assert on_state == m.valuation[\'on\'], "Succeeded in putting e on a pyramid."\n'
                                               'World reset to initial state.\n'
                                               'Already holding a thing of the right kind.\n'
                                               'I cannot see such a place to put anything.\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
