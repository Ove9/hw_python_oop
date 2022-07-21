class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        message = (f'Тип тренировки: {self.training_type}; '
                   f'Длительность: {self.duration:.3f} ч.; '
                   f'Дистанция: {self.distance:.3f} км; '
                   f'Ср. скорость: {self.speed:.3f} км/ч; '
                   f'Потрачено ккал: {self.calories:.3f}. ')
        return message


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * Training.LEN_STEP / Training.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
        self.duration,
        self.get_distance(),
        self.get_mean_speed(),
        self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

    def __init__(self, action: int,
                 duration: float,
                 weight: float) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        coeff_calorie_1: int = 18
        coeff_calorie_2: int = 20
        M_IN_H: int = 60
        calc_run = ((coeff_calorie_1 * super().get_mean_speed()
        ) - coeff_calorie_2) * (self.weight / Training.M_IN_KM
        ) * (self.duration * M_IN_H)
        return calc_run


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 height: int) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        coeff_calorie_3: float = 0.035
        coeff_calorie_4: float = 0.029
        M_IN_H: int = 60
        calc_walk = ((coeff_calorie_3 * self.weight +
                    (super().get_mean_speed() * 2 / self.height) *
                    coeff_calorie_4 * self.weight) * (self.duration * M_IN_H))
        return calc_walk


class Swimming(Training):
    """Тренировка: плавание."""

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    LEN_STEP: float = 1.38

    def get_mean_speed(self):
        return ((self.length_pool * self.count_pool
        ) / Training.M_IN_KM) / self.duration

    def get_spent_calories(self) -> float:
        coeff_calorie_5: float = 1.1
        coeff_calorie_6: int = 2
        calc_swim = (Swimming.get_mean_speed(self) + coeff_calorie_5
        ) * coeff_calorie_6 \
        * self.weight
        return calc_swim


def read_package(workout_type: str, data: list) -> Training:
    decoder = {'RUN': Running,
               'SWM': Swimming,
               'WLK': SportsWalking}
    data_check = decoder[workout_type](*data)
    return data_check


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
