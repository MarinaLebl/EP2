def test_sorteia_letra(palavra, restrito, execs=1000):
    test_results = {}
    for _ in range(execs):
        letra = sorteia_letra(palavra, restrito)
        if letra in test_results:
            test_results[letra] += 1
        else:
            test_results[letra] = 1
    return test_results
