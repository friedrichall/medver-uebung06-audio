import struct

cep_file = "src/Testdateien/CEP/0-AB.cep"

# Lese die .cep-Datei ein
with open(cep_file, "rb") as file:
    # Lese den 32-Bit-Integer am Anfang der Datei ein
    total_data_points = struct.unpack(">i", file.read(4))[0] # >i stands for big-endian order in file

    # Berechne die Anzahl der Merkmalsvektoren
    num_feature_vectors = (total_data_points - 1) // 13

    # Gehe zur Mitte der Datei
    file.seek(4 + (num_feature_vectors // 2) * 13 * 4)

    # Lese den 13-dimensionalen Merkmalvektor ein
    feature_vector = struct.unpack(">13f", file.read(13 * 4))

# Gib den Merkmalvektor aus
print("Merkmalvektor in der Mitte der MFCC-Datei:")
print(feature_vector)
