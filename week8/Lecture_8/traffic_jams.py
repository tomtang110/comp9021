# Written by Eric Martin for COMP9021


import tkinter as tk
from math import pi, cos, sin
from random import choice, randrange


class TrafficJams(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Traffic jams')
        self.circuit = Circuit()
        self.traffic = Traffic(self.circuit.road)
        self.control_board = ControlBoard(self.traffic)
        self.control_board.pack()
        self.circuit.pack()


class ControlBoard(tk.Frame):
    min_nb_of_cars = 30
    max_nb_of_cars = 60
    # In milliseconds
    delay = 10

    def __init__(self, traffic):
        tk.Frame.__init__(self, bd = 10, padx = 20, pady = 20)
        self.traffic = traffic
        self.nb_of_cars_scale = tk.Scale(self, length = 200, orient = tk.HORIZONTAL,
                                                                           label ='́Number of cars:',
                                              from_ = self.min_nb_of_cars, to = self.max_nb_of_cars,
                                                    tickinterval = 10, command = self.set_nb_of_cars
                                        )
        self.nb_of_cars_scale.pack(side = tk.LEFT, padx = 50)
        self.simulation_button = tk.Button(self, text = 'Start', command = self.simulate)
        self.simulation_button.pack(side = tk.LEFT, padx = 50)
        tk.Scale(self, length = 150, orient = tk.HORIZONTAL, label ='́Acceleration:',
                                     from_ = 0.01, to = 0.1, tickinterval = 0.03, resolution = 0.01,
                                                                     command = self.set_acceleration
                ).pack(side = tk.LEFT, padx = 50)
        tk.Scale(self, length = 150, orient = tk.HORIZONTAL, label ='Deceleration:',
                               from_ = 1, to = 10, tickinterval = 3, command = self.set_deceleration
                ).pack()
        self.simulating = False

    def set_nb_of_cars(self, nb_of_cars):
        self.traffic.nb_of_cars = int(nb_of_cars)
        self.traffic.generate_and_draw_cars()

    def set_acceleration(self, acceleration):
        self.traffic.acceleration = float(acceleration)

    def set_deceleration(self, deceleration):
        self.traffic.deceleration = int(deceleration)

    def simulate(self):
        if self.simulating is False:
            self.simulating = True
            self.nb_of_cars_scale.config(state = tk.DISABLED)
            self.simulation_button.config(text = 'Stop')
            self.keep_simulating()
        else:
            self.simulating = False
            self.nb_of_cars_scale.config(state = tk.NORMAL)
            self.simulation_button.config(text = 'Start')

    def keep_simulating(self):
        if self.simulating:
            self.traffic.simulate()
            self.after(self.delay, self.keep_simulating)


class Circuit(tk.Frame):
    offset = 10
    road_width = 20
    outer_diameter = 600
    inner_diameter = outer_diameter - road_width * 2
    middle_radius = (outer_diameter + inner_diameter) // 4
    centre = outer_diameter // 2 + offset
    road_colour = '#FFFAF0'
    centre_colour = '#F0FFF0'
    
    def __init__(self):
        tk.Frame.__init__(self, bd = 10, padx = 20, pady = 20)
        self.road = tk.Canvas(self, width = self.outer_diameter + 2 * self.offset,
                                                      height = self.outer_diameter + 2 * self.offset
                             )
        self.road.create_oval(self.offset, self.offset, self.outer_diameter + self.offset,
                                          self.outer_diameter + self.offset, fill = self.road_colour
                             )
        self.road.create_oval(self.road_width + self.offset, self.road_width + self.offset,
                                                self.inner_diameter + self.road_width + self.offset,
                                                self.inner_diameter + self.road_width + self.offset,
                                                                           fill = self.centre_colour
                             )
        self.road.pack()


class Car:
    def __init__(self, position, speed, colour):
        self.position = position
        self.speed = speed
        self.colour = colour
        self.car_at_the_front = None
        self.car_at_the_back = None
        self.drawn_car = None


class Traffic:
    # In km/h
    min_speed = 20
    # In km/h
    max_speed = 110
    # In metres
    circuit_length = 1000
    # In metres when multipled by speed in km/h
    factor_for_distance_per_iteration = ControlBoard.delay / 3600
    # In metres
    safety_distance = 10
    
    def __init__(self, road, nb_of_cars = ControlBoard.min_nb_of_cars, acceleration = 0.01,
                                                                                    deceleration = 1
                ):
        self.road = road
        self.nb_of_cars = None
        self.previous_nb_of_cars = None
        self.acceleration = acceleration
        self.deceleration = deceleration
        self.cars = None

    def generate_and_draw_cars(self):
        if self.previous_nb_of_cars:
            for i in range(self.previous_nb_of_cars):
                self.road.delete(self.cars.drawn_car)
                self.cars = self.cars.car_at_the_front
        self.previous_nb_of_cars = self.nb_of_cars
        positions = []
        free_positions = list(range(self.circuit_length))
        for _ in range(self.nb_of_cars):
            position = choice(free_positions)
            for gap in range(-self.safety_distance, self.safety_distance + 1):
                pos = (position + gap) % self.circuit_length
                if pos in free_positions:
                    free_positions.remove(pos)
            positions.append(position)
        positions.sort()
        self.cars = Car(positions[0], speed = randrange(self.min_speed, self.max_speed + 1),
                                                                        colour = self.random_color()
                       )
        current_car = self.cars
        for i in range(1, self.nb_of_cars):
            car = Car(positions[i], speed = randrange(self.min_speed, self.max_speed + 1),
                                                                        colour = self.random_color()
                     )
            current_car.car_at_the_front = car
            car.car_at_the_back = current_car
            current_car = car
        current_car.car_at_the_front = self.cars
        self.cars.car_at_the_back = current_car
        self.draw_cars()

    def random_color(self):
        r = hex(randrange(256))[2: ]
        if len(r) == 1:
            r = '0' + r
        g = hex(randrange(256))[2: ]
        if len(g) == 1:
            g = '0' + g
        b = hex(randrange(256))[2: ]
        if len(b) == 1:
            b = '0' + b
        return '#' + r + g + b

    def draw_cars(self):
        for _ in range(self.nb_of_cars):
            self.road.delete(self.cars.drawn_car)
            x = (Circuit.centre + cos(self.cars.position * 2 * pi / self.circuit_length) *
                                                                               Circuit.middle_radius
                )
            y = (Circuit.centre + sin(self.cars.position * 2 * pi / self.circuit_length) *
                                                                               Circuit.middle_radius
                )
            self.cars.drawn_car = self.road.create_oval(x - 4, y - 4, x + 4, y + 4,
                                                                             fill = self.cars.colour
                                                       )
            self.cars = self.cars.car_at_the_front

    def simulate(self):
        for _ in range(self.nb_of_cars):
            distance = ((self.cars.car_at_the_front.position - self.cars.position)
                                                        % self.circuit_length - self.safety_distance
                       )
            max_speed = min(self.cars.speed + self.acceleration, self.max_speed)
            if max_speed * self.factor_for_distance_per_iteration < distance:
                self.cars.speed = max_speed
            else:
                self.cars.speed = max(self.cars.car_at_the_front.speed - self.deceleration, 0)
            self.cars.position = (self.cars.position + self.cars.speed *
                                                              self.factor_for_distance_per_iteration
                                 ) % self.circuit_length
            self.cars = self.cars.car_at_the_back
        self.draw_cars()


if __name__ == '__main__':
    TrafficJams().mainloop()
