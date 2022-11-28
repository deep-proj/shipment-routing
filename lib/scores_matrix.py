from lib.ss_algorithm import calculate_score

def suitability_scores_matrix(drivers: list, addresses: list):
    """Constructs a matrix with suitability scores for all driver address combinations"""
    ss_scores = []
    for i, driver in enumerate(drivers):
        driver_name = driver["first_name"] + driver["last_name"]
        driver_ss = []
        for i, address in enumerate(addresses):
            street_name = address["street_name"]
            suitability_score = calculate_score(driver_name, street_name)
        
            driver_ss.append(suitability_score)
        ss_scores.append(driver_ss)
    return ss_scores