import json
from json.decoder import JSONDecoder

colour_string = '{"Colour": ["red", "Yellow", "Green"]}'
decoded_object = JSONDecoder().decode(colour_string)
print(decoded_object)