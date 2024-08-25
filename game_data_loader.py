import csv

def cast_as_int(*variables):
    casted_variables = []
    for variable in variables:
        casted_variable = int(variable)
        casted_variables.append(casted_variable)
    return casted_variables
def cast_as_float(*variables):
    casted_variables = []
    for variable in variables:
        casted_variable = float(variable)
        casted_variables.append(casted_variable)
    return casted_variables


def load_block_data(active_texture_pack) -> dict:
    file = open("game_data/block_data.csv", "r")
    file_content = csv.reader(file)

    temporary_dictionary = {}

    for line in file_content:
        key = line[0]
        del line[0]

        line[1] = float(line[1])

        temporary_dictionary[key] = line
    file.close()
    return temporary_dictionary

def load_particle_data(active_texture_pack) -> dict:
    file = open("game_data\particle_data.csv", "r")
    file_content = csv.reader(file)
    next(file_content)

    temporary_dictionary = {}

    for line in file_content:
        key, path, number_of_textures, size, r, g, b, gravityX, gravityY, drag, phase_duration = line

        number_of_textures, size, r, g, b = cast_as_int(number_of_textures, size, r, g, b)
        gravityX, gravityY, drag = cast_as_float(gravityX, gravityY, drag)

        if phase_duration == "None":
            phase_duration = None
        else:
            phase_duration = float(phase_duration)

        temporary_dictionary[key] = [path, number_of_textures, size, (r, g, b, 255), (gravityX, gravityY), drag, phase_duration]
    return temporary_dictionary

