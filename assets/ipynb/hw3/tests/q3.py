test = {   'name': 'q3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> minispec = {\'top\': r""";\n'
                                               '>>> % start Adj;\n'
                                               '>>> """;\n'
                                               '>>> };\n'
                                               ">>> minispec['adj'] = gramspec['adj'];\n"
                                               '>>> full_spec = assemble_spec(minispec);\n'
                                               '>>> new_grammar = grammar.FeatureGrammar.fromstring(full_spec);\n'
                                               '>>> parser = nltk.FeatureChartParser(new_grammar);\n'
                                               ">>> adjs_to_test = ['odd', 'even', 'red', 'green', 'blue'];\n"
                                               '>>> parsetests = [len(list(parser.parse([word]))) for word in adjs_to_test];\n'
                                               '>>> assert sum(parsetests) == 5\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
