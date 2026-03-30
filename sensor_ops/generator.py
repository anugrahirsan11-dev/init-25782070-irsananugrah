import random

def generate_temperature():
    """
    Menghasilkan suhu acak antara 20.0 - 40.0 °C
    """
    return round(random.uniform(20.0, 40.0), 2)


def generate_humidity():
    """
    Menghasilkan kelembapan acak antara 30.0 - 90.0 %
    """
    return round(random.uniform(30.0, 90.0), 2)