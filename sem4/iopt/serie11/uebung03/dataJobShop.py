def create_data_model():
	"""Speichert die Daten des Modells"""
	data = [# operation = (machine_id, processing_time)
        [(0, 4), (1, 2), (2, 3)],  # Auftrag 0
        [(1, 3), (2, 2)],  # Auftrag 1
        [(1, 2), (0, 2)],  # Auftrag 2
        [(2, 3), (0, 2), (1,3)]  # Auftrag 3
    ]
	return data
