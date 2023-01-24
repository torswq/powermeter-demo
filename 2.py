import json
repetidos = [1,2,3,"1","2","3",3,4,5]
r = [1,"5",2,"3"]
d_str = '{"valor":125.3,"codigo":123}

no_repetidos = list(set([str(no_repetido) for no_repetido in repetidos]))
valores_en_comun = [str(_) for _ in if str(_) in no_repetidos]
d_obj = json.loads(d_str)