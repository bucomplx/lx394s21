test = {   'name': 'q4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> parses = parse_sentence(gramspec, "put dana on an odd square");\n'
                                               '>>> first_parse = parses[0];\n'
                                               ">>> assert target_sem(first_parse) == nltk.sem.Expression.fromstring('\\Q.exists x.(oddtastic(x) & square(x) & Q(x))')\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
