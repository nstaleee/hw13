def humanize_car_trip_info(*, seconds: int, speed_matter_per_seconds: int | float, car_weight: int) -> str:
    MIN_ALLOWED_VALUE = 0
    if seconds < MIN_ALLOWED_VALUE:
        raise ValueError(f'seconds value cannot be less than {MIN_ALLOWED_VALUE}')
    if speed_matter_per_seconds < MIN_ALLOWED_VALUE:
        raise ValueError(f'speed_matter_per_seconds value cannot be less than {MIN_ALLOWED_VALUE}')
    if car_weight < MIN_ALLOWED_VALUE:
        raise ValueError(f'car_weight value cannot be less than {MIN_ALLOWED_VALUE}')

    result = f"Транспортний засіб вагою {car_weight} кг рухався {seconds} секунд зі швидкістю 3м/сек, " \
             f"і подолав відствнь {seconds * speed_matter_per_seconds} метрів"
    return result
